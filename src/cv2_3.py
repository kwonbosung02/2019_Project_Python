#-*- coding:utf-8 -*-
'''
import numpy as np
import cv2

img = cv2.imread("../img/road1.jpg", cv2.IMREAD_COLOR)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img,250,620)

ret, thresh = cv2.threshold(edges, 127, 255, 0)

contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(img, contours, -1, (0,255,0), 3)



cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt



FilePath = '../vid/road.mp4'

movie = cv2.VideoCapture(FilePath)

if movie.isOpened() == False:
    print( 'Cannot open this File' + (FilePath))
    exit()


while(True):

    ret, frame = movie.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayframe,250,420)

    ret, thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)

    contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    image = cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    cnt = contours[0]
    
    leftmost  = tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
    topmost   = tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost= tuple(cnt[cnt[:,:,1].argmax()][0])    
    #print(leftmost, rightmost, topmost, bottommost)    
    cv2.circle(image,leftmost,20,(0,0,255),-1)
    cv2.circle(image,rightmost,20,(0,0,255),-1)
    cv2.circle(image,topmost,20,(0,0,255),-1)
    cv2.circle(image,bottommost,20,(0,0,255),-1)
    print(leftmost)
    height = image.shape[0]
    width = image.shape[1]


    cv2.imshow('frame',edges)
    #plt.imshow(image)
    #plt.xticks([]) # x축 눈금
    #plt.yticks([]) # y축 눈금
    #plt.show()
    cv2.imshow('img',image)
    
    
    if cv2.waitKey(1) == 27:
        break

movie.release()
cv2.destroyWindow('frame')


