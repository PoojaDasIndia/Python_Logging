"""DEBUG -- Detailed information, typically of interest only when diagnosing problems.
    INFO -- Confirmation that things are working as expected.
  WARNING -- An indication that something unexpected happened, or indicative of some issue in the near future
                    (e.g. ‘disk space low’). The software is still working as expected.
   ERROR --  Due to a more serious issue, the software has not been able to perform some function.
CRITICAL -- A serious error, indicating that the program itself may be unable to continue running.

The default level is WARNING, which means that only events of this level and above will be tracked,
              unless the logging package is configured to do otherwise.
"""


class demoLogging1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_numbers(self):
        return self.a + self.b

    def multiply_number(self):
        return self.a + self.b


# calling function

dl = demoLogging1(4, 5)
sum_result = dl.add_numbers()
print(f"\nThe addition of number is {sum_result}")

multyply_result = dl.multiply_number()
print(f"The mulitiplication of number is {multyply_result} \n")
