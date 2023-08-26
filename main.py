def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = input('Please Enter Celcius: ')
    c = int(celcius)
    fahrenheit = ((c) * 9/5) + 32
    f = fahrenheit
    
    print(f'Celcius: \t {c:.2f}')
    print(f'Fahrenheit: \t {f:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
