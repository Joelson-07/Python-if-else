sal=float(input("digite sue slário: "))
if sal < 1000:
    des=sal*20/100
    aumento=sal+des
elif sal >= 1000 and sal <2000 :
    des=sal*30/100  
    aumento=sal+des
elif sal >= 2000:
    des=sal*10/100
    aumento=sal+des
print("o salário é de:" , sal)     
print("o desconto é de:" , des) 
print("o aumento é de:" ,aumento)    