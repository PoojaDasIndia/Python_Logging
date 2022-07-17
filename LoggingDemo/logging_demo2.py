import logging

print("This is first statement\n")
logging.info("This is info\n")
logging.warning("This is warning\n")


class demoLogging1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_numbers(self):
        s = self.a + self.b
        return s


    def multiply_number(self):
        s = self.a * self.b
        return s


# calling function

dl = demoLogging1(4, 8)
sum_result = dl.add_numbers()
logging.warning(f"The addition of number is {sum_result}\n")

multiply_result = dl.multiply_number()
logging.warning(f"The multiplication of number is {multiply_result} \n")


          