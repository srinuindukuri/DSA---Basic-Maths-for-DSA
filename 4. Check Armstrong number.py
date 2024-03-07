num = int(input("Enter the number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
dup = num
while(dup > 0):
    digit = dup % 10
    sum = sum + digit ** 3
    dup = dup // 10

if(sum == num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
