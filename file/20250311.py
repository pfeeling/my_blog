import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data\dat.csv')


# 판다스 데이터 프레임에서 저장하기
# csv로 저장하기

# 예제 데이터 생성
df = pd.DataFrame({
 'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 35],
 'Score': [90, 85, 88]
 })

df.to_csv("./data/sample.csv", index=False, sep=";", endcoding="utf-8")
#index=False 의 의미 : 인덱스 는 제외한다.(기본값은 True)
# sep=";" sep=";": 구분자 변경 가능 (, 대신 ; 사용 가능)
# encoding="utf-8": 한글 데이터 저장 시 사용


# Excel로 저장하기
# conda install openpyxl
df.to_excel("data/sample_data.xlsx", sheet_name='Sheet_name_1')


# -----------------

# 펭귄데이터에서 bill로 시작되는 칼럼들을 선택한후, 표준화(standardize)를 진행 
# 결과를 엑셀 파일로 저장해주세요 
# 표준화 평균대신 중앙값 사용
# 표준화 표준편차 대신 IQR(상위25%-하위 25%) 사용
# 시트 이름 penguin-std
# 파일이름 penguin.xlsx

import numpy as np
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()

# 펭귄데이터에서 bill로 시작되는 칼럼들을 선택
bill_data=penguins.loc[:,penguins.columns.str.startswith('bill')]

# 표준화 평균대신 중앙값 사용,# 표준화 표준편차 대신 IQR(상위25%-하위 25%) 사용
bill_data.describe()

def standardize(x):
    q2=np.nanmedian(x)
    x_info=x.describe()
    q1=x_info.iloc[4]#25%
    q3=x_info.iloc[6]#75%
    iqr=q3-q1
    return (x - q2)/iqr

filter_df=bill_data.apply(standardize,axis=0)

#엑셀
filter_df.to_excel("data/penguins_bill.xlsx", sheet_name='Sheet_name_1')




# -----------------------------------------------------------
# 날짜와 시간 다루기

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)
data = {'date': ['2024-01-01 12:34:56', '2024-02-01 23:45:01', '2024-03-01 06:07:08'],
 'value': [100, 201, 302]}
df = pd.DataFrame(data)
df.info()

#데이터 형식 변환: 날짜 전처리 하기 용이
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
# datetime64[ns]으로 변환된 것을 확인

pd.to_datetime('03-11-2024')
pd.to_datetime('2024-03-11')
pd.to_datetime('2024/03/01')
pd.to_datetime('03/11/2024')
# pd.to_datetime('11/2024/03')#에러남


pd.to_datetime('11-2024-03', format='%d-%y-%m')#에러남
pd.to_datetime('11-24-03', format='%d-%y-%m')

dt_obj=pd.to_datetime('2025년 03월 11일', format='%Y년 %m월 %d일')

dt_obj.year
dt_obj.month
dt_obj.day
dt_obj.minute
dt_obj.second
dt_obj.weekday()  #월화수목금토일=0,1,2,3,4,5,6,7
dt_obj.day_name()

df['date'].dt.year
df['date'].dt.hour
df['date'].dt.second


df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
df['day']=df['date'].dt.day
df['hour']=df['date'].dt.hour
df['minute']=df['date'].dt.minute
df['second']=df['date'].dt.second
df



#날짜 계산
current_date = pd.to_datetime('2025-03-11')
current_date = df['date']



#날짜벡터 만들기
pd.date_range(start='2021-01-01',end='2022-01-10', freq='D')

pd.date_range(start='2021-01-01',end='2022-01-10', freq='ME')

# 날짜 합치기
df.year
df.month
df.day

#입력값으로 딕셔너리를 넣어도 작동한다.
pd.to_datetime(dict(year=df.year, month=df.month, day=df.day))


# -------------------------------------------
#문자 다루기
#문자열다루기
data = {
'가전제품': ['냉장고', '세탁기', '전자레인지', '에어컨', '청소기'],
 '브랜드': ['LG', 'Samsung', 'Panasonic', 'Daikin', 'Dyson']
 }
df = pd.DataFrame(data)


df['가전제품'].str.len()#가전제품 칼럼의 문자열만
# 보는데 len으로 글자수를 센다

df['브랜드'].str.lower()#브랜드 칼럼의 문자열만보는데, 
#소문자로 다 바꾼다.
df['브랜드'].str.upper()#대문자로 다 바꾼다.
df['브랜드'].str.title()

df['브랜드'].str.contains('a')#시리즈 형식
df.columns.str.contains("a")#array형식


df['브랜드'].str.replace('a','aaaaB')
df['브랜드'].str.replace('a','')#a를 지울때

#문자열 분할
df['브랜드'].str.split('a')#시리즈, 컬럼내용은 리스트 형식
df['브랜드'].str.split('a',expand=True)#데이터 프레임, 왼쪽부터 채움.


# 문자열 공백 제거

df['가전제품'] = df['가전제품'].str.replace('전자레인지', ' 전자 레인지  ')
df['가전제품'].str.strip()

df['가전제품'].iloc[2]
df['가전제품'].str.strip().iloc[2]



nycflights=pd.read_csv('data/nycflights.csv')
nycflights.info()

