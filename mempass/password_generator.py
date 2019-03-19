#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Adapted from https://github.com/jesterpm/bin/blob/master/mkpasswd
"""

import itertools
import os
import sys

from secrets import choice
from warnings import warn
from zxcvbn import zxcvbn


strength_score = {
    0: "Very weak (0 out of 4)",
    1: "Weak (1 out of 4)",
    2: "Poor (2 out of 4)",
    3: "Moderate (3 out of 4)",
    4: "Strong! (4)",
}


class PasswordGenerator:

    filename = os.path.join("/usr", "share", "dict", "words")
    nwords = 3
    max_wordlength = 9

    def __init__(self, nwords=None, max_wordlength=None, filename=None, **kwargs):
        self._results = None
        self.filename = filename or self.filename
        self.nwords = nwords or self.nwords
        self.max_wordlength = max_wordlength or self.max_wordlength
        self.wordlist = self._read_file(self.filename)

    def get_password(self):
        password = " ".join(choice(self.wordlist) for _ in range(self.nwords))
        self._results = zxcvbn(password)
        self._results["password"] = None
        return password

    @property
    def results(self):
        score = strength_score.get(self._results.get("score"))
        warning = self._results.get("feedback").get("warning")
        suggestions = " ".join(self._results.get("feedback").get("suggestions")).strip()
        return dict(score=score, warning=warning, suggestions=suggestions)

    def _read_file(self, filename):
        return [
            line.split()[0]
            for line in itertools.islice(open(filename), 0, None)
            if len(line.split()[0]) < self.max_wordlength
            and line.split()[0].lower() == line.split()[0]
        ]


def mkpassword(nwords, verbose=None):
    pwgen = PasswordGenerator(nwords=nwords)
    password = pwgen.get_password()
    if verbose:
        p = sys.stderr.write
        p(f"password: {password}\n")
        p(f"score: {pwgen.results.get('score')}\n")
        warning = pwgen.results.get("warning")
        suggestions = pwgen.results.get("suggestions")
        if warning:
            warn(f"Warning: {warning}\n")
        if suggestions:
            p(f"{suggestions}\n")
    return password
