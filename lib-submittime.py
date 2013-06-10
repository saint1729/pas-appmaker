#!/usr/bin/env python
#coding: utf-8

'''
© Copyright 2013 Altair Engineering, Inc. All rights reserved.
This code is provided “as is” without any warranty, express or implied, or
indemnification of any kind. All other terms and conditions are as specified
in the Altair PBS Analytics EULA.
'''

import re
import os
import zipfile
import time

''' Change Directory to Job Stage '''

for variable in job.attr_export_env_to_job.split(','):
    if re.search('PAS_SUBMISSION_DIRECTORY', variable):

        value = re.match('(.*)=(.*)', variable).group(2)
        server = os.popen('hostname').read()
        regex = re.compile('^pbscp://%s(/.*)' % (server.strip()))
        stage = regex.match(value).group(1)

        os.chdir(stage)

''' Enable Logging '''

log = open('submittime.log', 'w')

logging = False

for variable in job.attr_export_env_to_job.split(','):
    if re.search('PAS_ENABLE_LOGGING', variable):

        logging = True

        log.write('\nExported Environment Variables\n')

        for variable in job.attr_export_env_to_job.split(','):
            (key, value) = re.match('(.*)=(.*)', variable).group()

            log.write('\n\t%s = %s' % (key, value))

''' Queue Options '''

job.attr_destination = userInputs['QUEUE']

if logging is True:
    log.write('\n' % (userInputs['QUEUE']))

''' Compute Manager Mail Options '''

if userInputs['MAIL_USERS']:
    job.attr_mail_list = userInputs['MAIL_USERS']

if userInputs['MAIL_POINTS']:
    mail_points = userInputs['MAIL_POINTS']

    if re.match(r"[abe]", mail_points):
        job.attr_mail_options = mail_points

''' Resources & Attributes '''

job.attr_resource = userInputs['RESOURCES']
job.attr_additional_attrs = userInputs['ATTRIBUTES']

log.close()
