def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = input('Please Enter Celcius: ')
    cs = int(celcius)
    fahrenheit = ((cs) * 9/5) + 32
    fs = fahrenheit
    
    print(f'Celcius: \t {cs:.2f}')
    print(f'Fahrenheit: \t {fs:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
