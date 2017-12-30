"""
#
# Author:       L. Saetta
# created:      30 december 2017
# last update:  30/12/2017
#
# published under MIT license (see LICENSE file)
"""

# pylint: disable=invalid-name

import json
import datetime
import configparser

config = configparser.ConfigParser()
config.read('gateway.ini')

OBDDATA_FORMAT_STRING = config['DEFAULT']['OBDDATA_FORMAT_STRING']

STFORMAT1 = "%d-%m-%Y %H:%M:%S"

class OBDIISimulator(object):
    """ This class simulate data from OBDII """

    # Constructor
    def __init__(self):
        self.connOK = False
    
        self.connOK = True

        print('Connected to OBDII...\n')

    def getENGINELOAD(self):
        # test reducing to 3 decimals
        eng_load = 33.3333395
        eng_load = self.format_float(eng_load)

        return eng_load
    
    # utility method to format float with a fixed number of decimals
    def format_float(self, value):
        return float(OBDDATA_FORMAT_STRING.format(value))

    # method definition
    def getMessage(self):
        msg = {}
        msg['DTIME'] = datetime.datetime.now().strftime(STFORMAT1)
        
        msg['ENGINE_LOAD'] = self.getENGINELOAD()
        msg['COOLANT_TEMP'] = 66
        msg['RPM'] = 1000
        msg['SPEED'] = 25
        msg['RUN_TIME'] = 100
        # msg['FUEL_LEVEL'] = 30
        msg['AMBIANT_AIR_TEMP'] = 12
        # msg['OIL_TEMP'] = 88

        return msg