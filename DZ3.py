###############1###################
value=int(input("введите значение"))
new_value=value/2 if value<100 else -(value)
print(new_value)
################2##################
value=int(input("введите значение"))
new_value=1 if value<100 else 0
print(new_value)
################3##################
value=int(input("введите значение"))
new_value=True if value<100 else False
print(new_value)
################4##################
my_str="qwerty"
print(my_str.upper())
#################5#################
my_str="QWERTY"
print(my_str.lower())
#################6#################
my_str="qwerty"
if len(my_str)<5:
    print(my_str,my_str)
else:
    print(my_str)
#################7#################
my_str="qrty"
if len(my_str)<5:
    print(my_str,my_str[::-1])
else:
    print(my_str)

