# PAS Application Maker

The intent of these commands is to remove the perception that setting up PBS Analytics is difficult, by providing
a simple and consistent experience for the majority of configuration cases. To achieve this, it's important that
these commands be seen as the primary configuration interface to PBS Analytics. For more advanced situations, our
documentation shall provide an "Advanced Configuration" section where administrators and AE's can learn about the
format and syntax of the individual configuration files for those few cases that may not be covered by these commands.

## Targeted for PAS 12.0.1 _(GA)_

### Configuration Commands

* pbsa-config-nodes _(functional)_
* pbsa-config-groups _(functional)_
* pbsa-config-holidays _(functional)_
* pbsa-config-exits _(functional)_
* pbsa-config-parser _(wip)_
* pbsa-config-dc _(wip)_
* pbsa-config-resources _(wip)_

### Dataset Commands
 
* pbsa-data-password _(functional)_
* pbsa-data-reset _(functional)_

## Installation Procedure

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

## Copyright

© Copyright 2012-2013 Altair Engineering, Inc. All rights reserved.