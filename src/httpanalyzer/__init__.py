

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

    def bot(self) -> float:
        from .src import BOTS_AGENT
        yes = 0.0
        no = 1.0
        user_agent = self._http_headers.get('user_agent', '').lower()
        for element in BOTS_AGENT:
            if element in user_agent:
                yes += 10.0
        return yes / (yes + no)
