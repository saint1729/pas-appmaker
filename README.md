# PAS Application Maker

Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sollicitudin felis id lobortis dictum. Nullam elementum rhoncus nisl ac faucibus.

## Synopsis

`pas-appmake Appname --ncpus --mem --script --arguments --input-file --compress-results --logging`

## Setup

Typically you add the COMMAND\_HOME variable to your pbsworks.conf file.
This variable must be set to the full path to your /pbsa-commands/ directory.

### App Home

Your App Home directory is where your application definitions reside. This is where App Maker will place your newly created application definitions.
By default App Maker assumes `/var/spool/pas/repository/applications/`. However, this is tunable using one of the two options below...

`export PAS_APP_HOME=/var/spool/pas/repository/applications`

or

`pas-appmaker --app-home /my/private/applications Appname --ncpus --script --arguments --logging`

### App Config

Your App Config directory is where your application definition template files are located. These files allow you to fully customize how App Maker generates your application definitions.
By default App Maker assumes `/var/spool/pas/conf/app-config/`. However, this is tunable using one of the two options below...

`export PAS_APP_CONFIG=/var/spool/pas/conf/app-config`

or

`pas-appmaker --app-config /my/private/app-config Appname --ncpus --script --arguments --logging`

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