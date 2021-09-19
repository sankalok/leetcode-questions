# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.append(len(arr) - 1)

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if(len(arr) == n):
        return True
    return False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if(len(arr) == 0):
        return True
    return False

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    return min(arr)
