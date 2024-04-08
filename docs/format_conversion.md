
# Format Conversions
It is possible to convert the dataset structure into other formats, such as, supervisely and YOLO detection with `converter.py`

|Conversion argument | short | description |
|---|---|---|
|`--dir`|`-d`| filepath to the directory to convert in format (default=`./dataset` ).|
|`--format`|`-f`| desired format [i.e.,`SLY`, `YOLO-det`] (default=`SLY` ). |
|`--inplace`|`-ip`| use it to convert the dataset within the `--dir` folder. As default, when not calling the argument, it is set to `False` and converts the dataset within a newly created folder. |
|`--include-depth`|`-depth`| use it to convert the dataset and include depth info. As default, when not calling the argument, it is set to `False` and does not consider depth files in the dataset format conversion. If called, the argument turns `True` and saves depth files within the same directory as color images. (default= `False`) |
|`--separator`|`-sep`| Separator to concat image information during renaming (default=`#` ). |


### Supervisely format
If further annotation effort is needed on the images composing the dataset, it is possible to convert the dataset into [supervisely format](https://docs.supervisely.com/customization-and-integration/00_ann_format_navi/01_project_structure_new) and then use the plugin [import-images-in-sly](https://app.supervisely.com/ecosystem/apps/import-images-in-sly-format?id=154) to import the conversion folder into a supervisely workspace.


Open a terminal and launch `converter.py`.
```
cd OpenAcces_RGBD_apple_dataset

python3 src/converter.py --format sly  # to not consider depth data
python3 src/converter.py --format sly -depth # to consider depth data

```
The output of the following command would be the following:
```
./dataset_SLY
    |
    |__ ann/
    |    |__ 2022_06_17#1_0m#HIGH#P1.png.json
    |    |__ 2022_06_17#1_0m#HIGH#P2.png.json
    |    |__ 2022_06_17#1_0m#LOW#P1.png.json
    |    |__ ...
    |
    |__ img/
    |    |__ 2022_06_17#1_0m#HIGH#P1.png
    |    |__ 2022_06_17#1_0m#HIGH#P2.png
    |    |__ 2022_06_17#1_0m#LOW#P1.png
    |    |__ ...
    |
    |__ meta.json
```
<br>

### YOLO detection format
If You need to work with the dataset in YOLO-det format, do the following.

Open a terminal and launch `converter.py`.
```
cd OpenAcces_RGBD_apple_dataset

python3 src/converter.py --format yolo-det  # to not consider depth data
python3 src/converter.py --format yolo-det -depth # to consider depth data

```
The output of the following command would be the following:
```
./dataset_YOLO-DET
    |
    |__images/
    |   |
    |   |__ train/
    |   |   |__ 2022_06_17#1_0m#HIGH#P1.png
    |   |   |__ 2022_06_17#1_0m#HIGH#P2.png
    |   |   |__ 2022_06_17#1_0m#LOW#P1.png
    |   |   |__ ...
    |   |   
    |   |__ val/
    |
    |__labels/
    |   |
    |   |__ train/
    |   |   |__ 2022_06_17#1_0m#HIGH#P1.txt
    |   |   |__ 2022_06_17#1_0m#HIGH#P2.txt
    |   |   |__ 2022_06_17#1_0m#LOW#P1.txt
    |   |   |__ ...
    |   |   
    |   |__ val/
    |
    |__ dataset.yaml
```

