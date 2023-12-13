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


# string split and join
def split_and_join(line):
    result = "-".join(line.split())
    return result


# What's your name?
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')


# Mutations
def mutate_string(string, position, character):
    altered_string = list(string)
    altered_string[position] = character
    result = ''.join(altered_string)
    return result

# replace can't be used as the position is given instead of the value to be changed.
