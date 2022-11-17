# -*- coding: utf-8 -*-

import imaplib
import email
from email.header import decode_header

import os

from Folder import Folder
from Mail import Mail

class Debug():

    #Types
    INFO = "Info"
    ERROR = "Error"
    WARNING = "Warning"
    SUCCESS = "Success"

    def __init__(self):


         #Status
        self.__displayErrors = True
        #Colors
        self.__blueColor = '\033[94m'
        self.__greenColor = '\033[92m'
        self.__orangeColor = '\033[93m'
        self.__redColor = '\033[91m'
        self.__defaultColor = '\033[0m'
        self.__bold = '\033[1m'   

        #prompt
        self.__displayPromptError = "["+self.__redColor+"Error"+self.__defaultColor+"] >>> "
        self.__displayPromptWarning = "["+self.__orangeColor+"Warning"+self.__defaultColor+"] >>> "
        self.__displayPromptSuccess = "["+self.__greenColor+"Success"+self.__defaultColor+"] >>> "
        self.__displayPromptInfo = "["+self.__blueColor+"Info"+self.__defaultColor+"] >>> "
        self.__displayPromptInput = "["+self.__bold+"Input"+self.__defaultColor+"] >>> "

    def displayErrors(self, displayErrorStatus=True):

        self.__displayErrors = displayErrorStatus

    def println(self, message, type=INFO):

        if(not self.__displayErrors):
            return 
        if(type==Debug.INFO):
            print(self.__displayPromptInfo+message)
        elif(type==Debug.ERROR):
            print(self.__displayPromptError+message)
        elif(type==Debug.WARNING):
            print(self.__displayPromptWarning+message)
        elif(type==Debug.SUCCESS):
            print(self.__displayPromptSuccess+message)
        else:
            print(self.__displayPromptError+" Bad type format for type in Debug.println method")



class MailBox(Debug):

    def __init__(self, server="smtp.gmail.com", username="", password=""):
        """ New instance of MailBox class"""

        super().__init__() 
        self.__username = username
        self.__password = password
        self.__server = server

        self.__messagesNumber = 0
        self.__totalMails = 0

        self.__imap = imaplib.IMAP4_SSL(self.__server)
        try:
            self.__imap.login(self.__username, self.__password)
            self.println("Connected to mailbox", self.SUCCESS)
        except:
            self.println("Error when connecting")

        
        self.openFolder("INBOX", Folder("InBox"))
        #self.__messagesNumber = int(self.__messages[0])
        #self.println("Number of message : "+str(self.messagesInFolder()), self.INFO)

        self.analyseFolders()

        self.__imap.logout()

    def __extractMimeHeader(self, message, mimeHeader):

        data, encoding = decode_header(message[str(mimeHeader)])[0]

        if(encoding == None): #Ignore encoding
            return data
        else:
            if(encoding=="unknown-8bit"):
                return data
            else:
                return data.decode(encoding)

    def totalMails(self):
        return self.__totalMails

    def messagesInFolder(self):
        return self.__messagesNumber

    def openFolder(self, folder, f):
        """Return list of Mail"""

        self.__status, self.__messages = self.__imap.select(folder)
        
        try:
            self.__countMessageInFolder = int(self.__messages[0].decode("utf-8"))
            self.__messagesNumber = int(self.__messages[0])
        except:
            self.__messagesNumber = 0
            return
            
        

        self.__totalMails += self.__messagesNumber

        if(self.__status == "OK"):
            self.println("Folder '"+folder+"' successfully opened ["+str(int(self.__messages[0]))+" message(s)] !", self.SUCCESS)
        else:
            self.println("Error in opening '"+folder+"' folder", self.ERROR)


        for index in range(self.__countMessageInFolder, 0, -1):

            # fetch the email message by ID
            res, message = self.__imap.fetch(str(index), "(RFC822)")
            mails = []
            for response in message: #New mail in folder

                if isinstance(response, tuple):

                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject

                    subject = self.__extractMimeHeader(msg, "Subject")
                    sender = self.__extractMimeHeader(msg, "From")


                    mail = Mail(subject, sender, "")
                    f.addMail(mail)

                    # if the email message is multipart
                    if(msg.is_multipart()):
                    # iterate over email parts
                        for part in msg.walk():

                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            contentMessage = "<Empty>"
                            try:
                                # get the email body
                                contentMessage = part.get_payload(decode=True).decode()
                            except:
                                pass
                        
                            if(content_type == "text/plain" and "attachment" not in content_disposition):
                                # print text/plain emails and skip attachments
                                pass#print(contentMessage)

                            elif("attachment" in content_disposition):
                                # download attachment
                                filename = part.get_filename()
                                if(filename):
                                    folder_name = self.clean(str(subject))
                                    if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                        try:
                                            os.mkdir(folder_name)
                                        except:
                                            pass
                                    filepath = os.path.join(folder_name, filename)
                                    #Download attachment and save it
                                    #open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                
                        content_type = msg.get_content_type() #Extract content type of email
                        try:
                            contentMessage = str(msg.get_payload(decode=True), encoding="utf-8")
                        except:
                            pass
                        if(content_type == "text/plain"):
                            # print only text email parts
                            pass#print(contentMessage)
                        if(content_type == "text/html"):
                            #if it's HTML, create a new HTML file and open it in browser
                            folder_name = self.clean(subject)
                            if(not os.path.isdir(folder_name)):
                                # make a folder for this email (named after the subject)
                                try:
                                    os.mkdir(folder_name)
                                except:
                                    pass
                            filename = "index.html"
                            filepath = os.path.join(folder_name, filename)
                            # write the file
                            #open(filepath, "w").write(contentMessage)
                            # open in the default browser
                            #webbrowser.open(filepath)
                            

    def analyseFolders(self):

        #self.println("List of folders : ")

        self.__foldersList = []

        self.__folders = self.__imap.list()
        self.__parent = None
        for f in self.__folders[1]:

            folder = self.analyseFolder(f.decode('utf-8'))

            self.openFolder("\""+folder.name()+"\"", folder)

            if(folder.hasChildren()):
                self.__parent = folder

            elif(self.__parent != None):
                if(self.__parent.name() in folder.name()):
                    self.__parent.addChild(folder)
                else:
                    self.__foldersList.append(self.__parent)
                    self.__parent = None
            else:
                self.__foldersList.append(folder)

    def getFolders(self):

        return self.__foldersList
            

    def clean(self, text):
        # clean text for creating a folder
        return "".join(c if c.isalnum() else "_" for c in str(text))

    def analyseFolder(self, rawFolderName):

        #split
        name = rawFolderName.split("/")
        hasCHildren = False

        if("HasChildren" in name[0]):
            hasCHildren = True
            #self.println(name[1]+" has children : "+str(hasCHildren))
        if(len(name)==2):
            name = name[1].replace("\"", " ")
        elif(len(name)==3):
            name = name[1].replace("\"", " ") +"/" + name[2].replace("\"", " ")
        else:
            return Folder("", hasChildren=hasCHildren)

        return Folder(name.strip(), hasChildren=hasCHildren)


def main():

    m = MailBox("smtp.gmail.com", "user@gmail.com", "password")
    print(m.totalMails())
    # for f in a.getFolders():
    #     print(f)
if( __name__ == "__main__"):
    main()