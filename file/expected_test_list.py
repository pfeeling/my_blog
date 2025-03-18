import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 2025.03.10 작성
#melt 사용 방법
sample = {
    'country': ['Afgahnistan','Brazil', 'China'],
    '1999': [745,37737,212258],
    '2000': [2666,80488,213766]
 }
sp = pd.DataFrame(sample)
print(sp)

#상기 데이터프레임을 긴 형식(long form)으로 변환하시오.

melted_sp=pd.melt(sp,
                  id_vars='country',
                  value_vars=['1999','2000'],
                  var_name='valiables',
                  value_name='cases')

# 상기 데이터프레임을 pivot() 함수 사용하여 melt 이전으로 변환하시오

df_pivoted=pd.pivot(melted_sp,
                    index='country',
                    columns='valiables',
                    values='cases').reset_index()
              

# 상기 데이터프레임의 올바른 shape를 작성하시오

df_pivoted.shape


#상기 데이터프레임의0,0 번째 값 

df_pivoted.iloc[0,0]


#상기 데이터프레임의 인덱스 이름 제거

df_pivoted.columns.name=None


#상기 데이터프레임의 인덱스 이름 작성

df_pivoted.columns.name='year'


#pivot_table()

df=pd.DataFrame({
    'School': ['A','A','B','B','C','C'],
    'Gender': ['M','F','M','F','M','F'],
    'City': ['North', 'South','North', 'South','North', 'South'],
    'Midterm': [10,20,30,40,50,60],
    'Final': [5,15,25,35,45,55]
})
print(df)

#학교별 중간고사 평균

mid=df.groupby('School')['Midterm'].mean().sort_values(ascending=False)

pivoted_df=pd.pivot_table(df,
                    index='School',
                    values='Midterm').reset_index()

#학교별 중간고사,기말고사 평균

Total=df.groupby('School')[['Midterm','Final']].mean()


#학교별 중간고사,기말고사 평균[컬럼 순서 조정]
Total2=df.groupby('School')[['Midterm','Final']].mean().reindex(columns=['Final','Midterm'])

pivoted_total=pd.pivot_table(df,
                    index='School',
                    values=['Midterm','Final']).reset_index()[['Midterm','Final']]


#도시별 학교별 중간고사,기말고사 평균[colmuns 옵션]

pivoted_total2=pd.pivot_table(df,
                    index='School',
                    columns='City',
                    values=['Midterm','Final']).reset_index()[['Midterm','Final']]


#[학교, 성별] 별 중간고사 평균

pivoted_Gender=pd.pivot_table(df,
                    index='School',
                    columns='Gender',
                    values='Midterm').reset_index()


#aggfunc 사용[나만의 함수]벡터 원소의 합에 제곱을 하는 함수 my_f
# 학교별 중간고사 총합의 제곱 

def my_f(x):
    return sum(x)**2

pivoted_df3=pd.pivot_table(df,
                    index='School',
                    values='Midterm',
                    aggfunc=(my_f)).reset_index()





#### 팔머펭귄 연습 ####
# 팔머펭귄 데이터 불러오기
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()

# 문제 1: 펭귄 종별 평균 부리 길이 구하기
# 펭귄 데이터에서 각 종(species)별로 평균 부리 길이(bill_length_mm)를
# 구하는 pivot_table()을 작성하세요.
penguins.info()

pivoted_bill_length=pd.pivot_table(penguins,
                                   index='species',
                                   values='bill_length_mm').reset_index()
print(pivoted_bill_length)


# 문제 2: 섬별 몸무게 중앙값 구하기
# 펭귄 데이터에서 각 섬(island)별로 몸무게(body_mass_g)의 중앙값(median)을
# 구하는 pivot_table()을 작성하세요.

pivoted_island=pd.pivot_table(penguins,
                                   index='island',
                                   values='body_mass_g',
                                   aggfunc=('median')).reset_index()



# 문제 3: 성별에 따른 부리 길이와 몸무게 평균 구하기
# 펭귄 데이터에서 성별(sex)과 종(species)별로
# 부리 길이(bill_length_mm)와 몸무게(body_mass_g)의
# 평균을 구하는 pivot_table()을 작성하세요.


pivoted_sex=pd.pivot_table(penguins,
                           index=['sex','species'],
                           values=['bill_length_mm','body_mass_g'],
                           aggfunc=('mean')).reset_index()

# 문제 4: 종과 섬에 따른 평균 날개 길이 구하기
# 펭귄 데이터에서 각 종(species)과 섬(island)별로
# 날개 길이(flipper_length_mm)의 평균을 구하는 pivot_table()을 작성하세요.

pivoted_flipper=pd.pivot_table(penguins,
                           index=['species','island'],
                           values='flipper_length_mm',
                           aggfunc=('mean')).reset_index()


