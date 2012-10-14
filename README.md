cpanel-deploy-new-relic-apps
============================

#Adding hook

To add the hook into cPanel, you should use the code below:

	/usr/local/cpanel/bin/manage_hooks add script /opt/myapp/makefile.py --stage post --category Whostmgr --event Accounts::Create
	
In general what you do, is to add a script, to the post stage of the Whostmgr::Accounts::Create hook of cpanel, this will be run after the creation of a new account.
