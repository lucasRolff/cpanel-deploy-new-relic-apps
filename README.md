cpanel-deploy-new-relic-apps
============================

#Adding hook

To add the hook into cPanel, you should use the code below:

	/usr/local/cpanel/bin/manage_hooks add script /opt/makehtaccess/makefile.py --stage post --category Whostmgr --event Accounts::Create
	
In general what you do, is to add a script, to the post stage of the Whostmgr::Accounts::Create hook of cpanel, this will be run after the creation of a new account.

To take a small overview, of what the code does:

```
#!/usr/bin/python
import sys, pwd, grp, os
import simplejson as json

rawData = sys.stdin.readlines()

hookdata = json.loads(rawData[0])

data = hookdata['data']
username = data['user']
domain = data['domain']
path = '/home/%s/.htaccess' % username

uid = pwd.getpwnam(username).pw_uid
gid = grp.getgrnam(username).gr_gid

file_content = """\
<IfModule mod_php5.c>
    php_value newrelic.appname "%s"
</IfModule>
""" % domain

with open(path, 'w') as f:
    f.write(file_content)

os.chown(path, uid, gid)
```
	
Above, you can see the code (located in makehtaccess folder).

The cPanel hook system will return a json string that we can read from stdin, so we use simplejson (It's included in the repository) to do this. After this we parse the json data, and assign some variables.

We then get the uid and gid from the user, since we need to make sure the file we create is owned by the user so it can delete or edit the file as needed.

We then write the `file_content` to the file stored in `path` and chown the file to the correct user.

###Are you running fcgi?
If you're running fcgi, using the php_values is not supported. The way to fix this, is using [htscanner Enhanced](https://github.com/piannelli/htscanner-enhanced) made by [Paolo Iannelli](http://www.paoloiannelli.com/).