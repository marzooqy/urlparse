import urllib.parse

def parse(url):
	parts = urllib.parse.urlparse(url)
	query = urllib.parse.parse_qs(parts[4])
	
	for name in query:
		query[name] = query[name][0]
		
	return {'scheme': parts[0], 'netloc': parts[1], 'path': parts[2], 'params': parts[3], 'query': query, 'fragment': parts[5]}

def unparse(parts):
	return urllib.parse.urlunparse((parts['scheme'], parts['netloc'], parts['path'], parts['params'], urllib.parse.urlencode(parts['query']), parts['fragment']))
