import csv,json, re

key_mapping = {
  'name' : 'name',
  'initial_release_date' : 'year',
  'directed_by' : 'director',
  'tagline': 'tagline',
}

result = []

with open('film.freebase.tsv', 'r') as source:
  reader = csv.DictReader(source, delimiter='\t')

  for row in reader:
    print 'working'
    movie = {}
    for key in key_mapping:
      data = None
      if key == 'initial_release_date':
        raw_date =  row.get(key)
        match_year = re.search(r'(\d{4})',row.get(key))
        data = match_year.group(1) if match_year else raw_date
      else:
        data = row.get(key)

      try:
        data = data.decode('ascii')
        movie[key_mapping[key]] = data
      except UnicodeDecodeError:
        continue

    result.append(movie)

with open('film.all.json', 'w') as destination:
  json.dump(result, destination)

print "done!"