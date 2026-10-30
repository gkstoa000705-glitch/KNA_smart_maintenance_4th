# 파일 입출력

#  open()
# 형식 : open(파일명, 모드, encoding)
# 모드 : r=읽기 w=새로쓰기 a=이어쓰기
# encoding = "utf-8" =>한글이 깨지지 않도록 하는 것을 의미

#FILE = 'data/08_press.cvs'

#f = open(FILE)

#실습 2
#with open("data/test,txt", "w", encoding="utf-8") as f:
#    f.write("쓰기 테스트\n")
#    f.write("이상 없음\n")

#with open("data/test,txt", "r", encoding="utf-8") as f:
#    print(f.read())

#실습 3
#with open("data/test,txt", "a", encoding="utf-8") as f:
#    f.write("쓰기테스트\n")
#    f.write("a로 열기\n")
#with open("data/test,txt", "r", encoding="utf-8") as f:
#    print(f.read())


# csv.reader
#with open(FILE, "r", encoding="utf-8") as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)

#실습 4
#import csv
#with open("data/08_press.csv", "r", encoding="utf-8") as f:
 #   reader = csv.reader(f)

  #  for row in reader:
   #    print(row)

#csv.writer
with open("date/08_summary.csv", "w", encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "상태"])
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 1])

with open("date/08_summary.csv", "r", encoding="utf-8")