'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
https://leetcode.com/problems/plus-one/
'''


from typing import List
def plusOne(self, digits: List[int]) -> List[int]:
    str_nums = [str(x) for x in digits]
    number = int("".join(str_nums))+1
    str_number = str(number)
    dig_list = []
    for digit in str_number:
        dig_list.append(int(digit))
    return dig_list


print(plusOne(1, [1, 2, 3, 9]))
#working!
#list of integers combined +1

