#-*- coding: utf-8 -*-
# enaltacleaner

import glob, os
import time
import calendar

from threading import Timer
from datetime import datetime
from zipfile import ZipFile
from datetime import date

# shelledure task
agendamento = calendar.firstweekday()
hoje = date.today()

def limpeza():
        # zip files
        meuzip = ZipFile('arquivo-' + str(hoje) + '.zip', 'a')
        meuzip.write('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/')
        meuzip.close()

        # sendmail with attachment
        
        # remove zipfile
        filelist = glob.glob("*.zip")
        for f in filelist:
                os.remove(f)

        # clear folder
        for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/*/'):
                for file in files:
                        if file.endswith(extencao):
                                os.remove(os.path.join(root, file))

if agendamento == hoje:
        limpeza()
