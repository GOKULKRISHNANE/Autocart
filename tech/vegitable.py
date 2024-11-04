
import urllib.request
import time
import cv2
import io

import time
import pyttsx3
import pymysql
import sys
import glob
from datetime import datetime

engine=pyttsx3.init()


def savedata(sql):
    db = pymysql.connect(host='localhost',user="root",password="root",port=3306,database="autocart" )
    c = db.cursor()
    c.execute(sql)
    
    db.commit()
    
    c.close()
    
    db.close()
    
from skimage.metrics import structural_similarity as compare_ssim

li=['back', 'ginger', 'tomato']

import cv2
import numpy as np
# from matplotlib import pyplot as plt

def surf_keypoint_matching(img1_path, img2_path):
    # Read the images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Check if images loaded properly
    if img1 is None or img2 is None:
        print('Could not open or find the images!')
        return

    # Create a SURF detector object
    surf = cv2.xfeatures2d.SURF_create(400)

    # Find keypoints and descriptors directly
    kp1, des1 = surf.detectAndCompute(img1, None)
    kp2, des2 = surf.detectAndCompute(img2, None)

    # Use FLANN based matcher for faster matching
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Perform the matching
    matches = flann.knnMatch(des1, des2, k=2)

    # Apply ratio test as per Lowe's paper
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Calculate the matching percentage
    total_keypoints = max(len(kp1), len(kp2))
    if total_keypoints > 0:
        matching_percentage = (len(good_matches) / total_keypoints) * 100
    else:
        matching_percentage = 0
        
    # print(img2_path)
    #
    # print(f"Matching Percentage: {matching_percentage:.2f}%")
    return matching_percentage







# Initialize the camera
cap = cv2.VideoCapture(1)  # Adjust the device index based on your configuration
cnt=0
try:
    # if ser.isOpen():
    #     ser.flushInput() #flush input buffer, discarding all its contents
    #     ser.flushOutput()#flush output buffer, aborting current output
        while True:
            if cnt<250:
                ret, frame1 = cap.read()
                cnt+=1
                continue
            else:
                ret, frame = cap.read()
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
#                 rsp=ser.readline().decode('utf-8').rstrip()
#                 if rsp!='':
#                     print(rsp)
#                     if 'FULL' in rsp:
#                         engine.say("Bin Fill")
#                         engine.runAndWait()

            grayA = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            if score>.94:
                print("not",score)
                time.sleep(5)
#                 continue
            else:
                print("cap",score)
                engine.say("Image Capture")
                engine.runAndWait()
                time.sleep(10)
                cv2.imwrite('test.jpg',frame)
#                 pred('test.jpg')
                m=[0,0,0]
                res=['tomato','ginger','chilly']
                m[0]=surf_keypoint_matching("test.jpg","tomato.jpg")
                m[1]=surf_keypoint_matching("test.jpg","ginger.jpg")
                m[2]=surf_keypoint_matching("test.jpg","chilly.jpg")
                print(m)
                largest_number = max(m)
                print('large',largest_number)
                index_of_largest = m.index(largest_number)
                print('index',index_of_largest)
                ress=res[index_of_largest]
                print(ress)


                sql="update veg set vegi='"+ ress +"'"
                print(sql)
                savedata(sql)




#                 print(res[index_of_largest])
#                 engine.say(res[index_of_largest])
#                 engine.runAndWait()
except Exception as ex:
                
    print(ex)
finally:
    cap.release()
    cv2.destroyAllWindows()


# In[ ]:




