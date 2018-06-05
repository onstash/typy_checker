"""
Packages that exposes type_checker decorator.
"""
__all__ = ("type_checker",)
__author__ = "Santosh Venkatraman<santosh.venk@gmail.com>"

import sys
sys.dont_write_bytecode = True

from .main import type_checker
