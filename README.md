cpanel-deploy-new-relic-apps
============================

#Adding hook

To add the hook into cPanel, you should use the code below:

	/usr/local/cpanel/bin/manage_hooks add script /opt/makehtaccess/makefile.py --stage post --category Whostmgr --event Accounts::Create
	
In general what you do, is to add a script, to the post stage of the Whostmgr::Accounts::Create hook of cpanel, this will be run after the creation of a new account.

To take a small overview, of what the code does:

	#!/usr/bin/python
	import sys
	
	rawData = sys.stdin.readlines()
	
	hookdata = eval(rawData[0].replace(':null', ':None'))
	data = hookdata['data']
	username = data['user']
	domain = data['domain']
	
	f = open('/home/%s/.htaccess' % username, 'w')
	f.write('<IfModule mod_php5.c>\n')
	f.write('    php_value newrelic.appname "%s"\n' % domain)
	f.write('</IfModule>\n')
	f.close()
	
Above, you can see the code (located in makehtaccess folder).

When reading from stdin, you'll get a json string returned, due to the lack of json module in Python2.4 which is default on CentOS 5.x systems, we're using eval instead, and we do some replacement of ':null' to ':None'.

What we then, do is to create a file, in the users directory, and putting in the newrelic.appname.

###Are you running fcgi?
If you're running fcgi, using the php_values is not supported. The way to fix this, is using [htscanner Enhanced](https://github.com/piannelli/htscanner-enhanced) made by [Paolo Iannelli](http://www.paoloiannelli.com/).
