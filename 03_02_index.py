# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식 : 문자열[번호] (젗 글자 = 0번)

#word = 'PYTHON'
#print(word[0],word[2],word[5] )
#음수 인덱스 : 뒤에서부터 -1,-2...
#print(word[-1],word[-2])

#print(word[6])   #IndexError: string index out of range

#실습1
#word = 'SIGNAL'
#print(word[0],word[2],word[5] )

#실습2
#word = 'SIGNAL'
#print(word[-1],word[-2] )

#슬라이싱 - 구간으로 잘라내기
#형식 : 문자열[시작 : 끝] (시작 포함, 끝 제외)
#word='PYTHON'
#print(word[1:4])

#생략가능
#-시작생략 = 처음부터(0번부터)
#-끝 생략 = 끝까지
#-둘다 생략 = 전체
#word = 'PYTHON'
#print(word[:3])
#print(word[3:])
#print(word[:])

#음수
#word = 'PYTHON'
#print(word[:-1])
#print(word[-3:])

#실습3
#word = 'SIGNAL'
#print(word[:3])
#print(word[3:6])

#실습4
#word = 'temp_sensor'
#print(word[:4])

#실습5
#word = 'temp_sensor'
#print(word[5:])

#실습6
#word = 'seonsor_01'
#print(word[-2:])

# step 간격주기
# 형식 : 문자열 [시작:끝:간격]
#word='PYTHON'
#print(word[::2])
#print(word[1::3])

#실습 7
#word = 'SIGNAL'
#print(word[::2])

#실습 8
#word = 'SIGNAL'
#print(word[::-1])

#문자열 연산과 검색
# -문자열 연결(+), 반복(*)

#len() - 글자수
#형식: len(문자열)
#print(len('PYTHON'))
#print(len('AI 분석'))
#print(len(' '))

# in / not in - 포함 / 불포함 여부(결과bool)
#형식 : '찾을 것' in 문자열
#print('고장' in '설비 고장 발생')
#print('정상' not in '설비 고장 발생')

#count
#형식 : 문자열.count('x')->개수
#print('banana'.count('a'))

#find
#형식 : 문자열.find('x') ->처음 나오는 위치
#print('banana'.find('a'))
#print('banana'.find('t'))

#실습 1
#number = '01012345678'
#print(len(number))

#실습 2
#print('고장' in '설비 고장 발생')
#print('정상'in'설비 고장 발생')

#실습 3
#print('sensor-01-temp'.count('-'))

#실습 4
#print('temp_2024'.find('_'))
#print('temp_2024'.find('5'))