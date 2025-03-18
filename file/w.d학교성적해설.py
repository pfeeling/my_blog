연습 문제
학교 성적 데이터
import pandas as pd 
import numpy as np
df = pd.read_csv('./본강의자료/data/grade.csv')
print(df.head())
df 데이터 프레임의 정보를 출력하고, 각 열의 데이터 타입을 확인하세요.
# 변수명 : 한글이면 깨지지 않았는지 
# 결측치 유무 
# 칼럼별 dtype 설정
print(df.info())
midterm 점수가 85점 이상인 학생들의 데이터를 필터링하여 출력하세요.
df['midterm']
df['midterm'] >= 85
filtered_df = df.loc[df['midterm'] >= 85]
print(filtered_df)
final 점수를 기준으로 데이터 프레임을 내림차순으로 정렬하고, 정렬된 데이터 프레임의 첫 5행을 출력하세요.
df.final
sorted_df = df.sort_values(by='final', ascending=False)
print(sorted_df.head())
gender 열을 기준으로 데이터 프레임을 그룹화하고, 각 그룹별 midterm과 final의 평균을 계산하여 출력하세요.
df.groupby('gender')
grouped_df = df.groupby('gender')[['midterm', 'final']].mean()
print(grouped_df)
student_id 열을 문자열 타입으로 변환하고, 변환된 데이터 프레임의 정보를 출력하세요.
# csv 데이터를 판다스에서 불러올 경우 str, object 둘다 무관  --> 수정 
# str 권장 

df['student_id'] = df['student_id'].astype('str')
df['student_id'] = df['student_id'].astype('object')
print(df.info())
object, str 관련
import pandas as pd

df = pd.DataFrame({'student_id': [1, 2, 3, 4, 5]})  # int형 데이터
print("변환 전 데이터 타입:")
print(df.dtypes)

# 'object' 타입으로 변환
df['student_id'] = df['student_id'].astype('object')
print("\n변환 후 데이터 타입:")
print(df.dtypes)

# 각 값의 실제 타입 확인
print("\n각 값의 실제 타입:")
print(df['student_id'].apply(type))
assignment 점수의 최대값과 최소값을 가지는 행을 각각 출력하세요.
max_idx = df['assignment'].idxmax()
min_idx = df['assignment'].idxmin()

max_value_row = df.loc[max_idx]
min_value_row = df.loc[min_idx]

print("Max value row:")
print(max_value_row)

print("\nMin value row:")
print(min_value_row)
midterm, final, assignment 점수의 평균을 계산하여 average 열을 추가하고, 첫 5행을 출력하세요.
# axis = 1 행 기준 
# axis = 0 열 기준
df[['midterm', 'final', 'assignment']]
df[['midterm', 'final', 'assignment']].mean(axis=1)

df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)


print(df.head())
아래의 추가 데이터를 생성하고, 기존 데이터 프레임과 student_id를 기준으로 병합하여 출력하세요.
# 추가 데이터 생성
additional_data = {
    'student_id': ['1', '3', '5', '7', '9'],
    'club': ['Art', 'Science', 'Math', 'Music', 'Drama']
}
df_additional = pd.DataFrame(additional_data)
df_additional.head()
df_additional.shape
df.shape

df_additional['student_id'].dtype
df['student_id'].dtype
print(df['student_id'].apply(type).unique())
print(df_additional['student_id'].apply(type).unique())
merged_df = pd.merge(df, df_additional, on='student_id', how='left')
print(merged_df.head())
merged_df
gender를 인덱스로, student_id를 열로 사용하여 average 점수에 대한 피벗 테이블을 생성하고 출력하세요.
df

pivot_table = df.pivot_table(values='average', index='gender', columns='student_id')
print(pivot_table)

df.info()
df.student_id

pivot_table.info()

# 칼럼 : student_id
# 채울 값 : average
# 행 index : gender 

df.student_id.unique() # 10개
df.gender.unique() # 2개
pivot_table.shape # 2 X 10 
midterm, final, assignment의 평균을 구하고, average 열을 생성하시오. 또한, 성별, 성적 유형(assignment, average, final, midterm)별 평균 점수를 계산하시오.
df = pd.read_csv('./data/grade.csv')
#| echo: false

# average 열 추가
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)

# melt 함수를 사용하여 데이터 프레임 변환
melted_df = pd.melt(df, id_vars=['student_id', 'name', 'gender'], value_vars=['midterm', 'final', 'assignment', 'average'], var_name='variable', value_name='score')

# gender를 기준으로 그룹화하고 평균 점수 계산
grouped_mean = melted_df.groupby(['gender', 'variable'])['score'].mean().reset_index()
print(grouped_mean)
midterm, final, assignment의 평균을 구하고, average 열을 생성하시오. 또한, 최대 평균 성적을 가진 학생의 이름과 평균 성적을 출력하시오.
# 학생별 평균 성적 계산하여 average 열에 저장
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)

