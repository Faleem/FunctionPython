import string

def dekripte(dekrip):
    mo_dekripte=""
    lis=dekrip.split("-")
    for eleman in lis:
        el= int(eleman)
        mo_dekripte += string.ascii_uppercase[el]
    print(mo_dekripte)
dekripte("0-11-14")        