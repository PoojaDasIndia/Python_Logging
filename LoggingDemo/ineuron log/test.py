import logging

logging.basicConfig(filename="C:\\Users\\HP\\Desktop\\Python\\Python_Logging\\logs\\test.log",
                    filemode="a",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s:%(levelno)s  - %(lineno)s| %(message)s',

                    datefmt='%d-%B-%y | %A | %H:%M:%S %p'

                    )


def divide(a, b):
    logging.info("Function for doing division of two numbers...")
    logging.info(f"The number enter by user is {a} and {b}")
    try:
        logging.debug("We are inside Function block...")
        div = a / b
        logging.info("We are completed a division operation")
        logging.info("Result of code is %s ", div)
    except Exception as e:
        logging.error(e)
        logging.exception(e)


divide(10, 100)