# 최대 평균 성적을 가진 학생 찾기
max_avg_student_idx = df['average'].idxmax()
max_avg_student = df.loc[max_avg_student_idx, ['name', 'average']]
print(f"Student with highest average score: {max_avg_student['name']}")
print(max_avg_student)
str, object 차이
Pandas 내부적으로도 object 타입, 실제 값이 모두 str로 저장

데이터가 문자열이 아닐 경우, 내부적으로 object 타입으로 처리하지만, 개별 요소의 데이터 타입(type())은 변하지 않을 수 있음.

import pandas as pd 
import numpy as np
df = pd.read_csv('./본강의자료/data/grade.csv')
print(df.head())
print(df.info())
# csv 데이터를 판다스에서 불러올 경우 str, object 둘다 무관  --> 수정 
# str 권장 

#df['student_id'] = df['student_id'].astype('str')
df['student_id'] = df['student_id'].astype('object')
print(df.info())
import pandas as pd

df = pd.DataFrame({'student_id': [1, 2, 3, 4, 5]})  # int형 데이터
print("변환 전 데이터 타입:")
print(df.dtypes)

# 'object' 타입으로 변환
df['student_id'] = df['student_id'].astype('object')
print("\n변환 후 데이터 타입:")
print(df.dtypes)

# 각 값의 실제 타입 확인
print("\n각 값의 실제 타입:")
print(df['student_id'].apply(type))
# 추가 데이터 생성
additional_data = {
    'student_id': ['1', '3', '5', '7', '9'],
    'club': ['Art', 'Science', 'Math', 'Music', 'Drama']
}
df_additional = pd.DataFrame(additional_data)
df_additional.head()
df_additional.shape
df.shape

df_additional.info()

df_additional['student_id'].dtype
df['student_id'].dtype
merged_df = pd.merge(df, df_additional, on='student_id', how='left')
print(merged_df.head())
merged_df
print(df['student_id'].apply(type).unique())
print(df_additional['student_id'].apply(type).unique())

Sangdon Kim
몇 초 전
연습 문제
공유 자전거 데이터
데이터셋은 런던 공유 자전거 시스템의 대여 기록을 다루고 있으며, 대여 및 반납 정보, 날씨 정보, 시간대 등의 다양한 특성(features)을 포함하고 있습니다.

datetime: 날짜 및 시간 정보
season: 계절 (1: 봄, 2: 여름, 3: 가을, 4: 겨울)
holiday: 공휴일 여부 (0: 공휴일 아님, 1: 공휴일)
workingday: 평일 여부 (0: 주말 또는 공휴일, 1: 평일)
weather: 날씨 상황 (1: 맑음, 2: 흐림, 3: 약간의 눈/비, 4: 폭우/폭설)
temp: 기온 (섭씨)
atemp: 체감 온도 (섭씨)
humidity: 습도 (%)
windspeed: 풍속 (m/s)
casual: 비회원 대여 수
registered: 회원 대여 수
count: 총 대여 수
데이터 불러오기
df = pd.read_csv(r'~/Desktop/슬기로운통계생활/lsbigdata/본강의자료/data/bike_data.csv')
print(df.head())
데이터 속성 변환
칼럼에 대한 설명을 확인한 후 데이터 형식을 적절하게 변경하겠습니다.

df = df.astype({'datetime' : 'datetime64[ns]',
                'weather' : 'int64',
                'season' : 'object', 
                'workingday' : 'object', 
                'holiday' : 'object'})
계절(season) == 1일 때, 가장 대여량이 많은 시간대(hour)을 구하시오.
df.season == 1
df_sub = df.loc[df.season == 1, ]


df_sub['datetime'].dt.hour
# 시간 정보 추출
df_sub['hour'] = df_sub['datetime'].dt.hour

# 계절별 및 시간대별 대여량 합계 계산
summary_data = (df_sub
                      .groupby(['season', 'hour'])
                      .agg({'count': 'sum'})
                      .reset_index()
                      )

summary_data.loc[summary_data['count'].idxmax(), 'hour']
각 계절(season)별 평균 대여량(count)을 구하시오.
df.groupby('season')
df.groupby('season')['count'].mean()
season_avg = df.groupby('season')['count'].mean().reset_index()
print(season_avg)
특정 달(month) 동안의 총 대여량(count)을 구하시오.
df['month'] = df['datetime'].dt.month
january_rentals = df.loc[df['month'] == 1, 'count'].sum()
print(f"1월 동안의 총 대여량은 {january_rentals}입니다.")
가장 대여량이 많은 날짜를 구하시오.
df['date'] = df['datetime'].dt.date

# 날짜별로 대여량 합계 계산
date_rentals = df.groupby('date')['count'].sum()

# 가장 대여량이 많은 날짜 찾기
max_rental_date = date_rentals.idxmax()
max_rental_count = date_rentals.max()
print(f"가장 대여량이 많은 날짜는 {max_rental_date}이며, 대여량은 {max_rental_count}입니다.")
시간대(hour)별 평균 대여량(count)을 구하시오.
# 시간 정보 추출
df['hour'] = df['datetime'].dt.hour

