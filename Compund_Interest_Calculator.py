# Compound Interest Calculator
# Below I will be using logical operators in Python to create my calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the Principle amount: "))
    if principle <= 0:
        print("Principle can't be 0 or less than zero")

while rate <= 0:
    rate = float(input("Enter the Interest rate amount: "))
    if rate <= 0:
        print("Interest Rate can't be 0 or less than zero")
        
while time <= 0:
    time = int(input("Enter the Time in  years: "))
    if time <= 0:
        print("Time can't be 0 or less than zero")

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)

print (f"Balance after {time} year/s: ${total:.2f}")