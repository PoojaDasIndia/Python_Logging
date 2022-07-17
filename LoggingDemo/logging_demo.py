import logging

logging.basicConfig(level=logging.DEBUG,
                    filename=r"C:\Users\HP\Desktop\Python\Python_Logging\logs\demolog1.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s:%(levelno)s | %(message)s',
                    datefmt='%d-%B-%y | %A | %H:%M:%S %p')


class demoLogging:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_numbers(self):
        return self.a + self.b

    def multiply_number(self):
        return self.a + self.b


# calling function
dl = demoLogging(4, 8)
sum_result = dl.add_numbers()
logging.info(f"The addition of number is {sum_result}\n")
multiply_result = dl.multiply_number()
logging.info(f"The mulitiplication of number is {multiply_result} \n")
logging.debug(f"This is debug")
logging.info(f"This is info")
logging.warning(f"This is warning")
logging.error(f"This is error")
logging.critical(f"This is critical")
