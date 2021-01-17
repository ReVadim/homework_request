import requests
import datetime
from pprint import pprint


def get_questions(tag: str, days: int):
    to_date = datetime.date.today()
    print(to_date)
    from_date = to_date - datetime.timedelta(days)
    print(from_date)
    url = "https://api.stackexchange.com/2.2/questions"
    params = {'tagged': tag,
              'site': 'stackoverflow',
              'fromdate': f'{from_date}',
              'todate': f'{to_date}'}
    response = requests.get(url, params=params)
    data = response.json()
    pprint(data)
    items = data['items']
    print(len(items))
    count = 0
    for item in items:
        print(item)
        count += 1
    return print(f'\n{count} questions with tag "python" for last {days} days')


get_questions('python', 1)
