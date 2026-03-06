

step_count = 0

num = int(input("give bigger number than 9: "))

if num > 9:
    print(num, end="")

    while num > 9:
        current_sum = 0
        temp = num

        while temp > 0:
            current_sum += temp % 10
            temp //= 10

        num = current_sum
        step_count += 1
        print(f" -> {num}", end="")

    print(f"\n Final value: {num}")
    print(f"Total step: {step_count}")

else:
    print(f"{num} is not bigger than 9")

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

n = int(input("Enter an integer between 10 and 100: "))

while n < 10 or n > 100:
    n = int(input("Invalid input. Enter a value between 10 and 100: "))

for i in range(1, n + 1):
    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)

print("\n--- Summary ---")
print(f"Fizz: {fizz_count}")
print(f"Buzz: {buzz_count}")
print(f"FizzBuzz: {fizzbuzz_count}")

import sys

num1 = int(input("Enter a number between 3 and 9: "))

if num1 < 3 or num1 > 9:
    print("give valid input")
    sys.exit(0)

for i in range(1, 2 * num1):
    if i <= num1:
        k = i
    else:
        k = 2 * num1 - i

    for j in range(1, k + 1):
        print(f"{j} ", end="")
    print()