while True:
    print("Add a number between 1 and 12 and I will create its times table.")
    times_number = int(input())
    if(1<= times_number <= 12):
        break

for i in range(1,13):
    print(str(times_number) + " times " + str(i) + " = " + str(times_number * i))

