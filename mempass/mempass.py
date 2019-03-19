#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Adapted from https://github.com/jesterpm/bin/blob/master/mkpasswd
"""

import sys

from warnings import warn

from .password_generator import PasswordGenerator


class Mempass:

    def __init__(self, nwords=None, verbose=None):
        self.password = None
        self.score = None
        self.warning = None
        self.verbose = True if verbose is None else False
        self.mkpassword(nwords or 5)

    def mkpassword(self, nwords):
        nwords = int(nwords)
        pwgen = PasswordGenerator(nwords=nwords)
        self.password = pwgen.get_password()
        self.score = pwgen.results.get("score")
        self.warning = pwgen.results.get("warning")
        self.suggestions = pwgen.results.get("suggestions")
        if self.verbose:
            p = sys.stderr.write
            p(f"password: {self.password}\n")
            p(f"score: {self.score}\n")
            if self.warning:
                warn(f"Warning: {self.warning}\n")
            if self.suggestions:
                p(f"{self.suggestions}\n")
        return None
