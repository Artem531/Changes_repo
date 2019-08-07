# This notebook convert .xml file of labels for KITTI dataset to .txt file with respect to camera axis

## Install
To install it you need:
1) Default Kitti env

## Run
To run it you need:
Start kitti-dataset notebook until # save .txt

## How must dir with data look like

1) data
  - 2011_09_26
    - calib_cam_to_cam.txt (must be here)
    - calib_imu_to_velo.txt (must be here)
    - calib_velo_to_cam.txt (must be here)
    1) 2011_09_26_drive_0001_sync
      - tracklet_labels.xml (must be here)
      1) image_00
	- ...
      1) image_01
	- ...
      1) image_02
	- ...
      1) image_03
	- ...
      1) oxts (must be here)
	- ...
      1) velodyne_points (must be here)
	- ...
						       


## Default dir for new .txt labeles is 
/KITTI-Dataset-master/result

                                        
## Visualize
To visualize it I add new main.py file later


