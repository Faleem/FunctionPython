import random
import string 

def alfa(t):
    rezilta =""
    while t >=1:
        alfabe= random.choice(string.ascii_lowercase+string.digits)
        if alfabe not in rezilta:
            rezilta+=alfabe
            t-=1
    print(rezilta)
alfa(12)
