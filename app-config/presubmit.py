#coding: utf-8

'''
© Copyright 2013 Altair Engineering, Inc. All rights reserved.
This code is provided “as is” without any warranty, express or implied, or
indemnification of any kind. All other terms and conditions are as specified
in the Altair PBS Application Services EULA.
'''

import time
import re
import grp
import pwd
import os
import sys
import shutil
import subprocess

__version__ = '13.0.0'


''' Exporting All Options to Environment '''

for key, value in os.environ.items():

    if re.match('PAS_', key):
        del os.environ[key]

    elif re.match('PAS_', value):
        del os.environ[key]

for variable in job.attr_export_env_to_job.split(','):

    (key, value) = variable.split('=', 1)
    os.environ[key.strip()] = value.strip()

if 'PAS_SOFTWARE' in os.environ:
    os.environ['PAS_APPLICATION'] = os.environ['PAS_SOFTWARE']

if 'PAS_EXECUTABLE_NAME' in os.environ:
    os.environ['PAS_EXECUTABLE'] = os.environ['PAS_EXECUTABLE_NAME']

''' Change Location to User Stage '''

if 'PAS_SUBMISSION_DIRECTORY' in os.environ:

    elements = os.environ['PAS_SUBMISSION_DIRECTORY'].split('/', 3)
    os.environ['PAS_USER_STAGE'] = elements[3].strip()
    os.chdir('/%s' % (elements[3]))


''' Logging '''

log = open('submit.log', 'w')

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

            os.environ['PAS_APPLICATION_HOME'] = application_home.strip()

            if logging is True:
                log.write('\n\nFound Application Home: %s\n' % (application_home))

            ''' Exporting Submit Environment '''

            if os.path.exists('%s/submittime/environment.submit' % (application_home)):

                path = ('%s/submittime/environment.submit' % (application_home))

                if logging is True:
                    log.write('\n\nFound Environment Submit: %s\n' % (path))

                environment_submit = open(path, 'r')

                for variable in environment_submit.readlines():

                    (key, value) = variable.split('=', 1)
                    os.environ[key.strip()] = value.strip()

            else:

                if logging is True:
                    log.write('\n\nNo Submit Environment Found\n')

            ''' Environment Variable Substitution '''

            if logging is True:
                log.write('\nSubstituting Environment Variables\n')

            for key, value in os.environ.items():

                if re.search('PAS_', value):

                    for k, v in os.environ.items():

                        if re.search('PAS_', k):

                            pattern = re.compile(k, re.UNICODE)

                            for match in pattern.findall(value):

                                value = re.sub(match, v, value)
                                os.environ[key.strip()] = value.strip()

            if logging is True:

                for key, value in os.environ.items():
                    log.write('\n\t%s = %s' % (key.strip(), value.strip()))

    conf.close()

''' Executing Submit Hook '''

if os.path.exists("%s/submittime/hook.submit" % (application_home)):

    if logging is True:
        log.write('\nFound Submit Hook\n\n')

    command = "%s/submittime/hook.submit" % (application_home)

    hook = subprocess.Popen(command, env=os.environ, shell=False, stdout=subprocess.PIPE)

    for line in hook.stdout.readlines():

        if logging is True:
            log.write(line)

    hook.wait()

    if os.path.exists('environment.import'):

        environment_import = open('environment.import', 'r')

        for variable in environment_import.readlines():

            (key, value) = variable.split('=', 1)
            os.environ[key.strip()] = value.strip()

        environment_import.close()

    if logging is True:
        log.write('\n\nSubmit Hook Return Code: %s\n' % (hook.returncode))

else:

    if logging is True:
        log.write('\n\nNo Submit Hook Found\n')

''' Processing Resources '''

if logging is True:
    log.write('\n\nProcessing Resource Requests\n')

resources = ''

if 'PAS_SOFTWARE' in os.environ:

    resources = ('software=%s' % (os.environ['PAS_SOFTWARE'].strip()))

    if logging is True:

        log.write('\n\tSoftware = %s'
                  % (os.environ['PAS_SOFTWARE'].strip()))

if 'PAS_WALLTIME' in os.environ:

    resources = ('%s walltime=%s' % (resources, os.environ['PAS_WALLTIME'].strip()))

    if logging is True:

        log.write('\n\tWalltime = %s'
                  % (os.environ['PAS_WALLTIME'].strip()))

if 'PAS_PLACE' in os.environ:

    resources = ('%s place=%s' % (resources, os.environ['PAS_PLACE']))

    if logging is True:

        log.write('\n\tPlace = %s'
                  % (os.environ['PAS_PLACE'].strip()))

if 'PAS_RESOURCES' in os.environ:

    resources = ('%s %s' % (resources, os.environ['PAS_RESOURCES'].strip()))

    if logging is True:
        log.write('\n\tResources = %s' % (os.environ['PAS_RESOURCES'].strip()))

if 'PAS_SELECT' in os.environ:

    if 'PAS_SELECT_STATEMENT' in os.environ:
        resources = ('%s+%s' % (resources, os.environ['PAS_SELECT'].strip()))

    else:
        resources = ('%s select=%s' % (resources, os.environ['PAS_SELECT'].strip()))

    if logging is True:

        log.write('\n\tSelect = %s'
                  % (os.environ['PAS_SELECT'].strip()))

