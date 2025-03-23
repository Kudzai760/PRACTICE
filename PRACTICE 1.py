def classify_number():
    while True:
        try:
            number = int(input("Enter an integer: "))

            if number > 0:
                return "Positive"
            elif number < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


result = classify_number()
print(f"The number is: {result}")