import string

def kripte (krip):
    mo_kripte=""
    for let in krip:
        t=string.ascii_lowercase.index(let)
        at=str(t)
        mo_kripte+=at + "-"
    print(mo_kripte)
kripte("alo")        

