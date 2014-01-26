#-*- coding: utf-8 -*-

import os, re, sys
import urllib
import smtplib
import time
from urllib2 import Request, urlopen, URLError

# FUNCIONS
def alerta(op='sim'):
   if op == 'sim':
      fromaddr = 'maisprodutivo@gmail.com'  
      toaddrs  = 'maisprodutivo@gmail.com'
      mensagem = 'Serviço Parado'
      username = 'maisprodutivo'  
      password = 'ddnumber1'  
      server = smtplib.SMTP('smtp.gmail.com:587')  
      server.starttls()  
      server.login(username,password)  
      server.sendmail(fromaddr, toaddrs, mensagem)  
      server.quit()
      print "E-mail enviado com sucesso"

def verificar_ping(ip = '177.126.161.84'):
   print "Verificando Servico ..."
   cmd = 'ping %s' % ip
   r = "".join(os.popen(cmd).readlines())
   if re.search ("Perdidos = 0", r):
      print "SERVICO >>> ON-LINE"
   else:
      print "SERVICO >>> OFF-LINE"
      alerta('sim')
   
def testar_link(url = 'http://matheusgodoy.me/'):
   req = Request(url)
   try:
       response = urlopen(req)
       print 'LINK >>> ON-LINE'
   except URLError, e:
       print 'LINK >>> OFF-LINE'
       alerta('sim')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# HEADER
print "- " * 30
print "PLANTAO ENALTA"
print "MONITORAMENTO DE PRODUTOS"
print
print

# DO THIS
print "Verificar servidor ARCGIS-SERVER"
verificar_ping('177.126.161.84')
print
print "Verificar SIGLOG V5"
verificar_ping('177.126.161.85')
print
print "Verificar MAPAS"
testar_link('http://www.arcgis.com/home/webmap/viewer.html?url=http%3a%2f%2f177.126.161.84%2fArcGIS%2frest%2fservices%2feth_ual%2fMapServer&source=sd')
print
print "Verificar PORTAL"
testar_link('http://portal.enalta.com')
print
print "Verificar SSMA"
testar_link('http://186.209.74.45:6789/Enalta.SSMA.ReportSetUpTestPage.html')
print

# FOOTNOTE
print
print "O MONITORAMENTO SERA INICIADO EM 1 MINUTO"
print "APROVEITE PARA TOMAR UM CAFE"
print  "- " * 30

# RESTART
time.sleep(60)
restart_program()