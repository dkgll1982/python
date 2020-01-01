class P:
    def __repr__(self):
        return "hi repr method"
    def __str__(self):
        return "hi str method"
p = P()
print(p)

dict = {'test': 'test.com', 'google': 'google.com'}
bit = b'123'
str1 = repr(dict)
str2 = repr(bit)
print(type(str1),type(str2),str1,str2)