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
