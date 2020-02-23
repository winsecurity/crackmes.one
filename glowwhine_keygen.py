import string
import random

# string.printable gives all ascii

# second char must be '@'
# sum must be equal to 0x12c  (300 in decimal)
# hex(ord('c'))

l = list(string.printable)

res = ''

temp = random.randint(0,len(l))
res += l[temp]
res += '@'

final =[]
for i in range(0,len(l)):
    res=''
    temp1 =  int(hex(ord(l[i])),16)
    if temp1< 0x12c:
        for j in range(i,len(l)):
            temp2 = int(hex(ord(l[j])),16)
            if temp1+temp2< 0x12c:
                for k in range(j,len(l)):
                    temp3 = int(hex(ord(l[k])),16)
                    if temp1+temp2+temp3 == 0x12c:
                        res += str(chr(temp1))+ str(chr(temp2))+ str(chr(temp3))
                        final.append(l[temp] +'@'+res)
                        break 


for every in range(len(final)):
    if len(final[every])==5:
        print(final[every])
