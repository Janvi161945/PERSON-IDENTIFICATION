from keras_facenet import FaceNet
import os
import numpy as np
embedder = FaceNet()

img1 = input("ENTER PATH OF 1st IMG")
FOLDER = input("ENTER PATH to the IMG DIRECTORY")



def get_distance(img1,img2,tresh=1.5):
    detections = embedder.extract(img1, threshold=0.95)
    detections1 = embedder.extract(img2, threshold=0.95)
    dictembd = detections[0]
    dictembd2 = detections1[0]
    embd1 = dictembd.get('embedding')
    embd2 = dictembd2.get('embedding')
    final_dist =  np.sum(np.square(embd1-embd2), axis=-1)
    print(final_dist)

    pred = np.where(final_dist<=tresh, 0, 1) 
    if (pred == 0):
        print("SAME\n")

    else:
        print("DIFFRENT\n")


for images in os.listdir(FOLDER):
    
    
    get_distance(img1,images)
