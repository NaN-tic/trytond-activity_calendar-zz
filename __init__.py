#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.

from trytond.pool import Pool
from .activity import *

def register():
    Pool.register(
        Activity,
        module='activity_calendar', type_='model')
