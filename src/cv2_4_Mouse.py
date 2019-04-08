#-*- coding:utf-8 -*-
'''
import numpy as np
import cv2


def CallBackFunction(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("x 좌표: ",x, "y 좌표", y)

img = cv2.imread("../img/road1.jpg", cv2.IMREAD_COLOR)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img,250,620)

ret, thresh = cv2.threshold(edges, 127, 255, 0)

contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

while(1):

    cv2.setMouseCallback('image',CallBackFunction)
    cv2.imshow('image',image)

    k = cv2.waitKey(1) & 0xFF
    if k ==  27:
        break

cv2.destroyAllWindows()
'''
import numpy as np
import cv2

def CallBackFunction(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("x 좌표: ",x, "y 좌표", y)

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

    cv2.setMouseCallback('img',CallBackFunction)
    cv2.imshow('frame',edges)
    cv2.imshow('img',image)
    
    

    if cv2.waitKey(1) == 27:
        break

movie.release()
cv2.destroyWindow('frame')

