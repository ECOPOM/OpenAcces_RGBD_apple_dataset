# OpenAcces_RGBD_apple_dataset
Bortolotti Gianmarco <a
    id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0003-2322-8561"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a>, 
Piani Mirko <a
    id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0001-7087-3761"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a>, 
Gullino Michele <a
    id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0002-8853-4247"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a>, 
Franceschini Cristiano <a
id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0002-4111-6400"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a>, 
Mengoli Dario <a
id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0002-6131-8026"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a>, 
Manfrini Luigi<a
id="cy-effective-orcid-url"
    class="no-text-decoration"
     href="https://orcid.org/0000-0003-4776-0608"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: middle">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
</a> 


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10687503.svg)](https://doi.org/10.5281/zenodo.10687503)


# The dataset
This dataset contains RGB (`.png`) and Depth (`.npy`) images togheter with annotations (`.json`) and ground truth data.\
Click [here](docs/data_description.md) to get a detailed description of data.


**For what purpose was the dataset created?**\
***Open_Access_RGBD_apple_dataset*** was developed specifically for the purpose of facilitating the development, testing and evaluation of fruit sizing algorithms which exploit RGB-D images. The dataset encompasses a wide range of lighting conditions, following most of the growth season of 24 Fuji apples distributed into two apple trees,from ~40 mm  size up to ~95 mm diameter. Consequently, this dataset presents an opportunity to develop RGB-D based sizing algorithms and evaluate their performances with the availability of caliper-measured ground truth data.

**What do the objects that comprise the dataset represent?**\
The dataset comprises labeled RGB-D images capturing the 2022 growth season of Fuji apples  (cv. Aztec) grown in Cadriano (Bologna, Italy) at the experimental farm of the University of Bologna (44.54824 °N, 11.41449 °E). The images, shot with an [Intel RealSense D435i](https://www.intelrealsense.com/depth-camera-d435i/) camera, depict two trees from different perspectives (e.g., top-of-the-canopy, bottom-of-the-canopy, full-canopy) and object-camera distances (e.g., 1.0 m, 1.5 m).

| |
|:---:|
|<img src=images/planar-cordon-training-system.jpeg> | 
| Planar cordon training system|

Trees are trained as "*planar cordons*", that is an innovative bi-dimensional training system that reduces fruit occlusions, while increasing light-interception and productivity. The narrow canopy and simple structure  of *planar cordon* trained trees have been proven to enhance orchard automation and computer vision systems ([Bortolotti, et. al 2021](10.1109/MetroAgriFor52389.2021.9628839)).\
The dataset, besides apples, also features **tennis balls** to aid performance evaluation. Apples have non-uniforma shapes, which implies that the computer vision system could detect a different diameter than the reference one, resulting in an increase of the sizing error. On the other side, tennis balls are iso-diametric, unlike apples, allowing for a better assessment of the sizing performance when comparing detected diameters and their reference.

**Is there a label or target associated with each instance?**\
Manual labeling and association with the reference growth data of 24 fruits and tennis balls was done. Ground truth data were distinguished into:
* [evaluation_ground_truth](data_ground_truth/evaluation_ground_truth_data.csv): contains cleaned reference data, with the fruit size adhering to fruit growth assumptions such as continuous growth or steady-state conditions. This dataset serves as a reference for evaluating the performance of sizing algorithms.
* [applicative_ground_truth](data_ground_truth/applicative_ground_truth_data.csv): includes raw reference data collected in the field from two reference trees, supplemented by data from other trees to enhance the statistical representativeness of field variability at each sampling date. This dataset accounts for human errors (e.g., selecting a different fruit reference diameter) and digital caliper errors, serving statistical purposes.
  
In addition to manual annotations, image labels also include fruit detection bbox coordinates obtained through both a pre-trained YOLOv5l-det model from [ultralytics](https://www.ultralytics.com/) and a trained on a custom dataset YOLOv5l model. The detections are distinguished from manual annotation within the image labels as showed in the [data_exploration](notebook/data_exploration.ipynb).


**What mechanisms or procedures were used to collect the data?**\
The data was collected using a D435i Intel Realsense camera, which was mounted on a tripod. The data was recorded by streaming the camera's feed into bag format with [intel® RealSense™ Viewer](https://www.intelrealsense.com/sdk-2/) and then extracting the frames for each date. Specifically, the camera was connected via a USB 3.0 interface to a PC running Ubuntu 18.04.

| | |
|:---:|:---:|
|<img src=images/D435i-camera.jpeg width=325 height= 578> | <img src=images/tripod-1_0m-LOW.jpeg width=325 height= 578> |
| Intel RealSense D435i sterocamera | Camera and tripod set-up while framing the bottom-of-the-canopy zone at 1.0 m distance |

### get more
* To get a detailed description of the data click [here](docs/data_description.md).
* [convert](./docs/format_conversion.md) the dataset structure into either Supervisely or YOLO format
* [research papers](./docs/research_papers.md) using this dataset.
___
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10687503.svg)](https://doi.org/10.5281/zenodo.10687503)

To **cite this dataset**, refere to it as:
> Bortolotti, G., Piani, M., Gullino, M., Franceschini, C., Mengoli, D., & Manfrini, L. (2024). OpenAcces_RGBD_apple_dataset [Data set]. https://doi.org/10.5281/zenodo.10687503
