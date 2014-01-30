#-*- coding: utf-8 -*-

import platform
import os, re, sys
import smtplib

# Faz teste de ping
print "Verificando conexao..."
cmd = "ping www.google.com"
resultado = "".join(os.popen(cmd).readlines())
print (resultado)

# Verifica qual a plataforma do usuario
print 'System:		', platform.system()
print 'Node:		', platform.node()
print 'Release:	', platform.release()
print 'Version:	', platform.version()
print 'Machine:	', platform.machine()
print 'Processor:	', platform.processor()

# Verifica a versao do Python

# Envia resultados por e-mail
fromaddr = 'maisprodutivo@gmail.com'  
toaddrs  = 'maisprodutivo@gmail.com'
mensagem = "texto"


username = 'maisprodutivo'  
password = 'ddnumber1'  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, mensagem)  
server.quit()
print "E-mail enviado com sucesso"




