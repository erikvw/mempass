#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest.case import TestCase
from mempass.command_line import main
from .password_generator import PasswordGenerator, mkpassword


class TestUser(TestCase):
    def test_make_password(self):
        pwgen = PasswordGenerator()
        self.assertTrue(pwgen.get_password())

    def test_make_password_strength(self):
        pwgen = PasswordGenerator(nwords=4)
        pwgen.get_password()
        self.assertEqual(pwgen._results.get("score"), 4)

    def test_make_password_strength2(self):
        pwgen = PasswordGenerator(nwords=4)
        pwgen.get_password()
        self.assertIn("Strong", pwgen.results.get("score"))

    def test_make_password_words(self):
        password = mkpassword(4)
        self.assertEqual(len(password.split(" ")), 4)

    def test_basic(self):
        main(4)
