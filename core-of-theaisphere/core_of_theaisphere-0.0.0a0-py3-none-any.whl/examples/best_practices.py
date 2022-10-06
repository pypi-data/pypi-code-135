"""
This script illustrates how to follow some best-practices for coding
"""
"""
Author: vickyparmar
File: best_practices.py
Created on: 05-10-2022, Wed, 17:38:09

Last modified by: vickyparmar
Last modified on: 05-10-2022, Wed, 17:44:58
"""

# Imports
from typing import List, Any
import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
logger = logging.getLogger(__name__)


# Class ListBestPractices
class ListBestPractices:
    """
            Description of the class.

            ...

            Parameter
            ---------
            a: List
                Description of variable a.
            b: Any
                Description of variable b.

            Method
            ------
            method1(param='abcd')
                Description of method 1.
            method2(param=xyz)
                Description of method 2.

            Raise
            -----
            type of Exception raised
                Description of raised exception.

            See Also
            --------
            othermodule : Other module to see.

            Notes
            -----
            The FFT is a fast implementation of the discrete Fourier transform:

            .. deprecated:: version
              `ndobj_old` will be removed in NumPy 2.0.0, it is replaced by
              `ndobj_new` because the latter works also with array subclasses.

            Example
            -------
            >>> provided an example
            """
    def __init__(self, a: List, b: Any):
        """
        Initializing the class instance
        Parameters
        ----------
        a: List
            Description of variable a
        b: Any
            Description of variable b
        """
        self.a = a
        self.b = b
        logger.info(f"A: {a}, B: {b}")
