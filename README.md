A thin wrapper for the `urllib.parse` standard library. Parses urls to mutable dictionaries instead of tuples.

###Example
Parse the url using `urlparse.parse`
```
import urlparse
parts = urlparse.parse('https://github.com/marzooqy/foo?test=hello_world')
# {'params': '', 'path': '/marzooqy/foo', 'query': {'test': 'hello_world'}, 'scheme': 'https', 'netloc': 'github.com', 'fragment': ''}
```

Modify the dictionary as you like:
```
parts['path'] = '/marzooqy/urlparse'
del parts['query']['test']
```

And unparse the dictionary using `urlparse.unparse`:
```
urlparse.unparse(parts)
# 'https://github.com/marzooqy/urlparse'
```
