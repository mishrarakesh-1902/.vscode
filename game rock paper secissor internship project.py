import random

rock = '''_ _ _ _ _ _ 
   ------ '    _ _ _ _ _ )
             (_ _ _ _ _ _ )
             (_ _ _ _ _ _ )
_ _ _         (_ _ _ _  )
      . _ _ _  (_ _ _ )

'''

paper = '''
           _ _ _ _ _ _ 
   ------ '      _ _ _ ) _ _ _ 
                  _ _ _ _ _ _ )
                  _ _ _ _ _ _ )
_ _ _              _ _ _ _  )
      . _ _ _ _ _ _ _ _ _ ) 
    
'''



scissors = '''
           _ _ _ _ _ _ 
   ------ '      _ _ _ ) _ _ _ 
                      _ _ _ _ )
                 __ _ _ _ _ _ _ )
_ _ _           (_ _ _ _  )
      . _ _ _ _ ( _ _ _ _ ) 
'''

game_images = [rock , paper , scissors]
user_choice = int(input("Enter your choice :  Type 0 for Rock , 1 for Paper , 2 for Scissors ."))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number , you lose .")

else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose :")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice>user_choice :
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")        
                