import  numpy as np

quest1 = np.array([4,1,2,5,3])
answer = np.array([1,2,3,4,5,0])




i = 1
while i > 0:
    print(quest1)
    x = int(input()) - 1
    movement = input()

    if movement =='l' :
        hold = quest1[x-1]
        quest1[x-1]=quest1[x]
        quest1[x]=hold

    elif movement =='r' :
        hold = quest1[x+1]
        quest1[x+1]=quest1[x]
        quest1[x]=hold

    i =(x)