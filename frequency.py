s="happy birthday"
freq={}
for name in s:
    if name not in freq:
        freq[name]=1
    else:
        freq[name]+=1
print(freq)
