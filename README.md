# PAS Application Maker

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

## Synopsis

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

## Installation

Typically you add the COMMAND\_HOME variable to your pbsworks.conf file.
This variable must be set to the full path to your /pbsa-commands/ directory.

`echo "COMMAND_HOME=/opt/pbsworks/12.0/portal/scripts/pbsa-commands" >> /etc/pbsworks.conf`

If you do not have your pbsworks.conf file in /etc, you can specify its
location directly via the PBSWORKS\_CONF\_FILE environment variable.

`export PBSWORKS_CONF_FILE=/path/to/pbsworks.conf`

Alternatively, you can override all of this behavior by setting the
PBSWORKS\_SERVER\_HOME and PBSWORKS\_COMMAND\_HOME
variables into your environment.

`export PBSWORKS_SERVER_HOME=/opt/pbsworks/12.0/portal`

and

`export PBSWORKS_COMMAND_HOME=/opt/pbsworks/12.0/portal/scripts/pbsa-commands`

It's good systems security to set proper file permissions for
all of the pbsa-commands.

`chmod 700 /opt/pbsworks/12.0/portal/scripts/pbsa-commands/bin/*`

Finally, you should add the pbsa-commands to your system path.

`export PATH=$PATH:/opt/pbsworks/12.0/portal/scripts/pbsa-commands/bin`

## Cookbook

### Recipe 1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

### Recipe 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

### Recipe 3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

### Recipe 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

### Recipe 5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

### Recipe 6

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

`pas-appmake Appname --select --ncpus --mem --script --environment --compress-results --logging`

## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.