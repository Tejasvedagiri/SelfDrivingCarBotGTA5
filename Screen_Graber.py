# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 20:06:04 2017

@author: Tejas
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
from KeyBoadInput import PressKey, W, A, S, D,ReleaseKey
import pyautogui

def roi(img,vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked

def process_img(original_image):
    #BGR = [0,255,255] Grey =[0]
     processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
     processed_image = cv2.Canny(processed_image,threshold1=200, threshold2=300)
     vertices = np.array([[10,500],[10,300],[300,200],[500,100],[800,400],[800,600]])
     processed_image = roi(processed_image,[vertices])
     
    # lines = cv2.HoughLinesP(processed_img)
     return processed_image


    
while(True):
    last_time = time.time()
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,600)))
    new_screen = process_img(screen)
            #print('up')
            #PressKey(W)
            #ReleaseKey(W)
    cv2.imshow('window',new_screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time =time.time()
    #cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
