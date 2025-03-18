import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/bike_data.csv')
print(df.head())
df.info()

df = df.astype({'datetime' : 'datetime64[ns]',
                 'weather' : 'int64',
                   'season' : 'object',
                   'workingday':'object',
                     'holiday':'object'})


# 계절(season) == 1일 때, 가장 대여량이 많은 시간대(hour)을 구하시오.
# 번역: season 값이 1인 컬럼값 중에서 hour[1~24]별 

df_spring=df[df['season']==1]

df_spring['datetime'].dt.hour#시간정보

df_spring=df_spring.assign(hour=df_spring['datetime'].dt.hour)#시간 컬럼 생성


df_spring[['hour','count']].sort_values(by='hour',ascending=False)
#시간대별 대여량[중복값 확인]

#시간별 대여량 count합
hour_count=pd.pivot_table(df_spring,
                      index='hour',
                      values='count',
                      aggfunc=('sum')).reset_index().sort_values(by='count',ascending=False)

hour_count.loc[hour_count['count'].idxmax(),'count']



# -----------------------------------

#시즌이 1일때로 한정
df_sub = df.loc[df.season == 1]

 # 시간 정보 추출
df_sub['datetime'].dt.hour

#['hour'] 라는 컬럼을 새로 생성
df_sub['hour'] = df_sub['datetime'].dt.hour

 # 계절별 및 시간대별 대여량 합계 계산
summary_data = df_sub.groupby(['season', 'hour']).agg({'count': 'sum'}).reset_index()


summary_data.loc[summary_data['count'].idxmax(),'hour']
# ------------------------------




# 각 계절(season)별 평균 대여량(count)을 구하시오

season_avg = df.groupby('season')['count'].mean().reset_index()

season_avg=pd.pivot_table(df,
                          index='season',
                          values='count',
                          aggfunc=['mean']).reset_index()





# 특정 달(month) 동안의 총 대여량(count)을 구하시오.

df['month'] = df['datetime'].dt.month
january_rentals = df[df['month'] == 1]['count'].sum()
# -------------------------
month_total=pd.pivot_table(df,
                          index=df['datetime'].dt.month,
                          values='count',
                          aggfunc=['sum']).reset_index()





# 가장 대여량이 많은 날짜를 구하시오

df['datetime'].dt.date

# 날짜별로 대여량 합계 계산
date_rentals = df.groupby('date')['count'].sum()


 # 가장 대여량이 많은 날짜 찾기
max_rental_date = date_rentals.idxmax()
 max_rental_count = date_rentals.max()

day_maxh_avg=pd.pivot_table(df,
                          index=df['datetime'].dt.date,
                          values='count',
                          aggfunc=['max']).reset_index().sort_values(ascending=False)




# 시간대(hour)별 평균 대여량(count)을 구하시오.

# 시간 정보 추출
df['hour'] = df['datetime'].dt.hour
 # 시간대별로 그룹화하여 평균 대여량 계산
hourly_avg = df.groupby('hour')['count'].mean().reset_index()
 print(hourly_avg.head())




# 특정 요일(weekday) 동안의 총 대여량(count)을 구하시오.

 # 요일 정보 추출 (0=Monday, 6=Sunday)
 df['weekday'] = df['datetime'].dt.weekday


 # 특정 요일 (예: Monday) 필터링
 
 monday_rentals = df[df['weekday'] == 0]['count'].sum()



# 주어진 Bike Sharing 데이터를 사용하여 넓은 형식(wide format)에서 긴 형식(long format)
# 으로 변환하시오. casual과 registered 열을 하나의 열로 변환하고, 각 기록의 대여 유형과 대여
# 수를 포함하는 긴 형식 데이터프레임을 만드시오.

melted_df = pd.melt(df,
    id_vars=['datetime', 'season'],  # 고정할 열
    value_vars=['casual', 'registered'],  # 녹일 열
    var_name='user_type',  # 새로 생성될 열의 이름
    value_name='user_count' # 새로 생성될 값 열의 이름
)

# 이전에 생성한 긴 형식 데이터프레임을 활용하여 각 계절(season)별로 casual과 registered 사
# 용자의 평균 대여 수(count)를 구하시오.

 # season과 user_type별로 그룹화하여 평균 대여 수 계산
avg_rentals = melted_df.groupby(['season', 'user_type'])['user_count'].mean().reset_index()


avg_rentals=pd.pivot_table(df,
                           index='season',
                           columns='user_type',
                           values='count',
                           aggfunc='mean').reset_index()



# -------------------------------------------------------

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None) # 전체 칼럼 정보 프린트 옵션
pd.reset_option('display.max_columns')

df = pd.read_csv('data/logdata.csv')
print(df.head(2))
df.info()



# 로그 칼럼에서 연도 정보만 추출하시오.
df['연도']=df['로그'].str.extract(r'(\d+)')


# 로그 칼럼에서 모든 시간 정보를 추출하시오.

df['시간']=df['로그'].str.extract(r'(\d{2}[:/.]\d{2}[:/.]\d{2})')



# 로그 칼럼에서 한글 정보만 추출하시오.
df['한글']=df['로그'].str.extract(r'([가-힣]+)')


# 로그 칼럼에서 특수 문자를 제거하시오.

df['특수문자제거']=df['로그'].str.replace(r'[^a-zA-Z0-9가-힣\s]','', regex=True)
print(df['특수문자제거'])


# 로그 칼럼에서 user, Amount 값을 추출한 후 각 유저별 Amount의 평균값을 계산하시오.
df.info()

df['user']=df['로그'].str.extract(r'User: (\S+)')
df['Amount']=df['로그'].str.extract(r'Amount: (\d+)').fillna(0).astype(int)

avg=df.groupby('user')['Amount'].mean().reset_index()


