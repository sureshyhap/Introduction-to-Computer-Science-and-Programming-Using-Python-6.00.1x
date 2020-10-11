# s = 'azcbobobegghakl'
# s = 'abcbcd'

list_alphabetical = []
length = len(s)
start, end = 0, 0

if length:
    while True:
        sub = s[start]
        i = 1
        if start + i >= length:
            break
        while sub <= s[start + i]:
            end += 1
            sub = s[start + i]
            i += 1
            if start + i >= length:
                list_alphabetical.append(s[start : end + 1])
                break
        if start + i >= length:
            break
        else:
            list_alphabetical.append(s[start : end + 1])
        start = end + 1
        end = start

sizes = []
for item in list_alphabetical:
    sizes.append(len(item))

maximum = max(sizes)
final_word = list_alphabetical[sizes.index(maximum)]
print("Longest substring in alphabetical order is:", final_word)
