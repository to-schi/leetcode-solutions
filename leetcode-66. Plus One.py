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

