# OpenAcces_RGBD_apple_dataset
\
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10687503.svg)](https://doi.org/10.5281/zenodo.10687503)

To **cite this dataset**, refere to it as:
> Bortolotti, G., Piani, M., Gullino, M., Franceschini, C., Mengoli, D., & Manfrini, L. (2024). OpenAcces_RGBD_apple_dataset [Data set]. https://doi.org/10.5281/zenodo.10687503

\
 Intel realsense d435i open access dataset of seasonal growth of fuji apple. 
 The dataset contains images and reference caliper ground truth data.
 Data were collected during 2022 season in a 3 years old apple orchard trained as 'Planar Cordon' (bidimensional training system).
 12 fruit on two trees (24 fruit in total) were monitored for their fruit size along the whole season.
 RGB-D pictures, manually labelled for the monitored fruit, were taken on 17 different dates from a fruit size of  40mm approx. to >80mm approx

 **For more detailed info check the 'data_exploration' Jupyter notebook in the notebook folder**
 
 Other information regarding the dataset and results obtained with that can be found in the following papers:
 - 67 Apple fruit sizing through low-cost depth camera and neural network application - https://doi.org/10.3920/978-90-8686-947-3_67
 - A Computer Vision Approach for Estimating Fruit Growth Rate in Orchards - IN PRESS in Acta Horticulturae as conference proceedings of ISHS PMOV conference

<br>

___
# Dataset enabled Format Conversions
### Supervisely format



|Conversion argument | short | description |
|---|---|---|
|`--dir`|`-d`| filepath to the directory to convert in format (default=`./dataset` ).|
|`--format`|`-f`| desired format (i.e.,`SLY`). In future will be added also `YOLO-det` (default=`SLY` ). |
|`--inplace`|`-ip`| use it to convert the dataset within the `--dir` folder. As default, when not calling the argument, it is set to `False` and converts the dataset within a newly created folder. |

Open a terminal and launch the conversion to the format specified with the `-f` argument.
```
cd OpenAcces_RGBD_apple_dataset

python3 src/converter.py --format SLY
```

