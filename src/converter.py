import os
import sys
import json
import shutil
import random
import argparse



class DatasetConverter:
    def __init__(self):
        argparser = argparse.ArgumentParser(description="Dataset Converter")
        argparser.add_argument('--format', '-f', help='Specify the conversion format', default='sly')
        argparser.add_argument('--dir', '-d', help='Specify the directory of the dataset to convert', default=os.path.join(os.getcwd(), 'dataset'))

        # Parse command-line arguments
        args = argparser.parse_args()

        #  Access the value of --format argument
        if args.format:
            print("Format specified:", args.format)
        else:
            print("No format specified")
                
        if args.format.lower() == 'sly':
            print('[CONVERSION] ... to supervisely')
            # STEPS to accomplish:
            # generate img
            # generate ann
            self.conversion_dir = f'./dataset_{args.format.upper()}'
            self.img_dir = os.path.join(self.conversion_dir, 'img')
            self.annotation_dir = os.path.join(self.conversion_dir, 'ann')
            os.makedirs(self.img_dir, exist_ok=True)
            os.makedirs(self.annotation_dir, exist_ok=True)

            # generate meta.json and save it in self.conversion_dir
            self.meta_json = {"classes": [], "tags": [], "projectType": "images"}
            self.proj_annot_dict = {}
            # host datset info
            self.unique_class_titles = []
            self.unique_ref_obj = []

            for cam_obj_distance in os.listdir(args.dir):
                for point_of_view in os.listdir(os.path.join(args.dir, f'{cam_obj_distance}')):
                    for date in os.listdir(os.path.join(args.dir, f'{cam_obj_distance}/{point_of_view}')):
                        for file in os.listdir(os.path.join(args.dir, f'{cam_obj_distance}/{point_of_view}/{date}')):
                            if file.endswith('.png'):
                                fn = os.path.join(args.dir, f'{cam_obj_distance}/{point_of_view}/{date}/{file}') 
                                # modify the name because when importing in sypervisely files `P*.*` will be overwritten
                                new_fn = os.path.join(self.img_dir, f'{date}#{cam_obj_distance}#{point_of_view}#{file}')
                                # clone file into proper folder
                                shutil.copyfile(fn, new_fn)
                            
                            elif file.endswith('.json'):
                                fn = os.path.join(args.dir, f'{cam_obj_distance}/{point_of_view}/{date}/{file}') 
                                # modify the name because when importing in sypervisely files `P*.*` will be overwritten
                                new_fn = os.path.join(self.annotation_dir, f'{date}#{cam_obj_distance}#{point_of_view}#{file}')
                                # clone file into proper folder
                                shutil.copyfile(fn, new_fn)

                                # read annotation file to compile the meta.json
                                with open(fn) as json_file:
                                    annot = json.load(json_file)
                                
                                for obj in annot['objects']:
                                    self.proj_annot_dict[obj['classTitle']] = (obj['classId'], obj['labelerLogin'])

                                    self.unique_class_titles.append(obj['classTitle'])
                                    if obj['description'] != '':
                                        self.unique_ref_obj.append(obj['description'])
            
            for class_title, class_info in self.proj_annot_dict.items():
                # random color assignment for labelling tool
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                # Convert the decimal values to hexadecimal and format them appropriately
                color_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)

                self.meta_json["classes"].append({
                                        "title": class_title,
                                        "description": class_info[1],
                                        "shape": "rectangle",
                                        "color":color_hex,
                                        "geometry_config": {},
                                        "id": class_info[0],
                                        "hotkey": "" })
            
            # save meta.json
            meta_json_file = os.path.join(self.conversion_dir, "meta.json")
            with open(meta_json_file, 'w') as outfile:
                json.dump(self.meta_json, outfile, indent=len(self.meta_json.keys()))
            outfile.close()


        elif args.format.lower() == 'yolo':
            print('[CONVERSION] ... to YOLO')
            self.conversion_dir = f'./dataset_{args.format.upper()}'
            os.makedirs(self.conversion_dir, exist_ok=True)

        print(f'\nDataset converted inside {self.conversion_dir}\n   UNIQUE CLASSES: {set(self.unique_class_titles)}\n   REFERENCE OBJECTS: {set(self.unique_ref_obj)}')


            



if __name__ == '__main__':
    
    DatasetConverter()