def perform_action():
    """

    :return:
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
        return True
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return False
