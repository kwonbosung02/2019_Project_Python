## 최종 완료

`from detection_class_fi import detection`을 이용해서 load line detection을 사용할 수 있다.

```python
from detection_class_fi import location_vertices_mask
from detection_class_fi import function_Mask
from detection_class_fi import return_hough
from detection_class_fi import draw_lines
```

위 또한 사용 가능하다.

line을 찾기 위한 함수는 def로 지정해두고, line을 찾을 식을 계산하는 함수는 class안에 구현하였다.

```python
from detection_class_fi import detection
from detection_class_fi import location_vertices_mask

r = detection('../vid/road2.mp4',3)
r.info()
```

영상 속 라인을 찾는 코드

