import requests
session = requests.Session()
user_id = 47957507
url = f'http://www.kinopoisk.ru/user/{user_id}'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
      }
cookies = {
    'Cookie': 'spravka=dD0xNjQ1NjIyMDg5O2k9MTA5LjI1Mi4xNzEuNjc7RD0yOTc2RTFFOUU0RDYwNjk3RDMwRDgwN0YxNEU3REU0MTExMjY2RDI5RkI4NjM1MzQzQzhCMTVERTYwQTFBMTAyNDU1M0ZDNEI7dT0xNjQ1NjIyMDg5OTAzNjU2MzYwO2g9OGJjYjcxYWRhOGE1NmUzMTdjZWE5YTA4ZmMyY2ZhN2Q=; i=KPLjjf0GwWVkxP23bMZ0gUELwFIraPhZt28DDyf0UqZsTS+3wzAj8ptwlp+JiA3hU0xuzX7xNuhlVAb2yUH/smbxuJw=; gdpr=0; _ym_uid=1645622067527761605; _ym_d=1645623954; _ym_visorc=w; _ym_isad=2; PHPSESSID=fc982502503cbf0166285c1435d12ad0; user_country=ru; yandex_gid=213; tc=1; my_perpages=%5B%5D; _csrf_…d8c413038ca83fc2c6daa1ea154b2e3178e42a6ebef508718b1841fffbcd1138d5a7c5feaac188b0aa01665d2b17cf06c7a2b5b5a627468c3b1a6ac69efc684043d8b2b1211b5c472a665a2e69c3a5f3a88de39cce; desktop_session_key.sig=yMZXtmTgUmaMeY4x8Keambr_g0k; mda_exp_enabled=1; ya_sess_id=noauth:1645622098; yandex_login=; ys=c_chck.3996376431; yandexuid=6545840251636882289; mda2_beacon=1645622098337; sso_status=sso.passport.yandex.ru:synchronized_no_beacon; cycada=Eauk/shLMxJZjbXI38vQHuugtN0YvMU+4E/0ptW9QPs=; yandex_plus_metrika_cookie=true'
}
# s = session.get(url + '/cookies', cookies=cookies)
# print(s.text)
r = requests.get(url, headers=headers)
print(r.text)