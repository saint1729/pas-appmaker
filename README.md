# PAS Application Maker

An easy to use framework for creating powerful application definitions.

## Synopsis

```bash
pas-appmaker Appname --script --arguments --input-file --include-files --logging
```

## Setup

This section will explain how to properly setup App Maker on your system. By design, App Maker is flexible, and can be installed anywhere.
The sub-sections below will explain how App Maker requires the location of two unique directories in order to function properly.

### App Home

The App Home directory is where your application definitions are stored. This is where App Maker will place the application definitions you are authoring.
By default App Maker assumes "/var/spool/pas/repository/applications/". However, this is tunable using one of the two options below...

```bash
export PAS_APP_HOME=/var/spool/pas/repository/applications
```

or at runtime...

```bash
pas-appmaker Appname --app-home /my/alternate/applications --ncpus --script --arguments --logging
```

### App Config

The App Config directory is where your App Maker template files are stored. The App Config templates allow you to fully customize how App Maker generates application definitions.
By default App Maker assumes "/var/spool/pas/conf/app-config/". However, this is tunable using one of the two options below...

```bash
export PAS_APP_CONFIG=/var/spool/pas/conf/app-config
```

or at runtime...

```bash
pas-appmaker Appname --app-config /my/alternate/app-config --ncpus --script --arguments --logging
```

## Tutorial: Basic Concepts

App Maker allows you the ability to present options to users in a variety of ways. 
You can also pre-define options by setting them in the submit envirionment.

### byForm

Examples of how to create applications where HTML form fields are how users prefer to request resources.

```bash
pas-appmaker byForm1 --select --ncpus --mem --place --application --executable --arguments --logging
```
```bash
pas-appmaker byForm2 --environment-submit PAS_SELECT=1 --ncpus --mem --application --script --input-file --include-files --logging
```
```bash
pas-appmaker byForm3 --environment-submit PAS_NCPUS=16,PAS_MEM=8gb,PAS_PLACE=pack --select --script --arguments --logging
```

### byStatement

Examples of how to create applications where advanced users, more comfortable with the command-line, can select resources and attributes using the familiar select and attribute syntax of qsub.

```bash
pas-appmaker byStatement1 --select-statement --additional-attributes --application --executable --arguments --logging
```
```bash
pas-appmaker byStatement2 --environment-submit PAS_SELECT_STATEMENT=PAS_SELECT_STATEMENT:walltime=10:10:00 --select-statement --executable --arguments --logging
```

### byDirective

Examples of how to create applications where resources and attributes are defined as PBS directives in a job script.

```bash
pas-appmaker byDirective1 --application --script --arguments --logging
```
```bash
pas-appmaker byDirective2 --environment-submit PAS_APPLICATION=Appname,PAS_SCRIPT=/path/to/job_script.sh --arguments --logging
```

## Tutorial: Advanced Concepts

These examples demonstrate how application authors can execute scripts at various phases of the application lifecycle.

### SubmitHook

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

`pas-submit SubmitHook --hook-submit /path/to/my/hook.script --ncpus --mem --logging`

### StartHook

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

`pas-submit StartHook --hook-start /path/to/my/hook.script --application --executable --ncpus --mem --logging`

### FinishedHook

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

`pas-submit FinishedHook --hook-finished /path/to/my/hook.script --select-statement --script --arguments`

## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.
