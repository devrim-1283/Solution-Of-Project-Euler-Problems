def main():
    print("""
    WELCOME TO TEMPERATURE CONVERTER
    Press Q to exit
    Developed by Devrim Tunçer
    GITHUB: https://github.com/devrim-1283
""")
    print(""" 
1- CELSIUS TO FAHRENHEIT
2- CELSIUS TO KELVIN
3- CELSIUS TO RANKINE
4- FAHRENHEIT TO CELSIUS
5- FAHRENHEIT TO KELVIN
6- FAHRENHEIT TO RANKINE
7- KELVIN TO CELSIUS
8- KELVIN TO FAHRENHEIT
9- KELVIN TO RANKINE
10- RANKINE TO CELSIUS
11- RANKINE TO FAHRENHEIT
12- RANKINE TO KELVIN
""")
    while True:
        choice = input("SELECT THE CONVERSION PROCESS: ")
        if choice.upper() == "Q":
            print("Successfully exited.")
            break
        try:
            if choice == "1":
                temp = float(input("CELSIUS: "))
                print(f"FAHRENHEIT: {temp * 1.8 + 32}")
            elif choice == "2":
                temp = float(input("CELSIUS: "))
                print(f"KELVIN: {temp + 273.15}")
            elif choice == "3":
                temp = float(input("CELSIUS: "))
                print(f"RANKINE: {(temp + 273.15) * 1.8}")
            elif choice == "4":
                temp = float(input("FAHRENHEIT: "))
                print(f"CELSIUS: {(temp - 32) / 1.8}")
            elif choice == "5":
                temp = float(input("FAHRENHEIT: "))
                print(f"KELVIN: {(temp - 32) / 1.8 + 273.15}")
            elif choice == "6":
                temp = float(input("FAHRENHEIT: "))
                print(f"RANKINE: {temp + 459.67}")
            elif choice == "7":
                temp = float(input("KELVIN: "))
                print(f"CELSIUS: {temp - 273.15}")
            elif choice == "8":
                temp = float(input("KELVIN: "))
                print(f"FAHRENHEIT: {(temp - 273.15) * 1.8 + 32}")
            elif choice == "9":
                temp = float(input("KELVIN: "))
                print(f"RANKINE: {temp * 1.8}")
            elif choice == "10":
                temp = float(input("RANKINE: "))
                print(f"CELSIUS: {(temp - 491.67) / 1.8}")
            elif choice == "11":
                temp = float(input("RANKINE: "))
                print(f"FAHRENHEIT: {temp - 459.67}")
            elif choice == "12":
                temp = float(input("RANKINE: "))
                print(f"KELVIN: {temp / 1.8}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
 