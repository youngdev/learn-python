# somadora2.py - somadora infinita - versao 2

print ("Digite os valores a somar seguidos de [ENTER].")
print ("Para encerrar digite zero: 0")
total = 0
while 1:
    n = float(input(':'))
    if n == 0: break
    total = total + n
print ("Total: %s" %(total))
