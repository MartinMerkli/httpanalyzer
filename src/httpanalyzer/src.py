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
    'expanse, a palo alto networks company',  # company searching for specific information
    'fasthttp',  # client for go
    'feedfetcher-google',  # search engine
    'fuzz faster u fool',  # automatic web fuzzer and pentesting tool
    'github.com/projectdiscovery/httpx',  # web scraper
    'go-http-client',  # client for go
    'google-read-aloud',  # search engine
    'google-site-verification',  # search engine
    'googlebot',  # search engine
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
    '${@die(md5',
    '${jndi:ldap://$',
    '(*),CONCAT(0x7e,md5(1)',
    '--exec=<divd',
    '.git/config',
    '.git/head',
    '.github/workflows/',
    '.oast.',
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
    '/solr/',
    '/xiao',
    '/~user/',
    '2ioep23yxgkpwamwajv0rhiznfa',
    '9568f36-d428-11d2-a769-00aa001acf42',
    '<script>alert(document.domain)</script>',
    '<svg/onload=alert',
    '?xdebug_session_start=phpstorm',
    '@java.lang.runtime@getruntime',
    '@zdi/powershell',
    'ActiveRecord::PendingMigrationError',
    'BinName.arm',
    'DashboardLayoutOneCol',
    'EJBInvokerServlet',
    'JMXInvokerServlet',
    'MBeanServerDelegate',
    'MPXnode/www/appConfig',
    'MethodAccessor.denyMethodExecution',
    'Mozi.a+jaws',
    'NULL,NULL,NULL,NULL',
    'OgnlContext@DEFAULT_MEMBER_ACCESS',
    'QueryComponentRendererValue',
    'String[]{\'sh\',\'-c\',\'id\'}',
    'W1siZyIsICJjb252ZXJ0IiwgIi1zaXplIDF4MSAtZGVwdGggOCBncmF5Oi9ldGMvcGFzc3dkIiwgIm91dCJdXQ',
    '\\win.ini',
    '_/;/WEB-INF',
    '__additional',
    '__clockwork/app',
    '_ignition/execute-solution',
    '_profiler/phpinfo',
    'aaaaaaaaaaaaaaaaaaaaaaaaaqr',
    'acsserver',
    'actuator',
    'admin',
    'ajaxServerSettingsChk',
    'ansible.cfg',
    'app_dev.php/_profiler',
    'appstate&dumpconfig=',
    'appveyor.yml',
    'audit/gui_detail_view.php',
    'bin/sqlnet.log',
    'boaform',
    'call_user_func_array&vars[0]',
    'casa/nodes/thumbprints',
    'cfide',
    'cgi-bin',
    'chmod+777',
    'class.cs_phpmailer',
    'clientlogin/?srid=&action=showdeny&url=',
    'cmd=nslookup',
    'cmdb/sslvpn_websession',
    'commpilot',
    'compliancepolicyelements',
    'core-cloud-config.yml',
    'core-r7rules',
    'cplugerror',
    'createpage-entervariables.action',
    'crlfinjection',
    'datagrid=179&json=',
    'debug.seam',
    'docker-cloud.yml',
    'dockerfile',
    'dockerrun.aws.json',
    'etc/passwd',
    'extend/pearcmd',
    'faces-redirect=true',
    'field=updatexml',
    'file:///etc/hosts',
    'foodbakery_radius',
    'ftpsync.settings',
    'google-api-private-key.json',
    'hnap1',
    'inicio.jsp',
    'inicio.pl',
    'interact.sh',
    'invokefunction&function=',
    'java.io.InputStreamReader',
    'java.lang.ProcessBuilder',
    'java.lang:type=Memory',
    'javascript:alert',
    'jira-webapp-dist',
    'jre-6u13-windows-i586-p',
    'karma.conf.js',
    'kustomization.yml',
    'lang_modvalidate.php',
    'libs/granite/ui',
    'linusadmin-phpinfo',
    'log_upload_wsgi.py',
    'mailsms/s?func=a',
    'mapname=poc.conf',
    'microsoft.exchange.ediscovery.exporttool.application',
    'microstrategy',
    'mirai.arm',
    'nginx-status',
    'nmaplowercheck',
    'nomgif=tarik',
    'oa_html/jtfwrepo.xml',
    'oauth2login?error=',
    'onload=confirm',
    'onmouseover=',
    'opensso/sessionservice',
    'org.apache.struts2.ServletActionContext',
    'org.apache.tomcat.instancemanager',
    'owa/auth/logon.aspx',
    'path=x&site[x][text]',
    'phpmyadmin',
    'pools/default/buckets',
    'portal_inc.lua',
    'profileIdx=web.item.graph',
    'readycloud_control.cgi',
    'remote/fgt_lang',
    'reset/IjEi.YhAmmQ.cdQp7CnnVq02aQ05y8tSBddl-qs',
    'rest/applinks/1.',
    'rm+-rf+*;wget',
    'rm+-rf+/tmp/*;wget',
    'scripts/wpnbr.dll',
    'select(md5',
    'settings.py',
    'sftp-config.json',
    'shareBox&query=app=Common',
    'showlogin.cc',
    'sms5/ajax.sms_emoticon',
    'spring-mvc-showcase/resources',
    'sqlitemanager',
    'src/Util/PHP/eval-stdin',
    'sslvpn_websession',
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
    'webfig',
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
