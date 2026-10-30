import math
import random


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    (int, int) -> int
    
    Generates 'n' interactive math problems focused on base-2 exponentiation 
    or logarithms based on the 'flag' value. It prompts the user for answers,
    validates them, and returns the total number of correct responses.
    
    precondition: flag must be exactly 0 (for logarithms) or 1 (for exponentiation). 
    n must be exactly 1 or 2 (representing the number of questions).
    '''
    correct_count = 0

    exponent1 = random.randint(0, 10)
    value1 = 2 ** exponent1
    
    print("Question 1:")
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
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    (number, number, number) -> None
    
    Prints a quadratic or linear equation based on coefficients a, b, and c,
    and then outputs the correct real or complex roots matching specific formats.
    
    precondition: a, b, and c are real numbers (integers or floats).
    '''
    if a == 0:
        if b == 0:
            print("The quadratic equation " + str(a) + "·x + " + str(c) + " = 0")
            if c == 0:
                print("is satisfied for all numbers x")
            else:
                print("is satisfied for no number x")
        else:
            print("The linear equation " + str(b) + "·x + " + str(c) + " = 0")
            root = -c / b
            print("has the following root/solution: " + str(root))
            
    else:
        print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
        
        discriminant = (b ** 2) - (4 * a * c)
        
        if discriminant > 0:
            root1 = (-b + (discriminant ** 0.5)) / (2 * a)
            root2 = (-b - (discriminant ** 0.5)) / (2 * a)
            print("has the following real roots:")
            print(str(root1) + " and " + str(root2))
            
        elif discriminant == 0:
            root = -b / (2 * a)
            print("has only one solution, a real root:")
            print(str(root))
            
        else:
            real_part = -b / (2 * a)
            imag_part = ((-discriminant) ** 0.5) / (2 * a)
            
            print("has the following two complex roots:")
            print(str(real_part) + " + i " + str(imag_part))
            print("and")
            print(str(real_part) + " - i " + str(imag_part))



# main

# your code for the welcome tmessage goes here
print("*******************************************")
print("*                                         *")
print("*   Welcome to my math quiz-generator     *")
print("*                                         *")
print("*******************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
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
            
            if score == num_questions:
                print("Congratulations " + name + "! You'll probably get an A tomorrow.")
            elif score == 0:
                print("I think you need some more practice " + name + ".")
            else:
                print("You did ok " + name + ", but I know you can do better.")

elif status=='2':

    # your code for welcome message
    header_msg = "*  quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "  *"
    stars_border = "*" * len(header_msg)
    empty_border = "*" + (" " * (len(header_msg) - 2)) + "*"
    
    print(stars_border)
    print(empty_border)
    print(header_msg)
    print(empty_border)
    print(stars_border)


    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.lower()
        question = question.strip()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            coeff_a = float(input("Enter a number the coefficient a: "))
            coeff_b = float(input("Enter a number the coefficient b: "))
            coeff_c = float(input("Enter a number the coefficient c: "))
            
            high_school_quiz(coeff_a, coeff_b, coeff_c)            
 
else:
    # your code goes here
    print(name + " you are not a target audience for this software.")

print("Good bye "+name+"!")
