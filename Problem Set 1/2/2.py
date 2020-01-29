# s = 'azcbobobegghakl'

i = 0
l_bob = len("bob")
l_s = len(s)
length_check = l_s - l_bob + 1
bob_count = 0

for i in range(length_check):
    if s[i] == 'b':
        if s[i + 1] == 'o' and s[i + 2] == 'b':
            bob_count += 1

print("Number of times bob occurs is:", bob_count)
 
