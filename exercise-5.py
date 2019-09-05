# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
term = 0
number = 0
second_num =0
last_number = 0


while term <= 50:
    print(f"term: {term}/ number: {last_number}") 
    term = term+1
    if number == 0:
        number += 1
    second_num = last_number
    last_number = number
    number = last_number + second_num


   
    
    

    
    
