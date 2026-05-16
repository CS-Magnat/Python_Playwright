import logging


def get_logger(name: str) -> logging.Logger:
    """
    Creates and configures a standard Python logger for the given module name.
    
    Sets the logging level to DEBUG and formats the output to include 
    timestamps, module names, and severity levels.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger