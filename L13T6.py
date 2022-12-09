from urllib.request import urlopen
import json

url_launches = 'https://api.spacexdata.com/v5/launches/'
body = json.load(urlopen(url_launches))

launches_success = []
for i in range(len(body)):
    if len(body[i]['crew']) != 0:
        if body[i]['success']:
            launches_success.append(body[i])

print('Welcome to Space X manned missions explorer')
search = 0
while True:
    try:
        search = int(input('Please, give the year to search for: '))
        print('\n', end='')
        break
    except:
        print('Faulty input, please try again.')

while True:
    print('Launch information descriptor')
    launches_search = []
    for i in range(len(launches_success)):
        years = str(launches_success[i]['date_utc']).split('-')
        if int(years[0]) == search:
            launches_search.append(launches_success[i])
    print('We have', len(launches_search), 'launch to choose from.')
    for i in range(len(launches_search) + 1):
        if i < 1:
            print(str(i - 1) + ')', 'Exit')
        else:
            print(str(i - 1) + ')', launches_search[i - 1]['date_utc'], '-', launches_search[i - 1]['name'])
    selection = int(input('Select launch to display more information: '))
    tag = ['Name', 'Flight Number', 'Date', 'Mission', 'Mission status', 'Launch Wikipedia article']
    print('\n', end='')
    if selection != -1:
        print('------------------')
        print('')
        detail = launches_search[selection]['details']
        if detail is None:
            detail = 'Missing'
        info = {'Name': launches_search[selection]['name'],
                'Flight Number': launches_search[selection]['flight_number'],
                'Date': launches_search[selection]['date_utc'],
                'Mission': detail,
                'Mission status': 'Successful',
                'Launch Wikipedia article': launches_search[selection]['links']['wikipedia']}
        for i in range(len(tag)):
            print(str(tag[i]) + ':', info[tag[i]])
        crews = launches_search[selection]['crew']
        print('The launch had a crew of', len(crews))
        print('')
        print('::CREW MEMBERS::')
        for i in range(len(crews)):
            url_crews = f'https://api.spacexdata.com/v4/crew/{crews[i]["crew"]}'
            body = json.load(urlopen(url_crews))
            print('  Crew member', i+1)
            print(' ', crews[i]['role'], body['name'])
            print('  Agency:'+body['agency'])
            print('  Wikipedia page:', body['wikipedia'])
            print('')
    else:
        break
