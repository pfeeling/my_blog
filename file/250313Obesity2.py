import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/Obesity2.csv')
print(df.head())


# Data description
# Gender : 성별
# Age : 나이
# Height : 키
# Weight : 몸무게
# SMOKE : 흡연 여부
# NObeyesdad : 비만 수준
# overweight_level_i : 과체중 수준 I
#  obesity_type : 비만 유형(I ~ III)

# 히스토그램 (Histogram) 코드

 # 히스토그램 그리기
#plt.figure(figsize=(6,4))


plt.hist(df[['Age']],
         bins=20,
         edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#이상치 판단후 삭제 
df['Age'].value_counts()
(df['Age']).describe()
df['Age'].isna().sum()# NAN값이 없다. 

df.loc[df['Age']>=100,:] #100세 이상의 표본
df.loc[~df['Age']>=100,:] #100세 이상의 표본을 제외
df.loc[df['Age']>=100,:]

df.drop(df[df['Age']>=100],axis=1)# 탐구 필요
df.drop(df[df['Age']>=100,:])
df.drop(df[df['Age']>=100].index)




# 히스토그램 (Histogram) 코드

import matplotlib.pyplot as plt
 # 히스토그램 그리기
#plt.figure(figsize=(6,4))
plt.hist(df[['Age']], bins=100, edgecolor='black', alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


#Histogram 상자 구하기
n=df['Age'].size
h=3.5*np.std(df[['Age']])/n**(1/3)#상자 너비
(max(df['Age']) - min(df['Age']))/h



# Scott's Rule
scott_bin_width = 3.5 * np.std(df['Age']) / (len(df['Age']) ** (1/3))
scott_bins = int((max(df['Age']) - min(df['Age'])) / scott_bin_width)
print('bin의 개수 :', scott_bins)


# 히스토그램 (Histogram) 코드????24

# scott's rule을 통해 구한 히스토그램은 다음과 같습니다.

import matplotlib.pyplot as plt
scott_bin_width = 3.5 * np.std(df['Age']) / (len(df['Age']) ** (1/3))
scott_bins = int((max(df['Age']) - min(df['Age'])) / scott_bin_width)
plt.hist(df[['Age']], bins=scott_bins, edgecolor='black', alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

df["Age"].plot(kind="hist",  # Age(나이) 변수에 대한 히스토그램을 그림
                bins=10,  # 데이터를 10개의 구간(bin)으로 나눔
                edgecolor="black",  # 각 막대의 테두리 색상을 검은색으로 설정
                alpha=0.7,  # 막대의 투명도를 0.7로 설정 (0=완전 투명, 1=완전 불투명)
                figsize=(8, 5))  # 그래프 크기를 가로 8, 세로 5 인치로 설정
plt.xlabel("Age")  # x축 라벨을 "Age"로 설정
plt.ylabel("Frequency")  # y축 라벨을 "Frequency"로 설정
plt.title("Histogram of Age")  # 그래프 제목을 "Histogram of Age"로 설정
plt.show()  # 그래프를 화면에 출력




# 밀도 곡선 (Density Plot)

import seaborn as sns
import matplotlib.pyplot as plt


 # 밀도 곡선 그리기
sns.kdeplot(df['Age'], fill=True)
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

#밀도 함수 그리기

# 밴드위스 조정

sns.kdeplot(df['Age'], bw_method=0.01, fill=True)
sns.kdeplot(df['Age'], bw_method=0.1, fill=True)
sns.kdeplot(df['Age'], bw_method=0.5, fill=True)
sns.kdeplot(df['Age'], bw_method=1, fill=True)
plt.xlabel("Age")
plt.ylabel("Density")
plt.legend(["bw=0.1", "bw=0.5"])
plt.show()


# Pandas를 이용하여 밀도 곡선을 그릴 수도 있습니다.
# Pandas를 활용한 밀도 곡선
df['Age'].plot(kind='kde', figsize=(8,5))
plt.xlabel("Age")
plt.ylabel("Density")
plt.title("Density Plot of Age")
plt.show()

# 막대그래프 (Bar Chart)
#x축에 범주형값이 들어간다.


([0, 1, 2, 3], [Text(0, 0, 'obesity_type_i'),
                Text(1, 0, 'obesity_type_iii'),
                 Text(2, 0, 'obesity_type_ii'),
                 Text(3, 0, 'overweight_level_i')])


# 범주형 데이터의 빈도 계산
category_counts = df['NObeyesdad'].value_counts()
# 막대그래프 그리기 (Matplotlib)


plt.figure(figsize=(6,5))
plt.bar(category_counts.index, category_counts.values,
        color='skyblue', alpha=0.7, edgecolor='black')
plt.xlabel("Obesity Level")
plt.ylabel("Count")

plt.ylim(250,350)# #y축 보여주는 범위 변경 250~350/ 
# 표본범위를 줄여 데이터 격차가 시각적으로 크게 만듬

plt.title("Bar Chart of Obesity Levels")
plt.xticks(rotation=45)  #[45도로 꺽어줘라]
plt.show()


# 막대그래프 그리기 (Seaborn)
# seaborn을 활용해서 시각화

plt.figure(figsize=(6,5))
sns.barplot(x=category_counts.index, y=category_counts.values,
            palette="rocket")
plt.xlabel("Obesity Level")
plt.ylabel("Count")
plt.title("Bar Chart of Obesity Levels")
plt.xticks(rotation=45)
plt.show()

# viridis,rocket, magma





# 상자그림 (Box Plot)







