# PAS Application Maker

An easy to use framework for making powerful application definitions.

## Synopsis

    pas-appmaker Appname --script --arguments --input-file --include-files --logging

## Setup

By design, App Maker is flexible, and can be installed anywhere!

### Required: App Home

The App Home directory is where your application definitions are located. 
By default App Maker assumes "/var/spool/pas/repository/applications/".

    export PAS_APP_HOME=/var/spool/pas/repository/applications

    pas-appmaker Appname --app-home /my/alternate/applications --ncpus --script --arguments --logging


### Required: App Config

The App Config directory is where your App Maker template files are located.
By default App Maker assumes "/var/spool/pas/conf/app-config/".

    export PAS_APP_CONFIG=/var/spool/pas/conf/app-config

    pas-appmaker Appname --app-config /my/alternate/app-config --ncpus --script --arguments --logging


### Optional: App Development Environment

Make these adjustments to have CM and PAS refresh your applications every minute.

Compute Manager

Check PAS for updated applications every minute.

``/opt/altair/pbsworks/12.0/services/cm/config/spring-config.xml``

```
<bean id="updateAppTrigger" class="org.springframework.scheduling.quartz.CronTriggerBean">
    <property name="jobDetail">
        <ref bean="updateAppBean" />
    </property>
    <property name="cronExpression">
        <value>0 * * * * ?</value>
    </property>
</bean>
```

PBS Application Services

Remove the time_stamp.txt file every minute.

``/etc/cron.d/pas-time_stamp.remove``

```
* * * * * root rm -rf /var/spool/pas/repository/time_stamp.txt
```

## Tutorial: Some basic concepts

App Maker allows you to present options to users in a variety of ways. 
You can also pre-define options by setting them explicitly before the job is submitted to PBS.

### byForm

A few examples of how to create applications where HTML form fields are how you would prefer users to request their resources.

```
pas-appmaker byForm1 --select --ncpus --mem --place --application --executable --arguments --logging
```
```
pas-appmaker byForm2 --environment-submit PAS_SELECT=1 --ncpus --mem --application --script --input-file --include-files --logging
```
```
pas-appmaker byForm3 --environment-submit PAS_NCPUS=16,PAS_MEM=8gb,PAS_PLACE=pack --select --application --script --arguments --logging
```

### byStatement

A few examples of how to create applications where advanced users, more comfortable with the command-line, could select resources and attributes using the familiar select and attribute syntax of qsub.

```
pas-appmaker byStatement1 --select-statement --additional-attributes --application --executable --arguments --logging
```
```
pas-appmaker byStatement2 --environment-submit PAS_SELECT_STATEMENT=select=4:ncpus=16:mem=8gb:walltime=10:10:00 --application --executable --arguments --logging
```
```
pas-appmaker byStatement3 --environment-submit PAS_SELECT_STATEMENT=PAS_SELECT_STATEMENT:walltime=10:10:00 --select-statement --application --executable --arguments --logging
```

### byDirective

A couple of examples that demonstrate how to create applications where resources and attributes are requested inside the job script.

```
pas-appmaker byDirective1 --application --script --arguments --logging
```
```
pas-appmaker byDirective2 --environment-submit PAS_APPLICATION=Appname,PAS_SCRIPT=/path/to/app_name.sh --arguments --logging
```

## Tutorial: More advanced concepts

App Maker allows you to modify and extend its core functionality using hooks written in a language(s) you are comfortable with.

### SubmitHook

Example of executing a Perl hook before the job is submitted to PBS. 
This hook will set the PAS_SELECT_STATEMENT to the resources you specify.

