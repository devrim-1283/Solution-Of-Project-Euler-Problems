import random
import string

def password(lenght,repetition=False):
    strings=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    all_char=strings+numbers+symbols
    password=""
    a=1
    while a<=lenght:
        if repetition==True:
            choice_char=random.choice(all_char)
            password+=choice_char
            all_char=all_char.replace(choice_char,"")
        else:
            password+=random.choice(all_char)
        a+=1
    return password

def main():
    print("""
Welcome to Random Password Generator
Press 0 to exit
Developed by Devrim Tunçer""")
    while True:
        try:
            lenght=int(input("Enter the desired password length: "))
            if lenght==0:
                print("Exit successful.........")
                break
            elif lenght<6:
                print("Password should be at least 6 characters long.")
                continue
            else:
                print("""
Can your password consist of repeated letters?
                  1- True (Yes,It can.)
                  2- False(NO It can not.)
""")
                repetition=int(input("Can your password consist of repeated letters?: "))
                if repetition==0:
                    print("Exit successful.........")
                    break
                elif repetition==1:
                    print(password(lenght,True))
                elif repetition==2:
                    print(password((lenght,True)))
                else:
                    raise ValueError
        except:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()