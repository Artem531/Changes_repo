from config.config_dict import get_default_config
from train import train_model
from infer import inference
from data_processing.prepare_dataset import prepare_data

from data_processing.prepare_dataset import get_data
from data_processing.kitti_datagen_experimental import KittiDataset


from utils.visualize_utils import visualize

import numpy as np
from structures.object_info import ObjectInfo
import math

def normalize_angle(angle):
    """
    Convert an angle to an angle belonging to the range -pi..pi
    :param angle: angle value in radians
    :return: angle value in radians
    """
    angle %= (2 * math.pi)
    angle = angle - 2 * math.pi if angle > math.pi else angle
    return angle

def open_and_visualize(path_to_velodyne, path_to_label,name, index):
    """
    open_and_visualize  cloud and label for checking
    :param path_to_velodyne:
    :param name:
    :param index:
    :return:
    """
    Config = get_default_config()
    dataset = [name]

    Data = KittiDataset(dataset, path_to_velodyne)
    labels = []
    with open(path_to_label + name + '.txt', encoding='utf-8', mode='r') as f:
        for label in f:
            #print(label)
            label = label.strip()
            label = label.split(' ')
            print(label[0])
            label = list(map(float, label[1:]))
            print(label[0])
            if not label:
                continue
            #print(label[13])
            angle = label[13]
            angle = normalize_angle(angle)
            bbox = [-label[11],
                    label[10],
                    label[8], label[9],
                    np.cos(angle), np.sin(angle)]
            print(bbox)
            labels.append(ObjectInfo(bbox))

    points = Data.get_velodyne(index)


    visualize([points], [labels])



if __name__ == '__main__':
    Config = get_default_config()

    path_to_velodyne = '/home/artem/Parser/KITTI-Dataset-master/XML_dataset'
    path_to_label = '/home/artem/Parser/KITTI-Dataset-master/XML_dataset/training/label_2/'
    open_and_visualize(path_to_velodyne, path_to_label, '0000000010', 0)

