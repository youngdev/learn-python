from zipfile import ZipFile
from datetime import date

hoje = date.today()

meuzip = ZipFile('arquivo-' + str(hoje) + '.zip', 'a')
meuzip.write('//Users//Matheus//Downloads//teste')
meuzip.close()