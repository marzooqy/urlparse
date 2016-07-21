# urlparse
Parse urls using `urlparse.parse`
```
import urlparse
parts = urlparse.parse('https://github.com/marzooqy/urlparse?test=hello_world')
# {'params': '', 'path': '/marzooqy/foo', 'query': {'test': 'hello_world'}, 'scheme': 'https', 'netloc': 'github.com', 'fragment': ''}
```

Modify the dictionary as you like:
```
parts['path'] = '/marzooqy/urlparse'
del parts['query']['test']
```

And unparse the dictionary:
```
urlparse.unparse(parts)
# 'https://www.github.com/marzooqy/urlparse'
```
