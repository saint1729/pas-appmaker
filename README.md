# PAS Application Maker

A simple framework for creating powerful application definitions.

## Example

`pas-appmaker Appname --executable --arguments --input-file --include-files --compress-results --logging`

## Setup

This section will explain how to properly setup App Maker on your system. By design, App Maker is flexible, and can be installed anywhere.
The sub-sections below desribe how App Maker requires the location of two unique directories in order to function properly.

### App Home

Your App Home directory is where your application definitions are located. This is where App Maker will place the applications you are working on.
By default App Maker assumes "/var/spool/pas/repository/applications/". However, this is tunable using one of the two options below...

`export PAS_APP_HOME=/var/spool/pas/repository/applications`

or at runtime...

`pas-appmaker --app-home /my/alternate/applications Appname --ncpus --script --arguments --logging`

### App Config

Your App Config directory is where your App Maker template files are located. App Config allows you to fully customize how App Maker generates application definitions.
By default App Maker assumes "/var/spool/pas/conf/app-config/". However, this is tunable using one of the two options below...

`export PAS_APP_CONFIG=/var/spool/pas/conf/app-config`

or at runtime...

`pas-appmaker --app-config /my/alternate/app-config Appname --ncpus --script --arguments --logging`


## Tutorial: Resources & Attributes

These basic examples bring focus to the three ways App Maker will allow submitting users to request job resources and attributes.
App Maker not only supports these very specific cases but any combination of these three cases as well.

### byForm

This example is geared towards the modern Web/Mobile user who typically expects HTML form fields.

`pas-appmaker byForm --select --ncpus --mem --queue --application --executable --arguments`

### byStatement

This example is geared towards advanced users who typically declare resources using a select statement.

`pas-appmaker byStatement --select-statement --additional-attributes --application --executable --arguments`

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


## Copyright

© Copyright 2013 Altair Engineering, Inc. All rights reserved.