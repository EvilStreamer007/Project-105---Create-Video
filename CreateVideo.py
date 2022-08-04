import os
import cv2

fileName = ""

path = "/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-105/Images"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    
    if ext in ['.gif','.png','.jpg', '.jpeg','.jfif']:
        fileName = path + '/' + fileName
        images.append(fileName)
    
    print("Images Compiled!")

count = len(images)
frame = cv2.imread(images[0])

width = int(cv2.CAP_PROP_FRAME_WIDTH)
height = int(cv2.CAP_PROP_FRAME_HEIGHT)

size = (width,height)

output = cv2.VideoWriter('/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-105/Test.mp4',cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(count - 1, 0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()