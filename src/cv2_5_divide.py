import numpy as np
import cv2

FilePath = '../vid/road2.mp4'
movie = cv2.VideoCapture(FilePath)

point1 = np.float32([[521,462],[185,607],[787,462],[1167,607]])
point2 = np.float32([[10,10],[10,900],[900,10],[900,900]])

def CallBackFunction(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("x 좌표: ",x, "y 좌표", y)    

def drawCircle_vertices(ret):
    cv2.circle(ret, (521,462), 10, (255,0,0),-1)
    cv2.circle(ret, (185,647), 10, (0,255,0),-1)
    cv2.circle(ret, (787,462), 10, (0,0,255),-1)
    cv2.circle(ret, (1167,647), 10, (0,0,0),-1) 

def check_Movie(mov):
    if mov.isOpened() == False:
        print( 'Cannot open this File' + (FilePath))
        exit()
    else :
        print("video is on ready!")

    return 0

def location_vertices_mask(img,vertices):
    mask = np.zeros_like(img)
    cha = img.shape[2]
    mask_color = (255,) * cha   
    
    cv2.fillPoly(mask,vertices,mask_color)
    mask_img = cv2.bitwise_and(img,mask)
    return mask_img


def give_cropimg(img):
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]
    location_vertices = [(0, frame_y-50),(frame_x / 2, frame_y / 2 ),(frame_x, frame_y-50),]
    return location_vertices_mask(frame,np.array([location_vertices],np.int32))

check_Movie(movie)

lower_yellow =  np.array([20,100,100])
upper_yellow =  np.array([30,255,255])
lower_white = np.array([0, 0, 212])
upper_white = np.array([130, 255, 255])

while(True):
    
    ret, frame = movie.read()
    crop_img = give_cropimg(frame) 

    hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
    Get = cv2.getPerspectiveTransform(point1, point2)

    dst = cv2.warpPerspective(frame, Get, (1000,1000))
    hsv2 = cv2.cvtColor(dst,cv2.COLOR_BGR2HSV)
    grayframe = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    mask_yellow = cv2.inRange(hsv,lower_yellow,upper_yellow)
    img_yellow = cv2.bitwise_and(hsv, hsv, mask = mask_yellow)
    img_yellow = cv2.cvtColor(img_yellow, cv2.COLOR_HSV2BGR)
    img_yellow_blur = cv2.GaussianBlur(img_yellow,(9,9),0)

    mask_white = cv2.inRange(hsv,lower_white,upper_white)
    img_white = cv2.bitwise_and(hsv,hsv, mask = mask_white)
    img_white = cv2.cvtColor(img_white,cv2.COLOR_HSV2BGR)
    img_white_blur = cv2.GaussianBlur(img_white,(9,9),0)

    mask_white2 = cv2.inRange(hsv2,lower_white,upper_white)
    img_white2 = cv2.bitwise_and(hsv2,hsv2, mask = mask_white2)
    img_white2 = cv2.cvtColor(img_white2,cv2.COLOR_HSV2BGR)
    img_white_blur2 = cv2.GaussianBlur(img_white2,(9,9),0)

    drawCircle_vertices(ret)
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]

    

    
    canny = cv2.Canny(grayframe,70,140)
    cv2.imshow('see->',dst)
    cv2.imshow('frame',frame)
    cv2.imshow('crop',crop_img)
    cv2.setMouseCallback('frame',CallBackFunction)
    #cv2.imshow('yellow',img_yellow_blur)
    cv2.imshow('white',img_white_blur)
    cv2.imshow('perspective_see',img_white_blur2)

    if cv2.waitKey(60) & 0xff == ord('q'):
        break

movie.release()
cv2.destroyAllWindows()




