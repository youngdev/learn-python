#-*- coding: utf-8 -*-

import zipfile
import glob

arquivozip = glob.glob('*.zip')
arquivo = arquivozip[0]
print "Arquivo ZIP: " + arquivo

# Extrair zip
zf = zipfile.ZipFile(arquivo, 'r')
zf.extractall()

# Verifica se possui arquivo .prj
if glob.glob('*.prj'):
    print "Possui arquivo .proj"
else:
    print "Não possui arquivo .proj"

# Verifica se é WGS84
for file in glob.glob('*.prj'):
    for line in open(file):
        print line.find('WGS84')
