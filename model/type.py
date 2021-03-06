from __future__ import annotations
import sys
import getpass
if getpass.getuser() == 'riccardoob':
    sys.path.append('/home/riccardoob')
elif getpass.getuser() == 'pi':
    sys.path.append('/home/pi')
    
from typing import TYPE_CHECKING

from mini_sql.model.types_enum import TypesEnum


class Type():
    """
    Describes a MySQL type uaing a TypesEnum ad an integer for the length.
    This class is used when declaring columns.

    Attributes
    ----------
    __type: TypesEnum
        The actual type of this ``Type`` instance
    __len: int
        The length of this type, the default value (-1) means that the length
        won't be specified at declaration

    Parameters
    ----------
    type: TypesEnum
        The actual type of this ``Type`` instance
    len: int, default -1
        The length of this type, the default value (-1) means that the length
        won't be specified at declaration
    """

    __type: TypesEnum # contains a TypesEnum object

    __len: int # contains the len that the type is going to be, -1 if not selected

    def __init__(self, type: TypesEnum, len: int = -1):
        self.__type = type
        self.__len = len
    
    def __str__(self) -> str:
        """
        Creates the MySQL compliant string to declare the type.

        Returns
        -------
        str
            MySQL compliant string declaration of the type.
        """
        if self.__type == TypesEnum.VARCHAR:
            string = (self.__type.value + '(10)' if self.__len == -1 else self.__type.value + '({len})'.format(len = self.__len))
        else:
            string = (self.__type.value if self.__len == -1 else self.__type.value + '({len})'.format(len = self.__len))
        return string
    
    def __repr__(self) -> str:
        string = str(self.__type)
        return '<' + string + '>'

    def __eq__(self, o: object) -> bool:
        return (self.__type == o.__type) and (self.__len == o.__len)

    def __hash__(self) -> int:
        return hash((self.__type, self.__len))