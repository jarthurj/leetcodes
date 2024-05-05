
def removeDuplicates(s, k):
    count = 0
    start_index = 1
    index = 1
    current_char = s[0]
    while k > 0:
        print(s)
        if index == len(s):
            index = 0
        # print(index, start_index)
        if s[index] == current_char:
            count += 1
            index += 1
            if count == 2:
                start_index = index - 1
        else:
            if count > 1:
                # print(s[0:start_index])
                s = s[0:start_index-1]+s[index:]
                k -= 1
                index = index - count
                # print(s)
            current_char = s[index]
            count = 1
            index += 1
            start_index = index
            
            
    return s

print(removeDuplicates("deeedbbcccbdaa",3))