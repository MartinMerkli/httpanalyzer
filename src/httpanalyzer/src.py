BOTS_AGENT = {
    'abuse.xmco.fr',  # company providing cyber-security monitoring
    'adidxbot',  # search engine
    'adsbot-google',  # search engine
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
    'https://github.com/imroc/req'  # client for go
    'internetmeasurement',  # automatic vulnerability disclosure
    'java/',  # java programming language
    'l9explore',  # pentesting tool
    'l9tcpid',  # tool for analyzing connections
    'libcurl',  # client for a variety of programming languages
    'libwww-perl',  # client for perl
    'masscan',  # web scraper
    'mediapartners-google',  # search engine
    'microsoftpreview',  # crawler
    'msnbot-media',  # search engine
    'netcraftsurveyagent',  # company providing cyber-security monitoring
    'netsystemsresearch',  # research project conducting cybersecurity studies
    'nmap',  # pentesting tool
    'node.js',  # javascript programming language
    'nvdorz',  # was trying to access the same sketchy url in regular intervals
    'pandalytics',  # company monitoring the internet
    'project-resonance',  # research project studying the security state of the internet
    'project_patchwatch'  # research project conducting network security studies
    'python',  # python programming language
    'report runner',  # suddenly changed user agent from node.js to this one
    'requests',  # client for python
    'scaninfo@paloaltonetworks.com',  # company searching for specific information
    'storebot-google',  # search engine
    'tchelebi',  # company providing cyber-security monitoring
    'urllib',  # client for python
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
    'msnbot-media',  # Bing
    'storebot-google',  # Google
}
BOTS_PATH = {
    '/robots.txt',
    '/sitemap.xml',
}
MALICIOUS_PATHS = {
    'etc/passwd',
    '/../',
    '/+cscoe+/',
    '/+cscou+/',
    '/+cscot+/',
    '/.env.',
    '/.config',
    '@java.lang.runtime@getruntime',
    '/.aws/',
    '/.ssh/id',
    'phpmyadmin',
    '<script>alert(document.domain)</script>',
    '?xdebug_session_start=phpstorm',
    '.oast.',
    'org.apache.tomcat.instancemanager',
    'onload=confirm',
    'utl_inaddr.get_host_name',
    'invokefunction&function=',
    'username=root&db=mysql',
    '${jndi:ldap://$',
    '\\win.ini',
    'admin',
    'acsserver',
    'cfide',
    'commpilot',
    'microstrategy',
    'sqlitemanager',
    'interact.sh',
    'actuator',
    'select(md5',
    'file:///etc/hosts',
    'field=updatexml',
    'audit/gui_detail_view.php',
    '/autodiscover/autodiscover.json?@',
    'wp-content',
    'boaform',
    'cgi-bin',
    'syscommand',
    'readycloud_control.cgi',
    'lang_modvalidate.php',
    'class.cs_phpmailer',
    'wp-includes',
    'wlwmanifest',
    'union+select+(select+concat',
    'compliancepolicyelements',
    '/config/',
    'oauth2login?error=',
    'javascript:alert',
    'microsoft.exchange.ediscovery.exporttool.application',
    'widget_tabbedcontainer_tab_panel',
    'trimprefix(base64_decode',
    'MethodAccessor.denyMethodExecution',
    'OgnlContext@DEFAULT_MEMBER_ACCESS',
    'org.apache.struts2.ServletActionContext',
    'java.io.InputStreamReader',
    'java.lang.ProcessBuilder',
    '${@die(md5',
    'shareBox&query=app=Common',
    'jre-6u13-windows-i586-p',
    'EJBInvokerServlet',
    'JMXInvokerServlet',
    'ajaxServerSettingsChk',
    'QueryComponentRendererValue',
    'MBeanServerDelegate',
    'java.lang:type=Memory',
    'profileIdx=web.item.graph',
    'libs/granite/ui',
    'foodbakery_radius',
    'String[]{\'sh\',\'-c\',\'id\'}',
    '<svg/onload=alert',
    'faces-redirect=true',
    'onmouseover=',
    'MPXnode/www/appConfig',
    'log_upload_wsgi.py',
    'NULL,NULL,NULL,NULL',
    'nmaplowercheck',
    'opensso/sessionservice',
    'nomgif=tarik',
    'syslog.rlog=',
    'DashboardLayoutOneCol',
    'createpage-entervariables.action',
    'core-r7rules',
    'src/Util/PHP/eval-stdin',
    'sms5/ajax.sms_emoticon',
    'mapname=poc.conf',
    'sum:sys.cpu.nice',
    'ActiveRecord::PendingMigrationError',
    'reset/IjEi.YhAmmQ.cdQp7CnnVq02aQ05y8tSBddl-qs',
    'cmdb/sslvpn_websession',
    '--exec=<divd',
    '_/;/WEB-INF',
    'jira-webapp-dist',
    'rm+-rf+/tmp/*;wget',
    'tmp;+wget+',
    'mirai.arm',
    'chmod+777',
    'BinName.arm',
    'rm+-rf+*;wget',
    'Mozi.a+jaws',
    'spring-mvc-showcase/resources',
    '.git/config',
    'W1siZyIsICJjb252ZXJ0IiwgIi1zaXplIDF4MSAtZGVwdGggOCBncmF5Oi9ldGMvcGFzc3dkIiwgIm91dCJdXQ',
    '(*),CONCAT(0x7e,md5(1)',
    'datagrid=179&json=',
    'clientlogin/?srid=&action=showdeny&url=',
    'path=x&site[x][text]',
    'wp-config',
    'wp-includes',
    '/xiao',
    'zimlet',
    'crlfinjection',
    '/~user/',
}
