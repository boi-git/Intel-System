import  numpy as np
quest1 = np.array([4,1,2,5,3])

print("before" )
print (quest1)
        
for i in range(0, len(quest1)):    
    for j in range(i+1, len(quest1)):    
        if(quest1[i] > quest1[j]):    
            temp = quest1[i];    
            quest1[i] = quest1[j];    
            quest1[j] = temp;    
     

     
print("after" )
print(quest1)