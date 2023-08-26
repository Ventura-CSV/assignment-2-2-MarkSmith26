def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = input('Please Enter Celcius: ')
    fahrenheit = (int(celcius) * 9/5) + 32

    print(f'Fahrenheit: {fahrenheit:.2f}'.format(float(fahrenheit))) 
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
