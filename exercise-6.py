# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of a season (Jan - Dec:").lower()
day = int(input("Enter the day of the month:"))

winter = ('jan', 'feb')
spring = ('apr', 'may')
summer =('jul', 'aug')
fall = ('oct', 'nov')

if month in winter:
    print(f'{month} {day} is in winter')
elif month in spring:
    print(f'{month} {day} is in spring')
elif month in summer:
    print(f'{month} {day} is in summer')
elif month in fall:
    print(f'{month} {day} is in fall')
elif month == 'dec' and day >= 21:
    print(f'{month} {day} is in winter')
elif month == 'dec' and day < 21:
    print(f'{month} {day} is in fall')
elif month == 'mar' and day <= 19:
    print(f'{month} {day} is in winter')
elif month == 'mar' and day > 19:
    print(f'{month} {day} is in spring')
elif month == 'jun' and day <= 20:
    print(f'{month} {day} is in spring')
elif month == 'jun' and day > 20:
    print(f'{month} {day} is in summer')
elif month == 'sep' and day <= 21:
    print(f'{month} {day} is in summer')
elif month == 'sep' and day > 21:
    print(f'{month} {day} is in fall')