# 시간대별로 그룹화하여 평균 대여량 계산
hourly_avg = df.groupby('hour')['count'].mean().reset_index()
print(hourly_avg.head())
특정 요일(weekday) 동안의 총 대여량(count)을 구하시오.
# 요일 정보 추출 (0=Monday, 6=Sunday)
df['weekday'] = df['datetime'].dt.weekday

# 특정 요일 (예: Monday) 필터링
df['weekday'] == 0

monday_rentals = df[df['weekday'] == 0]['count'].sum()
print(f"월요일 동안의 총 대여량은 {monday_rentals}입니다.")
주어진 Bike Sharing 데이터를 사용하여 넓은 형식(wide format)에서 긴 형식(long format)으로 변환하시오. casual과 registered 열을 하나의 열로 변환하고, 각 기록의 대여 유형과 대여 수를 포함하는 긴 형식 데이터프레임을 만드시오.
# melt를 사용하여 긴 형식으로 변환
melted_df = pd.melt(
    df,
    id_vars=['datetime', 'season'],  # 고정할 열
    value_vars=['casual', 'registered'],  # 녹일 열
    var_name='user_type',  # 새로 생성될 열의 이름
    value_name='user_count'  # 새로 생성될 값 열의 이름
)

print("\nmelt를 사용하여 변환된 데이터프레임:")
print(melted_df)
이전에 생성한 긴 형식 데이터프레임을 활용하여 각 계절(season)별로 casual과 registered 사용자의 평균 대여 수(count)를 구하시오.
# season과 user_type별로 그룹화하여 평균 대여 수 계산
avg_rentals = melted_df.groupby(['season', 'user_type'])['user_count'].mean().reset_index()
print("\n각 계절별 user_type의 평균 대여 수:")
print(avg_rentals)
앱 로그 데이터
데이터셋은 앱 로그에 대한 정보를 포함하고 있습니다.

로그 : 로그 정보
pd.set_option('display.max_columns', None) # 전체 칼럼 정보 프린트 옵션
df = pd.read_csv(r'~/Desktop/슬기로운통계생활/lsbigdata/본강의자료/data/logdata.csv')
print(df.head(2))
로그 칼럼에서 숫자 정보만 추출하시오.
\d+ : 1개 이상 숫자 추출
() : 캡처된 조건 추출
tt = df['로그'].str.extractall(r'(\d+)')
tt[0]
tt.index

df['로그']
# 0 :  2024 07 18 12 34 .. 
df['로그'][0]

df['로그'].str.extractall(r'(\d+)').groupby(level=0)
df['로그'][0]

df['로그'].str.extractall(r'(\d+)').groupby(level=0).agg(' '.join)

df['숫자 정보'] = df['로그'].str.extractall(r'(\d+)').groupby(level=0).agg(' '.join)
print("숫자 정보 추출:")
print(df.head(2))
로그 칼럼에서 모든 시간 정보를 추출하시오.
HH:MM:SS 형식 추출 -> \d{2}(2자리 숫자)
df['로그']
df['로그'].str.extract(r'(\d{2}:\d{2}:\d{2})')
df['시간 정보'] = df['로그'].str.extract(r'(\d{2}:\d{2}:\d{2})')
print(df[['로그', '시간 정보']].head())
로그 칼럼에서 한글 정보만 추출하시오.
[가-힣]
[가-힣]+
df['로그'].str.extract(r'([가-힣]+)')
df['한글 정보'] = df['로그'].str.extract(r'([가-힣]+)')
print("\n한글 정보 필터링:")
print(df.head(2))
로그 칼럼에서 특수 문자를 제거하시오.
a-zA-Z : 알파벳
0-9 : 숫자
가-힣 : 한글
\s : 공백 포함
^ : 부정 연산자
[] : 괄호 안에 하나라도 일치되는 문자 추출
[^a-zA-Z0-9가-힣\s]

df['특수 문자 제거'] = df['로그'].str.replace(r'[^a-zA-Z0-9가-힣\s]', '', regex=True)
print("\n특수 문자 제거:")
print(df.head(2))
로그 칼럼에서 유저, Amount 값을 추출한 후 각 유저별 Amount의 평균값을 계산하시오.
\s : 공백 포함
: 여러번 반복 가능
\s* : 공백 있어도 되고, 없어도 됨
d+ : 숫자 1개 이상
() : 캡처된 조건 추출
df.로그[0]
df.로그[1]

df['로그'].str.extract(r'(Amount:\s)')
df['로그'].str.extract(r'Amount:\s*(\d+)')
df['Amount'] = df['로그'].str.extract(r'Amount:\s*(\d+)').astype(float)
\s* : 공백 있어도 되고, 없어도 됨
[가-힣] : 첫 번째 한글 문자 매칭
[가-힣]+ : 1개 이상 연속된 한글 문자 매칭

df['로그'].str.extract(r'(User:\s*)')
df['로그'].str.extract(r'User:\s*([가-힣])')
df['로그'].str.extract(r'User:\s*([가-힣]+)')

df['User'] = df['로그'].str.extract(r'User:\s*([가-힣]+)')
grouped = df.groupby('User')['Amount'].mean().reset_index()
print("\n그룹별 평균 Amount 계산:")
print(grouped)