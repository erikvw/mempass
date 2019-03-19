#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from mempass import mkpassword


def main():
    try:
        nwords = int(sys.argv[1])
    except IndexError:
        return usage(sys.argv[0])
    else:
        mkpassword(nwords, verbose=True)
    return 0


def usage(argv0):
    p = sys.stderr.write
    p("Usage: %s nwords [nbits]\n" % argv0)
    p("Generates a password of nwords words")
    p("\nRecommended:\n")
    p("    %s 5\n" % argv0)
    return 1
