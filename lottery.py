from time import sleep
import random

# 사용자 입력 번호
enter_number = list(map(int, input("원하는 번호를 공백(' ')으로 구분해 적어주세요.").split()))

# 45 초과 번호 삭제
for i in enter_number:
    if i > 45:
        enter_number.remove(i)


generate_number_list = enter_number


# 랜덤 번호 뽑기
def generate_number():
    while len(generate_number_list) < 6:
        num = random.randint(1, 45)
        # 중복 번호 제거
        if num not in generate_number_list:
            generate_number_list.append(num)
    return sorted(generate_number_list)

user_number = generate_number()
print(f"당신의 번호는 아래와 같습니다. \n {user_number}")



check = input("당첨여부를 확인하시겠습니까? Y / N")

if check == "N" or check == "n":
    print("프로그램을 종료합니다.")

else:
    winning_number_list = []

    # 당첨 번호 뽑기
    def winning_number():
        while len(winning_number_list) < 6:
            num = random.randint(1, 45)
            # 중복 번호 제거
            if num not in winning_number_list:
                winning_number_list.append(num)
        winning_number_list.sort()
        # 보너스 번호 추가
        bonus = random.randint(1, 45)
        winning_number_list.append(bonus)
        return winning_number_list
    
    lottery_number = winning_number()
    
    print(f"당첨번호는 아래와 같습니다. \n {lottery_number}")

    # 지연시간 3초
    for i in range(3):
        i = 3 - i
        sleep(1)
        print(i)

    #  당첨확인
    def num_check(list_1, list_2):
        matching_number = set(list_1) & set(list_2[:6])
        cnt_matching_number = len(matching_number)
        # 1등(6개 일치)
        if cnt_matching_number == 6: 
            return("결과: 6개 일치\n축하합니다! '1등' 당첨입니다.")
        # 2등(5개 일치 + 보너스 번호 일치)
        elif cnt_matching_number == 5 and winning_num[6] in generate_num:
            return("결과: 5개 일치 및 보너스 번호 일치\n축하합니다! '2등' 당첨입니다.")
        # 3 ~ 5등
        elif cnt_matching_number == 5:
            return("결과: 5개 일치\n축하합니다! '3등' 당첨입니다.")
        elif cnt_matching_number == 4:
            return("결과: 4개 일치\n축하합니다! '4등' 당첨입니다.")
        elif cnt_matching_number == 3:
            return("결과: 3개 일치\n축하합니다! '5등' 당첨입니다.")
        # 낙첨
        else:
            return("아쉽게도 낙첨입니다.")

    print(num_check(user_number, lottery_number))


