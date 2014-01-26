import os
import sys
import platform

def uid():
us = {'Windows': 'USERNAME',
	'Linux': 'USER'}
u = us.get(platform.system())
return os.environ.get(u)

print 'Usuário:', uid()
print 'plataforma:', platform.platform()
print 'Diretório corrent:', os.path.abspath(os.curdir)
exep, exef = os.path.split(sys.executable)
print 'Executável:', exef
print 'Diretório do executável:', exep
