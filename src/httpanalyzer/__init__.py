

class Request:

    def __init__(self, http_headers: dict, ip: str, path: str, admin_pages: list = None) -> None:
        """
        Class for analyzing http traffic from the http headers and the ip address.
        :param http_headers: dictionary of the http headers
        :param ip: the ip address (preferably IPv4, but IPv6 works as well)
        :param path: the full path (beginning with /) the request tried to access
        :param admin_pages: all different admin tools you are using (see README.md for more information)
        """
        if admin_pages is None:
            admin_pages = []
        self._http_headers = http_headers
        self._ip = ip
        self._path = path
        self._admin_pages = admin_pages

        self._malicious_rating = None
        self._bot_rating = None
        self._search_rating = None

    def bot(self) -> float:
        """
        Get a rating on the possibility that this request was made by a bot.
        :return: float between 0.0 and 1.0 (NOT linear distribution)
        """
        from .src import BOTS_AGENT, BOTS_PATH
        yes = 0.0
        no = 1.0
        user_agent = self._http_headers.get('user_agent', '').lower()
        for element in BOTS_AGENT:
            if element in user_agent:
                yes += 10.0
        if self._path in BOTS_PATH:
            yes += 5.0
        self._bot_rating = yes / (yes + no)
        return self._bot_rating

    def search_engine(self) -> float:
        """
        Get a rating on the possibility that this request was made by a search engine.
        :return: float between 0.0 and 1.0 (NOT linear distribution)
        """
        from .src import SEARCH_ENGINE_AGENT, BOTS_PATH
        yes = 0.0
        no = 1.0
        user_agent = self._http_headers.get('user_agent', '').lower()
        for element in SEARCH_ENGINE_AGENT:
            if element in user_agent:
                yes += 10.0
        if self._path in BOTS_PATH:
            yes += 5.0
        self._search_rating = yes / (yes + no)
        return self._bot_rating

    def malicious(self) -> float:
        """
        Get a rating on the possibility that this request was made with malicious intends.
        :return: float between 0.0 and 1.0 (NOT linear distribution)
        """
        from .src import MALICIOUS_PATHS
        from .utils import url_decode
        yes = 0.0
        no = 1.0
        path = url_decode(self._path.lower())
        for element in MALICIOUS_PATHS:
            excluded = False
            for page in self._admin_pages:
                if page in element:
                    excluded = True
            if (element in path) and (not excluded):
                yes += 10.0
        self._malicious_rating = yes / (yes + no)
        return self._malicious_rating
