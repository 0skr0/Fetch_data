from urllib.request import urlopen
import json

options = ['Exit', 'Get all dead characters', 'Get characters by their name and living status']
print('Welcome to Rick & Morty API')
while True:
    print('You have to following options')
    for i in range(len(options)):
        print(str(i)+')', options[i])
    selection = int(input('Enter your selection: '))
    tag = ['id', 'name', 'type', 'species', 'origin', 'status']
    if selection == 1:
        url = 'https://rickandmortyapi.com/api/character/?status=dead'
        body = json.load(urlopen(url))
        max_pages = body['info']['pages']
        total = 0
        results = []
        limit_page = int(input('Enter limit of pages: '))
        if limit_page > max_pages:
            limit_page = max_pages
        for i in range(limit_page):
            body = json.load(urlopen(url))
            cnt = len(body['results'])
            print('Getting page', i + 1, 'url:', url)
            for j in range(cnt):
                text = ''
                for k in range(len(tag)):
                    if k < len(tag) - 1:
                        if tag[k].__eq__('origin'):
                            text += (tag[k] + ':' + str(body['results'][j][tag[k]]['name']) + ' - ')
                        else:
                            text += (tag[k] + ':' + str(body['results'][j][tag[k]]) + ' - ')
                    else:
                        text += (tag[k] + ':' + str(body['results'][j][tag[k]]))
                results.append(text)
            nextpage = body['info']['next']
            url = nextpage
            total += cnt
        for i in results:
            print(i)
        print('Total number of', total, 'dead characters')
    elif selection == 2:
        name = str(input('Enter character to search for: '))
        status = str(input('Enter living status (alive, dead, unknown): '))
        url = f'https://rickandmortyapi.com/api/character/?name={name}&status={status}'
        body = json.load(urlopen(url))
        max_pages = body['info']['pages']
        limit_page = int(input('Enter limit of pages: '))
        if limit_page > max_pages:
            limit_page = max_pages
        total = 0
        results = []
        for i in range(limit_page):
            body = json.load(urlopen(url))
            cnt = len(body['results'])
            print('Getting page', i + 1, 'url:', url)
            for j in range(cnt):
                text = ''
                for k in range(len(tag)):
                    if k < len(tag) - 1:
                        if tag[k].__eq__('origin'):
                            text += (tag[k] + ':' + str(body['results'][j][tag[k]]['name']) + ' - ')
                        else:
                            text += (tag[k] + ':' + str(body['results'][j][tag[k]]) + ' - ')
                    else:
                        text += (tag[k] + ':' + str(body['results'][j][tag[k]]))
                results.append(text)
            nextpage = body['info']['next']
            url = nextpage
            total += cnt
        for i in results:
            print(i)
        print('Total number of', total, status, name+'\'s', 'found')
    elif selection == 0:
        break
    # else:
    #     print('Wrong input!')
