import random


while True:
    # taking input from user for odd or even
    choose_Even_odd = input("Enter what to choose O(Odd) or E(Even): ")

    # printing what you have choose
    if choose_Even_odd == "odd" or choose_Even_odd == "Odd" or choose_Even_odd == "ODD" or choose_Even_odd == "o" or choose_Even_odd == "O":
        print("You have choosen Odd")
        choose_Even_odd = "Odd"
        Comp = "Even"
        break
    elif choose_Even_odd == "Even" or choose_Even_odd == "EVEN" or choose_Even_odd == "even" or choose_Even_odd == "e" or choose_Even_odd == "E":
        print("You have choosen Even")
        choose_Even_odd = "Even"
        Comp = "Odd"
        break
    else:
        print("\nerror! enter the correct word??\n")

while True:
    # taking input from the user for batting and boll
    you = int(input("\nEnter an number: "))
    Comp2 = random.randint(1,6)
    comp = 2
    # Error Handling
    if you > 6:
        print("Plese! Enter Number lower than 6 or 6")
        continue
    break

# seeing who win in this game for batting and boll
# add = Comp2 + you
add = comp + you
print(f"Computer choose: {Comp2}\n")
print(f"The add of you and computer is {add}")

if add%2 == 0:
    result_odd_even = "Even"
else:
    result_odd_even = "Odd"
print(f"The result is in {result_odd_even}")

if result_odd_even == choose_Even_odd:
    print("Congrats! You Win!")
    choose_result = "Win"
else:
    print("You loose!")
    choose_result = "Loose"

# printing who win you or computer for batting or booling

comp_bat_boll = random.randint(1, 2)
if choose_result == "Win":
    bat_or_ball = input("\nWhat you want to choose Batting(b) or Bolling(bo): ")
    if bat_or_ball == "b" or bat_or_ball == "B" or bat_or_ball == "batting" or bat_or_ball == "Batting" or bat_or_ball == "BATTING":
        bat_ball = "Batting"
    elif bat_or_ball == "bo" or bat_or_ball == "Bo" or bat_or_ball == "BO" or bat_or_ball == "bolling" or bat_or_ball == "Bolling" or bat_or_ball == "BOLLING":
        bat_ball = "Bolling"
elif choose_result == "Loose":
    if comp_bat_boll == 1:
        comp_bat_boll = 'Batting'
        print("Computer choose batting")
    elif comp_bat_boll == 2:
        comp_bat_boll = 'Bolling'
        print("Computer choose Bolling")


# in this we are writing who win or lose
You_play = None
Comp_play = None
add_bat_boll = 0
add_bat_boll2 = 0
add_bat_boll3 = 0

if bat_ball == "Batting":
    while True:
        Comp_play = random.randint(1,6)
        You_play = int(input("Your Turn: "))
        print(f"Comp Choose {Comp_play}\n")
        add_bat_boll3 += You_play
        if You_play>6:
            print("Please! write number lower than 6 or 6")
            continue
        elif You_play == Comp_play:
            print("game over! ")
            print(f"\nYou have targeted: {add_bat_boll2 + 1}\n")
            break
    print(f"\t\t\tComp Have to Target {add_bat_boll2 + 1}")
    while True:
        Comp_play = random.randint(1,6)
        You_play = int(input("Your Turn: "))
        print(f"Comp Choose {Comp_play}\n")
        add_bat_boll3 += Comp_play
        if You_play>6:
            print("Please! write number lower than 6 or 6")
            continue
        if You_play == Comp_play and add_bat_boll3>add_bat_boll2 + 1:
            print("You loosse! ")
            print(f"\nYou loose by {add_bat_boll3 - add_bat_boll2+1}")
            break
        if You_play == Comp_play and add_bat_boll3 == add_bat_boll2 + 1:
            print("You loosse! ")
            break
        if You_play == Comp_play and add_bat_boll3 < add_bat_boll2 + 1:
            print("\n\t\t\tCongrats! You Win! ")
            break

elif bat_ball == "Bolling":
    while True:
        Comp_play = random.randint(1,6)
        You_play = int(input("Your Turn: "))
        print(f"Comp Choose {Comp_play}\n")
        add_bat_boll3 += Comp_play
        if You_play>6:
            print("Please! write number lower than 6 or 6")
            continue
        elif You_play == Comp_play:
            print("game over! ")
            print(f"\nComp have targeted: {add_bat_boll2 + 1}\n")
            break
    print(f"\t\t\You Have to Target {add_bat_boll2 + 1}")
    while True:
        Comp_play = random.randint(1,6)
        You_play = int(input("Your Turn: "))
        print(f"Comp Choose {Comp_play}\n")
        add_bat_boll3 += You_play
        if You_play>6:
            print("Please! write number lower than 6 or 6")
            continue
        if You_play == Comp_play and add_bat_boll3>add_bat_boll2 + 1:
            print("Congrats! You Win! ")
            print(f"\nYou loose by {add_bat_boll3 - add_bat_boll2+1}")
            break
        if You_play == Comp_play and add_bat_boll3 == add_bat_boll2 + 1:
            print("You loosse! ")
            break
        if You_play == Comp_play and add_bat_boll3 < add_bat_boll2 + 1:
            print("\n\t\t\tYou Loosse! ")
            break