#   2 power     31	2,147,483,648
#   2 power     32	4,294,967,296

#    0x1acb0aad
#   449514157

#   0x4c7
#  2 power 64  9,223,372,036,854,775,807
# 1223


def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n


#n = 123455666322
for n in range(200000):
    temp = 449514157 * n

    #edx
    upper32 = bin(temp)
    upper32 = upper32[2:]
    upper32 = (64-len(upper32))*'0' + upper32
    upper32 = upper32[:32]
    #print(upper32)
    upper32 = rshift(int(upper32),7)#>>7

    sar_input =  rshift(n,31)
    diff = upper32 - sar_input
    temp3 = diff * 1223
    res = n-temp3
    if res==0:
        print(n)
        #break
#print(diff)


