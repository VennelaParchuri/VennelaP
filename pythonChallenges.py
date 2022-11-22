# Python Challenges

# Capital indexes
def capital_indexes(strn):
    list1 = []
    list2 = list(strn)
    for i in range(0,len(list2)):
        if list2[i].isupper():
            list1.append(i)
    return list1

# Middle Letter

def mid(strn):
    if len(strn)%2 == 0:
        return ''
    else:
        list1 = list(strn)
        return list1[int((len(strn)/2))]

# Online Status

def online_count(dictr):
    count = 0
    for x in dictr.values():
        if x.upper() == 'ONLINE':
            count+=1
    return count

# Randomness

import random
def random_number():
    x = random.randint(1,100)
    return x
    

# Type Check

def only_ints(x,y):
    if type(x) is int and type(y) is int:
        return True
    else:
        return False


# Double letters

def double_letters(strn):
    list1 = list(strn)
    for n in range(0,len(list1)-1):
        if list1[n]== list1[n+1]:
            return True
    return False


# Adding and removing dots

def add_dots(strn):
    list1 = list(strn)
    list2 = []
    for i in list1:
            list2.append(i)
            list2.append('.')
    str1 = ''.join(list2)
    return str1[0:len(str1)-1]

def remove_dots(strn):
    list1 = list(strn)
    str1 = ''
    for i in list1:
        if i == '.':
            continue
        else:
            str1 = str1+i
    return str1


# Counting syllables

def count(strn):
    count=1
    for i in strn:
        if i=='-':
            count+=1
    return count


# Anagrams

def is_anagram(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    count = 0
    for i in str1:
        if i in list2:


# Flatten a list

def flatten(list1):
    flatten_list = []
    for n in list1:
        if type(n) is list:
            for m in n:
                flatten_list.append(m)


# Min-maxing


def largest_difference(list1):
    min_num = min(list1)
    max_num = max(list1)
    return max_num - min_num


# Divisible by 3

def div_3(num):
    return num%3 == 0

# Palindrome

def palindrome(strn):
    return strn == strn[::-1]

# Up and down

def up_down(num):
    return (num-1,num+1)

# Consecutive zeros

def consecutive_zeros(strn):
    list1 = list(strn.split('1'))
    list2 = []
    for i in list1:
        list2.append(len(i))
    return max(list2)


# All equal

def all_equal(list1):
    if len(list1)>0:
        maxm = max(list1)
        count=0
        for i in list1:
            if maxm == i:
                count+=1
        return count == len(list1)
    else:
        return True


# Boolean and

def triple_and(str1,str2,str3):
    return str1==str2==str3 == True

# Writing short code

def convert(list1):
    return [str(i) for i in list1]

# Custom zip

def zap(a,b):
    list1=[]
    for i in range(0,len(a)):
        tup1 = (a[i],b[i])
        list1.append(tup1)
    return list1


# List xor

def list_xor(x,y,z):
    num = x
    list1 = y
    list2 = z
    if x in list1 and x in list2:
        return False
    elif x in list1 or x in list2:
        return True
    else:
        return False

# Counting parameters

def param_count(*args):
    count = 0
    for n in args:
        count+=1
    return count