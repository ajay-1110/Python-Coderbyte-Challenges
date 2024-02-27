#hcf/gcf
#First solution -
def Division(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2   
    return num1
result = Division(32, 16)
print(result)

#Second solution - 
def hcf(num1,num2):
    factor_1 = []
    factor_2 = []
    for i in range(1,num1+1):
        if num1%i == 0:
            factor_1.append(i)
    for i in range(1,num2+1):
        if num2%i == 0:
            factor_2.append(i)
        
    a = sorted(factor_1)
    hcf1 = a[0]
    for i in range(1,len(a)):
        if a[i] in factor_2:
            hcf1 = a[i]
    return hcf1

print(hcf(32,16))
