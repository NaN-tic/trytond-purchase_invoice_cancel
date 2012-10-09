#This file is part purchase_invoice_cancel module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .invoice import *

def register():
    Pool.register(
        Invoice,
        module='purchase_invoice_cancel', type_='model')
