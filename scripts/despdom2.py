# despdom1.py - Calculadora de despesas domesticas

print ('Balanco de despesas domesticas')
ana = input("Quanto gastou Ana?")
bia = input("Quanto gastou Bia?")
total = float (ana) + float (bia)
print ("Total de gastos = R$ %f" % (total))
media = total/2
print ("Gastos por pessoa = R$ %f" % (media))
if float (ana) < float (media):
    diferenca = media - ana
    print ("Ana deve pagar: R$ %f" % (diferenca))
else:
    diferenca = float (media) - float (bia)
    print ("Bia deve pagar: R$ %f" % (diferenca))

