from __config__ import (__BANNER__,
                        __ALERT__,
                        __BAD__,
                        __GOOD__)
from __functions__ import Utils

import requests
import pystyle

class Main(object):
    def __init__(self) -> None:
        self.Nano()
        proxylist = pystyle.Write.Input(  #type: ignore
            "⌈  Paste proxy path  ⌋ : ",
            pystyle.Colors.blue_to_purple,
            interval=0.0035
        )
        self.Nano()
        self.hits = []
        self.hits_file = 'hits.txt'
        for proxy in open(proxylist, "r").readlines():
            self.check(proxy)
        for proxy in self.hits:
            open(self.hits_file, 'a+').write(proxy + '\n')
        print(f'{__GOOD__} Total proxies: {len(self.hits)}')

    def Nano(self) -> None:
        Utils.clear()
        Utils.title('Starting.')
        print(__BANNER__)

    def check(self,
              proxy: str) -> None:
        url = 'http://www.google.com'
        proxy = proxy.strip()
        if not 'http://' in proxy:
            proxy = f'http://{proxy}'
        try:
            response = requests.get(
                url,
                proxies={'http': proxy},
                timeout=10
            )
            if response.status_code == 200:
                print(f'{__GOOD__} {proxy}')
                self.hits.append(proxy)
                proxy_hit = proxy.split('http://')
                open(self.hits_file, 'a+').write(f'{proxy_hit[1]}\n')
        except:
            print(f'{__BAD__} {proxy}')


if __name__ == '__main__':
    Main()
