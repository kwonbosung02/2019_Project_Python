# 2019_Project_Python
## License

<img align="right" src="http://opensource.org/trademarks/opensource/OSI-Approved-License-100x137.png">

The class is licensed under the [MIT License](http://opensource.org/licenses/MIT):

Copyright &copy; 2019 [BOSUNG](https://github.com/kwonbosung02).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

***

### 연구 주제 : Python OpenCV Line Tracking
#### 선정 이유

내 꿈은 어렸을 때 부터 로봇 연구원이 되는 것 이어서 지금까지 많은 로봇을 개발해왔다. 

개발을 해오면서 로봇이 주어진 명령을 수행하고, 사람이 명령하는데로만 동작되게끔 하는데에는 큰 어려움이 없지만, 로봇이 자율적으로, 스스로 판단하여 추가적으로 기능을 하고 동작하기 위해서는 로봇에 특별한 추가적인 요소가 필요하다는 것을 느꼈다. 

로봇에 필요한 여러 요소 중 가장 중요시 여긴 것이 시각적 요소인데 로봇에 시각적 요소를 추가하면 주변에 위치한 사물, 사람의 정보를 자율적으로 파악하고, 그에 대한 자율적인 행동을 할 수 있기 때문에다. DARPA robotics challenge 를 보면 로봇이 여러가지 미션을 수행해야 하는데 공통적으로 미션을 수행하기 위해서 가장 필요한 기능은 물론 움직이기 위한 엑추에이터도 있지만, 카메라를 이용해 미션 수행을 위한 목적지의 위치, 경로를 알아내는 것이다. 즉, 로봇에는 카메라를 통한 분석이 필수적이다. 

이러한 이유로 최근 임베디드, 로봇 분야에 사용되는 언어인 Python과 컴퓨터 비전을 목적으로한 OpenCV라이브러리(모듈)을 이용하여  영상을 분석해 라인(차선)을 따라가는  Line Tracking 프로그램을 제작해 보기로 하였다.

***

#### 아이디어 스케치

![](/img/idea.jpg)

***

