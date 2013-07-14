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
import subprocess


''' Exporting All Options to Environment '''

for variable in job.attr_export_env_to_job.split(','):

    (key, value) = variable.split('=', 1)
    os.environ[key.strip()] = value.strip()

''' Change Location to User Stage '''

if 'PAS_SUBMISSION_DIRECTORY' in os.environ:

    elements = os.environ['PAS_SUBMISSION_DIRECTORY'].split('/', 3)
    os.chdir(elements[3])

''' Logging '''

log = open('submittime.log', 'w')

logging = False

if 'PAS_LOGGING' in os.environ:

    logging = True

    log.write('\nExported Environment Variables\n')

    for key, value in os.environ.items():
        log.write('\n\t%s = %s' % (key.strip(), value.strip()))

''' Processing PAS Configuration '''

if os.path.exists('/etc/pas.conf'):

    conf = open('/etc/pas.conf', 'r')

    for line in conf.readlines():

        if re.match('PAS_HOME', line):

            (key, value) = line.split('=')

            if logging is True:
                log.write('\n\nFound PAS Home: %s\n' % (value.strip()))

            application_home = ('%s/repository/applications/%s'
                                % (value.strip(), os.environ['PAS_APPLICATION']))

            if logging is True:
                log.write('\n\nFound Application Home: %s\n' % (application_home))

            ''' Hook Execution '''

            if os.path.exists('%s/submittime/submittime.hook' % (application_home)):

                path = ('%s/submittime/submittime.hook' % (application_home))

                if logging is True:
                    log.write('\n\nFound Submission Hook: %s\n' % (path))

                # temporary way to execute hooks...
                #os.system('%s' % (path))

                #hook = subprocess.Popen(path, stdout=subprocess.PIPE)

                #if logging is True:
                #    log.write('\n\tSubmittime Hook PID: %s\n\n' % (str(hook.pid)))
                #
                #for output in hook.stdout.readlines():
                #
                #    if logging is True:
                #        log.write(output)

            else:

                if logging is True:
                    log.write('\n\nNo Submission Hook Found\n')
    conf.close()

''' Processing Resources & Attribuets '''

if logging is True:
    log.write('\n\nProcessing Resources & Attributes\n')

if 'PAS_QUEUE' in os.environ:

    job.attr_destination = os.environ['PAS_QUEUE']

    if logging is True:
        log.write('\n\tQueue = %s' % (os.environ['PAS_QUEUE']))

''' Select and Resource Builder '''

select = ''

if 'PAS_STATEMENT' in os.environ:

    select = ('%s;' % (os.environ['PAS_STATEMENT']))

    if logging is True:
        log.write('\n\tStatement = %s' % (os.environ['PAS_STATEMENT']))

if 'PAS_SELECT' in os.environ:
    select = ('%s:%s' % (select, os.environ['PAS_SELECT']))

#if userInputs['MEM']:
#    select = ('%s:%s' % (ncpus, userInputs['MEM']))

#if userInputs['MEM']:
#    select = ('%s:%s' % (ncpus, userInputs['MEM']))

job.attr_resource = select

log.close()
