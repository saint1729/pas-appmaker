# PAS Application Maker

A simple framework for creating powerful application definitions.

## Synopsis

```bash
pas-appmaker Appname --script --arguments --input-file --include-files --logging
```

## Setup

This section will explain how to properly setup App Maker on your system. By design, App Maker is flexible, and can be installed anywhere.
The sub-sections below will explain how App Maker requires the location of two unique directories in order to function properly.

### App Home

Your App Home directory is where your application definitions are stored. This is where App Maker will place the application definitions you are authoring.
By default App Maker assumes "/var/spool/pas/repository/applications/". However, this is tunable using one of the two options below...

```bash
export PAS_APP_HOME=/var/spool/pas/repository/applications
```

or at runtime...

```bash
pas-appmaker Appname --app-home /my/alternate/applications Appname --ncpus --script --arguments --logging
```

### App Config

Your App Config directory is where your App Maker template files are stored. The App Config templates allow you to fully customize how App Maker generates application definitions.
By default App Maker assumes "/var/spool/pas/conf/app-config/". However, this is tunable using one of the two options below...

```bash
export PAS_APP_CONFIG=/var/spool/pas/conf/app-config
```

or at runtime...

```bash
pas-appmaker Appname --app-config /my/alternate/app-config Appname --ncpus --script --arguments --logging
```

## Tutorial: Resources & Attributes

Users who submit jobs to HPC systems request resources for their jobs in different ways. Some using simple HTML form fields, and some using complex qsub select syntax. Other users may have been provided job scripts where PBS directives are embedded in the job script itself.  App Maker allows application authors the ability to describe resource options to users in a variety of different ways.

### byForm

Examples of how to create applications where HTML form fields are how users prefer to request resources.

```bash
pas-appmaker byForm --select --ncpus --mem --place --job-arrays --script --arguments --logging
```

```bash
pas-appmaker byForm --ncpus --mem --waltime --executable --environment --arguments --compress-results --logging
```

```bash
pas-appmaker byForm --evironment-submit PAS_SELECT=1,PAS_NCPUS=2,PAS_MEM=2gb --waltime --script --environment --arguments --compress-results --logging
```

### byStatement

This example is geared towards advanced users who typically declare resources using a select statement.

```bash
pas-appmaker byStatement --select-statement --additional-attributes --application --executable --arguments
```

```bash
pas-appmaker byStatement --select-statement --additional-attributes --application --executable --arguments
```

### byDirective

This example is geared towards users who like to request resources and attributes using PBS directives in job scripts.

`pas-appmaker byDirective --application --script --arguments`

## Tutorial: Executables & Job Scripts

The examples below demonstrate the various ways that App Maker supports defining the job executable or script.
You will also see how easy it is to pass arguments to the job executable or script, as well as pass environment variables to the job.

### GenericExec

This example assumes no default application name or executable. It will allow the submitting user to define both at submit time.

`pas-appmaker GenericExec --application --executable --arguments --environment --logging`

### GenericScript

This example assumes no defaults, much like GenericExec. However, this example allows the user to provide a job script instead of an executable path.

`pas-appmaker GenericScript --application --script --arguments --environment --logging`


## Tutorial: Variables & Stubstitution

App Maker allows you to set the value to user options in the background by explicitly setting environment variables. You can also use the "key" to an option in the value of a variable
and expect App Maker to substitute that "key" with its "value".

### Variables

In this example, you will see how easy it is to pre-define the value to App Maker options at runtime.

`pas-appmaker Variables --environment-submit PAS_SELECT=1,PAS_NCPUS=2,PAS_MEM=1gb --script --arguments`

### Substitution

In this example, you will see how you can substitute the key of an option with its value.

`pas-appmaker Substitution --ncpus --mem --executable --environment-start "PAS_ARGUMENTS=-procs PAS_NCPUS -mem PAS_MEM"`

## Tutorial: Hooks

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
