import numpy as np
import cv2
import math
import numpy.core.numeric as NX

def location_vertices_mask(img,vertices):
    mask = np.zeros_like(img)
    cha = img.shape[2]
    mask_color = (255,) * cha

    cv2.fillPoly(mask,vertices,mask_color)
    mask_img = cv2.bitwise_and(img,mask)
    return mask_img

def function_Mask(img,lower_arrray,upper_array):
    mask_ = cv2.inRange(img,lower_arrray,upper_array)
    img = cv2.bitwise_and(img,img,mask = mask_)
    img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    return cv2.GaussianBlur(img,(9,9),0)

def return_hough(img):
    return cv2.HoughLinesP(img,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
        )    
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

class detection:

  
  file = 'null'
  key = 0

  def __init__(self, file, key):
    print("init_processing...")
    lower_yellow =  np.array([20,100,100])
    upper_yellow =  np.array([30,255,255])
    lower_white = np.array([0, 0, 212])
    upper_white = np.array([130, 245, 255])
    self.file = file
    self.key = key
    movie = cv2.VideoCapture(file)
    ret , frame = movie.read()

    point1 = np.float32([[521,462],[185,607],[787,462],[1167,607]])
    point2 = np.float32([[10,10],[10,900],[900,10],[900,900]])

    frame_y = frame.shape[0]
    frame_x = frame.shape[1]
    location_vertices = [(0, frame_y-20),(frame_x / 2, frame_y / 2 ),(frame_x, frame_y-20),]
    
    
    print("location_get_mast ::ok")
    while(True):
      
      crop_img = location_vertices_mask(frame,np.array([location_vertices],np.int32))
      hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)

      grayframe_crop = cv2.cvtColor(crop_img,cv2.COLOR_RGB2GRAY)

      img_yellow_blur = function_Mask(hsv,lower_yellow,upper_yellow)#yellow hsv detection

      img_white_blur = function_Mask(hsv,lower_white,upper_white)   #white hsv detection
    
      canny_blur = cv2.Canny(img_white_blur,100,200)

      frame_y = frame.shape[0]
      frame_x = frame.shape[1]

      canny = cv2.Canny(grayframe_crop,100,200)
      frame_y = frame.shape[0]
      frame_x = frame.shape[1]
      print("img_processing___ ::ok")

      lines = return_hough(canny_blur)
      left_line_x = []
      left_line_y = []
      right_line_x = []
      right_line_y = []

      if lines is not None:
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
      min_y = int(frame.shape[0] * (3 / 5))
      max_y = int(frame.shape[0] * (1))

      print("get__coorinates___::ok")
   
      if left_line_x is not None and left_line_y is not None:
        try:
          poly_left = np.poly1d(np.polyfit(
          left_line_y,
          left_line_x,
          deg=1
          ))
          prev_poly_left = poly_left
        except:
          poly_left = prev_poly_left
        left_x_start = int(poly_left(max_y))
        left_x_end = int(poly_left(min_y))
      if left_line_x is None or left_line_y is None:
        pass

      if right_line_x is not None and right_line_y is not None:
        try:
          poly_right = np.poly1d(np.polyfit(
          right_line_y,
          right_line_x,
          deg=1
          ))  
        
          prev_poly_right = poly_right
        except:
   #     print("NO+deg")
          poly_right = prev_poly_right
        right_x_start = int(poly_right(max_y))
        right_x_end = int(poly_right(min_y))
      if right_line_x is None or right_line_y is None:
        pass

      array_left_line = [int(left_x_start), int(max_y), int(left_x_end), min_y]
      array_right_line =[int(right_x_start), int(max_y), int(right_x_end), min_y]
        
      if array_left_line == 0:
        pass
      if array_right_line == 0:
        pass

      line_image = draw_lines(
      frame,
      [[array_left_line, array_right_line,]],(0,255,255),3,)

      cv2.imshow('frame',line_image)
      if cv2.waitKey(10) & 0xff == ord('q'):
        break
    movie.release()
    cv2.destroyAllWindows()


    if movie.isOpened() == False:
        print("error")
        print("="*30)
    else:
        print("pass")
        print("="*30)

  def __del__(self):
    print('done')
    print("="*30)
  def info(self):
    print('file_path : ', self.file)
    print('key : ', self.key)
  


 

  
  
