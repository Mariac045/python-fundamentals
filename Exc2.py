#Print the Sum of a Current Number and a Previous number

#Write Python code to iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.

previous_number = 0
for i in range(1,10):
    sum= previous_number + i
    print("Current number: ", i, "previous number: ", previous_number, "sum: ", sum)

    previous_number = i