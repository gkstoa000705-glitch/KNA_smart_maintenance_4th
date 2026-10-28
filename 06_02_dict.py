# 딕셔너리
# 형식 : {키: 값, 키: 값} - 키는 문자열
# -리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)로 찾는다

#sensors ={"모터온도":78, "진동":0.5}
#print(sensors)
#print(sensors["모터온도"])
#print(type(sensors))
#print(sensors["유량"])

# 추가 / 수정 / 삭제
# 형식:딕셔너리[키]= 값
#형식:(삭제) del딕셔너리[키]
# 
#sensors ["펌프압력"] = 95
##sensors ["모터온도"] = 80
#del sensors["진동"]
#print(sensors)

#get / in
#형식 : 딕셔너리.get(키, 기본값) / 키 in 딕셔너리
#print(sensors.get("유량))"))
#print(sensors.get("유량"))

#실습1
#sensors = {"S01" : 75, "S02": 78, "S03":85}
#print(sensors["S02"])
#sensors["S04"] = 90
#sensors["S01"] = 80
#print("추가 수정된 딕셔너리:", sensors)
#print(sensors.get("S05", 0))
#print("S01" in sensors)

# keys / values/ items / len
#sensors ={"모터온도":78, "진동":0.5}
#print(list(sensors.keys()))
#print(list(sensors.values()))
#avg = sum(sensors.values(())) / len(sensors)
#print(avg)

#sensors = {"모터온도":78, "진동":0.5}
#for name, value in sensors.items():
#    print(name, value)

#for k in sensor.keys()
#for v in sensors.keys()

# update - 여러 항목을 한번에 갱신(키가 있으면 수정, 없으면 추가)

#실습 2
#sensors = {"온도": 25, "습도": 60}
#data = {"온도":28, "조도": 300}
#sensors.update(data)
#print(sensors)
#del sensors["습도"]
#print("센서 수:", len(sensors))

#실습 3
#sensors = {"온도":80 , "진동": 55, "압력":95}
#avg = sum(sensors.values()) / len(sensors)
#print("평균:", round(avg, 1))

#top =""
#high = 0
#for name, value in sensors.items():
#    if value > high:
#        high = value
#        top = name
#print("최댓값 센서:", top, high)

# zip : 센서명 - 값 매핑하기
#name = ["온도", "진동", "압력"]
#values = [78, 0.5, 95]
#sensors = dict(zip(name, values))
#print(sensors)

# 딕셔너리의 값에 리스트 / 딕셔너리 - 중첩 딕셔너리
#plant ={
#    "1번모터":{"온도":78, "상태": "정상"},
#    "2번펌프":{"압력":95, "상태": "경고"}
#}

#print(plant["2번펌프"]["압력"])

#실습 4
#name = ["온도", "진동", "압력"]
#values = [78, 0.5, 95]
#sensors = dict(zip(name,values))
#print(sensors)
#for name, value in sensors.items():
#    print(name, "-", value)

#실습 5
#sensors = {"온도": 80, "습도": 60, "압력": 90}
#limits = {"온도": 70, "습도": 65, "압력": 95}
#경고온도 = []
#for name, value in sensors.items():
#    if value>limits[name]:
#        경고온도.append(name)
#print("경고센서:", 경고온도)

#실습 6
#machine = {
#    "1번펌프": {"압력": 80, "상태": "정상"},
#    "2번펌프": {"압력": 95, "상태": "경고"}
#}
#print(machine["2번펌프"]["압력"])
#for name, value in machine.items():
#    if value["상태"] == "경고":
#       print(name + "점검필요")

#실습 7
rows = ["온도, 78", "압력,95", "진동,0.5"]
sensors = {}
for row in rows:
    name, value = row.split(",")
    sensors[name] = float(value)
print(sensors)

#실습 8
sensors = {"온도": 100, "압력": 95, "진동": 91}
limits = {"온도": 80, "압력": 90, "진동": 100}
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))
danger = set()
for name, value in sensors.items():
    if value > limits[name]:
        danger.add(name)
print("위험센서:", sorted(danger))