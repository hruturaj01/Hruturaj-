#project.py:
#        UNIT CONVERTER PROJECT – PYTHON

def length_converter():
    print("\n Length Converter")
    print("1. Meter → Kilometer")
    print("2. Kilometer → Meter")
    print("3. Centimeter → Meter")
    print("4. Meter → Centimeter")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value in: "))

    if choice == 1:
        print("Result:", value / 1000, "km")
    elif choice == 2:
        print("Result:", value * 1000, "m")
    elif choice == 3:
        print(" Result:",value / 100, "m")
    elif choice == 4:
        print("Result:", value * 100, "cm")
    else:
        print("Invalid Input")


def temperature_converter():
    print("\nTemperature Converter")
    print("1.Celsius → Fahrenheit")
    print("2.Fahrenheit → Celsius")

    cho = int(input("Enter choice: "))
    value = float(input("Enter temperature: "))

    if cho == 1:
        result = (value * 9/5) + 32
        print("Result:", result, "°F")
    elif cho == 2:
        result = (value- 32) *5/9
        print("Result:", result, "°C")
    else:
        print("Invalid Input")



def weight_converter():
    print("\n Weight Converter -")
    print("1. Kilogram → Gram")
    print("2. Gram → Kilogram")
    print("3. Kilogram → Pounds")
    print("4. Pounds → Kilogram")

    c = int(input("Enter choice: "))
    value = float(input("Enter weight: "))

    if c == 1:
        print("Result:", value * 1000, "g")
    elif c == 2:
        print("Result:", value / 1000, "kg")
    elif c == 3:
        print("Result:", value * 2.2046, "lbs")
    elif c == 4:
        print("Result:", value / 2.20, "kg")
    else:
        print("Invalid Input")

while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length Converter")
    print("2. Temperature Converter")
    print("3. Weight Converter")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        length_converter()
    elif ch == 2:
        temperature_converter()
    elif ch == 3:
        weight_converter()
    elif ch == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")



