# -*- coding: utf-8 -*-
import xml
import xml.dom.minidom
import xml.dom.minidom as minidom
import sys

dom1 = minidom.parse(sys.argv[1])
doc = dom1.getElementsByTagName('Document')
folderlist = dom1.getElementsByTagName('Folder')

doc[0].removeChild(folderlist[0])

output = dom1.toxml()

arquivo_saida = open(sys.argv[2], 'w')

arquivo_saida.write(output)

arquivo_saida.close()