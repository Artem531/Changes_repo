# This notebook convert .xml file of labels for KITTI dataset to .txt file with respect to camera axis

## Install
To install it you need:
1) Default Kitti env

## Run
To run it you need:
Start kitti-dataset notebook until # save .txt

## How must dir with data look like

### standart (specify date and drive or specify sync folder)
```
Changes_repo
├── data
│   ├── 2011_09_26
│   │   ├── calib_cam_to_cam.txt (must be here because I can't change pykitti.raw class init)
│   │   ├── calib_imu_to_velo.txt (must be here because I can't change pykitti.raw class init)
│   │   ├── calib_velo_to_cam.txt (must be here because I can't change pykitti.raw class init)
│   │   ├── 2011_09_26_drive_0001_sync
│   │   │   ├── tracklet_labels.xml (must be here)
│   │   │   ├── image_00
│   │   │       ├── ...
│   │   │   ├── image_01
│   │   │       ├── ...
│   │   │   ├── image_02
│   │   │       ├── ...
│   │   │   ├── image_03
│   │   │       ├── ... 
│   │   │   ├── oxts (must be here)
│   │   │       ├── ...
│   │   │   ├── velodyne_points (must be here)
│   │   │       ├── ...
```

### alternative (specify sync folder)
```
Changes_repo
├── data
│   ├── 2011_09_26
│   │   ├── calib_cam_to_cam.txt (must be here because I can't change pykitti.raw class init)
│   │   ├── calib_imu_to_velo.txt (must be here because I can't change pykitti.raw class init)
│   │   ├── calib_velo_to_cam.txt (must be here because I can't change pykitti.raw class init)

2011_09_26_drive_0001_sync
├── ├── tracklet_labels.xml (must be here)
│   ├── image_00
│       ├── ...
│   ├── image_01
│       ├── ...
│   ├── image_02
│       ├── ...
│   ├── image_03
│       ├── ... 
│   ├── oxts (must be here)
│       ├── ...
│   ├── velodyne_points (must be here)
│       ├── ...
```

## Default dir for new .txt labeles is 
- result

                                        

