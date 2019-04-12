import numpy as np
import cv2

FilePath = '../vid/road2.mp4'
movie = cv2.VideoCapture(FilePath)

point1 = np.float32([[521,462],[185,607],[787,462],[1167,607]])
point2 = np.float32([[10,10],[10,900],[900,10],[900,900]])
#--------------------------------------------------------------------------------#
def CallBackFunction(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("x 좌표: ",x, "y 좌표", y)    
#--------------------------------------------------------------------------------#
def drawCircle_vertices(ret):
    cv2.circle(ret, (521,462), 10, (255,0,0),-1)
    cv2.circle(ret, (185,647), 10, (0,255,0),-1)
    cv2.circle(ret, (787,462), 10, (0,0,255),-1)
    cv2.circle(ret, (1167,647), 10, (0,0,0),-1) 
#--------------------------------------------------------------------------------#
def check_Movie(mov):
    if mov.isOpened() == False:
        print( 'Cannot open this File' + (FilePath))
        exit()
    else :
        print("video is on ready!")

    return 0
#--------------------------------------------------------------------------------#
def location_vertices_mask(img,vertices):
    mask = np.zeros_like(img)
    cha = img.shape[2]
    mask_color = (255,) * cha   
    
    cv2.fillPoly(mask,vertices,mask_color)
    mask_img = cv2.bitwise_and(img,mask)
    return mask_img
#--------------------------------------------------------------------------------#
def give_cropimg(img):
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]
    location_vertices = [(0, frame_y-50),(frame_x / 2, frame_y / 2 ),(frame_x, frame_y-50),]
    return location_vertices_mask(frame,np.array([location_vertices],np.int32))
#--------------------------------------------------------------------------------#
def function_Mask(img,lower_arrray,upper_array):
    mask_ = cv2.inRange(img,lower_arrray,upper_array)
    img = cv2.bitwise_and(img,img,mask = mask_)
    img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    return cv2.GaussianBlur(img,(9,9),0)
#--------------------------------------------------------------------------------#

check_Movie(movie)

lower_yellow =  np.array([20,100,100])
upper_yellow =  np.array([30,255,255])
lower_white = np.array([0, 0, 212])
upper_white = np.array([130, 245, 255])



while(True):
    
    ret, frame = movie.read()
    crop_img = give_cropimg(frame) 

    hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
    Get = cv2.getPerspectiveTransform(point1, point2)

    dst = cv2.warpPerspective(frame, Get, (1000,1000))
    hsv2 = cv2.cvtColor(dst,cv2.COLOR_BGR2HSV)
    grayframe = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)


    img_yellow_blur = function_Mask(hsv,lower_yellow,upper_yellow)
    
    img_white_blur = function_Mask(hsv,lower_white,upper_white)

    img_white_blur2 = function_Mask(hsv2,lower_white,upper_white)

    drawCircle_vertices(ret)
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]

    canny = cv2.Canny(grayframe,70,140)
    
    get_edge1 = cv2.Canny(img_white_blur,70,140)
    get_edge2 = cv2.Canny(img_white_blur2,70,140)
    #lines1 = cv2.HoughLines(get_edge1,1,np.pi/180,200)
    lines = cv2.HoughLines(get_edge1,1,np.pi/180,200)
    """if lines is not None:
        for line in lines[0]:
            pt1 = (line[0], line[1])
            pt2 = (line[2], line[3])
            cv2.line(get_edge1, pt1, pt2, (0, 0, 255), 3)
    """
    """
    for i in range(len(lines1)):
        for rho,theta in  lines1[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(get_edge1,(x1,y1),(x2,y2),(0,0,255),2)
    """
    lines = cv2.HoughLinesP(get_edge1, 1, np.pi/180, 50, maxLineGap=130)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    lines2 = cv2.HoughLinesP(get_edge2, 1, np.pi/180, 50, maxLineGap=130)
    if lines2 is not None:
        for line in lines2:
            x1, y1, x2, y2 = line[0]
            cv2.line(dst, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow('see->',dst)
    cv2.imshow('frame',frame)
    #cv2.imshow('crop',crop_img)
    #cv2.setMouseCallback('frame',CallBackFunction)
    #cv2.imshow('yellow',img_yellow_blur)

    #cv2.imshow('white',img_white_blur)
    #cv2.imshow('perspective_see',img_white_blur2)

    #cv2.imshow('canny_blur',get_edge1)
    #cv2.imshow('canny_blur_perspective',get_edge2)
    cv2.imshow('hough1',get_edge1)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

movie.release()
cv2.destroyAllWindows()




