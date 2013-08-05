#coding: utf-8

'''
© Copyright 2013 Altair Engineering, Inc. All rights reserved.
This code is provided “as is” without any warranty, express or implied, or
indemnification of any kind. All other terms and conditions are as specified
in the Altair PBS Application Services EULA.
'''

import os
import sys
import signal
import subprocess

__version__ = '13.0.0-beta1'


''' Logging '''

log = open('actions.log', 'w')

logging = False

if 'PAS_LOGGING' in os.environ:

    if os.environ['PAS_LOGGING'] == 'true':
        logging = True


''' Hook Execution '''

if os.path.exists('actions.hook'):

    hook = subprocess.Popen('actions.hook', stdout=subprocess.PIPE)

    if logging is True:

        log.write('\n\nActions Hook Found\n')
        log.write('\n\tActions Hook PID: %s' % (str(hook.pid)))

    for output in hook.stdout.readlines():

        if logging is True:
            log.write(output)

    if logging is True:
        log.write('\n\tActions Hook Return Code: %s' % (str(hook.returncode)))


''' Send Signal '''

if 'PAS_ACTION_SEND_SIGNALS' in os.environ:

    pid_file = open('runtime.pid', 'r')
    pid_num = int(pid_file.readline())
    pid_file.close()

    signal_name = os.environ['PAS_ACTION_SIGNALS']

    if signal_name == 'Suspend':

        os.kill(pid_num, signal.SIGTSTP)
        sys.stdout.write('Suspend signal sent.')

    elif signal_name == 'Resume':

        os.kill(pid_num, signal.SIGCONT)
        sys.stdout.write('Resume signal sent.')

    elif signal_name == 'Terminate':

        os.kill(pid_num, signal.SIGTERM)
        sys.stdout.write('Terminate signal sent.')


'''Shell Commands'''

if 'PAS_ACTION_SHELL_COMMANDS' in os.environ:

    for command in os.environ['PAS_ACTION_SHELL_COMMANDS']:
        os.system(command.strip())


log.close()
sys.stdout.flush()
sys.exit(0)
