import random

def  main():
    print(""" 
Welcome to Number Guessing Game
          

Objective:

    The goal of the game is to guess a secret number chosen by the computer. The secret number is between 1 and 100.

How to Play:

    The computer randomly selects a secret number between 1 and 100.
    You need to guess the number by entering your guess.

Feedback:

    After each guess, the computer will tell you whether:
        Your guess is too low and you need to guess a higher number.
        Your guess is too high and you need to guess a lower number.
        You've guessed the correct number, and the game will end.

Winning the Game:

    The game ends when you correctly guess the secret number.
    The game will also tell you how many guesses it took to find the correct number.

Rules:

    The number range is between 1 and 100.
    You must enter a valid number as your guess. If you enter something other than a number, the game will prompt you to try again.
    The game continues until you guess the secret number.
          
developed by Devrim Tunçer
""")
    number_list=list(range(1,101))
    while True:
        print("""
Let' Gooooooooooo
I chose a number, guess it


Select Game Difficulty
          1. Easy - Unlimited Trial
          2. Medium - 10 Trial
          3. Difficult - 5 Trial
          4. Impossible - 1 Trial

""")
        answer=random.choice(number_list)
        try:
            difficulty=int(input("(Press 0 to exit) Select Game Difficulty: "))
            if difficulty==0:
                print("Exit succesful............")
                break
            elif difficulty==1:
                while True:
                    yours_answer=int(input("(Press 0 to exit) Guess it: "))
                    if yours_answer==0:
                        print("Exit succesful............")
                        break   
                    elif yours_answer>100 or yours_answer<0:
                        print("Please enter a valid number.")
                        continue
                    elif yours_answer==answer:
                        print("Correct guess, congratulations. Let's start again....")
                        break  
                    elif yours_answer<answer:
                        print("Your guess is too low. Try a higher number.")
                        continue
                    elif yours_answer>answer:
                        print("Your guess is too high. Try a lower number.")
                        continue
            elif difficulty==2:
                a=10
                while a>=0:
                    if a==0:
                        print("You no longer have the right to try, you lost:( ")
                        break
                    yours_answer=int(input("(Press 0 to exit) Guess it: "))
                    if yours_answer==0:
                        print("Exit succesful............")
                        break   
                    elif yours_answer>100 or yours_answer<0:
                        print("Please enter a valid number.")
                        continue
                    elif yours_answer==answer:
                        print("Correct guess, congratulations. Let's start again....")
                        break  
                    elif yours_answer<answer:
                        print("Your guess is too low. Try a higher number.")
                        a-=1
                        continue
                    elif yours_answer>answer:
                        a-=1
                        print("Your guess is too high. Try a lower number.")
                        continue
            elif difficulty==3:
                a=5
                while a>=0:
                    if a==0:
                        print("You no longer have the right to try, you lost:( ")
                        break
                    yours_answer=int(input("(Press 0 to exit) Guess it: "))
                    if yours_answer==0:
                        print("Exit succesful............")
                        break   
                    elif yours_answer>100 or yours_answer<0:
                        print("Please enter a valid number.")
                        continue
                    elif yours_answer==answer:
                        print("Correct guess, congratulations. Let's start again....")
                        break  
                    elif yours_answer<answer:
                        print("Your guess is too low. Try a higher number.")
                        a-=1
                        continue
                    elif yours_answer>answer:
                        a-=1
                        print("Your guess is too high. Try a lower number.")
                        continue

            elif difficulty==4:
                    yours_answer=int(input("(Press 0 to exit) Guess it: "))
                    if yours_answer==0:
                        print("Exit succesful............")   
                    elif yours_answer>100 or yours_answer<0:
                        print("Please enter a valid number.")
                    elif yours_answer==answer:
                        print("Correct guess, congratulations. Let's start again....") 
                    elif yours_answer<answer:
                        print("Your guess is too low. You lost :(")
                        a-=1
                    elif yours_answer>answer:
                        a-=1
                        print("Your guess is too high. You lost :(")
            else:
                raise ValueError

        except:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()