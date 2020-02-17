import feedparser
import requests
import os
import sys
import gzip

def get(author):
    # Request arxiv api
    url = 'http://export.arxiv.org/api/query?search_query=au:{}'.format(author)
    feed = feedparser.parse(url)
    start_url = 'https://arxiv.org/e-print/'
    
    # Save urls and names
    urls = []
    names = []
    for i in range(len(feed.entries)):
        entry = feed.entries[i]
        ids = entry['id']
        names.append(entry['title'])
        if 'math' in ids:
            end_url = ids.split('/')[-2:]
            urls.append(f'{start_url}{end_url[0]}/{end_url[1]}')
        else:
            end_url = ids.split('/')[-1]
            urls.append(f'{start_url}{end_url}')


    # Make folder to save that shit
    try:
        os.makedirs(author)
    except:
        pass

    # Save those files
    for i in range(len(urls)):
        myfile = requests.get(urls[i], allow_redirects=True)
        try:
            # arxiv saves encodes it .tex files as gzips.
            contents = gzip.decompress(myfile.content)
            open('{}/{}.{}'.format(
                author,
                names[i],
                'tex'), 'wb').write(contents)
        except:
            pass

    print('Done')
