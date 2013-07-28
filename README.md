# PAS Application Maker

An easy to use framework for making powerful application definitions.

## Synopsis

```
pas-appmaker Appname --script --arguments --input-file --include-files --logging
```

## Setup

This section will explain how to properly setup App Maker on your system. By design, App Maker is flexible, and can be installed anywhere.
The sub-sections below will explain how App Maker requires the location of two unique directories in order to function properly.

### App Home

The App Home directory is where your application definitions are stored. This is where App Maker will place the application definitions you are authoring.
By default App Maker assumes "/var/spool/pas/repository/applications/". However, this is tunable using one of the two options below...

```
export PAS_APP_HOME=/var/spool/pas/repository/applications
```
```
pas-appmaker Appname --app-home /my/alternate/applications --ncpus --script --arguments --logging
```

### App Config

The App Config directory is where your App Maker template files are stored. The App Config templates allow you to fully customize how App Maker generates application definitions.
By default App Maker assumes "/var/spool/pas/conf/app-config/". However, this is tunable using one of the two options below...

```bash
export PAS_APP_CONFIG=/var/spool/pas/conf/app-config
```

or at runtime...

```
pas-appmaker Appname --app-config /my/alternate/app-config --ncpus --script --arguments --logging
```

## Tutorial: Some basic concepts

App Maker allows you to present options to users in a variety of ways. 
You can also pre-define options by setting them explicitly before the job us submitted.

### byForm

Examples of how to create applications where HTML form fields are how users prefer to request resources.

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

Examples of how to create applications where advanced users, more comfortable with the command-line, can select resources and attributes using the familiar select and attribute syntax of qsub.

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

Examples of how to create applications where resources and attributes are defined as PBS directives in a job script.

```
pas-appmaker byDirective1 --application --script --arguments --logging
```
```
pas-appmaker byDirective2 --environment-submit PAS_APPLICATION=Appname,PAS_SCRIPT=/path/to/app_name.sh --arguments --logging
```

## Tutorial: More advanced concepts

App Maker allows you to modify and extend its core functionality using hooks written in a language(s) you are comfortable with.

### Hook1

Example of executing a Perl hook before the job is submitted to PBS. 
This hook will set the PAS_SELECT_STATEMENT to the resources you specify.

```perl
#!/usr/bin/env perl

use strict;
use warnings;

my @resources = qw/select=1 ncpus=2 mem=1gb walltime=08:00:00/;

$ENV{'PAS_SELECT_STATEMENT'} = join ':', @resources;

exit(0);

```
```
pas-submit Hook1 --hook-submit /path/to/my/hook.pl --application --executable --arguments --logging
```

### Hook2

Example of executing a Python hook before the job starts. 
This hook will set the PAS_LOGGING option to true, and will also set a job executable with the PAS_EXECUTABLE option.

```python
#!/usr/bin/env python
#coding: utf-8

import os
import sys

os.environ['PAS_LOGGING'] = 'true'
os.environ['PAS_EXECUTABLE'] = '/path/to/job_exec.bin'

sys.exit(0)

```
```
pas-submit Hook2 --hook-start /path/to/my/hook.py --environment-submit PAS_SELECT=1 --ncpus --mem --input-file --include-files --arguments
```

## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.
