import logging

class LoggerrDemo:

    @staticmethod
    def sample_logger():

        # Step 1. create logger
        logger=logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)

        # Step 2. create console handler (ch) or file handler (ch) and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler(r"C:\Users\HP\Desktop\Python\Python_Logging\logs\Adv_demolog2.log", mode="a")

        # Step 3. Create formatter  - how you want your logs to be formatted
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s:%(levelno)s | %(message)s', datefmt='%d-%B-%y | %A | %H:%M:%S %p')
        formatter1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s | %(message)s', datefmt='%d-%B-%y | %A | %H:%M:%S %p')

        # Step 4. Add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        # Step 5. Add console handler(ch) to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        # Step 6. 'application' code - log messages
        logger.debug(f"This is debug")
        logger.info(f"This is info")
        logger.warning(f"This is warning")
        logger.error(f"This is error")
        logger.critical(f"This is critical")



LoggerDemo.sample_logger()
