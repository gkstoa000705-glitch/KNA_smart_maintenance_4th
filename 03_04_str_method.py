#메서드 -점(.)문법
#형식:문자열.메서드이름()(-->꼭 괄호를 붙여야 실행)
#word='python'
#print(word.upper())                       #모두 대문자로
#print(word.count('p'))
#print(word)
#print('NORMAL'.lower())                   #모두 소문자로

#print('python is'.capitalize())        #Python is
#print('hong gil'.title())              #Hong Gil

#실습1
#word='ready'
#print(word.upper())

#실습2
#word='WARNING'
#print(word.lower())

#실습3
#word='kim chul soo'
#print(word.title())

#실습4
#word1 = 'fault'
#word2 = 'FAULT'
#print(word1 == word2)
#print(word1.lower() == word2.lower())

#확인 메서드 : is*** 메서드는 참/ 거짓 반환
#print('ABC.isupper(), 'abc.islower())

#공백 정리 -strip
#형식 : .strip() = 앞뒤 공백 제거
#raw='  정상  '
#print('['+raw+']')
#print('['+raw.strip()+']')

# .lstrtip() ->왼쪽 공백 제거 / .rstrip() -> 오른쪽 공백 제거
#주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거X
# strip() 으로 특정 문자 제거 ->strip('문자')
#s='###정상###'
#print(s.strip("#"))

#실습5
#a="ABC"
#b="abc"
#c="Abc"
#print(a.isupper())
#print(a.islower())
#print(b.isupper())
#print(b.islower())
#print(c.isupper())
#print(c.islower())

#실습6
#name='sensor_log.csv'
#print(name.startswith('sensor'))  #False
#print(name.endswith('.csv'))      #False
#print(name.startswith('sensor')) 
#print(name.endswith('.csv'))  

#실습7
#code = " 가동중 "
#print("["+code.strip()+"]")

#실습8
#code = " 대기 "
#print("["+code.lstrip()+"]")
#print("["+code.rstrip()+"]")

#실습9
#code='***경고***'
#print(code.strip("*"))

#체이님 -메서드 이어붙이기
#형식:문자열.strip().lower() ->왼쪽부터 차례로 적용
#clean = '     NORMAL     '.strip().lower()
#print(clean)

#실습 10
#code = ' WARNING '.strip().lower()
#print(code)

#실습 11
#code = ' 경보 '
#print(code.strip())
#code = ' 경보 '
#code = code.strip()
#print(code)