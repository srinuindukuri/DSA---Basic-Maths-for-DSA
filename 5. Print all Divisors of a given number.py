N = int(input('Enter the number :'))
# initialize an empty list
arr = []
# get the divisors of number
for i in range(1, N+1):
    if N % i == 0:
        # append to list
        arr.append(i)
# sort them in increasing order
sorted(arr)
# print the list
print(arr)
