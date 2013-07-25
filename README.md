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

`pas-appmaker --app-home /my/private/applications Appname --ncpus --script --arguments --logging`

### App Config

Your App Config directory is where your App Maker template files are located. App Config allows you to fully customize how App Maker generates application definitions.
By default App Maker assumes "/var/spool/pas/conf/app-config/". However, this is tunable using one of the two options below...

`export PAS_APP_CONFIG=/var/spool/pas/conf/app-config`

or at runtime...

`pas-appmaker --app-config /my/private/app-config Appname --ncpus --script --arguments --logging`

## Examples

These basic examples bring focus to the three ways App Maker will allow submitting users to request job resources and attributes.

### byForm

This example is geared towards the modern Web/Mobile user who typically expects HTML form fields.

`pas-appmaker byForm --select --ncpus --mem --queue-list --application --executable --arguments`

### byStatement

This example is geared towards advanced users who typically declare resources using a select statement.

`pas-appmaker byStatement --select-statement --additional-attributes --application --executable --arguments`

### byDirective

This example is geared towards users who like to request resources and attributes using PBS directives in job scripts.

`pas-appmaker byDirective --application --script --arguments`

## App Maker Cookbook

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