str=input("enter a string:")
index_start=0
index_last=len(str)-1
flag=1
for s in str:
    if  index_start==(int)((len)(len(str)-1)/2):
        break
    if s !=str[index+last]:
        flag=0
        break
    index_last=index_last-1
    idex_start=index_start+1
if flag==0:
    print(str,"is not a palindrome")
else:
    print(str,"is a palindrome")
