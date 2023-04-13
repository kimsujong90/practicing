my_foods=['pizza','falafel','carrot cake']

friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nmy friend's favorite foods are:")
print(friend_foods)

for value in my_foods:
    print(value)
    
word=my_foods.index('cannoli')

print(my_foods[:word])

# --------------------구분선1

human=('baby','man','woman')
print(human)

# ---------------------구분선2

cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

car='Audi'
car.lower()=='audi'
print(car)

# ----------------------구분선3

requested_topping='mushrooms'
if requested_topping !='anchovies':
    print("hold the anchovies!")

requested_toppings=['mushrooms','onions','pineapple']

# -----------------------구분선4

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

if user in banned_users:
    print(f"{user.title()}, you can't post a response if you wish.")

# ------------------------구분선5

age=17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# ------------------------구분선6

age = 12

if age < 4:
    print("\nYour admission cost is $0.")
elif age <18:
    print("\nYour admission cost is $25.")
else:
    print("\nYour admission cost is $40.")

age2 = 12

if age2 <4:
    price = 0
elif age2 < 18:
    price = 25
else:
    price = 40

print(f"\nYour admission cost is ${price}.")

# ------------------------구분선7

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# ------------------------구분선8




    
