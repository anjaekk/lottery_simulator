import random


# 랜덤 번호 뽑기
generate_number_list = []


def generate_number(n):
    for i in range(n):
        num = random.randint(1, 45)
        generate_number_list.append(num)
    return sorted(generate_number_list)

print(generate_number(6))


# 당첨 번호 뽑기
winning_number_list = []


def winning_number():
    for i in range(6):
        num = random.randint(1, 45)
        winning_number_list.append(num)
    winning_number_list.sort()
    bonus = random.randint(1, 45)
    winning_number_list.append(bonus)
    return winning_number_list

print(winning_number())


