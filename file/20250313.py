import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------데이터 시각화-------------20250313
plt.plot([1, 2, 3, 4])
plt.ylabel('Some Numbers') # y축 라벨
plt.xlabel('Some percent') # x축 라벨
plt.show()
#point. x축은 y축의 인덱스 값  


# X-Y 데이터 시각화
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])# x축, y축
plt.show()

#넘파이 벡터가 plot()에 작동하는지. 

# y=x^3의 그래프
x=np.arange(-10,11,2)
y=x**3
plt.plot(x,y)

# 플롯 스타일 지정
x=np.arange(-10,11,0.5)
y=x**3
plt.plot(x,y,'ro')#빨간점을 찍어준다
plt.axis([0, 6, 0, 20])  # 축 범위 설정(0~6x축, 0~20y축)
plt.show()


# 여러 개의 그래프 그리기

t = np.arange(0., 5., 0.2)  # 0~5 사이 0.2 간
plt.plot(t, t, 'r--',  # 빨간색 점선
t, t**2, 'bs',  # 파란색 정사각형 마커
t, t**3, 'g^')  # 초록색 삼각형 마커
plt.show()


#펭귄데이터 불러오기
#부리길이, 부리깊이(x,y)순서쌍 점찍기

# 팔머펭귄 데이터 불러오기
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()
penguins
penguins.info()



length=penguins['bill_length_mm']
depth=penguins['bill_depth_mm']
# 1차 시도
plt.plot(length,depth,'ro')#빨간점을 찍어준다
plt.ylabel('Some bill_length_mm') # y축 라벨
plt.xlabel('Some bill_depth_mm') # x축 라벨
plt.show()

plt.plot(penguins['body_mass_g'], penguins['bill_length_mm'], 'r--', 
         penguins['body_mass_g'], penguins['bill_depth_mm'], 'bs',
         penguins['body_mass_g'], penguins['flipper_length_mm'], 'g^')
plt.ylabel('depth_length_flipper') # y축 라벨
plt.xlabel('body_mass_g') # x축 라벨
plt.show()



# 키워드 인수를 사용한 플로팅
mydata = {'x': np.arange(50),
          'y': np.random.randn(50) * 10}
plt.scatter('x', 'y', data=mydata)  #데이터 프레임
plt.show()

# scatter()데이터 프레임

data = {'my_x': np.arange(50),
        'my_y': np.random.randn(50) * 10}
mydata=pd.DataFrame(data)
plt.scatter('my_x', 'my_y', data=mydata)  #데이터 프레임

penguins.columns
plt.scatter('body_mass_g','flipper_length_mm', data=penguins)
plt.show()

# 범주형 데이터 시각화

names = ['A', 'B', 'C']
values = [1, 10, 100]
plt.bar(names, values)  # 막대 그래프
plt.suptitle('Categorical Plotting')
plt.show()

#서브플랏
names = ['A', 'B', 'C']
values = [1, 10, 100]
plt.figure(figsize=(9, 3)) #그래프의 크기를 가로x세로 9,3으로 설정하겠다. 
                        #3x3 그래프 연달아 3개 
plt.subplot(231)
plt.bar(names, values)  # 막대 그래프

plt.subplot(132)
plt.scatter(names, values)  # 산점도

plt.subplot(233)
plt.plot(names, values)  # 선 그래프


# 여러 개의 서브플롯 만들기

def f(t):
   return np.exp(-t) * np.cos(2*np.pi*t)

t = np.arange(0., 5., 0.1)
t2 = np.arange(0., 5., 0.02)
plt.figure()

plt.subplot(211)
plt.plot(t, f(t), 'bo',
          t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# 로그 스케일 적용하기

def f(t):
   return np.exp(-t) * np.cos(2*np.pi*t)
t = np.arange(0., 5., 0.1)
t2 = np.arange(0., 5., 0.02)
plt.figure()

plt.subplot(211)
plt.plot(t, f(t), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.xscale('log')
plt.yscale('log')
plt.show()

#그래프 annotation[그래프에 글자쓰기]

plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.text(2, 25, 'LS_song', fontsize=15)#2,25 글자가 시작하는 위치
plt.show()


#그래프 범례
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label='test')
plt.title("Example Plot")  # 그래프 제목 추가
plt.xlabel("X Axis")  # x축 라벨 추가
plt.ylabel("Y Axis")  # y축 라벨 추가
plt.legend(loc="upper left")  # 범례 추가 (위치
plt.show()




