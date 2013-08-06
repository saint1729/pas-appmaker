#coding: utf-8

'''
© Copyright 2013 Altair Engineering, Inc. All rights reserved.
This code is provided “as is” without any warranty, express or implied, or
indemnification of any kind. All other terms and conditions are as specified
in the Altair PBS Application Services EULA.
'''

import subprocess
import zipfile
import os
import sys
import datatime
import shutil
import shlex

__version__ = '13.0.0-prototype1'


''' Logging '''

log = open('start.log', 'w')

logging = False

if 'PAS_LOGGING' in os.environ:

    if os.environ['PAS_LOGGING'] == 'true':
        logging = True

''' Importing Start Environment '''

if os.path.exists('environment.start'):

    if logging is True:
        log.write('\n\nFound Start Environment\n')

    environment_start = open('environment.start', 'r')

    for variable in environment_start.readlines():

        (key, value) = variable.split('=', 1)
        os.environ[key.strip()] = value.strip()

else:

    if logging is True:
        log.write('\n\nNo Start Environment Found\n')

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

''' Executing Start Hook '''

if os.path.exists("hook.start"):

    if logging is True:
        log.write('\nFound Start Hook\n\n')

    command = "hook.start"

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
        log.write('\n\nStart Hook Return Code: %s\n' % (hook.returncode))

else:

    if logging is True:
        log.write('\n\nNo Start Hook Found\n')

os.system('%s %s' % (os.environ['PAS_EXECUTABLE'], shlex(os.environ['PAS_ARGUMENTS'])))

log.close()

sys.stdout.flush()
sys.exit(0)
