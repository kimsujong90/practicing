# if문 피자 토핑 연습

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#if문 여러 리스트 다루기
print("-"*5)

available_toppings = ['mushrooms','olives','green peppers'
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

#if문 practice 1
print("-"*5)

greeting_names=['admin','aaaa','ssss','dddd','ffff']
name = 'aaaa'

if name =='admin':
    print(f"{name} 님 안녕하세요, 상태보고서를 보시겠습니까?")
else:
    print(f"{name} 님 안녕하세요, 다시 로그인 해주셔서 감사합니다.")

#if문 practice 2
print("-"*5)

greeting_names.clear()

if greeting_names:
    for greeting_name in greeting_names:
        print(f"Good morning {greeting_name}!")
else:
    print("리스트에 사용자가 있어야합니다")

#if문 practice 3
print("-"*5)

current_users = ['brad','john','tom','juliet','smith']
new_users = ['brad','jackson','peter','tom','joy']

current_users_lower=[current_user.lower for current_user in current_users]

for new_user in new_users:
    if new_user.lower in current_users_lower:
        print(f"{new_user.title()} 의 이름은 이미 사용중입니다.")
    else:
        print("가입을 축하드립니다")

#if문 practice 4
print("-"*5)

ranking = ['1st', '2nd', '3rd', '5th', '4th', '8th', '7th','6th','9th']
ranking.sort()

for rank in ranking:
    if rank == '1st':
        print(rank)
    elif rank == '2nd':
        print(rank)
    elif rank == '3rd':
        print(rank)
    else:
        print(rank)


#if문 practice 4 - 해답지

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("\n1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

#dictionary

alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])
