import random


# 랜덤 번호 뽑기
generate_number_list = []


def generate_number(n):
    while len(generate_number_list) < n:
        num = random.randint(1, 45)
        # 중복 번호 제거
        if num not in generate_number_list:
            generate_number_list.append(num)
    return sorted(generate_number_list)
print(generate_number(6))


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


#  당첨된 번호 수
def count_matching_number(list_1, list_2):
    matching_number = set(list_1) & set(list_2)
    return len(matching_number)

print(count_matching_number(generate_number(6), winning_number()))