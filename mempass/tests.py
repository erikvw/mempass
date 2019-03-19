#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest.case import TestCase

from mempass import PasswordGenerator, mkpassword


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

    def test_make_password_main(self):
        self.assertEqual(mkpassword(4), 0)

    def test_make_password_main2(self):
        self.assertEqual(mkpassword(0), 0)

    def test_make_password_value(self):
        self.assertRaises(ValueError, mkpassword, "blah")
