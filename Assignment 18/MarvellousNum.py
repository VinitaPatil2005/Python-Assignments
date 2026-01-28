
def ChkPrime(No):
    for i in range(2, No):
        if (No % i) == 0:
            return False
    return True