from pygooglenews import GoogleNews

gn = GoogleNews(country='ES')

search = gn.search('CIAGC')

for new in search["entries"]:
    print(new["published"])

