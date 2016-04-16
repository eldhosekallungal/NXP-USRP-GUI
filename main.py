'''
Created on Apr 14, 2016

@author: nxa27820
'''
import paramiko
from mainFrame import MyFrame1
import wx
import thread
import findUsrp
import tx
from panel import MyPanel1
# import transmission already included in the main program itself


class SSHESession():
    def __init__(self):
        self.serverIP = "192.168.0.3"
        self.serverPort = 22
        self.password = '12welcome?'
        self.client = None;
        self.session = None
class subFrame(MyFrame1, MyPanel1, SSHESession):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        SSHESession.__init__(self)
    def disable_server(self, event):
        if(self.m_checkBox1.GetValue()):
            self.m_textCtrl7.Disable()
            self.m_button1.Disable()
        else:
            self.m_textCtrl7.Enable()
            self.m_button1.Enable()
    def ssh_connect(self, event):
        thread.start_new_thread(self.testConnect, ())
        
    def testConnect(self):
        self.m_staticText6.SetLabel("connecting")
        userName = self.m_textCtrl7.GetValue()
        try:
            self.client = paramiko.Transport((self.serverIP, self.serverPort))
            self.client.connect(username = userName, password = self.password)
            self.session = self.client.open_channel(kind='session')
            self.m_staticText6.SetLabel("Success")
        except paramiko.ssh_exception.SSHException:
            self.m_staticText6.SetLabel("Failed")
    
    def usrp_find(self, event):
        if(self.m_checkBox1.GetValue()):
            if(self.m_radioBtn2.GetValue()):
                findUsrp.findUsrpOnHost(True, self.m_textCtrl2.GetValue())
            else:
                findUsrp.findUsrpOnHost(False, self.m_textCtrl2.GetValue())
        else:
            if(self.session.active):
                self.session = self.client.open_channel(kind = 'session')
            if(self.m_radioBtn2.GetValue()):
                findUsrp.findUsrpOnServer(True, self.session, self.m_textCtrl2.GetValue())
            else:
                findUsrp.findUsrpOnServer(False, self.session, self.m_textCtrl2.GetValue())

    def usrp_start(self, event):
        IPFlag = self.m_radioBtn1.GetValue()
        serial = self.m_textCtrl2.GetValue()
        fileName = self.m_textCtrl6.GetValue()
        freq = self.m_textCtrl9.GetValue()
        if(self.m_checkBox1.GetValue()):
            tx.startTransmissionOnHost(IPFlag, serial, fileName, freq)
        else:
            if(self.session.active):
                self.session = self.client.open_channel(kind = 'session')
            tx.startTransmissionOnServer(IPFlag, self.session, serial, fileName, freq)
    def usrp_abort(self, event):
        if(self.session.active):
            self.session = self.client.open_channel(kind = 'session')
        thread.start_new_thread(self.session.exec_command, ('killall tx_samples_from_file',))
    def file_search(self, event):
        userName = self.m_textCtrl7.GetValue()
        panel = subPanel(None)
        thread.start_new_thread(panel.ssh_search, (self.serverIP, userName, self.password, self.m_textCtrl6))
        panel.Show(True)


class subPanel(MyPanel1):
    def __init__(self, parent):
        MyPanel1.__init__(self, parent)
        self.textBox = None
        self.clipData = ''
        self.fileList = ''
    def copy(self, event):
        indx = self.m_listBox1.GetSelection()
        self.clipData = self.m_listBox1.GetString(indx)
        self.clipData.replace('\n','')
        self.textBox.SetValue(self.clipData)
    def ssh_search(self, server, userName, password, textBox):
        self.textBox = textBox
        filePath = './*.iq*'
        command = 'ls ' + filePath
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username = userName, password = password)
        stdin, stdout, stderr = ssh.exec_command(command)
        self.fileList = stdout.read().splitlines()
        for files in self.fileList:
            print files
            self.m_listBox1.Append(files + '\n')
        ssh.close()
def main():
    app = wx.App(False)
    frame = subFrame(None)
    frame.Show(True)
    app.MainLoop()
if __name__ == '__main__':
    main();
    