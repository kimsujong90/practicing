word = input("Input a word : ")
word_list = list(word)
print(word_list)

result=[]
for _ in range(len(word_list)):
    aa = word_list
    result.append(aa.pop())

print(result)
print(word[::-1])
