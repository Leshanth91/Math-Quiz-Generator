import math
import random


def elementary_school_quiz(flag, n):
    '''(int, int) -> int
    Generates n math questions for exponents or logarithms and returns the score.
    
    Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    correct_count = 0

    # Pick a random power between 0 and 10 and compute its value
    exponent1 = random.randint(0, 10)
    value1 = 2 ** exponent1
    
    print("Question 1:")
    # Check if testing logarithms (0) or exponentiation (1)
    if flag == 0:
        question_text1 = "2 to what is " + str(value1) + " i.e. what is the result of log_2 (" + str(value1) + ")? "
        user_answer1 = int(input(question_text1))
        if user_answer1 == exponent1:
            correct_count = correct_count + 1
    else:
        question_text1 = "What is the result of 2^" + str(exponent1) + "? "
        user_answer1 = int(input(question_text1))
        if user_answer1 == value1:
            correct_count = correct_count + 1

    # Run the exact same logic for a second question if n was set to 2
    if n == 2:
        exponent2 = random.randint(0, 10)
        value2 = 2 ** exponent2
        
        print("Question 2:")
        if flag == 0:
            question_text2 = "2 to what is " + str(value2) + " i.e. what is the result of log_2 (" + str(value2) + ")? "
            user_answer2 = int(input(question_text2))
            if user_answer2 == exponent2:
                correct_count = correct_count + 1
        else:
            question_text2 = "What is the result of 2^" + str(exponent2) + "? "
            user_answer2 = int(input(question_text2))
            if user_answer2 == value2:
                correct_count = correct_count + 1

    return correct_count


def high_school_quiz(a,b,c):
    '''(number, number, number) -> None
    Solves and prints the roots of a linear or quadratic equation.
    
    Preconditions: a, b, and c are valid numbers.
    '''
    # Handle degenerate cases where 'a' is zero
    if a == 0:
        if b == 0:
            print("The quadratic equation " + str(a) + "·x + " + str(c) + " = 0")
            if c == 0:
                print("is satisfied for all numbers x")
            else:
                print("is satisfied for no number x")
        else:
            # If a is 0 but b is not, it reduces down to a simple linear line equation
            print("The linear equation " + str(b) + "·x + " + str(c) + " = 0")
            root = -c / b
            print("has the following root/solution: " + str(root))
            
    else:
        print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
        
        # Calculate the discriminant to determine what types of roots exist
        discriminant = (b ** 2) - (4 * a * c)
        
        # Two distinct real roots
        if discriminant > 0:
            root1 = (-b + (discriminant ** 0.5)) / (2 * a)
            root2 = (-b - (discriminant ** 0.5)) / (2 * a)
            print("has the following real roots:")
            print(str(root1) + " and " + str(root2))
            
        # One repeating real root
        elif discriminant == 0:
            root = -b / (2 * a)
            print("has only one solution, a real root:")
            print(str(root))
            
        # Negative discriminant creates imaginary numbers (Complex Roots)
        else:
            real_part = -b / (2 * a)
            imag_part = ((-discriminant) ** 0.5) / (2 * a)
            
            print("has the following two complex roots:")
            print(str(real_part) + " + i " + str(imag_part))
            print("and")
            print(str(real_part) + " - i " + str(imag_part))



# main

# Print introductory greeting banners
print("*******************************************")
print("*                                         *")
print("*   Welcome to my math quiz-generator     *")
print("*                                         *")
print("*******************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

# Branch 1: Elementary School Option
if status=='1':
    # Dynamic header generation that automatically matches string lengths
    header_msg = "*  " + name + ", welcome to my quiz-generator for elementary school students.  *"
    stars_border = "*" * len(header_msg)
    empty_border = "*" + (" " * (len(header_msg) - 2)) + "*"
    
    print(stars_border)
    print(empty_border)
    print(header_msg)
    print(empty_border)
    print(stars_border)
    
    practice_prompt = name + " what would you like to practice? Enter\n0 for inverse of exponentiation\n1 for exponentiation\n"
    quiz_type = int(input(practice_prompt))
    
    # Input validation checks for topic choice and problem quantities
    if quiz_type != 0 and quiz_type != 1:
        print("Invalid choice. Only 0 or 1 is accepted.")
    else:
        num_questions = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
        
        if num_questions < 0 or num_questions > 2:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
        elif num_questions == 0:
            print("Zero questions. OK. Good bye")
        else:
            print(name + ", here is your " + str(num_questions) + " questions:")
            score = elementary_school_quiz(quiz_type, num_questions)
            
            # Print unique closing performance message evaluation
            if score == num_questions:
                print("Congratulations " + name + "! You'll probably get an A tomorrow.")
            elif score == 0:
                print("I think you need some more practice " + name + ".")
            else:
                print("You did ok " + name + ", but I know you can do better.")

# Branch 2: High School Option
elif status=='2':

    header_msg = "*  quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "  *"
    stars_border = "*" * len(header_msg)
    empty_border = "*" + (" " * (len(header_msg) - 2)) + "*"
    
    print(stars_border)
    print(empty_border)
    print(header_msg)
    print(empty_border)
    print(stars_border)


    flag=True
    # While loop to repeatedly prompt the user to solve systems until they pass an exit string
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # Sanitize text checks by standardizing letters down to lower case
        question = question.lower()
        question = question.strip()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            coeff_a = float(input("Enter a number the coefficient a: "))
            coeff_b = float(input("Enter a number the coefficient b: "))
            coeff_c = float(input("Enter a number the coefficient c: "))
            
            # Send numerical floats straight into execution block
            high_school_quiz(coeff_a, coeff_b, coeff_c)            
 
else:
    print(name + " you are not a target audience for this software.")

print("Good bye "+name+"!")
