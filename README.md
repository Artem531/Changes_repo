(Please download this and open in text Editor, i don't know how to write spaces in 'How must dir with data look like' )

### Next time I will check all unnecessary folders and delete them, sorry 

## Install
To install it you need:
1) Default Kitti env

## Run
To run it you need:
Start kitti-dataset notebook until # save .txt

## How must dir with data look like

data
    2011_09_26
	      calib_cam_to_cam.txt (must be here)
              calib_imu_to_velo.txt (must be here)
              calib_velo_to_cam.txt (must be here)
              2011_09_26_drive_0001_sync
                                        tracklet_labels.xml (must be here)
                                        image_00
						...
                                        image_01
						...
                                        image_02
						...
                                        image_03
						...
                                        oxts (must be here)
						...
                                        velodyne_points (must be here)
						...
						       

there is other folders you don't need this. 
## Default dir for new .txt labeles is 
/KITTI-Dataset-master/result

                                        
## Visualize
To visualize it run main.py there is open_and_visualize() function
and save clouds and labels in XML_dataset folder


