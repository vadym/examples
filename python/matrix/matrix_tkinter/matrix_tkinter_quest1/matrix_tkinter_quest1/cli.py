print("DEBUG: Module 'cli.py' is executing")

from matrix_tkinter_quest1.core import loggerConfigure
from matrix_tkinter_quest1.gui import Gui

import argparse
import logging

#import pkg_resources
#
#filename = "cli.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))


def command_default(args):
    """Function to get be called by '.set_defaults(func=)' of the 'argparse' parser for default section"""
    logging.info("DEBUG: command_default()")

    # Create the GUI object (and execute the class constructor).
    Gui()

def args_parse():
    """Configure argparse"""

    parser = argparse.ArgumentParser(description='The CLI/GUI application to manage a HTML-tag statistic.')
    parser.add_argument("-v", "--verbose", action="count", help="Verbosity level")
    parser.set_defaults(func=command_default)

    #subparsers = parser.add_subparsers(help='List of commands')

    # A '' command
    #get_parser = subparsers.add_parser('get', help='')
    #get_parser.add_argument('', action='store', help='')
    #get_parser.set_defaults(func=)

    return parser.parse_args()


def main():
    """Main function"""
    loggerConfigure()

    args = args_parse()

    try:
        # Execute a function according to the command-line agruments.
        args.func(args)

    except Exception as e:
        logging.warning("DEBUG: %s" % e)
