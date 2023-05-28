# Key Programming Activities Program
This program performs key programming activities such as calculating the factorial of a number and checking if a number is prime. It is written in Python.

## Factorial Calculation
The calculate_factorial function calculates the factorial of a given number. It uses a loop to multiply the numbers from 1 to the given number. The factorial value is then returned.

## Prime Number Check
The check_prime function determines whether a number is prime or not. It checks if the number is less than or equal to 1 and returns False in such cases. For numbers greater than 1, it iterates from 2 to the square root of the number and checks if any of these values divide the number evenly. If a divisor is found, the function returns False. Otherwise, it returns True.

## Main Program Execution
In the main program section, the user is prompted to enter a positive integer. The input is then converted to an integer using the int function.

The program proceeds to calculate the factorial of the entered number using the calculate_factorial function. The result is stored in the factorial variable.

Next, the program checks if the entered number is prime by calling the check_prime function. The result is stored in the is_prime variable.

Finally, the program displays the factorial of the number and whether it is prime or not.

## Usage
1.Make sure you have Python installed on your machine.
2.Open a Python-compatible IDE or text editor.
3.Copy and paste the program code into a new Python file.
4.Save the file with a .py extension, such as program.py.
5.Run the program.
6.Enter a positive integer when prompted.
7.The program will calculate the factorial of the number and display the result.
8.It will also indicate whether the number is prime or not. 

Feel free to modify and use this program according to your needs.

