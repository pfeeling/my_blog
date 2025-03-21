import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1.범주형 변수 = 문자열을 사용한 데이터를 효율적으로 저장하는 방법

values = pd.Series(['apple','orange','apple','orange']*2)
values
values.unique()
values.value_counts()



#take 메서드p.326
values=pd.Series([0,1,0,0]*2)
dim=pd.Series(['apple','orange'])
#values=index,  dim=value
dim.take(values)  


# p327
fruits=['apple','orange','apple','orange']*2
N=len(fruits)

#rng 
rng=np.random.default_rng(seed=12345)
  


#integers 3이상 15미만의 정수를 N개 생성,uniform 0이상 4이하의 실수를 N개 생성
df=pd.DataFrame({'fruits':fruits,
                 'basket_id':np.arange(N),
                 'count': rng.integers(3,15, size=N),
                 'weight': rng.uniform(0,4, size=N)},
                 columns=['basket_id','fruits','count','weight'])

#범주형 변수 변환 p328

fruits_cat=df['fruits'].astype('category')

c=fruits_cat.array

c.categories

c.codes

dict(enumerate(c.categories))

df['fruits']=df['fruits'].astype('category')
df.info()

##범주형 변수를 Series 만들듯이 직접 생성 1
pd.Categorical(['food','bar', 'baz','foo','bar'])


##범주형 변수를 Series 만들듯이 직접 생성 2
categories=['food','bar', 'baz']
codes=[0,1,2,0,1]
pd.Categorical.from_codes(codes,categories)

#p.330 순서부여
pd.Categorical.from_codes(codes,categories, ordered=True)

#판다스 범주형 변수 연산
draws=rng.standard_normal(1000)
draws

bins=pd.qcut(draws, 4,
        labels=['q1','q2','q3','q4'])
bins.codes[:5]


#문제: 무게 변수를 기준으로 "가벼움, 중간, 무거움" 으로 구분
#weight_cat를 변수를 추가해주세요
df
df.describe()


df['weight_cat']=pd.qcut(df['weight'],3 , labels=['가벼움', '중간', '무거움'])


#문제: 각 그룹의 weight 평균 구하기

df.groupby('weight_cat')['weight'].mean()

pd.pivot_table(df,
               index='weight_cat',
               values='weight').reset_index()



#p. 332 범주형 칼럼 메모리 작게 차지함
N=10_000_000
labels=pd.Series(['foo','bar','bax','qux']*(N//4))
len(labels)

labels_cat=labels.astype('category')
labels_cat

#약 60배 정도 메모리 사용량의 차이가 있음
labels.memory_usage(deep=True)

labels_cat.memory_usage(deep=True)


#카테고리컬 변수 메서드 
s=pd.Series(['a','b','c','d']*2)
cat_s=s.astype('category')
cat_s.cat.categories
cat_s.cat.codes

##보유한 변수값이 전체 변수의 일부분일 경우
cat_s
actual_cat=['a','b','c','d','e','f']
cat_s2=cat_s.cat.set_categories(actual_cat)
cat_s2

#문제 cat_s의 첫번째 원소를 'e'로 바꿔주세요
cat_s.iloc[0]='e' #error


#문제 cat_s2의 첫번째 원소를 'e'로 바꿔주세요
cat_s2.iloc[0]='e'
cat_s2.cat.codes

cat_s.value_counts()
cat_s2.value_counts()


#더미변수 생성법
#get_dummies
#8x4
pd.get_dummies(cat_s, dtype=int)
#8x3  인덱스에 컬럼값을 대입해서 일치하는 값을 보여준다. 
pd.get_dummies(cat_s, dtype=int, drop_first=True)

# -----------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/Obesity2.csv')
print(df.head())


output = df["NObeyesdad"].value_counts()
(output.plot(kind="bar",
             color=["skyblue", "salmon"], 
             edgecolor="black"))
plt.xlabel("NObeyesdad")
plt.ylabel("Count")
plt.show()
# --------------------------------



cat_s.value_counts().plot(
    kind="bar",
    color="blue",
    edgecolor="black")

plt.xlabel("string")
plt.ylabel("Count")
plt.title("var chart of cat_s")
plt.show()
# ----------------------------------


##범주형 변수를 Series 만들듯이 직접 생성 1
cat_var1=pd.Categorical(['foo','bar', 'baz','foo','bar'])


##범주형 변수를 Series 만들듯이 직접 생성 2
categories=['foo','bar', 'baz']
codes=[0,1,2,0,1]
cat_var2=pd.Categorical.from_codes(codes,categories)


cat_var1.value_counts().plot(
    kind="bar",
    color="blue",
    edgecolor="black")

plt.xlabel("string")
plt.ylabel("Count")
plt.title("var chart of cat_var1")
plt.show()


cat_var2.value_counts().plot(
    kind="bar",
    color=["red","green"],
    edgecolor="black")

plt.xlabel("string")
plt.ylabel("Count")
plt.title("var chart of cat_var2")
plt.show()



# ----------------------------2025.03.20

p=np.array([0.16,0.18,0.20])/0.54
bug_p=np.array([0.05,0.02,0.03])

#p(2022|B)=?
p(2022교 B)/p(B)
#p(B)=
sum(bug_p*p)

#p(2022교B)=?


import numpy as np
import pandas as pd
#P(S|B)
p=np.array([0.5,0.3,0.2])#사전분포
break_p=np.array([0.01,0.02,0.03])


#사후 분포(접시 한번 깨짐)
#P(S|B)=0.294
p[0]*break_p[0]/sum(break_p*p)
#P(J|B)=0.353
p[1]*break_p[1]/sum(break_p*p)
#P(M|B)=0.353
p[2]*break_p[2]/sum(break_p*p)

#사후 분포(접시두번 깨짐)
p=np.array([0.294,0.353,0.353])#사전분포
#P(S|B)=0.142
p[0]*break_p[0]/sum(break_p*p)
#P(J|B)=0.342
p[1]*break_p[1]/sum(break_p*p)
#P(M|B)=0.514
p[2]*break_p[2]/sum(break_p*p)