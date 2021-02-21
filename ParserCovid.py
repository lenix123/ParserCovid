import requests
from bs4 import BeautifulSoup


class Covid:
    url = 'https://www.google.com/search?q=%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0+' \
          '%D0%BF%D0%BE+%D0%BA%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81%D1%83&oq=%D1%8' \
          '1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0+%D0%BF%D0%BE+%D0%BA%D0%BE%D1%80%D0%BE%' \
          'D0%BD%D0%BE&aqs=chrome.3.69i57j0i10j0i10i433l2j0i10.11372j0j1&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}

    def __init__(self):
        self.full_page = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.full_page.content, 'html.parser')

    def covid_globe(self):
        items = self.soup.find('div', class_='o6Yscf').find_all('td', {'jsname': 'VBiLTe'})
        info = []
        for item in items:
            info.append(item.find('span').get_text())
        print('Случаи заболевания: ' + info[0] + "; " + "Выздоровело: " + info[1] + "; " + "Умерло: " + info[2])

    def covid_country(self, name):
        name = name.strip()
        countries = self.soup.find('div', class_='iaUz9d').find_all('tr', {'class': 'viwUIc'})
        not_found = True
        for country in countries:
            if country.find('td', {'data-vfs': name}):
                info = []
                items = country.find_all('td')
                for item in items:
                    info.append(item.find('span').get_text())
                print('Страна: ' + info[0] + '; ' + 'Случаи заболевания ' + info[1] + '; '
                      + 'Выздоровело ' + info[2] + '; ' + 'Умерло ' + info[3])
                not_found = False
                break
        if not_found:
            print("No results for: " + name)

    def top_five_countries(self):
        countries = self.soup.find('div', class_='iaUz9d').find_all('tr', {'class': 'viwUIc'}, limit=6)
        for i in range(1, 6):
            print(i, countries[i].find('span').get_text())
