import os
import time
import wx
import subprocess
from threading import Timer
from datetime import datetime

TRAY_TOOLTIP = 'Enalta - Cleaner'
TRAY_ICON = 'icon.png'
extencao = '.xml'
today = datetime.now()
day = today.day
month = today.month
year = today.year



def limpeza_agendada():
    if today.day == 14 and today.month == 03:
        limpar()
    elif today.day == 25 and today.month == 03:
        limpar()
    elif today.day == 01 and today.month == 04:
        limpar()
    elif today.day == 10 and today.month == 04:
        limpar()
    elif today.day == 15 and today.month == 04:
        limpar()
    elif today.day == 22 and today.month == 04:
        limpar()
    elif today.day == 29 and today.month == 04:
        limpar()
    else:
        pass


def limpar():
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/InserirCargas'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/InserirCargas'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarInstancias'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarInstancias'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarInstancias'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarInstancias'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarRegrasPesagem'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ListarRegrasPesagem'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/PesarSaida'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/PesarSaida'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/PesarEntrada'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/PesarEntrada'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/SortearAnalises'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/SortearAnalises'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    ####
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ValidarUsuario'):
        for file in files:
            if file.endswith(extencao):
                os.remove(os.path.join(root, file))
    time.sleep(1)
    for root, dirs, files in os.walk('/inetpub/wwwroot/enalta.integracao.server/bkp/enalta.integracao.server/log/Backup/ValidarUsuario'):
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        limpeza_agendada()
    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Limpar Backups', self.on_limpar)
        menu.AppendSeparator()
        create_menu_item(menu, 'Sair', self.on_exit)
        return menu
    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)
    def on_left_down(self, event):
        limpar()
    def on_limpar(self, event):
        limpar()
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

def main():
    app = wx.App(0)
    TaskBarIcon()
    app.MainLoop()

if __name__ == '__main__':
    main()