# 리스트
# 형식 : 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.
#temps = [25, 26, 24, 28, 27]
#machines = ["펌프", "모터", "압축기"]
#mixed = ["펌프", 87, True]
#print(len(temps))
#print(len([]))

#실습1
#temp = [25, 26, 24, 27, 26]
#print(temp)
#print(len(temp))
#list = []
#print(list)
#print(len(list))

#실습2
#temp = [22, 24, 25, 27, 26, 23]
#print(temp[0])
#print(temp[3])
#print(temp[-1])

#실습3
#code = [100, 105, 110, 115, 120, 122]
#first = code[0]
#last = code[-1]
#print(first + last)
#print((first + last) / 2)

#실습4
#temp = [22, 24, 27, 25, 26, 29, 28, 30, 21, 23]
#first = temp[:3]
#print(first)
#last = temp[-3:]
#print(last)
#print(len(first))

#실습5
#code = [3, 4 ,5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
#first = code[:6]
#print(first)
#second = code[6:]
#print(len(first), len(second))

# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새로운 값 / 값 in 리스트

# 값 추가 - append, insert, extend
# 형식 : 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)

#실습 6
#temp = [25, 26, 240, 28, 27]
#print(240 in temp)
#idx = temp.index(240)
#temp[idx] = 24
#print(temp)
#print(240 in temp)

#실습 7
#numbers = []
#numbers.append(30)
#print(numbers)
# numbers.insert(0, 28)
#print(numbers)
#numbers.extend([31, 32])
#print(numbers)

# 정렬, 탐색 - sort, reverse / count, index
# 형식 : 리스트.sort() .reverse() .count(값) .index(값)

#실습8
temp = [25, 26, 999, 24, 28, 26]
temp.remove(999)
print(temp)
value = temp.pop(1)
print("꺼낸값" , value)
del temp[0]
print(temp)

#실습9
temp = [28, 24, 30, 22, 26, 24, 27]
temp.sort()
print(temp)
temp.reverse()
print(temp)
print(temp.count(24))
print(temp.index(24))