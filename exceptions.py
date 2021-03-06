import sys
import getpass
if getpass.getuser() == 'riccardoob':
    sys.path.append('/home/riccardoob')
elif getpass.getuser() == 'pi':
    sys.path.append('/home/pi')



class ZeroColumns(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class ZeroTables(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class SyntaxError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class PrimaryKeyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class ForeignKeyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class NoSuchColumn(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class WrongClauseOrder(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''
            
class NoSuchTable(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class NoSuchDatabase(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''

class DatabaseNotSelected(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return ''