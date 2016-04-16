import paramiko
import subprocess
from panel import MyPanel1
import wx

def findUsrpOnHost(flag, serial):
    panel = MyPanel1(None)
    if(flag):
        try:
            out = subprocess.check_output(['uhd_find_devices', '--args=addr='+serial])
            panel.m_listBox1.Append(out)
        except subprocess.CalledProcessError as e:
            panel.m_listBox1.Append(e.output)
    else:
        try:
            out = subprocess.check_output(['uhd_find_devices', '--args=serial='+serial])
            panel.m_listBox1.Append(out)
        except subprocess.CalledProcessError as e:
            panel.m_listBox1.Append(e.output)
    panel.Show(True)
def findUsrpOnServer(flag, session, serial):
    panel = MyPanel1(None)
    stdout_data = []
    stderr_data = []
    nbytes = 4096
    panel.Show(True)
    if(flag):
        session.exec_command("uhd_find_devices --args=addr=" + serial)
    else:
        session.exec_command("uhd_find_devices --args=serial=" + serial)
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break
    panel.m_listBox1.Append(''.join(stdout_data))
    panel.m_listBox1.Append(''.join(stderr_data))