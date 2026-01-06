
str = "hello world"
words = str.split()
newString = ""
for x in words:
    
    temp = x[0].upper()+x[1:]
    newString = newString +temp+" "
print(newString)
