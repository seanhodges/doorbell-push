#!/usr/bin/env python
"""
SYNOPSIS

    doorbell.py [-v,--verbose,-t,--test]

DESCRIPTION

    Send a push notification when the doorbell is pushed

AUTHOR

    Sean Hodges <seanhodges84@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.
"""

import sys, os, traceback, optparse
import time
import re
import traceback
import logging
import RPi.GPIO as GPIO

from gcm import GCM
from datetime import datetime

# Set the GCM API and reg keys here
API_KEY=
REG_KEY=

def main ():
    global options, args

    logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)
    logger = logging.getLogger('doorbell')

    # Setup GPIO input
    logger.info('Initialising...')
    buttonPin = 25
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN)

    logger.info('Listening for bell pushes')
    while True:
        input = GPIO.input(buttonPin)
        if (input):
            logger.debug('Doorbell activated')
            send_push_notification()
            time.sleep(10.00) # Wait for bell sound to finish
        time.sleep(0.005)

def send_push_notification ():

    current_date = datetime.now().isoformat("T")

    gcm = GCM(API_KEY)
    data = {'date': current_date, 'location': 'Home'}

    reg_ids = [REG_ID]

    res = gcm.json_request(
        registration_ids=reg_ids, data=data,
        collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
    )

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option ('-t', '--test-run', action='store_true', default=False, help='test script with fake booking')
        (options, args) = parser.parse_args()
        if options.verbose: print time.asctime()
        main()
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME:',
        if options.verbose: print (time.time() - start_time)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
