import random

# 사용자 입력 번호
enter_number = list(map(int, input().split()))

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

print(generate_number())


# 당첨 번호 뽑기
winning_number_list = []


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

print(winning_number())


#  당첨확인
def check(generate_num, winning_num):
    matching_number = set(generate_num) & set(winning_num[:6])
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
