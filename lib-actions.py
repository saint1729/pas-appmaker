import sys
import os
import signal

pid_file = open('runtime.pid', 'r')
pid_num = int(pid_file.readline())
pid_file.close()

if 'PAS_ACTION_SIGNAL' in os.environ:

    signal_name = os.environ['PAS_ACTION_SIGNAL']

    if signal_name == 'Suspend':

        os.kill(pid_num, signal.SIGTSTP)
        sys.stdout.write('Suspend signal sent.')

    elif signal_name == 'Resume':

        os.kill(pid_num, signal.SIGCONT)
        sys.stdout.write('Resume signal sent.')

    elif signal_name == 'Terminate':

        os.kill(pid_num, signal.SIGTERM)
        sys.stdout.write('Terminate signal sent.')
