def Count_digits(n):
    count = 0
    x = n
    while(x != 0):
        x = x // 10
        count += 1
    return count


n = int(input("Enter the number: "))
print("Number of digits in", n, "is", Count_digits(n))
