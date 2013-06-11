#coding: utf-8

'''
© Copyright 2013 Altair Engineering, Inc. All rights reserved.
This code is provided “as is” without any warranty, express or implied, or
indemnification of any kind. All other terms and conditions are as specified
in the Altair PBS Analytics EULA.
'''

import subprocess
import zipfile
import os
import sys
import datatime
import shutil

__version__ = '12.0.0'

''' Enable Logging '''

log = open('runtime.log', 'w')

logging = False

if 'PAS_ENABLE_LOGGING' in os.environ:
    if os.environ['PAS_ENABLE_LOGGING'] == 'true':

        logging = True

        log.write('\nRuntime Environment Variables\n')

        for variable in os.environ.split(';'):
            (key, value) = re.match('(.*)=(.*)', variable).group()

            log.write('\n\t%s = %s' % (key, value))

''' Hook Execution '''

if os.path.exists('execution.hook'):

    hook = subprocess.Popen('execution.hook', stdout=subprocess.PIPE)

    if logging is True:

        log.write('\n\nExecution Hook Found\n')
        log.write('\n\tExecution Hook PID: %s' % (str(hook.pid)))

    for output in hook.stdout.readlines():

        if logging is True:
            log.write(output)

    if logging is True:
        log.write('\n\tExecution Hook PID: %s' % (str(hook.pid)))

''' Input File Processing '''

if 'PAS_INPUT_FILE' in os.environ:

    input_file = os.path.basename(os.environ['PAS_INPUT_FILE'])

    if logging is True:
        log.write('\n\nFound an Input File\n' % (input_file))

    if zipfile.is_zipfile(input_file):
        package = zipfile.ZipFile(input_file, 'r')

        if logging is True:
            log.write('\n\tReading Input File ZIP Archive: %s' % (input_file))

        for file in package.namelist():

            if re.search('master', file, re.IGNORECASE):

                os.environ['PAS_MASTER_FILE'] = file

                if logging is True:
                    log.write('\n\tFound Master File: %s' % (file))

            elif re.search('starter', file, re.IGNORECASE):

                os.environ['PAS_STARTER_FILE'] = file

                if logging is True:
                    log.write('\n\tFound Starter File: %s' % (file))

            elif re.search('engine', file, re.IGNORECASE):

                os.environ['PAS_ENGINE_FILE'] = file

                if logging is True:
                    log.write('\n\tFound Engine File: %s' % (file))

        package.close

        os.system("unzip %s" % (input_file))

    else:

        os.environ['PAS_INPUT_FILE'] = input_file

        if logging is True:
            log.write('\n\tUsing Input File: %s' % (input_file))

    sys.stdout.flush()

''' Job Argument Processing '''

if 'PAS_JOB_ARGS' in os.environ:

    if logging is True:
        log.write('\n\nProcessing Job Arguments\n')

    for key, value in os.environ.items():
        if re.match(key, os.environ['PAS_JOB_ARGS']):

            regex = re.compile(key)
            regex.sub(value, os.environ['PAS_JOB_ARGS'])

            if logging is True:
                log.write('\n\tModifying: %s' % (key))

        sys.stdout.flush()

''' Executing Job Script '''

if 'PAS_JOB_SCRIPT' in os.environ:

    if logging is True:
        log.write('\n\nExecuting Job Script\n\n')

    job_script = os.path.basename(os.environ['PAS_JOB_SCRIPT'])
    job_script = job_script.replace('%20', ' ')

    def run(interpreter):

        runtime = subprocess.Popen(interpreter, job_script,
                                    os.environ['PAS_JOB_ARGS']], stdout=subprocess.PIPE)

        if logging is True:
            log.write('\n\tJob Script PID: %s' % (str(runtime.pid)))

        ''' Send Signal Processing '''

        pid_file = open('runtime.pid', 'w')
        pid_file.write(str(runtime.pid))
        pid_file.close()

        def trap_signal(signum, stack):

            signal_name = str(signum)

            if logging is True:
                log.write('\n\tReceived Signal: %s' % (signal_name))

            sys.stdout.write()
            sys.stdout.flush()

        ''' Standard Output '''

        for output in runtime.stdout.readlines():

            signal.signal(signal.SIGTSTP, trap_signal)
            signal.signal(signal.SIGCONT, trap_signal)
            signal.signal(signal.SIGTERM, trap_signal)

            sys.stdout.write(output)
            sys.stdout.flush()

        ''' Compress Results '''

        if 'PAS_COMPRESS_RESULTS' in os.environ:

            if os.environ['PAS_COMPRESS_RESULTS'] == 'true':

                job_name = job_script.replace('%20', ' ')

                os.system("zip \"%s-results.zip\" *" % (job_name))

                if logging is True:
                    log.write('\n\tCompressing Results: %s-results.zip' % (job_name))

                sys.stdout.flush()

        log.close()
        sys.stdout.flush()
        sys.exit(runtime.returncode)

    file = open(job_script, 'r')
    line = file.readline()
    file.close()

    if line.startswith('#!'):
        run(re.match('^#!(.*)', line).group(1))

    else:
        run(os.environ['PAS_PYTHONPATH''])

log.close()
sys.stdout.flush()
sys.exit(0)
