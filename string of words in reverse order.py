def reversewords():
    s=input("Enter a string: ")
    s=s.strip()
    s=s.split()
    s.reverse()
    return " ".join(s)
print(reversewords())
