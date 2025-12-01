import random
import string

# strint.punctuation 是标点符号
total       = string.ascii_letters + string.digits + string.punctuation
length      = 16
password    = "".join(random.sample(total,length))
print(password)