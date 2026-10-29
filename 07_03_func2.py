#거의 항상 같은 값을 매번 적는 번거로움을 줄임, 필요할 때만 덮어쓴다
#def report(name, value, unit="도"):
#    print(name + ": "+str(value) + unit)
#report("압축기A", 75.3)
#report("펌프1", 7.2, "bar")

#실습 1
#def sensor(value, limit=90):
#    result = "정상" if value <= limit else "경고"
#    return str(value) + "->" +result
#print(sensor(78))
#print(sensor(95))
#print(sensor(78, 50))

# 지역변수와 범위(스코프)
# 함수 안의 변수, 함수 바깥 변수를 읽을 수 있찌만, 바깥에서는 함수 안 지역변수를 읽을 수 없음
#def calc():
#    result = 10 + 5
#    return result

#print(calc())

#x = 10
#def change():
#    x = 20

#change()
#print(x)

#실습2
#함수 선언
#지역변수 생성
#함수 밖에서 해당 지역변수 호출, 결과 확인
#def calc():
#    number = 30
#    print("함수안:", number)
#calc()
#print("함수박:", number)    #NameError: name 'number' is not defined

#실습 3
#def calc(a , b):
#    return(a + b) / 2
#def avg(avg):
#    if avg >= 80:
#        print("평균", avg, "->정상")
#    else:
#        print("평균", avg, "->경고")
#result = calc(78, 92)
#avg(result)
