import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input()  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    header = response.headers
    cookies = response.cookies
    printf(header)
    for cookie in cookies:
        print(cookie.name, cookie.value)
    more(html)
