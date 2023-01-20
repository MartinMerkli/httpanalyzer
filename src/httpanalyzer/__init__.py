

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

