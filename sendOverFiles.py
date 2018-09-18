import paramiko
import time

class transmission:
    __sftpObject = None #list obj
    __sftpObj = None
    __data = {
        'username' : '.',
        'ip' : '.',
        'userServer' : '.',
        'password' :  '.'
    }
    __readStart = True

    __lastLine= str()
    def __init__(self):
        self.attemptConnection()
        #self.__data['username'] = yourName


    def readingLog(self): 
        print(id(self.__sftpObject))
        self.__sftpObject.seek(0)
        tmp = list(self.__sftpObject)
        print(len(tmp))
        print(self.__lastLine, " AND ", str(tmp[len(tmp)-1]).strip('\n'))
        if self.__readStart:
            tmpWord = str()
            for line in tmp: 
                tmpWord+=str(line)
            self.__lastLine = str(tmp[len(tmp)-1]).strip('\n')
            self.__readStart = False
            return tmpWord
            
        elif self.__lastLine == str(tmp[len(tmp)-1]).strip('\n'):
            print("1")
            return ""
        else:
            print("2")
            self.__lastLine = str(tmp[len(tmp)-1]).strip('\n')
            return "\n" + str(tmp[len(tmp)-1])

       # return str('test')#(str(self.__sftpObject[len(self.__sftpObject)-1]).strip('\n'))
        
        #for line in self.__sftpObject:
        #    line=str(line)
        #    line=line.strip('\n')
        #   #print(str(line))


    def writingLog(self, text):
        print(text)
        self.__sftpObj.write("\n"+text)

    def attemptConnection(self):
        try:
            attempt = paramiko.SSHClient()
            attempt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            attempt.connect(
                self.__data['ip'], 
                port = 22,
                username = str(self.__data['userServer']), 
                password = str(self.__data['password']), 
                timeout = 0.2, 
                banner_timeout = 10, 
                auth_timeout = 3)
            x=attempt.open_sftp()
            self.__sftpObj = (x.open(filename='/home/erik/HW', mode='a'))
            self.__sftpObject = x.open(filename='/home/erik/HW', mode='r')

        except:
            print("Failed")
    
#try:
#    attempt = paramiko.Transport(('10.0.1.14', 22))
#    attempt.connect(username='x', password='x')
#    f=paramiko.SFTPClient.from_transport(attempt)
#    f.put('/home/erik/Documents/Programming/Python/plottingData.py', '/home/erik/t')
#except:
#    print("Failed")
#    exit