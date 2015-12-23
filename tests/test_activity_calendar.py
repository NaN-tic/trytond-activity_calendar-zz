# This file is part of the activity_calendar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ActivityCalendarTestCase(ModuleTestCase):
    'Test Activity Calendar module'
    module = 'activity_calendar'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ActivityCalendarTestCase))
    return suite
