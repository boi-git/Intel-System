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
    print("select the value 1~5")
    x = int(input()) - 1
    print("Maneuver l or r")
    movement = input()
    l_r(x,movement)
    i=np.array_equal(quest1,answer)

print(quest1)