# 문제 5: 종과 성별에 따른 부리 깊이 합계 구하기
# 펭귄 데이터에서 종(species)과 성별(sex)별로
# 부리 깊이(bill_depth_mm)의 총합(sum)을 구하는 pivot_table()을 작성하세요.
penguins.info()

pivoted_bill_depth=pd.pivot_table(penguins,
                           index=['species','sex'],
                           values='bill_depth_mm',
                           aggfunc=('sum')).reset_index()




# 문제 6: 종별 몸무게의 변동 범위(Range) 구하기
# 펭귄 데이터에서 각 종(species)별로 몸무게(body_mass_g)의
# 변동 범위 (최댓값 - 최솟값) 를 구하는 pivot_table()을 작성하세요.
# 힌트: aggfunc에 사용자 정의 함수를 활용하세요.

penguins['body_mass_g'].max()-penguins['body_mass_g'].min()

def my_d(x):
   return max(x)-min(x)
pivoted_=pd.pivot_table(penguins,
                           index='species',
                           values='body_mass_g',
                           aggfunc=(my_d)).reset_index()


# ------------------------
df = pd.read_csv('./data/dat.csv')
df.head()
df.info()


# 'school', 'sex', 'paid', 'goout' 칼럼을 선택해서 출력하시오

df[['school', 'sex', 'paid', 'goout']]


# 'Dalc'은  'dalc' 로 'Walc' 은 'walc'로 칼럼 이름을 변경하시오

df=df.rename(columns={'Dalc':'dalc','Walc':'walc'})

# 'goout' 칼럼의 NAN값을 최빈값으로 변환하시오
df['goout'].unique()
df['goout'].mode()
df['goout'].value_counts()

df.loc[df['goout'].isna(),'goout']=3.0


# 'goout' 칼럼의 dtype을 float64 에서 int64로 바꾸시오

df['goout']=df['goout'].astype('int64')



#  assign()
# 기존칼럼에 famrel_quality 칼럼을 새롭게 생성하시오
# famrel_quality은 famrel 값이 2보다 작거나 같으면, 'Low'
# 4보다 작거나 같으면 'Medium', 그 이상은 'High'가 출력되는 값이다.
# df1 = df.copy()

df1 = df.copy()
df1.info()

def my_f(x):
    if x<=2:
       return 'Low'
    elif x<=4:
        return 'Medium'
    else:
        return 'High'
        
df1=df1.assign(famrel_quality=df1['famrel'].apply(my_f))


# 기존에 있던 famrel 칼럼을 
# 2보다 작거나 같으면, 'Low'
# 4보다 작거나 같으면 'Medium', 그 이상은 'High'가 출력되도록 수정하시오
# df2 = df.copy()

df2 = df.copy()
df2.info()

def my_f(x):
   if x<=2:
       return 'Low'
   elif x<=4:
       return 'Medium'
   else:
       return 'High'


df2=df2.assign(famrel=df2['famrel'].apply(my_f))





# number타입의 칼럼을 출력하시오, 
df.info()

df.select_dtypes('number')
df.select_dtypes('int64')

# object타입 칼럼을 출력하시오, 
df.select_dtypes('object')
# --------------------------------------------------------------3.11

import numpy as np
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()

# 펭귄데이터에서 bill로 시작되는 칼럼들을 선택한후, 표준화(standardize)를 진행 
# 표준화 평균대신 중앙값 사용
# 표준화 표준편차 대신 IQR(상위25%-하위 25%) 사용
# 해당값 추출
bills=penguins.loc[:,penguins.columns.str.startswith('bill')]
bills

def standardize(x):
    q1=x.median()
    q2=x.quantile(0.75)
    q3=x.quantile(0.25)
    irq=q2-q3
    irq.replace(0, np.nan, inplace=True)
    return (x-q1)/irq

standardize(bills)



# pd.to_datetime('03-11-2024')
# pd.to_datetime('2024-03-11')
# pd.to_datetime('2024/03/01')
# pd.to_datetime('03/11/2024')
pd.to_datetime('11/2024/03')
# 성립하지 않는 함수 찾으시오



#날짜벡터 만들기


# '2021-01-01',부터 '2022-01-10', 까지 일별로 출력하시오

pd.date_range(start='2021-01-01',end='2022-01-10' ,freq='D')



# '2021-01-01',부터 '2022-01-10', 까지 월말 별로 출력하시오

pd.date_range(start='2021-01-01',end='2022-01-10', freq='Me')



#문자열다루기
data = {
'가전제품': ['냉장고', '세탁기', '전자레인지', '에어컨', '청소기'],
 '브랜드': ['LG', 'Samsung', 'Panasonic', 'Daikin', 'Dyson']
 }
