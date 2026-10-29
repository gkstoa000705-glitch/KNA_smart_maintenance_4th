# 매개변수와 반환값

# 매개변수와 인지
# 형식:
# def 함수이름(매개변수):
#  ....
# 호출
# 함수이름(인자)

#def check(name):
#    print(name + " 점검을 시작합니다. ")

#check("압축기1")                   #"압축기1" = 인자
#check("펌프1")

# 실습2
#def sensor(name, temp):
#    print(name, temp, "도")
#sensor("모터", 78)
#sensor("펌프", 92)
#sensor(78, "모터")

#실습 3
#def a(name, number):
   # print(name, number)
#a(name="모터", number=78)
#a(number=78, name="모터")
#a("펌프", number=92)

#return
# -print: 사람이 확인할 수 있게 출력
# return: 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
#def add(a,b):
#    return a+b
#    print("실행 안됨")
#total = add(3,4)
#print(total)

#실습 4
#def add(a, b):
#    return a + b / 2

#avg = add(80, 90)
#print(avg)
#print(avg*2)

#여러값 반환 / 언패킹
# 쉼표로 여러 값을 return 하면 듀플로 묶여서 돌아옴 -> 언패킹 가능

#def min_max(values):
#       return min(values), max(values)

#print(min_max([75, 10 , 100]))
#low, high = min_max([75, 10, 100])
#print(low, high)

#none = report("펌프", 10)
#print(none)

#실습 5
def sensor(values):
    low = min(values)
    high = max(values)
    avg = sum(values) / len(values)

    return low, high, avg
a, b, c = sensor([78, 85, 92])
print(a, b, c)