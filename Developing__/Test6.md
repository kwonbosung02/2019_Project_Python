### Test6

cv2_6.py

***

#### Hough Line Transfrom

[hough_opencv_document][https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html]

`cv2.HoughLines` `cv2.HoughLinesp`두가지를 사용해볼 예정이다

***

#### 허프변환

허프변환은 이미지에서 이미지에서 모양을 찾는 가장 유명한 방법이다.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Hough_transform_diagram.svg/800px-Hough_transform_diagram.svg.png)

이미지 출저 : 위키피디아

`y = mx + c` 를 `r = x cos [] + y sin []`의 형태로 표현한다

3개의 점이 있고, 핑크색 직선을 찾는데 각 점 ( x , y )에서 삼각함수를 이용해 []를 1~180 사이로 변화를 하면서 r을 구한다. 그러면 ( [] , r )로 구성된 2차원 배열을 구할 수 있다.

![](https://opencv-python.readthedocs.io/en/latest/_images/image022.png)

 이렇게 해서 구한 2차원 배열을 다시 그래프로 만들면 위와 같이 사인파 그래프가 구현된다고 한다. 세 그래프가 만날 확률이 가장 높은 [] 가 60이고 r 이 80인 점을 구할 수 있다. 

이와 같은 방법을 OpenCv에서 구현할 수 있다.

***

`cv2.HoughLines(image,rho,theta,threshold)  `

HoughLines 함수의 사용 방법이다.

+ image : CannyEdge를 선 적용해야함
+ rho : r 범위 0 ~ 1 실수
+ theta : 0 ~ 180 사이의 각도
+ threshold : 만나는 점의 기준, 숫자가 적으면 많은 선 검출, 정확도 떨어짐. 숫자 많으면 정확도 상승

`cv2.HoughLinesP(image,rho,theta,minLineLength,MaxLineGap)`

확률 허프 변환 함수의 사용방법이다. 선의 시작점, 끝점을 리턴해준다.

+ image : 위와 동일
+ rho : 위와 동일
+ theta : 위와 동일
+ minLineLength : 선의 최소길이 설정
+ MaxLineGap : 선과 선 사이의 최소 간격













