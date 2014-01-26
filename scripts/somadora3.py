# somadora3.py - somadora infinita - versao 3

print ("Digite os valores a somar seguidos de [ENTER].")
print ("Para encerrar digite zero: 0")
total = 0
while 1:
    try:
        n = float(input(':'))
        total = total + n
    except:
        break
print ("Total: %s" %(total))
