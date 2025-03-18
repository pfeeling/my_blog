import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)


#뉴욕 항공 정보
df=pd.read_csv('data/nycflights.csv')
df.info()
df.describe()


#----------------------------------------------------------------
# 지연에 대한 극단값을 먼저 확인.

#항공사별 출발지 최대 지연 시간 확인
temp6 = df.groupby('carrier').dep_delay.max()
temp6

#항공사별 출발지 최소 지연 시간 확인
temp7 = df.groupby('carrier').dep_delay.min()
temp7

#항공사별 출발지 최대, 최소 지연 시간 
carr = pd.DataFrame([temp6,temp7])
carr = carr.T
carr.columns = ['max','min']

# 항공사별 출발지 최대, 최소 지연 시간 [carrier의 극단값 확인]
carr.sort_values(by='max',ascending=False)



# 어느 정도 잘라야 하나? 확인[특정 항공사HA, AA의 value 확인]
df[df.carrier == 'HA'].dep_delay.sort_values(ascending=False).head(10)
df[df.carrier == 'DL'].dep_delay.sort_values(ascending=False).head(10)
df[df.carrier == 'AA'].dep_delay.sort_values(ascending=False).head(10)


#항공사별 지연 출발 평균, 최소, 최대값
df.groupby('carrier')['dep_delay'].agg(['mean','min','max']).sort_values(by='max',ascending=False)



#월별 딜레이를 확인하는데 극단값 제외

#출발지 딜레이 극단값 제거[상위 0.1프로, 하위 0.1프로 제거]
M_dep_delay = df.loc[(df.dep_delay>= df.dep_delay.quantile(0.001))&(df.dep_delay<= df.dep_delay.quantile(0.999))]
print(len(df)-len(M_dep_delay))

#도착지 딜레이 극단값 제거 [상위 0.1프로, 하위 0.1프로 제거]
M_arr_delay = df.loc[(df.arr_delay>= df.arr_delay.quantile(0.001))&(df.arr_delay<= df.arr_delay.quantile(0.999))]
print(len(df)-len(M_arr_delay))



#len(df)
#len(temp1)
#월별 도착지 지연 시간의 평균
M_d_mean_a = M_arr_delay.groupby(['month'])['arr_delay'].mean()
print(M_d_mean_a)

#월별 출발지 지연 시간의 평균
M_d_mean_d = M_dep_delay.groupby(['month'])['dep_delay'].mean()
print(M_d_mean_d)

#도착지, 출발지 지연의 평균값[시리즈]를 데이터 프레임화
ans = pd.DataFrame([M_d_mean_d,M_d_mean_a])
ans = ans.T

#[도착지 최소값 기준]도착지, 출발지 지연의 월별 평균값
ans.sort_values(by='dep_delay')



#9,10,11월이 출발, 도착 시간 지연이 다른 달에 비해 낮은 편이다.
# ----------------------------------------------------------

# int날짜 정보를 문자열로 변환[월화수목금토일]
df['date'] = pd.to_datetime(df[['year','month','day']])
df.date.head(3)
df['weekday'] = df['date'].dt.day_name()
df.weekday.head(10)


#요일별 평균 출발 지연 시간
temp1 = M_dep_delay.groupby(['weekday'])['dep_delay'].agg(['mean','min','max']).reset_index()
temp1 = temp1.rename(columns={'mean': 'dep_mean', 'min': 'dep_min', 'max': 'dep_max'})
temp1.sort_values(by='dep_mean')

#요일별 평균 도착 지연 시간
temp2 = M_arr_delay.groupby(['weekday'])['arr_delay'].agg(['mean','min','max']).reset_index()
temp2 = temp2.rename(columns={'mean': 'arr_mean', 'min': 'arr_min', 'max': 'arr_max'})
temp2.sort_values(by='arr_mean')

# 데이터 프레임화
ans4 = pd.merge(temp1, temp2, on='weekday', how='inner').sort_values(by='dep_mean')
print(ans4)

#일주일중 토요일이 출발, 도착시 지연시간이 제일 낮다. 

