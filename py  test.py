value=int(input("type meant"))
new_value=value/2 if value<100 else -(value)
print(new_value)
#######
new_value=1 if value<100 else 0
print(new_value)
#######
new_value=True if value<100 else False
print(new_value)
############
my_str="qwerty"
print(my_str.upper())
##########
my_str='QWERTY'
print(my_str.lower())
########
my_str="123456"
if len(my_str)<5:
    print(2*my_str)
else:
    print(my_str)
############
my_str="123"
if len(my_str)<5:
    print(my_str,my_str[::1])
else:
    print(my_str)