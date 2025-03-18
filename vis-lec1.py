import pandas as pd
import numpy as np

# 설치 conda install matplotlib
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('This is also Numbers')
plt.ylabel('Some Numbers')
plt.show()

# 넘파이 벡터가 plot() 작동하는지?
# y = x^3 그래프를 그리고 싶다.
# x축 -10, 10까지 범위를 생각하고,
# y축은 해당하는 값을 발생
x = np.arange(-10, 11, 0.5)
y = x**3
plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20]) # 축범위
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 그래프 여러개
x = np.arange(0., 5., 0.2) # 0~5 사이 0.2 간
plt.plot(x, x, 'r--', # 빨간색 점선
         x, x**2, 'bs', # 파란색 정사각형 마커
         x, x**3, 'g^') # 초록색 삼각형 마커
plt.show()


# 펭귄 데이터 불러오기
# 부리 길이, 부리 깊이 (x, y) 순서쌍 점찍기!
# 팔머펭귄 데이터 불러오기
from palmerpenguins import load_penguins
penguins = load_penguins()

x=penguins["bill_length_mm"]
y=penguins["bill_depth_mm"]
plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# scatter() - 데이터 딕셔너리
mydata = {'x': np.arange(50),
          'y': np.random.randn(50) * 10}
plt.scatter('x', 'y', data=mydata)
plt.show()

# scatter() - 데이터 데이터프레임
data = {'my_x': np.arange(50),
        'my_y': np.random.randn(50) * 10}
mydata=pd.DataFrame(data)
plt.scatter('my_x', 'my_y', data=mydata)
plt.show()

# 펭귄 데이터 scatter()
penguins.columns
plt.scatter("body_mass_g",
            "flipper_length_mm",
            data=penguins)
plt.show()


names = ['A', 'B', 'C']
values = [1, 10, 100]
plt.bar(names, values) # 막대 그래프
plt.title('Categorical Plotting')
plt.show()


# 서브 플랏
names = ['A', 'B', 'C']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values) # 막대 그래프
plt.subplot(234)
plt.scatter(names, values) # 산점도
plt.subplot(236)
plt.plot(names, values) # 선 그래프
plt.suptitle('Categorical Plotting')
plt.show()


# 
names = ['A', 'B', 'C']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(231)
plt.bar(names, values) # 막대 그래프
plt.subplot(132)
plt.scatter(names, values) # 산점도
plt.subplot(233)
plt.plot(names, values) # 선 그래프
plt.suptitle('Categorical Plotting')
plt.show()


# 최근 꽂힌 무언가...
# 음악, 음식, 취미? 등등...
# JPOP 요네즈 켄시 - 레몬
# POP 070Shake - 네오 서프 (뮤비 미쳤음)
# 클래식 말러Mahler - 심포니 No 1
# 뮤지컬 Dear 에바넨스 - Waving through the window (한국어버전)
# KPOP 소녀시대 - 다시만난세계
# KPOP 아이브
# 에스파 - 위플레시
# 보이넥스트도어 - 오늘만ILoveYou

# 클라이밍 - 해냈다는 성취감, 
# 1일 (2만원 + 대여료)

# 러닝 크루 5명 (추가 모집 받습니다.)
# 화, 목 7시 축구장으로 오세요.
# 전문가 의견: 장비 신경 쓰지 말고, 뛰기나 해라.

# 아침 7시 헬스장 (추가 모집 합니다.)
# 저녁 7시 헬스장 (상돈님 연장 수업,
#                 고무줄 밴드 대여가능)

# 농구 크루 (추가모집)
# 점심 먹고, 저녁먹고

# 축구 1명, (놀아주세요!)
# 배드민턴 부서 개설 요청 (주연 학생에게로)

# 테니스

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
plt.xscale("log")
plt.yscale("log")
plt.show()


# 그래프 Annotation
plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.text(2, 25, 'LS Bigdata School', fontsize=15)
plt.show()


# 그래프 범례 (legend)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label="test")
plt.title("Example Plot") # 그래프 제목 추가
plt.xlabel("X Axis") # x축 라벨 추가
plt.ylabel("Y Axis") # y축 라벨 추가
plt.legend(loc="upper right") # 범례 추가 (위치
plt.show()

# 그래프 그리기 실습
import pandas as pd
import numpy as np
df = pd.read_csv('./data/Obesity2.csv')
df.info()


#plt.figure(figsize=(6,4))
plt.hist(df['Age'],
         bins=20,
         edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Age 변수 이상치 판단 후 삭제
df=df.loc[~(df['Age'] >= 100), :]
df

# df.drop(df.loc[df['Age'] >= 100,:].index)
# df=df.drop(df[df['Age'] >= 100].index)

plt.hist(df['Age'],
         bins=20,
         alpha=0.1, # 투명도 결정 옵션
         edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# histogram 상자개수 정하기
n=df['Age'].size
h=3.5 * np.std(df['Age']) / n**(1/3) # 상자너비
int((max(df['Age']) - min(df['Age'])) / h) #상자갯수

# 밀도함수 그리기
import seaborn as sns

sns.kdeplot(df['Age'], bw_method=0.01, shade=True)
sns.kdeplot(df['Age'], bw_method=0.1, shade=True)
sns.kdeplot(df['Age'], bw_method=0.5, shade=True)
sns.kdeplot(df['Age'], bw_method=1, shade=True)


# 바차트
# 범주형 데이터의 빈도 계산
category_counts = df['NObeyesdad'].value_counts()

# 막대그래프 그리기 (Matplotlib)
plt.figure(figsize=(6,5))
plt.bar(category_counts.index, category_counts.values, 
        color='skyblue', alpha=0.7, edgecolor='black')
plt.xlabel("Obesity Level")
plt.ylabel("Count")
plt.title("Bar Chart of Obesity Levels")
plt.xticks(rotation=45)  # 라벨 가독성을 위해 회전
plt.show()

# 막대그래프 그리기 (Seaborn)
# y축 보여주는 범위 변경 250~350
plt.figure(figsize=(6,5))
sns.barplot(x=category_counts.index, 
            y=category_counts.values, 
            palette="Blues_r")
plt.xlabel("Obesity Level")
plt.ylabel("Count")
plt.ylim(250, 350) # 축범위 조정
plt.title("Bar Chart of Obesity Levels")
plt.xticks(rotation=45)  # 라벨 가독성을 위해 회전
plt.show()

# flights 데이터 분석 및 시각화