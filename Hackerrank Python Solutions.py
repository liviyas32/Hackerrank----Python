'''INTRODUCTION'''
# Say "Hello, World!" With Python 
print("Hello, World!")


# Python If-Else
n = int(input().strip())
    if n%2 == 0:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        elif n>20:
            print("Not Weird")
    else:
        print("Weird")


# Arithmetic Operators
    a = int(input())
    b = int(input())
    
    # sum
    print(a+b)
    # difference
    print(a-b)
    # product
    print(a*b)


# Python : Division
    a = int(input())
    b = int(input())
    
    # integer division
    print(a//b)
    # float division
    print(a/b)


# Loops
    n = int(input())
    for i in range(n):
        print(i**2)


# Print Function
    n = int(input())
    for i in range(1,n+1):
        print(i, end = "")


# Write a Function
def is_leap(year):
    leap = False
    
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            leap = True
        
    return leap

year = int(input())
print(is_leap(year))


'''BASIC DATA TYPES'''
# List Comprehensions
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])


# Find the Runner-Up Score!
    n = int(input())
    arr = map(int, input().split())
    
    # convert arr into list
    arr = list(arr)
    
    # remove duplicates
    distinct_arr = list(set(arr)) 
    
    # find winner_score
    top_score = max(distinct_arr) 
    
    while top_score in arr:
        # remove winner_score from original array
       arr.remove(top_score)
    # print the max_score(runner_score) after removing winner_score
    print(max(arr))
