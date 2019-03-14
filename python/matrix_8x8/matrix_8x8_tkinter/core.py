print("DEBUG: Module 'core.py' is executing")

import logging
import sys

def loggerConfigure():
    # Generic logger outputs to the process STDOUT
    logging.basicConfig(#stream=sys.stdout,
                        filename='main.log',
                        level=logging.INFO)
    # Override defaults by the logging config file.

    # See 'logging.fileConfig()' to configure logging
    # without the application code modifications.
    #logging.config.fileConfig('logging.conf')

    # Dedicated logger 1

    #logger = logging.getLogger(__name__ + '.get')
    #logger.setLevel(logging.INFO)

    ##
    # INFO messages formatter
    #

    #info_formatter = logging.Formatter('%(asctime)s %(message)s')

    # Put output to the file.
    #info_handler = logging.FileHandler('get.log')
    #info_handler.setLevel(logging.INFO)
    #info_handler.setFormatter(info_formatter)

    #logger.addHandler(info_handler)

    ##
    # WARNING messages formatter
    #

    #warning_formatter = logging.Formatter('%(date)s %(time)s %(fqdn)s')
    #
    #warning_handler = logging.StreamHandler()
    #warning_handler.setLevel(logging.WARNING)
    #warning_handler.setFormatter(warning_formatter)
    #
    #logger.addHandler(warning_handler)
