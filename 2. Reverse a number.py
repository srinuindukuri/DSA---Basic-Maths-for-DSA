num = int(input("Enter the number: "))
reverse_num = 0

while (num > 0):
    # Extract last digit
    digit = num % 10
    # Append last digit
    reverse_num = reverse_num * 10 + digit
    # Shrinking num by discarding last digit
    num = num // 10

print("Reverse number is", str(reverse_num))
