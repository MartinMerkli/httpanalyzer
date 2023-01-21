

class Request:

    def __init__(self, http_headers: dict, ip: str, path: str, admin_page: list = None) -> None:
        """
        Class for analyzing http traffic from the http headers and the ip address.
        :param http_headers: dictionary of the http headers
        :param ip: the ip address (preferably IPv4, but IPv6 works as well)
        :param path: the full path (beginning with /) the request tried to access
        :param admin_page: all different admin tools you are using (see README.md for more information)
        """
        if admin_page is None:
            admin_page = []
        self._http_headers = http_headers
        self._ip = ip
        self._path = path
        self._admin_page = admin_page

        self._malicious_rating = None
        self._bot_rating = None

    def bot(self) -> float:
        yes = 0.0
        no = 1.0
        user_agent = self._http_headers.get('user_agent', '').lower()
        ua_blacklist = {
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
        for element in ua_blacklist:
            if element in user_agent:
                yes += 10.0
        return yes / (yes + no)
