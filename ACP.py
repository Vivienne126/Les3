name=input("Enter your name")
total_days=int(input("Enter the total number of working days"))
total_absent=int(input("Enter the total number of absent days"))
percentage = (total_days / total_absent) * 100
print(f"Your percentage: {percentage}")

if percentage>=75:
    print(f"{name} is eligible to take the exam , with a percentage of {percentage}")
elif percentage<75:
    print(f"{name} is  not eligible to take the exam , with a percentage of {percentage}")
else:
    print("Invalid input...")

