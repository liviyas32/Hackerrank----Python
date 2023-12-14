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
# replace can't be used as the position is given instead of the value to be changed.
def mutate_string(string, position, character):
    altered_string = list(string)
    altered_string[position] = character
    result = ''.join(altered_string)
    return result


# Find a string
def count_substring(string, sub_string):
    count = 0
    flag = 0
    for i in range(0,(len(string) - len(sub_string))+1):
        if string[i] == sub_string[0]:
            flag = 1
            for j in range(len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
    return count


# Text Wrap
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    result = wrapper.fill(text = string)
    return result


# Capitalize!
def solve(s):
    str_list = []
    for i in s.split(' '):
        i = i.capitalize()
        str_list.append(i)
    result = ' '.join(str_list)
    return result


