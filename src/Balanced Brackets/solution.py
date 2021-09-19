def isBalanced(s):
    # Write your code here
    result = []
    count_Open = 0
    count_Closed = 0
    for i in s:
        if ((i == '}' or i == ']' or i == ')') and len(result) == 0):
            return 'NO'
        if(i == '[' or i == '{' or i == '('):
            result.append(i)
            count_Open += 1
            continue
        if(i == ')'):
            count_Closed += 1
            if(result[-1] == '('):
                result.pop()
            continue
        if(i == '}'):
            count_Closed += 1
            if(result[-1] == '{'):
                result.pop()
            continue
        if(i == ']'):
            count_Closed += 1
            if(result[-1] == '['):
                result.pop()
            continue
    if(len(result) == 0 and count_Open == count_Closed):
        return 'YES'
    return 'NO'
