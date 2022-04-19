from pickle import FALSE
import  numpy as np

quest1 = np.array([4,1,2,5,3])
answer = np.array([1,2,3,4,5])

def l_r(move,choice):
     if choice =='l' :
         hold = quest1[move-1]
         quest1[move-1]=quest1[move]
         quest1[move]=hold
     elif choice =='r' :
        hold = quest1[move+1]
        quest1[move+1]=quest1[move]
        quest1[move]=hold


i = False
while i ==False :
    print(quest1)
    x = int(input()) - 1
    movement = input()
    l_r(x,movement)
    i=np.array_equal(quest1,answer)

