import random
# print multiline instruction
# performstring concatenation of string
print("Winning Rules Of The Colors ChoicesGame As Follows : " + "\nEnter A Number From One To Five And Match Computer ChoiceTo Win The Computer.")
computer_score = 0
player_score = 0
while True:
    print("Red = 1 \nYellow = 2 \nOrange = 3 \ngreen = 4 \nblue = 5 \nTake A Turn : ")

    # Take The Input From User
    player_choice = int(input("User Turn : "))

    # Looping Until User Enter Invalid Input
    while player_choice > 5 and player_choice < 1 :
        player_choice = int(input("Enter Valid Input : "))

    # InitializeValue Of Choice_col Variable
    # Corresponding To The player_choice Value
    if player_choice == 1:
        choice_col = 'Red'
    elif player_choice == 2:
        choice_col = 'Yellow'
    elif player_choice == 3:
        choice_col = 'Orange'
    elif player_choice == 4:
        choice_col = 'Green'
    else:
        choice_col = 'Blue'

    # print user choice
    print("User Color Choice Is : " + choice_col)
    print("\nNow Its Computer Turn To Choose A Color .....")

    # Computer Chooses Randomly Any Number
    computer_choice = random.randint(1 , 5)

    # Looping Until compu_choice value is equal to the choice value
    while computer_choice == player_choice:
        computer_choice = random.randint(1 , 5)

    # InitializeValue Of compu_hoice_col Variable
    # Corresponding To The computer_choice Value
    if computer_choice == 1:
        compu_choice_col = 'Red'
    elif computer_choice == 2:
        compu_choice_col = 'Yellow'
    elif computer_choice == 3:
        compu_choice_col = 'Orange'
    elif computer_choice == 4:
        compu_choice_col = 'Green'
    else:
        compu_choice_col = 'Blue'

    print("Computer Color Choice Is :  " + compu_choice_col)

    # conditions for winning
    if(choice_col == compu_choice_col):
        player_score +=1
        print("player_score : " + str(player_score))
        print("computer_score : " + str(computer_score))
    else:
        computer_score +=1
        print("player_score : " + str(player_score))
        print("computer_score : " + str(computer_score))

    print("Do You Want To Play Again ? (Y/N)")
    answer = input()

    # if user input n or N then condition is true
    if answer == 'n' or answer =='N':
        break

# After Coming Out Of The While Loop
# We print Thanks for playing and the overallresult of the game
if computer_score == player_score:
    print("Game Is Tied")
    print("\nThanks For Playing")
elif computer_score < player_score:
    print("Player Is Vectories")
    print("<== User Wins ==>")
    print("\nThanks For Playing")
elif computer_score > player_score:
    print("\n<== Computer Wins ==>")
    print("\nPlayer Is Defeated")
    print("\nThanks For Playing")



