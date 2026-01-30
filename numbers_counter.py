even_count = 0
odd_count = 0
sum_big = 0

for i in range(7):
    num = int(input())

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if num > 10:
        sum_big += num

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of big numbers:", sum_big)
