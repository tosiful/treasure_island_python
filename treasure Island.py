print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


choose1=input('you are going to "left" or "right" ').lower()

if(choose1=="left"):
    choose2=input('you are going to "swim" or "wait" ').lower()
    if choose2=="wait":
        door=input('you are choose "red","blue" or "yellow"').lower()
        if door=="red":
            print("game over")
        elif door=="blue":
            print("game over")
        elif door=="yellow":
        
            print("game WIn")
        else:
            print("game over")
            
    else:
        print("game over")
    
else:
    print("game over")
    