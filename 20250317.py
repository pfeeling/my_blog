import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#상자그림

# -------------------
# 20250317
# -------------------------

# 5 4 1 2 3
# 중앙값 3

# 1.숫자를 오름차순으로 정렬

# 2. 크기순 중앙값 찾기
# 데이터 개수가
#  짝수인지 홀수인지 확인
# 홀수인경우: 중앙에 있는 값이 하나
# 짝수인 경우:중앙 두 값의 평균

# 사분위수
# 데이터의 분포를 4등분하는숫자
# 3개
# Q1[데이터 하위 25%: first quartile]  Q2[데이터중앙값: second quartile] Q3[데이터 상위 25%:third quartile]


# 데이터 정의
data = [7, 9, 16, 36, 39, 45, 46, 48, 51]

# Seaborn을 사용하여 Boxplot 그리기
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title('Boxplot')
plt.ylabel('값')
plt.show()



np.random.seed(25317)
dat=np.random.randint(1,21,size=15)
# q1,q2,q3 구하기 

[ 1,  3,  3,  5,  5,  6,  6,  8, 11, 13, 13, 15, 18, 18, 20]
np.sort(dat)
q2 중앙값
q2=np.median(dat)

#q1
q1=5

#q3
dat[dat>q2]

#예제

np.random.seed(957)
y=np.random.randint(1,21,size=15)
np.sort(y)


# q2
q2=np.median(y)

#q1
q1=y[y<q2]
np.sort(q1)
#q3
q3=y[y>q2]
np.sort(q3)


np.random.seed(25317)
x=np.random.randint(1,21,size=15)
np.sort(x)

# q2
q2=np.median(x)
q2
#q1
q1=x[x<q2]
np.sort(q1)
#q3
q3=x[x>q2]
np.sort(q3)

q1,q2,q3
iqr=q3-q1


np.random.seed(957)
y=np.random.randint(1,21,size=15)
y[3]=40

# q1,q2,q3 값 구하고 상자 그림 그리기

np.sort(y)
 6   9   17 
# q2
q2=np.median(y)
q2
#q1
q1=np.sort(y[y<q2])

#q3
q3=np.sort(y[y>q2])

# ---------------------
q2=9
q1=6
q3=17
iqr=11


import seaborn as sns
import matplotlib.pyplot as plt
#상자 그림 그리기
df = pd.read_csv('data/Obesity2.csv')
print(df.head())


# 상자그림(Box Plot) 그리기
plt.figure(figsize=(6,5))
sns.boxplot(x=df['NObeyesdad'], 
            y=df['Weight'], 
            palette="Pastel1")
plt.xlabel("Obesity Level")
plt.ylabel("Weight")
plt.title("Box Plot of Weight by Obesity")
plt.xticks(rotation=45)
plt.show()

#산점도

import matplotlib.pyplot as plt
# 산점도 그리기

plt.figure(figsize=(6,5))
plt.scatter(df['Height'], df['Weight'],
            alpha=0.3, # alpha 값을 낮추면 값의 표현이 더 잘됨. 
            color="blue", 
            edgecolors='black')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()
# ---------------------------------------------






# ------------------------------
# 비만 종류별 데이터 포인트 색깔을 변경
# NObeyesdad


df['NObeyesdad'].unique()

plt.figure(figsize=(6,5))
sns.scatterplot(df,
                x="Height",
                y="Weight",
                hue="NObeyesdad")  
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("scatterplot of Height vs Weight")
plt.show() 




# -----------------------------------------
# 히트맵 (Heatmap)

# 상관행렬 계산
corr_matrix = (df[['Age', 
                   'Height', 
                   'Weight']].corr())#상관계수 구하는식

# 히트맵 그리기
plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, 
            annot=True, #히트맵 사각형에 계수값 포함 한다는 의미
            cmap="coolwarm",
            fmt=".2f",linewidths=0.5)
            # " .2f"소수점 2자리까지
plt.title("Heatmap of Feature correlations")       
plt.show()


# 상기의 산점도
plt.figure(figsize=(6,5))
sns.scatterplot(df,
                x="Height",
                y="Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("scatterplot of Height vs Weight")
plt.show() 


plt.figure(figsize=(6,5))
sns.scatterplot(df,
                x="Height",
                y="Age")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("scatterplot of Height vs Weight")
plt.show() 

# 히트맵 (Heatmap) 코드 2

rows, cols = 4, 5
np.random.seed(42)
voltage_data = 220 + np.random.randn(rows, cols) * 5  # 평균 220V, ±5V의 변동
high_voltage_positions = [(1, 3), (2, 4)]
for r, c in high_voltage_positions:
    voltage_data[r, c] += 15  # 특정 위치의 전압 증가
df_voltage = pd.DataFrame(voltage_data, index=[f"Row {i+1}" for i in range(rows)], 
                          columns=[f"Col {j+1}" for j in range(cols)])
plt.figure(figsize=(9, 6))
sns.heatmap(df_voltage, annot=True, cmap="coolwarm", cbar=True)
plt.show()


# 시계열 라인 그래프 (Time Series Line Graph)

dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
values = np.cumsum(np.random.randn(30)) + 50
df_timeseries = pd.DataFrame({"Date": dates, "Value": values})
# 시계열 그래프 그리기
plt.figure(figsize=(8,5))
plt.plot(df_timeseries['Date'], df_timeseries['Value'], marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.show()

# pd.date_range() 함수는 일정 범위의 날짜를 생성하는 함수입니다.
# start='2023-01-01': 시작 날짜를 2023년 1월 1일로 설정
# periods=30: 총 30개의 날짜 생성 (즉, 2023년 1월 1일부터 30일까지)
# freq='D': 빈도를 하루 단위(일간)로 설정

# np.random.randn(30): 평균이 0, 표준편차가 1인 정규분포를 따르는 난수를 30개 생성
# np.cumsum(): 누적 합 계산 → 랜덤하게 생성된 값들이 점점 증가/감소하는 패턴을 가짐
# + 50: 전체 데이터 값을 50을 기준으로 변동하도록 설정

# Date(날짜)와 Value(값)으로 구성된 pandas 데이터프레임 생성


# plt.plot(x, y, marker='o', linestyle='-'):
# x축: 날짜 (df_timeseries['Date'])
# y축: 값 (df_timeseries['Value'])
# marker='o': 데이터 포인트를 원형 마커(●)로 표시
# linestyle='-': 선을 연결하여 시계열 변화를 보여줌

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
# 모자이크 그래프 (Mosaic Plot) 코드
plt.figure(figsize=(8,5))
mosaic(df, ['Gender', 'NObeyesdad', ], 
       title="Mosaic Plot of Gender vs Obesity Level")
plt.show()
#젠더별 전체 데이터중 타입마다 차지하는 정도를 보여줌



import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)  # 0에서 2π까지 100개의 점 생성
y = np.cos(t)

plt.plot(t, y)
plt.xlabel("t (radian)")
plt.ylabel("cos(t)")
plt.title("Cosine Function")
plt.grid(True)
plt.show()