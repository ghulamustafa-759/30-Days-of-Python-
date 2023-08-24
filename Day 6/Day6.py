year = int(input("Enter the year you want to check : \n"))


def leap_year(yr):
        isLeap = True
        if yr % 4 == 0:
            isLeap = True

            if yr % 100 == 0:
                isLeap = False

                if yr % 400 == 0:
                    isLeap = True

                else:
                    isLeap = False
            else:
                isLeap = True
        else:
            isLeap = False

        return isLeap

ans = leap_year(year)

if ans:
    print(f"{ans} is a leap Year.")
else:
    print(f"{ans} is not a leap year.")