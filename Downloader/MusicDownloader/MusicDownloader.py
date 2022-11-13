#!/usr/bin/python3
# rm */.*.mood
from curses import ERR
import ytmdl
import eyed3
import os
import sys
from datetime import datetime

from Debug.Debug import Debug


class Runtime():
    """This class compute duration time between TaskRuntime.start() and TaskRuntime.stop() call"""

    def __init__(self):

        self.__startTime = None
        self.__stopTime = None
        self.__duration = 0
        self.__averageTimes = []
        self.__maxAverageValues = 10

    def start(self):
        """Save start time"""
        self.__startTime = datetime.now()

    def stop(self):
        """Save end time"""
        self.__stopTime = datetime.now()
        self.__duration = self.__stopTime - self.__startTime

        if(len(self.__averageTimes)<=self.__maxAverageValues):
            self.__averageTimes.append(self.__duration.total_seconds())

    def runtime(self):
        """Return duration in s"""
        return self.__duration

    def averageRuntime(self):
        """Return average duration time"""
        time = 0
        for t in self.__averageTimes:
            time+=t
        return time/len(self.__averageTimes)




class MusicDownloader(Debug):

    def __init__(self):

        super().__init__()
        self.__taskRuntime = Runtime()


    def directoryHandler(self, directoryName):
        """Create directory if similar name doesn't exist -> return real directory name"""

        allDirectories = os.scandir(os.getcwd())
        self.__allDirectoriesLower = []
        self.__allDirectories = []

        #Store all directories
        for d in allDirectories:
            if(d.is_dir()):
                self.__allDirectoriesLower.append(d.name.lower())
                self.__allDirectories.append(d.name)

        index = 0
        found = False
        #Return real current name if similar has been found
        for d in self.__allDirectoriesLower:
            
            if(directoryName.lower() == d):
                self.__curentDirectory = self.__allDirectories[index]
                return self.__allDirectories[index]
            index+=1
        
        if(not found):
            self.println("Creation of '"+directoryName+"' directory", self.INFO)
            os.mkdir(directoryName)
            return directoryName

    def saveFiles(self, filename):

        """Export list of musics in txt file"""
        alldir = os.scandir(os.getcwd())
        self.__allFilesLower = []
        bigStr = ""
        #Store all directories
        for f in alldir:
            if(f.is_file()):
                pass
            elif(f.is_dir):
                allFiles = os.scandir(os.getcwd()+"/"+str(f.name))
                #print(f.name)
                for a in allFiles:
                    bigStr += a.name.replace(".mp3", " ").replace("-", " ").strip()+"\n"

        file = open("saved_musics.txt", "w")
        file.write(bigStr)
        file.close()
                    


    def fileHandler(self, directory, filename):
        """Create directory if similar name doesn't exist -> return real directory name"""

        allFiles = os.scandir(os.getcwd()+"/"+directory)
        self.__allFilesLower = []

        #Store all directories
        for f in allFiles:
            if(f.is_file()):
                self.__allFilesLower.append(f.name.lower())

        #print(filename.lower())
        #print(self.__allFilesLower)
        if(filename.lower() in self.__allFilesLower):
            return None

        if(os.path.exists(directory+"/"+filename)):
           return None 
        else:
            if(os.path.exists(filename)):
                return None
            else:
                return filename


    def downloadMusics(self):

        #stats
        count_downloaded = 0
        count_existings = 0
        count_error = 0
        averageTimes = []
        for indexItem in range(0,len(self.__authors)):

            #print(self.__authors[indexItem])
            self.__taskRuntime.start()
            if(self.__moveInDirectory):

                directory = self.directoryHandler(self.__authors[indexItem])
                filename  = self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3"

                file = self.fileHandler(directory, filename)

                if(file==None):
                    self.println("File '"+filename+"' already exists") 
                    count_existings+=1
                    continue
                
                
                command = "yt-dlp \"ytsearch1:"+self.__authors[indexItem]+""+self.__titles[indexItem]+" \" --extract-audio --audio-format mp3 --parse-metadata 'title:%(title)s' --output \""+directory+"/"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3\" --add-metadata > .log.txt"
                status = os.system(command)
                

                if(status == False):
                    if(os.path.exists(directory+"/"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3")):
                        self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' downloaded in '"+directory+"' directory!", self.SUCCESS)
                        audioFile = eyed3.load(directory+"/"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3")
                        audioFile.tag.artist = self.__authors[indexItem]
                        audioFile.tag.title = self.__titles[indexItem]
                        audioFile.tag.track_num = 1
                        audioFile.tag.save()
                        count_downloaded+=1
                    else:
                        self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' not downloaded !", self.ERROR)
                        count_error+=1
                else:
                    self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' not downloaded !", self.ERROR)
                    count_error+=1

            else:
                #Don't move in directory
                filename  = self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3"

                file = self.fileHandler("", filename)
                command = "yt-dlp \"ytsearch1:"+self.__authors[indexItem]+""+self.__titles[indexItem]+" \" --extract-audio --audio-format mp3 --parse-metadata 'title:%(title)s' --output \""+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3\" --add-metadata > .log.txt"
            
                if(file==None):
                    self.println("File '"+filename+"' already exists") 
                    count_existings+=1
                    continue

                status = os.system(command)

                if(status == False):
                    if(os.path.exists(self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3")):
                        self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' downloaded !", self.SUCCESS)

                        #Edit metadata
                        audioFile = eyed3.load(self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3")
                        audioFile.tag.artist = self.__authors[indexItem]
                        audioFile.tag.title = self.__titles[indexItem]
                        audioFile.tag.track_num = 1
                        audioFile.tag.save()
                        count_downloaded+=1
                    else:
                        self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' not downloaded !", self.ERROR)
                        count_error+=1
                else:
                    self.println("File '"+self.__authors[indexItem]+" - "+self.__titles[indexItem]+".mp3' not downloaded !", self.ERROR)
                    count_error+=1
            self.__taskRuntime.stop()

            #print(self.__taskRuntime.averageRuntime())
            #print(self.__taskRuntime.averageRuntime()*(len(self.__authors)-indexItem))
        
        #Display stats
        self.println("##################################", self.INFO)
        self.println("############ STATS ###############", self.INFO)
        self.println("##################################", self.INFO)
        self.println("Number of music(s) successfully downloaded : "+str(count_downloaded)+" / "+str(len(self.__authors)), self.SUCCESS)
        self.println("Number of music(s) already in directories : "+str(count_existings)+" / "+str(len(self.__authors)), self.WARNING)
        self.println("Number of music(s) badly downloaded : "+str(count_error)+" / "+str(len(self.__authors)), self.ERROR)

    def loadSettings(self):
        """Set settings"""

        answer = input("[Input] >>> Do you want move each music in folder called by name of artists ? (y/n) : ")
        if(answer == "y"):
            self.__moveInDirectory = True
        else:
            self.__moveInDirectory = False

    def loadFile(self):
        """Set input filename"""

        self.println("List of files in directory : ", self.INFO)

        allFiles = os.scandir(os.getcwd())
        selectAllFiles = []

        #Store all files
        for f in allFiles:
            if(f.is_file()):
                selectAllFiles.append(f.name)

        #Display result
        for f in range(0, len(selectAllFiles)):
            print("\t["+str(f)+"] > "+selectAllFiles[f])
        print("\t["+str(len(selectAllFiles))+"] > other file")

        filenameSelect=input(self.getInputPrompt()+"Your choice ? : ")

        #check type
        filename=""
        if(int(filenameSelect)<0 or int(filenameSelect)>len(selectAllFiles)):
            self.println("Please select a valid number", self.ERROR)
            exit(0)
        if(int(filenameSelect) == len(selectAllFiles)):
            filename = input(self.getInputPrompt()+"What is your filename ? :")
        else:
            filename = selectAllFiles[int(filenameSelect)]

        if(os.path.exists(filename)):
            self.println("File '"+filename+"' loaded !", self.SUCCESS)
        else:
            self.println("File '"+filename+"' doesn't exist !", self.ERROR)
            exit(0)

        self.__file = open(filename, "r")
        self.__authors = []
        self.__titles = []

        for line in self.__file.readlines():

            tmpLine = line.replace("\n", "")

            checkBracket = tmpLine.split("(")

            if(len(checkBracket)>=2):
                self.println("Content after first '(' will be ignored  ("+line.replace("\n", "")+")", self.WARNING)
                tmpLine = checkBracket[0]

            splittedLine = tmpLine.split("-")

            if(len(splittedLine) == 2):
                pass
            elif(len(splittedLine) == 3):
                self.println("Content after second '-' will be ignored  ("+line+")", self.WARNING)
                author = splittedLine[0].strip()
                title = splittedLine[1].strip()
            else:
                self.println("Bad line format - "+line, self.ERROR)
                self.println("Line must be 'Artist - Title' format", self.ERROR)
                continue

            author = splittedLine[0].strip().replace("\n", " ")
            title = splittedLine[1].strip().replace("\n", " ")

            self.__authors.append(author.strip())
            self.__titles.append(title.strip())



def main():
    
    downloader = MusicDownloader()

    downloader.loadFile()
    downloader.loadSettings()
    downloader.downloadMusics()


if(__name__ == "__main__"):

    main()
  