```
#!/usr/bin/perl

use strict;
use warnings;

use IO::File;

if (not defined $ENV{'PAS_SELECT_STATEMENT'}) {
    $ENV{'PAS_SELECT_STATEMENT'} = 'select=1:ncpus=1:mem=1gb';
}

if (not defined $ENV{'PAS_ADDITIONAL_ATTRIBUTES'}) {
    $ENV{'PAS_ADDITIONAL_ATTRIBUTES'} = 'group_list=hpcteam@cluster';
}

### Export any environment changes to App Maker and exit.

my $environment = IO::File->new('environment.import', 'w');

if (defined $environment) { 

    for my $variable (keys %ENV) {
        print $environment "$variable=$ENV{$variable}\n";
    }
}

undef $environment and exit(0);

```
```
pas-submit SubmitHook --hook-submit /path/to/my/hook.pl --application --executable --arguments --logging
```

### StartHook

Example of executing a Python hook before the job starts. 
This hook will set the PAS_LOGGING option to true, and will also set a job executable with the PAS_EXECUTABLE option.

```
#!/usr/bin/env python
#coding: utf-8

import os
import sys

os.environ['PAS_LOGGING'] = 'true'

if not 'PAS_EXECUTABLE' in os.environ:
    os.environ['PAS_EXECUTABLE'] = '/path/to/program.bin'

### Export any environment changes to App Maker and exit.

environment = open('environment.import', 'w')

for k, v in os.environ.items():
    environment.write('%s=%s\n', % (k, v))

environment.close()
sys.exit(0)

```
```
pas-submit StartHook --hook-start /path/to/my/hook.py --environment-submit PAS_SELECT=1 --ncpus --mem --input-file --include-files --arguments
```

### FinishedHook

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Tutorial: Bringing it all together

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### OptiStruct

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### RADIOSS

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Abaqus

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### NASTRAN

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### LS-Dyna

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Reference

```
Usage: pas-appmaker <APPLICATION> [Options]

A simple framework for making powerful application definitions.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --app-home=$PAS_HOME/repository/applications
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
  --app-config=$PAS_HOME/conf/app-config
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.

  Resources:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus.

    --select-statement  Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --select            Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --ncpus             Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --pcpus             Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --mpiprocs          Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --ompthreads        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --mem               Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --vmem              Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --walltime          Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --arch              Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --place             Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --additional-resources
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.

  Attributes:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus.

    --depend            Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --group-list        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --additional-attributes
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.

  Options:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus. Curabitur et augue vehicula, elementum lacus ornare,
    adipiscing massa. Maecenas ut massa posuere, consequat felis quis,
    interdum orci.

    --account           Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --queue             Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --mail              Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.
    --job-arrays        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus.

  Execution:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus. Curabitur et augue vehicula, elementum lacus ornare,
    adipiscing massa. Maecenas ut massa posuere, consequat felis quis,
    interdum orci.

    --application       Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --environment       Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --executable        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --script            Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --arguments         Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.

  Files:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus. Curabitur et augue vehicula, elementum lacus ornare,
    adipiscing massa. Maecenas ut massa posuere, consequat felis quis,
    interdum orci.

    --input-file        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --master-file       Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --starter-file      Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --engine-file       Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --include-files     Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --compress-results  Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.

  Actions:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus. Curabitur et augue vehicula, elementum lacus ornare,
    adipiscing massa. Maecenas ut massa posuere, consequat felis quis,
    interdum orci.

    --send-signals      Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --shell-commands    Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.

  Developer Tools:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl
    ac faucibus. Curabitur et augue vehicula, elementum lacus ornare,
    adipiscing massa. Maecenas ut massa posuere, consequat felis quis,
    interdum orci.

    --logging           Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --environment-submit=ENVIRONMENT_SUBMIT
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --environment-start=ENVIRONMENT_START
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --environment-actions=ENVIRONMENT_ACTIONS
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --environment-finished=ENVIRONMENT_FINISHED
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --hook-submit=HOOK_SUBMIT
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --hook-start=HOOK_START
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --hook-actions=HOOK_ACTIONS
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
    --hook-finished=HOOK_FINISHED
                        Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit. In sollicitudin felis id lobortis dictum. Nullam
                        elementum rhoncus nisl ac faucibus. Curabitur et augue
                        vehicula, elementum lacus ornare, adipiscing massa.
                        Maecenas ut massa posuere, consequat felis quis,
                        interdum orci.
```

## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.
