def findDuplicate(nums):
    # Floyd's Cycle Detection Algorithm (Tortoise and Hare)
    tortoise = nums[0]
    hare = nums[0]
    
    # Phase 1: Find the intersection point of the two pointers
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Phase 2: Find the entrance to the cycle (duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return tortoise

# Test the function
test_array = [1, 3, 4, 2, 2]
result = findDuplicate(test_array)
print(f"The duplicate number is: {result}")
