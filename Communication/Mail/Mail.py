# -*- coding: utf-8 -*-


class Mail():

    def __init__(self, title="Title", sender="", content="Content", attachments=[]):
        """ New instance of Mail class"""

        self.__title = title
        self.__content = content
        self.__sender = sender
    
    def title(self):
        return self.__title

    def content(self):
        return self.__content

    def sender(self):
        return self.__sender

    def __str__(self):

        return "Mail <'"+str(self.__title)+"'> sent by '"+str(self.__sender)+"'"