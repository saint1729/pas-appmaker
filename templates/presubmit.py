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
import datetime
import shutil


''' Submittime Setup '''

for variable in job.attr_export_env_to_job.split(','):

    ''' Export ALL Options to Environment '''

    key = re.match('(.*)=(.*)', variable).group(1)
    value = re.match('(.*)=(.*)', variable).group(2)
    os.environ[key] = value

    ''' Determine Stage Directory '''

    if re.search('PAS_SUBMISSION_DIRECTORY', variable):

        value = re.match('(.*)=(.*)', variable).group(2)
        server = os.popen('hostname').read()
        regex = re.compile('^pbscp://%s(/.*)' % (server.strip()))
        stage = regex.match(value).group(1)

        os.environ['PAS_STAGE_DIRECTORY'] = stage

if os.path.exists('submittime/submission.hook'):
    shutil.copy2('submittime/submission.hook', os.environ['PAS_STAGE_DIRECTORY'])

os.chdir(os.environ['PAS_STAGE_DIRECTORY'])

''' Enable Logging '''

log = open('submission.log', 'w')

logging = False

if re.search('PAS_ENABLE_LOGGING', variable):

    logging = True

    log.write('\nExported Environment Variables\n')

    for variable in job.attr_export_env_to_job.split(','):
        (key, value) = re.match('(.*)=(.*)', variable).group()

        log.write('\n\t%s = %s' % (key, value))

''' Hook Execution '''

if os.path.exists('submission.hook'):

    hook = subprocess.Popen('submission.hook', stdout=subprocess.PIPE)

    if logging is True:

        log.write('\n\nSubmission Hook Found\n')
        log.write('\n\tSubmission Hook PID: %s' % (str(hook.pid)))

    for output in hook.stdout.readlines():

        if logging is True:
            log.write(output)

    if logging is True:
        log.write('\n\tSubmission Hook PID: %s' % (str(hook.pid)))


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
