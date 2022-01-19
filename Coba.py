# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("f", end= "*ck ")
            # ending line after each row
        print("\r")

# Driver Code
n = 9
pypart(n)

carriage_return = "I will use a carriage\r return"
print(carriage_return)

