BOTS_AGENT = {
    'abuse.xmco.fr',  # company providing cyber-security monitoring
    'adidxbot',  # search engine
    'adsbot-google',  # search engine
    'aiohttp',  # client for python
    'alexa site audit',  # crawler
    'apache-httpclient',  # client for java
    'apis-google',  # search engine
    'baiduspider',  # search engine
    'bingbot',  # search engine
    'bingpreview',  # search engine
    'bit.ly/3ezndno',  # company creating statistics about server software
    'censysinspect',  # company providing cyber-security monitoring
    'cfnetwork',  # client for swift
    'cyberwarcon',  # was trying to access the same uncommon url in regular intervals
    'domains project',  # project creating statistics about domain names
    'duckduckgo',  # search engine
    'expanse, a palo alto networks company',  # company searching for specific information
    'fasthttp',  # client for go
    'feedfetcher-google',  # search engine
    'fuzz faster u fool',  # automatic web fuzzer and pentesting tool
    'github.com/projectdiscovery/httpx',  # web scraper
    'go-http-client',  # client for go
    'google-read-aloud',  # search engine
    'google-site-verification',  # search engine
    'googlebot',  # search engine
    'guayoyo',  # was trying to access sketchy urls on websites
    'hello world',  # generic bot user agent
    'hello, momentum',  # generic bot user agent
    'hello, umad?',  # generic bot user agent
    'hello, world',  # generic bot user agent
    'http banner detection',  # research project conducting network security studies
    'https://csirt.divd.nl/',  # automatic vulnerability disclosure
    'https://developers.google.com/',  # search engine
    'https://gdnplus.com',  # crawler
    'https://github.com/imroc/req',  # client for go
    'internetmeasurement',  # automatic vulnerability disclosure
    'java/',  # java programming language
    'l9explore',  # pentesting tool
    'l9tcpid',  # tool for analyzing connections
    'libcurl',  # client for a variety of programming languages
    'libwww-perl',  # client for perl
    'masscan',  # web scraper
    'mediapartners-google',  # search engine
    'microsoftpreview',  # crawler
    'mj12bo',  # search engine
    'msnbot-media',  # search engine
    'netcraftsurveyagent',  # company providing cyber-security monitoring
    'netsystemsresearch',  # research project conducting cybersecurity studies
    'netwalk.ankweb',  # research project
    'nmap',  # pentesting tool
    'node.js',  # javascript programming language
    'nvdorz',  # was trying to access the same sketchy url in regular intervals
    'pandalytics',  # company monitoring the internet
    'project-resonance',  # research project studying the security state of the internet
    'project_patchwatch',  # research project conducting network security studies
    'python',  # python programming language
    'report runner',  # suddenly changed user agent from node.js to this one
    'requests',  # client for python
    'scaninfo@paloaltonetworks.com',  # company searching for specific information
    'security.ipip.net',  # research project conducting network security studies
    'semrush',  # crawler
    'storebot-google',  # search engine
    'tchelebi',  # company providing cyber-security monitoring
    'urllib',  # client for python
    'vcenter',  # was trying to access sketchy urls on websites
    'yandex',  # search engine
    'zgrab',  # pentesting tool
}
SEARCH_ENGINE_AGENT = {
    'adidxbot',  # Bing
    'adsbot-google',  # Google
    'apis-google',  # Google
    'baiduspider',  # Baidu
    'bingbot',  # Bing
    'bingpreview',  # Bing
    'duckduckgo',  # DuckDuckGo
    'feedfetcher-google',  # Google
    'google-read-aloud',  # Google
    'google-site-verification',  # Google
    'googlebot',  # Google
    'mediapartners-google',  # Google
    'microsoftpreview',  # Bing
    'mj12bo',  # Majestic
    'msnbot-media',  # Bing
    'storebot-google',  # Google
    'yandex',  # Yandex
}
BOTS_PATH = {
    '/robots.txt',
    '/sitemap.xml',
}
MALICIOUS_PATHS = {
    '${\'\'.class.forname(\'javax',
    '${@die(md5',
    '${jndi:ldap://$',
    '&_method=__construct&method=*&filter[]=',
    '(*),concat(0x7e,md5(1)',
    '--exec=<divd',
    '.git/config',
    '.git/head',
    '.github/workflows/',
    '.idea/httprequests',
    '.oast.',
    '.remote-sync.json',
    '.svn/entries',
    '.vscode/sftp.json',
    '.well-known/security.txt',
    '.well-known/security.txt',
    '/+cscoe+/',
    '/+cscot+/',
    '/+cscou+/',
    '/../',
    '/.aws/',
    '/.config',
    '/.env.',
    '/.ssh/id',
    '/autodiscover/autodiscover.json?@',
    '/config/',
    '/console',
    '/solr/',
    '/xiao',
    '/~user/',
    '2ioep23yxgkpwamwajv0rhiznfa',
    '3c625c27b4da33d3d5c12e8d02104755',
    '9568f36-d428-11d2-a769-00aa001acf42',
    '<script>alert(document.domain)</script>',
    '<svg/onload=alert',
    '?gid=1&page=2&rlist[]=@`%27`',
    '?xdebug_session_start=phpstorm',
    '@java.lang.runtime@getruntime',
    '@zdi/powershell',
    '\\win.ini',
    '_/;/web-inf',
    '__additional',
    '__clockwork/app',
    '_ignition/execute-solution',
    '_profiler/phpinfo',
    'aaaaaaaaaaaaaaaaaaaaaaaaaqr',
    'acsserver',
    'activerecord::pendingmigrationerror',
    'actuator',
    'adjuncts/3a890183',
    'admin',
    'ajax_url_encode.php?link_url=',
    'ajaxserversettingschk',
    'ansible.cfg',
    'api/tools/protocol/checkupdate',
    'app_dev.php/_profiler',
    'appstate&dumpconfig=',
    'appveyor.yml',
    'atmail/webmail/?format=',
    'audit/gui_detail_view.php',
    'bin/sqlnet.log',
    'binname.arm',
    'boaform',
    'call_user_func_array&vars[0]',
    'casa/nodes/thumbprints',
    'casa/nodes/thumbprints',
    'cfide',
    'cgi-bin',
    'checkscriptcompile?value=@grabconfig',
    'chkisg.htm?sip=1.1.1.1 | cat',
    'chmod+777',
    'class.cs_phpmailer',
    'clientlogin/?srid=&action=showdeny&url=',
    'cmd=nslookup',
    'cmdb/sslvpn_websession',
    'com.vmware.vsan.client',
    'commpilot',
    'compliancepolicyelements',
    'conn.php.bak',
    'controller?mode=8700&operation=1&datagrid=179',
    'core-cloud-config.yml',
    'core-r7rules',
    'cplugerror',
    'createpage-entervariables.action',
    'crlfinjection',
    'cubemail/filemanagement.php?action=dl&f=',
    'dashboardlayoutonecol',
    'datagrid=179&json=',
    'debug.seam',
    'docker-cloud.yml',
    'docker-compose',
    'dockerfile',
    'dockerrun.aws.json',
    'docs/cplugerror.html',
    'ecp/Current/exporttool/microsoft',
    'ejbinvokerservlet',
    'etc/local.xml',
    'etc/passwd',
    'extend/pearcmd',
    'faces-redirect=true',
    'fhem/filelog_logwrapper?dev=',
    'field=updatexml',
    'file:///etc/hosts',
    'foodbakery_radius',
    'forums/search/z-->"><',
    'ftpsync.settings',
    'gcloud/credentials.db',
    'google-api-private-key.json',
    'gponform/diag_form',
    'hnap1',
    'inicio.jsp',
    'inicio.pl',
    'interact.sh',
    'invokefunction&function=',
    'irj/go/km/navigation',
    'java.io.inputstreamreader',
    'java.lang.processbuilder',
    'java.lang:type=memory',
    'javascript:alert',
    'jira-webapp-dist',
    'jmxinvokerservlet',
    'jolokia/read/getdiagnosticoptions',
    'jre-6u13-windows-i586-p',
    'karma.conf.js',
    'ker_portal/c/version.js',
    'kustomization.yml',
    'kvmlm2/index.dhtml?fname=&language=',
    'lang_modvalidate.php',
    'libs/granite/offloading/content/view',
    'libs/granite/ui',
    'linusadmin-phpinfo',
    'loadframe?frame_name=x&src=x&single_signout=',
    'log_upload_wsgi.py',
    'magmi/web/ajax_pluginconf.php',
    'mailsms/s?func=a',
    'mapname=poc.conf',
    'mbeanserverdelegate',
    'methodaccessor.denymethodexecution',
    'microsoft.exchange.ediscovery.exporttool.application',
    'microstrategy',
    'mifs/.;/services',
    'mirai.arm',
    'mozi.a+jaws',
    'mpxnode/www/appconfig',
    'msmtprc',
    'nginx-status',
    'nmaplowercheck',
    'nomgif=tarik',
    'null,null,null,null',
    'oa_html/jtfwrepo.xml',
    'oauth2login?error=',
    'ognlcontext@default_member_access',
    'onload=confirm',
    'onmouseover=',
    'opensso/sessionservice',
    'option=com_joomlaupdater&controller=',
    'org.apache.struts2.servletactioncontext',
    'org.apache.tomcat.instancemanager',
    'org.jenkinsci.plugins.workflow.cps.cpsflowdefinition',
    'owa/auth/logon.aspx',
    'path=x&site[x][text]',
    'paytm_action=curltest&url=',
    'phpmyadmin',
    'plugins/advanced-dewplayer',
    'plus/ajax_officebuilding.php?act=key&key=',
    'pools/default/buckets',
    'portal/portal.mwsl',
    'portal0000.htm',
    'portal_inc.lua',
    'printenv.pl',
    'profileidx=web.item.graph',
    'putty.ppk',
    'pvc/v1/increase/1&post_ids=0',
    'querycomponentrenderervalue',
    'qvisdvr',
    'readycloud_control.cgi',
    'redis.conf',
    'remote/fgt_lang',
    'reset/ijei.yhammq.cdqp7cnnvq02aq05y8tsbddl-qs',
    'rest/applinks/1.',
    'rm+-rf+*;wget',
    'rm+-rf+/tmp/*;wget',
    'scripts/wpnbr.dll',
    'secret_token.rb',
    'seeyon/thirdpartycontroller.do',
    'select(md5',
    'sess-bin/login_handler.cgi',
    'settings.py',
    'sftp-config.json',
    'sharebox&query=app=common',
    'showlogin.cc',
    'sms5/ajax.sms_emoticon',
    'spring-mvc-showcase/resources',
    'sqlitemanager',
    'src/util/php/eval-stdin',
    'sslvpn_websession',
    'streaming/clients_live.php',
    'string[]{\'sh\',\'-c\',\'id\'}',
    'sum:sys.cpu.nice',
    'syscommand',
    'syslog.rlog=',
    'system/accountmanage/account',
    'telerik.web.ui.webresource.axd',
    'tmp;+wget+',
    'tmui/locallb/workspace',
    'trimprefix(base64_decode',
    'union+select+(select+concat',
    'user_secrets.yml',
    'username=root&db=mysql',
    'utl_inaddr.get_host_name',
    'vendor/phpunit',
    'ventrilo_srv.ini',
    'w1sizyisicjjb252zxj0iiwgii1zaxplidf4msatzgvwdgggocbncmf5oi9ldgmvcgfzc3dkiiwgim91dcjdxq',
    'web_vms/level15',
    'webfig',
    'wgetrc',
    'widget_tabbedcontainer_tab_panel',
    'wlwmanifest',
    'wp-config',
    'wp-content',
    'wp-includes',
    'wp-login',
    'xmldata?item=cpqkey',
    'zimlet',
    '嘍嘊set-',
}
