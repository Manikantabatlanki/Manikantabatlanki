def checkpassword(pwd):
    valid=False
    if len(pwd)>=8:
        for ch in pwd:
            if ord(ch)>=65 and ord(ch)<=90:
                valid =True
                break
        else:
            valid=False
            
        if valid==True:
            for ch in pwd:
                if ord(ch)>=97 and ord(ch)<=122:
                    valid=True
                    break
            else:
                valid =False
        if valid==True:
            for ch in pwd:
                if ord(ch)>=48 and ord(ch)<=57:
                    valid=True
                    break
            else:
                 valid=False
        if valid==True:
            for ch in pwd:
                if ord(ch)<=47 or (ord(ch)>=58 and ord(ch)<=64 )\
                   or (ord(ch)>=91 and ord(ch)<=96):
                    valid =True
                    break
            else:
                valid=False
        
        return valid


p=input('enter a password:')
res=checkpassword(p)
print(res)
                   

