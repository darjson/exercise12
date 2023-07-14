ones=["","One","Two","three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
ty=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
result=""
num=int(input("Plese enter Any number between 1 and 9999:"))
if num>=1 and num<=9999:
    if num>=1000:
        result=ones[int(num/1000)] + " Thousand "
        num = num % 1000
    if num >= 100:
        result+=ones[int(num/100)] + " Hundred "
        num = num % 100
    if num >= 20:
        result+=ty[int(num/10)]
        num = num % 10
    if num>=1:
        result+=" "+ ones[num]
else:
     print("Invalid number....")
print(result)

# result=""
# num=int(input("Plese ENter Any number:"))
# if num>=1 and num<=9999:
#     if num>=1000:
#         result = ones[ int(num/1000)  ] + " Thousand "
#         num = num % 1000
#     if num>=100:
#         result += ones[ int(num/100) ] + " Hundred "
#         num = num % 100
#     if num>=20:
#         result+=ty[int(num/10)]
#         num = num % 10
#     if num>=1:
#         result+=" "+ ones[num]
# else:
#     print("Invalid number....")
# print(result)