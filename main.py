def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = input('Please Enter Celcius: ')
    fahrenheit = int(celcius) * 1.8 + 32

    print(f'Fahrenheit: \t {fahrenheit}') 
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
