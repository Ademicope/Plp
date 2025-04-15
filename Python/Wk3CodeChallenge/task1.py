def power(base, exponent):
    """
       This function tests whether the result 
       of taking the power of a number 
       to another number gives a result greater than 5000
    """
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
def divisible_by_10(number):
    """
         This function tests whether a number is divisible by 10
    """ 
    if number % 10 == 0:
        return True
    else:
        return False

answer = power(5, 5)
print(answer)