if 'PAS_NCPUS' in os.environ:

    resources = ('%s:ncpus=%s' % (resources, os.environ['PAS_NCPUS'].strip()))

    if logging is True:
        log.write('\n\tNcpus = %s' % (os.environ['PAS_NCPUS'].strip()))

if 'PAS_PCPUS' in os.environ:

    resources = ('%s:pcpus=%s' % (resources, os.environ['PAS_PCPUS'].strip()))

    if logging is True:
        log.write('\n\tPcpus = %s' % (os.environ['PAS_PCPUS'].strip()))

if 'PAS_MPIPROCS' in os.environ:

    resources = ('%s:mpiprocs=%s' % (resources, os.environ['PAS_MPIPROCS'].strip()))

    if logging is True:
        log.write('\n\tMpiprocs = %s' % (os.environ['PAS_MPIPROCS'].strip()))

if 'PAS_OMPTHREADS' in os.environ:

    resources = ('%s:ompthreads=%s' % (resources, os.environ['PAS_OMPTHREADS'].strip()))

    if logging is True:
        log.write('\n\tOmpthreads = %s' % (os.environ['PAS_OMPTHREADS'].strip()))

if 'PAS_MEM' in os.environ:

    resources = ('%s:mem=%s' % (resources, os.environ['PAS_MEM'].strip()))

    if logging is True:

        log.write('\n\tMem = %s'
                  % (os.environ['PAS_MEM'].strip()))

if 'PAS_VMEM' in os.environ:

    resources = ('%s:vmem=%s' % (resources, os.environ['PAS_VMEM'].strip()))

    if logging is True:

        log.write('\n\tVmem = %s'
                  % (os.environ['PAS_VMEM'].strip()))

if 'PAS_ARCH' in os.environ:

    resources = ('%s:arch=%s' % (resources, os.environ['PAS_ARCH'].strip()))

    if logging is True:

        log.write('\n\tArch = %s'
                  % (os.environ['PAS_ARCH'].strip()))

if logging is True:
    log.write('\n\tFinal Resource Request = %s\n' % (resources.strip()))

job.attr_resource = resources.strip()


''' Processing Attributes '''

if logging is True:
    log.write('\n\nProcessing Attributes\n')

attributes = []

if 'PAS_ATTRIBUTES' in os.environ:

    if re.search('\w+', os.environ['PAS_ATTRIBUTES']):

        for attribute in os.environ['PAS_ATTRIBUTES'].split(','):
            attributes.append(attribute)

        if logging is True:

            log.write('\n\tAttributes = %s'
                      % (os.environ['PAS_ATTRIBUTES'].strip()))

if 'PAS_DEPEND' in os.environ:

    if re.search('\w+', os.environ['PAS_DEPEND']):

        attributes.append('depend=%s'
                          % (os.environ['PAS_DEPEND'].strip()))

        if logging is True:

            log.write('\n\tDependancy = %s'
                      % (os.environ['PAS_DEPEND'].strip()))

if 'PAS_GROUP_LIST' in os.environ:

    if re.search('\w+', os.environ['PAS_GROUP_LIST']):

        attributes.append('group_list=%s'
                          % (os.environ['PAS_GROUP_LIST'].strip()))

        if logging is True:

            log.write('\n\tGroup List = %s'
                      % (os.environ['PAS_GROUP_LIST'].strip()))

if logging is True:
    log.write('\n\tFinal Attribute Request = %s\n' % (','.join(a for a in attributes)))

job.attr_additional_attrs = ','.join(a for a in attributes)


''' Processing Options '''

# Account
if 'PAS_ACCOUNT' in os.environ:

    if re.search('\w+', os.environ['PAS_ACCOUNT']):

        job.attr_accounting_label = os.environ['PAS_ACCOUNT'].strip()

        if logging is True:

            log.write('\n\tAccount = %s'
                      % (os.environ['PAS_ACCOUNT']).strip())

# Queues
if 'PAS_QUEUE' in os.environ:

    job.attr_destination = os.environ['PAS_QUEUE']

    if logging is True:

        log.write('\n\tQueue = %s'
                  % (os.environ['PAS_QUEUE']))

# Mail Handling (Compute Manager User Settings)
if 'MAIL_POINTS' in os.environ:

    if re.match(r"[abe]", os.environ['MAIL_POINTS']):
        job.attr_mail_options = os.environ['MAIL_POINTS'].strip()

if 'MAIL_USERS' in os.environ:
    job.attr_mail_list = os.environ['MAIL_USER'].strip()

# Mail Handling (Application)
if 'MAIL_OPTIONS' in os.environ:

    if re.match(r"[abe]", os.environ['MAIL_OPTIONS']):
        job.attr_mail_options = os.environ['MAIL_OPTIONS']

if 'MAIL_EMAILS' in os.environ:

    if re.match('@', os.environ['MAIL_EMAILS']):
        job.attr_mail_list = os.environ['MAIL_EMAILS'].strip()


''' Importing Environment (and cleaning up our mess) '''

job.attr_export_env_to_job = ','.join(n for n in os.environ)

for key, value in os.environ.items():

    if re.match('PAS_', key):
        del os.environ[key]

    elif re.match('PAS_', value):
        del os.environ[key]

log.close()

os.chown('submit.log',
         pwd.getpwnam(os.environ['AIF_USER']).pw_uid,
         pwd.getpwnam(os.environ['AIF_USER']).pw_gid)

sys.stdout.flush()
sys.exit(0)
