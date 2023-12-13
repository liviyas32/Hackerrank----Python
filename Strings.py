"""STRINGS"""
# String Validators
if __name__ == '__main__':
    s = input()
    str_fun = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper ]
    for fun in str_fun:
        ans = any(fun(i) for i in s)
        print(ans)


# swapcase
def swap_case(s):
    string = ''
    for i in s:
        if i.islower() == True:
            string = string + i.upper()
        else:
            string = string + i.lower()
    
    return string



