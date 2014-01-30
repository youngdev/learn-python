# -*- coding: utf-8 -*- 
import urllib
import os, re, sys
from datetime import datetime
import time

# Deleta o arquivo imagem.jpg
os.remove("imagem.jpg")

# Busca a data e hora atual
data = datetime.now().strftime('%Y%m%d%H')

# Cria o arquivo juntando a data + extecao
arquivo = "S11219894_" + data + "30.jpg"

print "Imagem de satelite encontrada"

# Cria o endereço da url juntando o url + arquivo criado anteriormente
endereco = 'http://pituna.cptec.inpe.br/repositorio5/goes12/goes12_web/ams_col_alta/2013/07/' + arquivo

# Faz o Download do arquivo
f = open(arquivo,'wb')
f.write(urllib.urlopen(endereco).read())
f.close()

# Renomeia o arquivo para o nome imagem.jgp
os.rename(arquivo, "imagem.jpg")

# Aguarda 15 minutos
time.sleep(10)

# Reinicia o programa
def reiniciar_programa():
    python = sys.executable
    os.execl(python, python, * sys.argv)
reiniciar_programa()