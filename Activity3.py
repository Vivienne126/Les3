n=int(input("Enter the number"))
print(f"Your number is {n}")

if n>50:
    print("Number is greater than 50")
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
else:
    print(f"{n} is less than 50")