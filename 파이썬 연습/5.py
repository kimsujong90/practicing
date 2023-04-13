import random as r
import time as t

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
n=1
print("[타자 게임] 준비되면 엔터!")
input()
start=t.time()

q=r.choice(w)

while n<=5:
    print("문제 ",n)
    print(q)
    x=input()
    if q==x:
        print("pass")
        n=n+1
        q=r.choice(w)
    else:
        print("fail, try again")

end=t.time()
et=end-start
et=format(et,".2f")
print("타자시간 :",et,"초")

        
    



    

