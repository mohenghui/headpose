from email.mime import image
from scipy.io import loadmat
from utils import draw_axis
import os
import cv2
annotations_path="./data/annotations"
annotations=os.listdir(annotations_path)

image_path="./data/images"
for i in annotations:
    a=loadmat(os.path.join(annotations_path,i))
    name,tail=os.path.splitext(i)
    pitch,yaw,roll=a['Pose_Para'][0][:3]

    img=cv2.imread(os.path.join(image_path,name+".jpg"))
    cv2.imshow("test",draw_axis(img,yaw,pitch,roll))
    print(pitch)
    cv2.waitKey(0)