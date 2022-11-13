# -*- coding: utf-8 -*-
#####################################################################################################
#################################### Includes #######################################################
#####################################################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#regex module
import re

#####################################################################################################
#################################### Class Mail #####################################################
#####################################################################################################
class Attachment():

    def __init__(self, name="Title", type="Content"):
        """ New instance of Attachment class"""


class MailSender():


    ########################################################
    ################## Initializer #########################
    ########################################################
    def __init__(self):
        """ New instance of MailHandler class"""

        #Internal 
        self.__logFilename = ""     #Default filename of logs (+path)

        #Data
        self.__sender = ""          #Default sender (mail)
        self.__password = ""        #Default password
        self.__recipient = ""      #Recipients
        self.__attachments = []     #Array of attachments

        self.__contentType = "html"     #Default content type
        self.__encoding = "utf-8"       #Default encoding
        self.__mimeMultipart  ="mixed"  #Defaut MIMEMultiPart [mixed, text, attachement]  #alternative -> mixed, attachement


        self.__title = "default title"  #default title (object) of mail
        self.__content  = ""     #default content of mail

        #SMTP
        self.__smtp = None          #default instance of SMTP
        self.__smtpServer = ""      #Defaut SMTP server
        self.__smtpPort = 1000      #Defaut SMTP port

        self.__sentMail = 0

    ########################################################
    ################## Internal ############################
    ########################################################
    def __checkType(self, arg, typeArg):
        
        """This method is allowed to check the type of argument passed in function"""
        assert type(arg) is typeArg, "Expected "+str(typeArg)+" but real type is "+str(type(arg))

    def setLogFile(self, filename):
        """This method is allowed to set the path and filename of log file"""
        self.__checkType(filename, str)

        self.__logFilename = filename
        
    def __writeLogs(self, message):
        """Write log message in file"""
        self.__checkType(message, str)
        
        tmpFile = open(self.__logFilename, "a")
        tmpFile.write(message+"\n")
        tmpFile.close()

    def __checkEmail(self, address):
        """Checking address forma, return True if format is valid, else false"""
        self.__checkType(address, str)

        return re.search(re.compile(r"[^@]+@[^@]+\.[^@]+"), address) #End regex expression

    def __checkBeforeSending(self):
        """Check content mail before sending"""
        print("Checking")

    ########################################################
    ################## Data ################################
    ########################################################
    def setSender(self, sender, password):
        """ Set sender email and password"""

        self.__checkType(sender, str)
        self.__checkType(password, str)

        self.__sender = sender
        self.__password = password

    def setRecipient(self, recipient):
        """Set recipient"""
        self.__checkType(recipient, str)

        if(self.__checkEmail(recipient)):
            self.__recipient = recipient
            return True
        else:
            print("Bad format for <"+recipient+"> mail")
            return False

    def addAttachment(self, inputFilename, outputFilename):
        """ Add more than one attachment"""

        file = open(inputFilename, "r")
        attachment = MIMEApplication(file.read(), outputFilename)

        # After the file is closed
        attachment['Content-Disposition'] = 'attachment; filename="%s"' % outputFilename

        self.__attachments.append(attachment)
        

    def setTitle(self, title):
        """set object for mail"""
        self.__checkType(title, str)

        self.__title = title

    def setContent(self, content):
        """set content for mail"""
        self.__checkType(content, str)

        self.__content = content

    def setEncoding(self, encoding):
        """ Set encoding"""
        self.__checkType(encoding, str)

        self.__encoding = encoding


    def setContentType(self, type):
        """ Set content type (text, attachement)"""
        self.__checkType(type, str)

        self.__contentType = type


    def setServer(self, server, port):
        """ Choose smtp server and port"""
        self.__checkType(server, str)
        self.__checkType(port, int)

        self.__smtpServer = server
        self.__smtpPort = port

    def reset(self):

        #Content
        self.__title = "default title"  #default title (object) of mail
        self.__content  = "<p></p>"     #default content of mail

        #Data
        self.__sender = ""          #Default sender (mail)
        self.__password = ""        #Default password
        self.__recipient = []      #Array of recipients
        self.__attachments = []     #Array of attachments

    ########################################################
    ################## Send ################################
    ########################################################

    def send(self):
        """Send email"""

        message = MIMEMultipart(self.__mimeMultipart)                          
        message['Subject'] = self.__title
        message['From'] = self.__sender
        message['To'] = self.__recipient

        #Multipurpose Internet Mail Extensions
        self.__smtp = smtplib.SMTP(self.__smtpServer, self.__smtpPort)

        mime = MIMEText(self.__content, self.__contentType, self.__encoding)
        message.attach(mime)
        
        self.__smtp.ehlo()
        self.__smtp.starttls()

        self.__smtp.login(self.__sender, self.__password)

        if(len(self.__attachments)>0):
            for a in self.__attachments:
                message.attach(a)

        try:
            #self.__smtp.set_debuglevel(0)
            self.__checkBeforeSending()
            self.__smtp.sendmail(self.__sender, self.__recipient, message.as_string())
            print(">>> Message sent to "+self.__recipient)

        except smtplib.SMTPResponseException: #SMTPRecipientsRefused, SMTPResponseException
            print(">>> Cannot send the email to "+self.__recipient)
            
        self.__smtp.quit()
        #self.__writeLogs(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+" : Mail sent to "+self.__recipient)
        return True

#TTI -> Accès à un fichier avec les références les plus connues (delais moyens) 


def main():

#Ajouter Accuse recept

    recipient = input("What is the recipient (and sender) ? : ")
    password = input("What is the application password ? : ")
    mail = MailSender()

    mail.setServer("smtp.gmail.com", 587)
    mail.setLogFile("log.txt")
    mail.setContentType("html")
    mail.setEncoding("utf-8")
    mail.setSender(recipient, password)

    mail.addAttachment("README.md", "README.md")
    mail.setRecipient("user@domain")
    mail.setTitle("Title")
    mail.setContent("<h1>Title</h1><h2>Sub-title</h2>Content edited by <b>Python</b>")
    #mail.addAttachment("image.png", "outputName.png")
    mail.send()



if __name__ == "__main__":

    main()
