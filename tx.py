import subprocess
import thread

def startTransmissionOnHost(flag, serial, fileName, freq):
    if(flag):
        try:
            thread.start_new_thread(subprocess.check_output, (['tx_samples_from_file',  'args=addr='+ serial,
                                            '--file=' + fileName, '--rate=250e3', '--freq=' + freq,
                                             '--ref=external', '--ant=TX/RX'],))
        except:
            print "exception occured"
    else:
        try:
            thread.start_new_thread(subprocess.check_output(['tx_samples_from_file',  'args=serial='+ serial,
                                            '--file=' + fileName, '--rate=250e3', '--freq=' + freq,
                                             '--ref=external', '--ant=TX/RX'],))
        except subprocess.CalledProcessError as e:
            print e.output

def startTransmissionOnServer(flag, session, serial, fileName, freq):
    if(flag):
        command = 'tx_samples_from_file args=addr=' + serial +' --file=' + fileName + ' --rate=250e3 --freq=' + freq + ' --ref=external --ant=TX/RX'
    else:
        command = 'tx_samples_from_file args=serial='+ serial + ' --file=' + fileName + ' --rate=250e3 --freq=' + freq + ' --ref=external --ant=TX/RX' 
    thread.start_new_thread(session.exec_command,(command,))
    