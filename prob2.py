import random
import string
import hashlib


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
   
   

def solution(my_string):
    for i in range(len(my_string)):
        j = i + 1
        while j < len(my_string):
            if my_string[i] == my_string[j]:
                return my_string[i]
            j += 1  
    return "Null"            


if __name__ == '__main__':
    my_string = randomString()
    print(my_string)
    print(solution(my_string))