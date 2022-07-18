import os
import logging
from datetime import date
# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)
# ch=logging.StreamHandler()
# formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s', datefmt='%d-%B-%y|%A| %H:%M:%S %p')
# ch.setFormatter(formatter)
# logger.addHandler(ch)

class data:

    def __init__(self, file_name, file_type, dt, size):
        self.file_name=file_name
        self.file_type=file_type
        self.date=dt
        self.size=size

    @staticmethod
    def log(msg):
        os.system('cls')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch=logging.StreamHandler()
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s', datefmt='%d-%B-%y|%A| %H:%M:%S %p')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.info(msg)

    def File_open(self):
        
        try:
            file = open(self.file_name+"."+self.file_type, "w")
            file.write("Hello Python pooja das")
            
        except Exception as e:
            return self.log(e)
            # logger.error(e)
            # print(e)

            
    def File_read(self):
        try:
            file = open(self.file_name+"."+self.file_type, "r")
            file.seek(0)
            return self.log(file.read())
            # logger.info(file.read())
            # print(file.read())
        except Exception as e:
            return self.log(e)
            # logger.error(e)
            # print(e)
    
    def File_append(self):
        try:
            file= open(self.file_name+"."+self.file_type, "a")
            file.write("hello 123 test Hello Python")


        except Exception as e:
            return self.log(e)
            # logger.error(e)
            # print(e)


d=data(r"C:\Users\HP\Desktop\Python\Python_Logging\logs\python", "txt", date.today(), 52)

d.File_open()
d.File_read()
d.File_append()
d.File_read()

