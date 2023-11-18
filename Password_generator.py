import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol='()[]{};_#$%*!.:-'
numbers='0123456789'

all=lower + upper + numbers + symbol
length=15
password="".join(random.sample(all,length))
print("The generated password is: ",password)