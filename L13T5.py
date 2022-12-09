from urllib.request import urlopen
import json

options = ['Exit', 'Get all dead characters', 'Get characters by their name and living status']
print('Welcome to Rick & Morty API')
while True:
    print('You have to following options')
    for i in range(len(options)):
        print(str(i)+')', options[i])
    selection = int(input('Enter your selection: '))
    print('\n', end='')
    tag = ['ID', 'name', 'type', 'species', 'origin', 'status']
    if selection == 1:
        url = 'https://rickandmortyapi.com/api/character/?status=dead'
        body = json.load(urlopen(url))
        max_pages = body['info']['pages']
        total = 0
        results = []
        limit_page = int(input('Enter limit of pages: '))
        print('\n', end='')
        if limit_page > max_pages:
            limit_page = max_pages
        for i in range(limit_page):
            body = json.load(urlopen(url))
            cnt = len(body['results'])
            print('Getting page', i + 1, 'url:', url)
            for j in range(cnt):
                results.append(body['results'][j])
            nextpage = body['info']['next']
            url = nextpage
            total += cnt
        for i in range(total):
            info = {'ID': str(results[i]['id']) + ' - ',
                    'name': str(results[i]['name']) + ' - ',
                    'type': str(results[i]['type']) + ' ',
                    'species': str(results[i]['species']) + ' - ',
                    'origin': str(results[i]['origin']['name']) + ' - ',
                    'status': str(results[i]['status']) + '\n'}
            for j in range(len(tag)):
                print(str(tag[j]) + ':' + info[tag[j]], end='')
        print('Total number of', total, 'dead characters')
    elif selection == 2:
        name = str(input('Enter character to search for: '))
        print('\n', end='')
        status = str(input('Enter living status (alive, dead, unknown): '))
        print('\n', end='')
        url = f'https://rickandmortyapi.com/api/character/?name={name}&status={status}'
        body = json.load(urlopen(url))
        max_pages = body['info']['pages']
        limit_page = int(input('Enter limit of pages: '))
        print('\n', end='')
        if limit_page > max_pages:
            limit_page = max_pages
        total = 0
        results = []
        if limit_page > max_pages:
            limit_page = max_pages
        for i in range(limit_page):
            body = json.load(urlopen(url))
            cnt = len(body['results'])
            print('Getting page', i + 1, 'url:', url)
            for j in range(cnt):
                results.append(body['results'][j])
            nextpage = body['info']['next']
            url = nextpage
            total += cnt
        for i in range(total):
            info = {'ID': str(results[i]['id']) + ' - ',
                    'name': str(results[i]['name']) + ' - ',
                    'type': str(results[i]['type']) + ' ',
                    'species': str(results[i]['species']) + ' - ',
                    'origin': str(results[i]['origin']['name']) + ' - ',
                    'status': str(results[i]['status']) + '\n'}
            for j in range(len(tag)):
                print(str(tag[j]) + ':' + info[tag[j]], end='')
        print('Total number of', total, status, name+'\'s', 'found')
    elif selection == 0:
        break
    # else:
    #     print('Wrong input!')
