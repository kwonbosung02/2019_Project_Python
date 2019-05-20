import numpy as np
import cv2
import math

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


def give_cropimg(frame):
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]
    location_vertices = [(0, frame_y-50),(frame_x / 2, frame_y / 2 ),(frame_x, frame_y-50),]
    return location_vertices_mask(frame,np.array([location_vertices],np.int32))


def function_Mask(img,lower_arrray,upper_array):
    mask_ = cv2.inRange(img,lower_arrray,upper_array)
    img = cv2.bitwise_and(img,img,mask = mask_)
    img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    return cv2.GaussianBlur(img,(9,9),0)


def draw_lines(img, lines,color=[255,255,0],thickness=3):
    line_ = np.zeros((int(img.shape[0]),int(img.shape[1]), 3), dtype=np.uint8,)
    if lines is None:
        return
    img = np.copy(img)
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_,(int(x1),int(y1)),(int(x2),int(y2)),color,thickness)
    img = cv2.addWeighted(img,0.8,line_,1.0,0.0)
    return img


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
    grayframe_crop = cv2.cvtColor(crop_img,cv2.COLOR_RGB2GRAY)

    img_yellow_blur = function_Mask(hsv,lower_yellow,upper_yellow)

    img_white_blur = function_Mask(hsv,lower_white,upper_white)
    canny_blur = cv2.Canny(img_white_blur,100,200)


 
    #canny_blur = give_cropimg(canny_blur)

    img_white_blur2 = function_Mask(hsv2,lower_white,upper_white)

    drawCircle_vertices(ret)
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]

    canny = cv2.Canny(grayframe_crop,100,200)
    frame_y = frame.shape[0]
    frame_x = frame.shape[1]
 
    
    #lines1 = cv2.HoughLines(get_edge1,1,np.pi/180,200)
    #lines = cv2.HoughLines(get_edge1,1,np.pi/180,200)

    lines = cv2.HoughLinesP(
    canny_blur,
    rho=6,
    theta=np.pi / 60,
    threshold=160,
    lines=np.array([]),
    minLineLength=40,
    maxLineGap=25
    )
    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1) 
            if math.fabs(slope) < 0.5:
                continue
            if slope <= 0:
                left_line_x.extend([x1, x2])
                left_line_y.extend([y1, y2])
            else:
                right_line_x.extend([x1, x2])
                right_line_y.extend([y1, y2])
    min_y = frame.shape[0] * (3 / 5)
    max_y = frame.shape[0] 
    poly_left = np.poly1d(np.polyfit(
        left_line_y,
        left_line_x,
        deg=1
    ))
    left_x_start = int(poly_left(max_y))
    left_x_end = int(poly_left(min_y))
    poly_right = np.poly1d(np.polyfit(
        right_line_y,
        right_line_x,
        deg=1
    ))
    right_x_start = int(poly_right(max_y))
    right_x_end = int(poly_right(min_y))
    line_image = draw_lines(
        frame,
        [[
            [int(left_x_start), int(max_y), int(left_x_end), min_y],
            [int(right_x_start), int(max_y), int(right_x_end), min_y],
        ]],
        (0,255,0),
        3,
    )





    cv2.imshow('see->',dst)
    cv2.imshow('frame',line_image)
    cv2.imshow('crop',crop_img)
    cv2.imshow('cropCanny',canny)
    cv2.imshow('djk',canny_blur)
    #cv2.imshow('crop',crop_img)
    #cv2.setMouseCallback('frame',CallBackFunction)
    #cv2.imshow('yellow',img_yellow_blur)

    #cv2.imshow('white',img_white_blur)
    #cv2.imshow('perspective_see',img_white_blur2)

    #cv2.imshow('canny_blur',get_edge1)
    #cv2.imshow('canny_blur_perspective',get_edge2)
    #cv2.imshow('hough1',get_edge1)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

movie.release()
cv2.destroyAllWindows()
