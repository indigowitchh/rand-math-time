def DaysLeft(month, day):
    if month == 5:
        return 12 - day
    if month == 4:
        return 30 - day + 12
    if month == 3:
        return 31 - day + 12 + 30
    if month == 2:
        return 28 - day + 12 + 30 + 31

print("Let's see how many days seniors have left!")
m = int(input("enter todays month"))
d = int(input("enter todays day"))
print("seniors have: ", DaysLeft(m, d), "days left")
