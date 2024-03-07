

def Prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input("Enter the number: "))
    ans = Prime(n)
    if n != 1 and ans == True:
        print("Prime number")
    else:
        print("Not a prime number")
