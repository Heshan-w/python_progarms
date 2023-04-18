import math

nums = [5, 15, 20, 23, 45, 67, 78, 89, 90, 99]
lower = 0
upper = len(nums) + 1
middle = math.floor((lower+upper)/2)
type(middle)
found = False
valueSearched = int(input("enter number to be searched : "))

while not found:
    if valueSearched == nums[middle - 1]:
        found = True
        print(f"value found at postion {middle}")
        quit()
    elif valueSearched > nums[middle - 1]:
        lower = middle
        middle = math.floor((lower+upper)/2)
    elif valueSearched < nums[middle - 1]:
        upper = middle
        middle = math.floor((lower+upper)/2) 
    if middle == lower or middle == upper:
        found = True
if found == True:
    print("value not found in list")    
