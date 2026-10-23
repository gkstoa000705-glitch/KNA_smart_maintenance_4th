#실습5
#date = ['2025', '01', '15']
#result = '-'.join(date)
#print(result)

#실습6
#print('2025', '1', '15', sep='-')
#print('2025', '1', '15', sep=',')

#실습7
#date = '2025/01/15'
#result = '-'.join(date.split('/'))
#print(result)

#실습8
#raw="1,NORMAL,25.3"
#parts = raw.split(",")
#status=parts[1].strip().lower()
#print(status)

#실습1
#name="PUMP_A"
#temp=87
#print(f"설비{name}, 온도{temp}도")

#실습2
#score1=85
#score2=87
#score3=89
#print(f"평균{(score1+score2+score3) / 3}")

#실습3
#number = 87.456
#print(f"측정값{number:.1f}")
#print(f"측정값{number:.2f}")

#실습4
raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(',')
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())
print(f'[센서{sid}] 상태{status},측정값{value:.2f}')


