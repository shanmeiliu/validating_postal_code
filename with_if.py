"""
Author: Charmaine Liu
Nov 25, 2019
"""
def validatingPostalCode(P):
    try:
        if int(P) > 999999 or int(P) < 100000:
            return False
    except Exception as e:
            print (e)
            return False
    count=0
    for i in range(0,4):
        if P[i] == P[i+2]:
            count+=1
   # print (count)
    if count>1:
        return False
    return True


    
if __name__=='__main__':
    print("please enter the postal code you want to validate")
    P=input()
    print (validatingPostalCode(P))