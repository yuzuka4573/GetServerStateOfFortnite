import time
import slackweb
import requests
from bs4 import BeautifulSoup

slack = slackweb.Slack(url="[ Your Slack webhook URLS ]")

url = "http://status.epicgames.com"
query_selector_map = {
    "Website and Forums": "body > div.layout-content.status.status-index.starter > div.container > div.components-section.font-regular > div.components-container.one-column > div > div.child-components-container > div:nth-of-type(1) > span.component-status",
    "Game Services": "body > div.layout-content.status.status-index.starter > div.container > div.components-section.font-regular > div.components-container.one-column > div > div.child-components-container > div:nth-of-type(2) > span.component-status",
    "Login Server": "body > div.layout-content.status.status-index.starter > div.container > div.components-section.font-regular > div.components-container.one-column > div > div.child-components-container > div:nth-of-type(3) > span.component-status",
    "MatchMaking": "body > div.layout-content.status.status-index.starter > div.container > div.components-section.font-regular > div.components-container.one-column > div > div.child-components-container > div:nth-of-type(6) > span.component-status"
}

prev = {
    'qqqq': 'aaaa',
    'dddd': 'iiii',
    'wwww': 'uuuu',
    'gggg': 'eeee'
}


def get_soup():
    instance = requests.get(url)
    return BeautifulSoup(instance.text, 'lxml')


while True:
    soup = get_soup()

    now = {}
    for title, qs in query_selector_map.items():
        now[title] = soup.select_one(qs).text.strip()

    if not now == prev:
        text = '\n'.join(f'{title}: {status}' for title, status in now.items())
        slack.notify(text=text)
        r = requests.post(dis_url, data=text)

    prev = now

    time.sleep(300)
