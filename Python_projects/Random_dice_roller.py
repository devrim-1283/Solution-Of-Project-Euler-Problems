import random
def main():
    list_dice_number=[1,2,3,4,5,6]
    print(""""
          Welcome to Random Dice Roller

          Press q to exit
          
          Developed by Devrim Tunçer
          """)
    while True:
        try:
            start=input("Please press 'space' : ")
            if start=="q":
                break
            elif start==" ":
                print(random.choice(list_dice_number))
            else:
                raise ValueError
        except:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()