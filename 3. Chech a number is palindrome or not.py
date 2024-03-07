# Using Iteration Method

num = int(input("Enter the number: "))
dup = num
reverse_num = 0
while (dup > 0):
    # Extract the last digit
    digit = dup % 10
    # Append the last digit
    reverse_num = reverse_num * 10 + digit
    dup = dup // 10
if num == reverse_num:
    print("It's a palindrome")
else:
    print("Not a palindrome")
