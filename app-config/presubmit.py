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

for key, value in os.environ.items():

    if re.match('PAS_', key):
        del os.environ[key]

    elif re.match('PAS_', value):
        del os.environ[key]

for variable in job.attr_export_env_to_job.split(','):

    (key, value) = variable.split('=', 1)
    os.environ[key.strip()] = value.strip()

''' Change Location to User Stage '''

if 'PAS_SUBMISSION_DIRECTORY' in os.environ:

    elements = os.environ['PAS_SUBMISSION_DIRECTORY'].split('/', 3)
    os.chdir('/%s' % (elements[3]))

''' Logging '''

log = open('submittime.log', 'w')

logging = False

if 'PAS_LOGGING' in os.environ:

    if os.environ['PAS_LOGGING'] == 'true':
        logging = True

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

            ''' Importing Environment '''

            if os.path.exists('%s/submittime/submittime.environment' % (application_home)):

                path = ('%s/submittime/submittime.environment' % (application_home))

                if logging is True:
                    log.write('\n\nFound Submission Environment to Import: %s\n' % (path))

                submittime_import = open(path, 'r')

                for variable in submittime_import.readlines():

                    (key, value) = variable.split('=', 1)
                    os.environ[key.strip()] = value.strip()

            else:

                if logging is True:
                    log.write('\n\nNo Submission Environment to Import Found\n')

            ''' Environment Variable Parser '''

            if logging is True:
                log.write('\nParsing Environment Variables\n')

            for key, value in os.environ.items():

                if re.search('PAS_', value):

                    for key_parser, value_parser in os.environ.items():

                        if re.search('PAS_', key_parser):

                            if re.match(key_parser, value):

                                value = re.sub(key_parser, value_parser, value)
                                os.environ[key.strip()] = value.strip()

            ''' Export All Options and Environment Variables '''

            if logging is True:

                log.write('\nExported Options and Environment Variables\n')

                for key, value in os.environ.items():
                    log.write('\n\t%s = %s' % (key.strip(), value.strip()))

            ''' Hook Execution '''

            if os.path.exists('%s/submittime/submittime.hook' % (application_home)):

                path = ('%s/submittime/submittime.hook' % (application_home))

                if logging is True:
                    log.write('\n\nFound Submission Hook Import: %s\n' % (path))

                #hook = subprocess.Popen(path, stdout=PIPE).communicate()[0]

            #    if logging is True:
            #        log.write('\n\tSubmittime Hook PID: %s\n\n' % (str(hook.pid)))
            #
            #    for output in hook.stdout.readlines():
            #
            #        if logging is True:
            #            log.write(output)
            #else:
            #
            #    if logging is True:
            #        log.write('\n\nNo Submission Hook Import Found\n')

    conf.close()

''' Processing Resource Requests '''

if logging is True:
    log.write('\n\nProcessing Resource Requests\n')

statement = ('software=%s' % (os.environ['PAS_APPLICATION'].strip()))

if 'PAS_STATEMENT' in os.environ:

    statement = ('%s %s' % (statement, os.environ['PAS_STATEMENT'].strip()))

    if logging is True:
        log.write('\n\tStatement = %s' % (os.environ['PAS_STATEMENT'].strip()))

if not 'PAS_SELECT' in os.environ:
    os.environ['PAS_SELECT'] = '1'

if 'PAS_SELECT' in os.environ:

    if 'PAS_STATEMENT' in os.environ:
        statement = ('%s+%s' % (statement, os.environ['PAS_SELECT'].strip()))

    else:
        statement = ('%s select=%s' % (statement, os.environ['PAS_SELECT'].strip()))

    if logging is True:
        log.write('\n\tSelect = %s' % (os.environ['PAS_SELECT'].strip()))

if 'PAS_NCPUS' in os.environ:

    statement = ('%s:ncpus=%s' % (statement, os.environ['PAS_NCPUS'].strip()))

    if logging is True:
        log.write('\n\tNcpus = %s' % (os.environ['PAS_NCPUS'].strip()))

if 'PAS_PCPUS' in os.environ:

    statement = ('%s:pcpus=%s' % (statement, os.environ['PAS_PCPUS'].strip()))

    if logging is True:
        log.write('\n\tPcpus = %s' % (os.environ['PAS_PCPUS'].strip()))

if 'PAS_MPIPROCS' in os.environ:

    statement = ('%s:mpiprocs=%s' % (statement, os.environ['PAS_MPIPROCS'].strip()))

    if logging is True:
        log.write('\n\tMpiprocs = %s' % (os.environ['PAS_MPIPROCS'].strip()))

if 'PAS_OMPTHREADS' in os.environ:

    statement = ('%s:ompthreads=%s' % (statement, os.environ['PAS_OMPTHREADS'].strip()))

    if logging is True:
        log.write('\n\tOmpthreads = %s' % (os.environ['PAS_OMPTHREADS'].strip()))

if 'PAS_MEM' in os.environ:

    statement = ('%s:mem=%s' % (statement, os.environ['PAS_MEM'].strip()))

    if logging is True:
        log.write('\n\tMem = %s' % (os.environ['PAS_MEM'].strip()))

if 'PAS_VMEM' in os.environ:

    statement = ('%s:vmem=%s' % (statement, os.environ['PAS_VMEM'].strip()))

    if logging is True:
        log.write('\n\tVmem = %s' % (os.environ['PAS_VMEM'].strip()))

if 'PAS_WALLTIME' in os.environ:

    statement = ('%s:walltime=%s' % (statement, os.environ['PAS_WALLTIME'].strip()))

    if logging is True:
        log.write('\n\tWalltime = %s' % (os.environ['PAS_WALLTIME'].strip()))

if 'PAS_ARCH' in os.environ:

    statement = ('%s:arch=%s' % (statement, os.environ['PAS_ARCH'].strip()))

    if logging is True:
        log.write('\n\tArch = %s' % (os.environ['PAS_ARCH'].strip()))

if 'PAS_PLACE' in os.environ:

    statement = ('%s place=%s' % (statement, os.environ['PAS_PLACE']))

    if logging is True:
        log.write('\n\tPlace = %s' % (os.environ['PAS_PLACE'].strip()))

if logging is True:
    log.write('\n\nFinal Resource Request = %s\n' % (statement.strip()))

job.attr_resource = statement.strip()

''' Processing Attribute Requests '''

if 'PAS_QUEUE' in os.environ:

    job.attr_destination = os.environ['PAS_QUEUE']

    if logging is True:
        log.write('\n\tQueue = %s' % (os.environ['PAS_QUEUE']))

''' Importing Environment to Runtime '''
job.attr_export_env_to_job = ','.join(n for n in os.environ)

log.close()
