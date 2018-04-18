1. How do we convert a string to uppercase or lowercase?
    Use upper() or lower() to convert a string
>>> name = "CAPSLOCK"
>>> new_name = name.lower()
>>> print(new_name)
capslock

2. How do we get length of a string?
    Use len() function
>>> name="CAPTAIN"
>>> len(name)
7

3. How do we print a string, one character per line?
    Use for loop
name = "name"
for n in name:
    print(n)

4. How do we compare two strings?
a= "stringa"
b= "stringb"
if a==b:
    print("stringa la stringb")
elif a<b:
    print("stringa dung truoc stringb theo bang chu cai alphabet")
else:
    print("stringa dung sau stringb theo bang chu cai alphabet")
