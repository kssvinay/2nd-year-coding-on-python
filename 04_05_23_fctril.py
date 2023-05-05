class Factorial:
    def _init_(self, number):
        self.number = number

    def get_factorial(self):
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        return factorial

number_input = int(input("Enter the number to find factorial: "))
factorial_obj = Factorial(number_input)
factorial = factorial_obj.get_factorial()
print(f"The factorial of {number_input} is {factorial}.")
