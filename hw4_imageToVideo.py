import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import glob
import os


def image_to_video(key):
    path = 'image/'
    filelist = os.listdir(path)
    #filelist = os.listdir(os.getcwd())


    # Support 'jpg' format
    fourcc = VideoWriter_fourcc(*"MJPG")
    size = (640,480)

    fps = 1/3 # three seconds per pic
    size = (1200, 630)
    video = cv2.VideoWriter(key + ".avi", fourcc, fps, size)

    for item in filelist:
        if item.endswith('.jpg'): 
            item = path + item
            print(item)
            frame = cv2.imread(item)
            # resize the make the size match the video
            frame = cv2.resize(frame,size)
            video.write(frame)
    video.release()


if __name__ == '__main__':
    image_to_video('Honda')


