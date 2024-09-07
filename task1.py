def cardType(digits):
  if digits[0]==4:
    print("Visa")
  elif digits[0]==3:
    print("American Express")
  elif digits[0]==5:
    print("master card")



def isValid(nums):
 digits=nums[::-1]
 tmp1=[]  
 tmp2=[]
 for i in range(0,len(digits),2):
  tmp2.append(digits[i])
 for i in range(1,len(digits),2):
    ans=digits[i]*2
    if ans>9:
     c1=ans%10
     c2=int(ans/10)
     ans=c1+c2
    tmp1.append(ans)
 total=sum(tmp1)+sum(tmp2)
 if total%10 == 0:
   cardType(nums)
   return ""
 else:
   return "not a valid card"

def main():
 digits=[4,1,5,8,3,0]
 print(isValid(digits))


main()