import  numpy as np

quest1 = np.array([4,1,2,5,3])




#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(quest1)):    
    print(quest1[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(quest1)):    
    for j in range(i+1, len(quest1)):    
        if(quest1[i] > quest1[j]):    
            temp = quest1[i];    
            quest1[i] = quest1[j];    
            quest1[j] = temp;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(quest1)):    
    print(quest1[i], end=" ");    