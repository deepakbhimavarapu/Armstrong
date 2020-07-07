# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
    # Your code goes here
    temp = num
    s = 0
    while(num > 0):
        r = num % 10
        s = s + (r * r * r)
        num = num // 10
    if s == temp:
        return True
    return False
