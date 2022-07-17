import os
import logging
from datetime import date
class data:

    def __init__(self, file_name, file_type, dt, size):
        self.file_name=file_name
        self.file_type=file_type
        self.date=dt
        self.size=size
        
    @staticmethod
    def log(msg):
        os.system('cls')
        logging.getLogger().setLevel(logging.DEBUG)
        ch=logging.StreamHandler()
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s', datefmt='%d-%B-%y|%A|')
        ch.setFormatter(formatter)
        logging.getLogger().addHandler(ch)
        logging.info(msg)

    def File_open(self):
        
        try:
            file = open(self.file_name+"."+self.file_type, "w")
            file.write("Hello Python pooja das")
            
        except Exception as e:
            self.log(e)
            
    def File_read(self):
        try:
            file = open(self.file_name+"."+self.file_type, "r")
            file.seek(0)
            self.log(file.read())
        except Exception as e:
            self.log(e)
    
    def File_append(self):
        try:
            file= open(self.file_name+"."+self.file_type, "a")
            file.write("hii. test Hello Python")
            
        except Exception as e:
            self.log(e)


d=data("logs\\python", "txt", date.today(), 52)

d.File_open()
d.File_read()
d.File_append()


