n1=input("Qual é o seu sexo Masculino(M) ou Feminino(F): ")
n2=int(input("Qual é sua idade: "))
if n1=="F" and n2>=50:
    print("ELEGÍVEL PARA APOSENTADORIA")
elif n1=="M" and n2>=65: 
    print("ELEGÍVEL PARA APOSENTADORIA")
else:
      print("NÃO ELEGÍVEL PARA APOSENTADORIA")