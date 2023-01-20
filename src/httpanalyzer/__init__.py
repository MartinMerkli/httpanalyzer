

class Request:

    def __init__(self, http_headers: dict, ip: str) -> None:
        """
        Class for analyzing http traffic from the http headers and the ip address.
        :param http_headers: dictionary of the http headers
        :param ip: the ip address (preferably IPv4, but IPv6 works as well)
        """
        self._http_headers = http_headers
        self._ip = ip

        self._malicious_rating = None
        self._bot_rating = None

