print("DEBUG: Module '__main__.py' is executing")

#from .cli import main
from matrix_tkinter_coloring1.cli import main

#import pkg_resources
#
#filename = "__main__.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))

if __name__ == '__main__':
    main()
