q1>def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for s_char, t_char in zip(s, t):
        if s_char not in s_map:
            s_map[s_char] = t_char
        elif s_map[s_char] != t_char:
            return False

        if t_char not in t_map:
            t_map[t_char] = s_char
        elif t_map[t_char] != s_char:
            return False

    return True
q2>def isStrobogrammatic(num):
    mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in mapping or mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True
q3>def addStrings(num1, num2):
    result = []
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry != 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        summation = digit1 + digit2 + carry
        result.insert(0, str(summation % 10))
        carry = summation // 10

        i -= 1
        j -= 1

    return ''.join(result)
q4>def reverseWords(s):
    words = s.split()  # Step 1: Split the string into words
    reversed_words = [word[::-1] for word in words]  # Step 2: Reverse each word

    return ' '.join(reversed_words)  # Step 3: Join the reversed words back into a string
q5>def reverseStr(s, k):
    s_list = list(s)  # Step 1: Convert the string to a list of characters
    n = len(s)
    start = 0
    end = k - 1

    while start < n:
        s_list[start:end+1] = reversed(s_list[start:end+1])  # Step 3a: Reverse the characters

        start += 2 * k  # Step 3b: Update start
        end = min(start + k - 1, n - 1)  # Step 3b: Update end, considering the special cases

    return ''.join(s_list)  # Step 4: Convert the list back to a string

q6>def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s_concat = s + s
    if goal in s_concat:
        return True
    else:
        return False
q7>def backspaceCompare(s, t):
    stack_s = []
    stack_t = []

    for char in s:
        if char != '#':
            stack_s.append(char)
        elif stack_s:
            stack_s.pop()

    for char in t:
        if char != '#':
            stack_t.append(char)
        elif stack_t:
            stack_t.pop()

    return stack_s == stack_t
q8>def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            slope = float('inf')
        else:
            slope = dy / dx

        dx_new = x - x1
        dy_new = y - y1

        if dx_new == 0:
            slope_new = float('inf')
        else:
            slope_new = dy_new / dx_new

        if slope_new != slope:
            return False

    return True
