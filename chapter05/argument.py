def print_somthing(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_somthing("Sungchul", "Teamlab")
print_somthing(your_name= "Teamlab", my_name= "sungchul")
print_somthing("sungcul\n", your_name= "teamlab")
# print_somthing(your_name="teamlab","sungchul")

def print_somthing_2(my_name, your_name = "TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_somthing_2("Sungchul", "teamlab")
print_somthing_2(your_name= "Teamlab", my_name= "sungchul")
print_somthing_2("sungcul")
# print_somthing(your_name="teamlab","sungchul")

def asterisk_test(a, b, *args):
    print("a: {0}, b: {1}".format(a,b))
    for i, v in enumerate(args):
        print("args[{0}]: {1}".format(i, v))

asterisk_test(1,2,3,4,5)
print()
asterisk_test(1,2,3,4,5,6,7,8,9,10)

