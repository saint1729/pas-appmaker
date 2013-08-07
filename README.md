# PAS Application Maker

An easy to use framework for making powerful application definitions.

## Help

    pas-appmaker --help

## Setup

This section is for administrators who are deploying App Maker in their environment for the first time.
If App Maker is already deployed and configured on this system please skip ahead to the Tutorials section.

### Required: App Home

The App Home directory is where your application definitions are located. 
By default App Maker assumes "/var/spool/pas/repository/applications/".

    export PAS_APP_HOME=/var/spool/pas/repository/applications
    
    or
    
    pas-appmaker Appname --ncpus --script --arguments --logging --app-home /my/alternate/applications


### Required: App Config

The App Config directory is where your App Maker template files are located.
By default App Maker assumes "/var/spool/pas/conf/app-config/".

    export PAS_APP_CONFIG=/var/spool/pas/conf/app-config
    
    or
    
    pas-appmaker Appname --ncpus --script --arguments --logging --app-config /my/alternate/app-config 


### Optional: App Environment

Make these adjustments to have CM and PAS refresh your applications every minute.

Compute Manager

Check PAS for updated applications every minute.

    vim /opt/altair/pbsworks/12.0/services/cm/config/spring-config.xml

    <bean id="updateAppTrigger" class="org.springframework.scheduling.quartz.CronTriggerBean">
        <property name="jobDetail">
            <ref bean="updateAppBean" />
        </property>
        <property name="cronExpression">
            <value>0 * * * * ?</value>
        </property>
    </bean>

PBS Application Services

Remove the time_stamp.txt file every minute.

    vim /etc/cron.d/pas-timestamp-remove

    * * * * * root rm -rf /var/spool/pas/repository/time_stamp.txt

### Optional: App Updates

You can easily download and deploy automatic updates.

    vim /etc/cron.daily/pas-appmaker-update
    
    #!/bin/sh
    
    cd /var/spool/pas/repository
    wget ftp://ftp.altair.com/pub/outgoing/pas-appmaker/pas-appmaker-`date +%F`.tar.gz
    tar -xvf pas-appmaker-`date +%F`.tar.gz

## Tutorial: Some basic concepts

App Maker allows you to present resources, atrributes and other job options to users in a variety of different ways.

### byForm

An example of how to create an application where HTML form fields are how you would prefer users to request their resources.

    pas-appmaker byForm --select --ncpus --mem --place --application --executable --arguments --logging

### byStatement

An example of how to create an application where advanced users, more comfortable with the command-line, can request resources and attributes using the familiar select and attribute syntax of qsub.

    pas-appmaker byStatement --select-statement --additional-attributes --application --executable --arguments --logging

### byDirective

An example that demonstrates how to create an application where resources are requested from inside the job script.

    pas-appmaker byDirective --application --script --arguments --logging


## Tutorial: Making real-world applications

A few examples of how App Maker can easily create application definitions for common solvers.

### OptiStruct

    pas-appmaker OptiStruct --ncpus --mem --arguments --master-file --include-files --compress-results --logging --environment-submit PAS_SELECT=1 --environment-start PAS_EXECUTABLE=/path/to/optistruct,ALTAIR_LICENSE_FILE=6200@host

### RADIOSS

    pas-appmaker RADIOSS --ncpus --mem --arguments --master-file --starter-file --engine-file --compress-results --logging --environment-submit PAS_SELECT=1 --environment-start PAS_EXECUTABLE=/path/to/radioss,ALTAIR_LICENSE_FILE=6200@host

### Abaqus

    pas-appmaker Abaqus --select --ncpus --mem --place --input-file --include-files --arguments --environment --compress-results --logging --environment-start PAS_EXECUTABLE=/path/to/abaqus


## Tutorial: Some advanced concepts

App Maker allows you to modify and extend its core functionality using hooks written in a language(s) you are comfortable with.

### SubmitHook

Example of executing a Perl hook before the job is submitted to PBS. 

Hook

    #!/usr/bin/env perl

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

Command

    pas-appmaker SubmitHook --application --executable --arguments --logging --hook-submit /path/to/my/hook.pl 


### StartHook

Example of executing a Python hook before the job starts. 

Hook

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

Command

    pas-appmaker StartHook --application --ncpus --mem --script --input-file --include-files --arguments --logging --environment-submit PAS_SELECT=1 --hook-start /path/to/my/hook.py 


## Downloads

You can download hourly developer snapshots at anytime.

    ftp://ftp.altair.com/pub/outgoing/pas-appmaker


## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.
