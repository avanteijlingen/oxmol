"""
Representation of chemical element.

This is a thin wrapper around the PyO3 base class: it calls the
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to truly subclass
PyO3 classes from Python, so this is all we are able to do on the Python
end.

"""

from typing import Type, TypeVar
from .oxmol import PyElement

E = TypeVar('E', bound='Element')


class Element(PyElement):
    """
    A chemical element. Represented in ``molecule.rs`` as a Rust enum.

    :param atomic_number: an ``int``, the atomic number.

    """
    def __new__(cls: Type[E], atomic_number: int) -> E:
        return PyElement.__new__(cls, atomic_number)

    @classmethod
    def from_symbol(cls: Type[E], symbol: str) -> PyElement:
        """
        Create an element from its atomic symbol.
        """
        return PyElement.from_symbol(symbol)
