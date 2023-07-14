nums=[]
while True:
    num=int(input("Please input a number:"))
    if num==0:
        break
        print("-----------")
    nums.append(num)
print("You have entered ",len(nums), "numbers")
print("The sum of all numbers",sum(nums))
print("The biggest number you enterted",max(nums))
print("The smallestr number you enterted",min(nums))
