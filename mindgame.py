


def game():
    print("Welcome to the mind game romi!!! let's check you have brain or not:" )
    name= input ("Enter your age romi: ")
    print("Nice to meet you let's start the game romi don")
    print("Game is like i will keep one number between 1 to 20 and you need to guess exact number")

    correctnum= 7
    

    while True:
        
        user = input("Enter your number that you guess or press 'q' to quit the game: ").strip()

        if user.lower() == 'q':
            print("You tried your best bye")
            break

        #game sure it is a number

        if not user.isdigit():
            print("please put number!!!")
            continue

        guess = int(user)
        
        if guess <1 or guess > 20:
            print("Please put between 1 to 20")
            continue
        if guess == correctnum:
            print("Congrats you are damn good panda don hahahahahaha")
            again= input("Do you wanna play again press 'p' ")

            if again == 'p':
                continue
            else:
                print("Quiting the game......")
                break

        elif guess > correctnum:
            print("You guess bigger number tried low")
        else:
            print(" Please try big number")
game()




        
             
        
        


            
    
            
            
            


    

    
