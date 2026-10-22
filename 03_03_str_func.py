#index
#주의)위치를 반환하지만 없으면 오류
email = 'hong@company.com'
at = email.index('@')
print(at)
print(email[:at])

#startswith / endswith 
#형식 : 문자열.startswith('x')->bool
print('EQp-001'.startswith('EQP'))
print('cmapss.csv'.endswith('csv'))

#실습5
print('sensor_log.csv'.startswith('sensor'))
print('sensor_lpg.csv'.endswith('.csv'))

#실습6
label = "warning"
print(label =='warning')
print(label =='WARNING')