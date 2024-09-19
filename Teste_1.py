max = int(input("Digiteum número"))

for num in range(1, max + 1):
    if num % 15 ==0:
        print("FIZZBUZZ")
    elif num % 5 ==0:
        print("BUZZ")
    elif num % 3 ==0:
        print("FIZZ")
    else:
        print(num)
