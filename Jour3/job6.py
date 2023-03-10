s ="abcdefghijklmnopqrstuvwxyz" * 10
n = 1 #nombre de cara dans la ligne 
i = 0 #position du premier cara

while i +n < len(s):
    print(s[i:i+n])
    i += n
    n += 1         
