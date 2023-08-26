import random

l1=[1,2,3,4,5,6,7,8,9,10,11,12]
random.shuffle(l1)
player1=[1,3,5,7,9,11]
player2=[2,4,6,8,10,12]
for i in l1:  

    print("lucky num : ",i)
    if i in player1:
        player1.remove(i)
        
    elif player2:
        player2.remove(i)
    
    else:
        pass
    print("Player1",player1)
    print("Player2",player2)
    if player1 == []:
       print("Player1 Won")
       break 
    elif player2 == []:
        print("Player2 Won")
        break
    else:
        pass
    
       
   
    

       
 
        
