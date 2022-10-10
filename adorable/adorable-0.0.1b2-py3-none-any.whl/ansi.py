from __future__ import annotations

from abc import ABC
from sys import stdout
from typing import Any, Optional, Sequence, TextIO


class Ansi(ABC):
    def __str__(self):
        return self.enable_str()
    
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        """
        Styles a string.
        
        Parameters
        ----------
        args
            Objects to style. The ``str()`` function will
            be called on each object.
        
        sep
            String that seperates ``args``.
        
        Returns
        -------
        The styled string.
        """
        return paint(*args, style = self, **kwargs)
    
    def enable_str(self) -> str:
        """
        Returns escape sequence to enable the ansi style.
        """
        return get_ansi_string(*self._ansi)
    
    def enable(self, file: Optional[TextIO] = None) -> None:
        """
        Enables the ansi style.
        
        Parameters
        ----------
        file
            File to write to. Defaults to stdout.
        """
        file = file or stdout
        file.write(self.enable_str())
    
    def disable_str(self) -> str:
        """
        Returns escape sequence to disable the ansi style.
        """
        return get_ansi_string(*self._off)
    
    def disable(self, file: Optional[TextIO] = None) -> None:
        """
        Disables the ansi style.
        
        Parameters
        ----------
        file
            File to write to. Defaults to stdout.
        """
        file = file or stdout
        file.write(self.disable_str())

class AnsiNull(Ansi):
    def __init__(self):
        self._ansi = []
        self._off = []

def get_ansi_string(*args: Any) -> str:
    """
    Creates an ansi escape sequence by seperating each
    argument with a semicolon (``;``). Every provided
    argument will be turned into a string.
    """
    return f"\x1b[{';'.join(map(str, args))}m"

def paint(*args: Any, style: Optional[Ansi] = None, sep: str = " ") -> str:
    """
    Styles a string.
    
    Parameters
    ----------
    args
        Objects to style. The ``str()`` function will
        be called on each object.
    
    style
        Ansi object that style the string.
    
    sep
        String that seperates ``args``.
    
    Returns
    -------
    The styled string.
    """
    content = sep.join(map(str, args))
    
    if style is None:
        return content
    
    elif not isinstance(style, Ansi):
        raise TypeError(f"expected `None`, `Ansi` for argument `style`, got {style.__class__.__name__}")
    
    return f"{style}{content}{style.disable_str()}"

def printc(*args: Any, **kwargs: Any) -> None:
    """
    Prints a styled string.
    
    This function takes the same argument as the
    built-in print function. It also provides
    an extra parameter.
    
    Parameters
    ----------
    style
        Ansi objects that style the string.
    """
    paint_kwargs = {}
    
    for key in ["style", "sep"]:
        if key in kwargs:
            paint_kwargs[key] = kwargs.pop(key)
    
    print(paint(*args,
        **paint_kwargs
    ), **kwargs)
