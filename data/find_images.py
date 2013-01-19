
import json
from urllib2 import Request, urlopen
from urllib import urlencode

API_KEY = u"[FIXME]"
PRIVATE_URL = u'FIXME.apiary.io'

headers = {u"Accept": u"application/json"}

result = []

with open('film.json', 'r') as source:
  movies = json.load(source)

  for movie in movies:
    if not movie.get(u'name'): continue

    print u"%s" % movie.get(u'name')

    query = {
      u'query' : movie.get(u'name'),
      u'year' : movie.get(u'year'),
      u'api_key' : API_KEY,
      u'include_adult' : u'false',
      }

    request = Request(u"{url}/3/search/movie?{query}".format(url=PRIVATE_URL, query= urlencode(query)), headers=headers)

    print u'...querying the moviedb'

    response_body  = json.load( urlopen(request))


    matches = response_body.get(u"results")

    if matches:
      print u'...match found'

      tvdb_movie = matches[0]

      movie[u'thetvdb_id'] = tvdb_movie.get(u'id')
      movie[u'image'] = tvdb_movie.get(u'poster_path')
      result.append(movie)
    else:
      print u'...no match found'

print json.dumps(result, sort_keys=True,indent=2, separators=(u',', u': '))

