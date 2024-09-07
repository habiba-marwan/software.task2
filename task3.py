def format_string(s,operations):
 def reverse(s):
  return s[::-1]
 def toUpper(s):
   for i in s:
     x=ord(i)-32
     if x>=65 and x<=90:
      s = s.replace(i,chr(x))
   return s  
 def capitalize(s):
   x=ord(s[0])-32
   s = s.replace(s[0],chr(x))
   for i in range(len(s)):
    if s[i] == " ":
       x=ord(s[i+1])-32
       s = s.replace(s[i+1],chr(x))
   return s
 

 for operation in operations:
  if operation == "reverse":
   s=reverse(s)
  elif operation == "capitalize":
   s=capitalize(s)
  elif operation == "uppercase":
   s=toUpper(s)
 return s


def main():
 s=format_string("hello world!",["capitalize","reverse"])
 print(s)


  
 


main()