df = pd.DataFrame(data)


#가전제품 칼럼의 문자열 개수를 시리즈 형식으로 출력하시오

df['가전제품'].str.len()

#브랜드 칼럼을 모두 소문자로 바꾸시오
df['브랜드'].str.lower()

#브랜드 칼럼을 모두 대문자로 바꾸시오
df['브랜드'].str.upper()
#브랜드 칼럼의 앞글자만 모두 대문자로 바꾸시오
df['브랜드'].str.title()

#브랜드 칼럼의 a가 들어가는 값에 aaaaB를 넣으시오

df['브랜드'].str.replace('a','aaaaB')

#브랜드 칼럼의 a가 들어가는 값에 a를 모두 지우시오
df['브랜드'].str.replace('a','')

#문자열 분할

# 브랜드  칼럼중 'a'를 기준으로  나누어 시리즈 형식으로 출력하시오 

df['브랜드'].str.split('a')#시리즈, 컬럼내용은 리스트 형식


#  칼럼중 'a'를 기준으로  나누어 데이터 형식으로 출력하시오

df['브랜드'].str.split('a',expand=True)#데이터 프레임, 왼쪽부터 채움.


# 문자열 공백 제거
# 
df['가전제품'] = df['가전제품'].str.replace('전자레인지', ' 전자 레인지  ')

# 해당 함수식에서 출력되는 전자레인지의 공백을 제거하시오

df['가전제품'].str.strip()

# ===========================================/아래답, pandas8.117
df = pd.read_csv('./data/grade.csv')
print(df.head())
df['가전제품'] = df['가전제품'].str.replace('전자레인지', ' 전자 레인지  ')
df['가전제품'].str.strip()

df['가전제품'].iloc[2]
df['가전제품'].str.strip().iloc[2]


# 학교 성적 데이터

# df 데이터 프레임의 정보를 출력


# midterm 점수가 85점 이상인 학생들의 데이터를 필터링하여 출력

# final 점수를 기준으로 데이터 프레임을 내림차순으로 정렬하고, 
# 정렬된 데이터 프레임의 첫 5행 을 출력하세요.

# gender 열을 기준으로 데이터 프레임을 그룹화하고, 각 그룹별 
# midterm과 final의 평균을 계산하여 출력


# student_id 열을 문자열 타입으로 변환하고, 변환된 데이터 프레임의 정보를 출력


# assignment 점수의 최대값과 최소값을 가지는 행을 각각 출력

# midterm, final, assignment 점수의 평균을 계산하여 
# average 열을 추가하고, 첫 5행을 출력



# 추가 데이터 생성
additional_data = {
 'student_id': ['1', '3', '5', '7', '9'],
 'club': ['Art', 'Science', 'Math', 'Music', 'Drama']
 }
df_additional = pd.DataFrame(additional_data)

# 아래의 추가 데이터를 생성하고, 
# 기존 데이터 프레임과 student_id를 기준으로 병합하여 출력

# gender를 인덱스로, student_id를 열로 사용하여 
# average 점수에 대한 피벗 테이블을 생성하고 출력

# midterm, final, assignment의 평균을 구하고, average 열을 생성하시오.
# 또한, 성별, 성적 유형(assignment, average, final, midterm)별 평균 점수를 계산



# midterm, final, assignment의 평균을 구하고, average 열을 생성하시오
# 또한, 최대 평균 성적을 가진 학생의 이름과 평균 성적을 출력하시오.






# -----------------------------

df = pd.read_csv('data/bike_data.csv')
print(df.head())
df.info()

df = df.astype({'datetime' : 'datetime64[ns]',
                 'weather' : 'int64',
                   'season' : 'object',
                   'workingday':'object',
                     'holiday':'object'})

# 계절(season) == 1일 때, 가장 대여량이 많은 시간대(hour)을 구하시오.

# 각 계절(season)별 평균 대여량(count)을 구하시오.

# 특정 달(month) 동안의 총 대여량(count)을 구하시오.

# 가장 대여량이 많은 날짜를 구하시오

# 시간대(hour)별 평균 대여량(count)을 구하시오.

# 특정 요일(weekday) 동안의 총 대여량(count)을 구하시오


# 주어진 Bike Sharing 데이터를 사용하여 넓은 형식(wide format)에서 긴 형식(long format)
# 으로 변환하시오. casual과 registered 열을 하나의 열로 변환하고, 각 기록의 대여 유형과 대여
# 수를 포함하는 긴 형식 데이터프레임을 만드시오.


# 긴 형식 데이터프레임을 활용하여 각 계절(season)별로 casual과 registered 사
# 용자의 평균 대여 수(count)를 구하시오.