# print("Python" , "JAVA", sep=",", end = "?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(4), str(score).rjust(4), sep=":")
#     # ljust , rjust << 정렬과 빈칸 설정

# #은행 대기 순번표
# #001,002,003, ...
# for num in range(1,21) :
#     print("대기번호 : "+ str(num).zfill(3)) # 값이 없는 빈공간은 0으로 채우는 것


# answer = input("아무 값이나 입력하세요 : ") # 입력을 받은 값은 항상 문자열로 저장됨
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다")

# # 빈 자리는 빈공간으로 두로, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기 +- 부호도 붙이기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이기, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(100000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# 파일 입출력 ----------------------------------------------

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close

# # 한번에 모든 내용 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close


# pickle -------------------------------------------------
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30,"취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close

# with ----------------------------------------------------
# import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file))

# # with open("study.txt", "w", encoding="utf8") as study_file:
# #     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



#퀴즈

for i in range(1,5) :
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
        
