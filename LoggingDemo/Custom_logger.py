import inspect
import logging


class cust_LoggerDemo:
    @staticmethod
    def cust_logger(logLevel=logging.DEBUG):
        # Set Class/method name from where its called
        logger_name = inspect.stack()[1][3]

        # Step 1. create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Step 2. create console handler (ch) or file handler (ch) and set the log level
        fh = logging.FileHandler(r"C:\Users\HP\Desktop\Python\Python_Logging\logs\Automation.log", mode="a")

        # Step 3. Create formatter  - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(name)s:%(filename)s - %(levelname)s | %(message)s',
                                      datefmt='%d-%B-%y | %A | %H:%M:%S %p')

        # Step 4. Add formatter to console or file handler
        fh.setFormatter(formatter)

        # Step 5. Add console handler(ch) to logger

        logger.addHandler(fh)

        # Step 6. 'application' code - log messages
        logger.debug(f"This is debug")
        logger.info(f"This is info")
        logger.warning(f"This is warning")
        logger.error(f"This is error")
        logger.critical(f"This is critical")
        # return logger


ld = cust_LoggerDemo()
ld.cust_logger()
