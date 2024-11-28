import random
def main():
    while True:
        print("""
Welcome to Random Name Picker

Pres q or 0 to exit
          
Developed by Devrim Tunçer
""")
        try:
            members=int(input("How many people or objects do I have to choose between?:  "))
            if members<0:
                raise ValueError
            if members==0:
                print("Exit succesfully...........")
                break
            list_members=list()
            a=1
            while members>0:
                list_members.append(input(f"{a} members: "))
                a+=1
                members-=1
            choice_number=int(input(f"How many choices do you want to make? (members={a-1}): "))
            if choice_number==0:
                print("Exit succesfully...........")
                break
            if choice_number<=0:
                raise ValueError
            while True:
                print(random.choice(list_members))
                choice_number-=1
                if choice_number==0:
                    print("The choises are over...........")
                    break
                else:
                    continue_or_not=input("Press 'space' to continue(Press q to exit): ")
                if continue_or_not==" ":
                    continue
                elif continue_or_not=="q":
                    print("The choises are over...........")
                    break
                else:
                    raise ValueError
        except:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()