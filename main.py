from numerical_analysis_alghorithms import bisection_method
from numerical_analysis_alghorithms import false_position_method
from numerical_analysis_alghorithms import secant_method

while True:
    print('\nChoose an alghorithm (0 for quit):')
    print('1. Bisection method')
    print('2. False position method')
    print('3. Secant method')
    user_choice = input('>> ')
    try:
        user_choice = int(user_choice)
    except:
        print('Please enter an integer!')
        continue

    if user_choice == 0:
        break
    elif user_choice == 1:
        result = bisection_method()
        print('result is', result)
    elif user_choice == 2:
        result = false_position_method()
        print('result is', result)
    elif user_choice == 3:
        result = secant_method()
        print('result is', result)
    else:
        print('Wrong number!')
