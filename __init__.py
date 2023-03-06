import os
import sys
from colorama import Fore as c
import fade
import requests
import pystyle


# Clear function
def clear():
    """Clears console screen."""
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


# Title function
def title(title=None):
    """Sets console title."""
    try:
        os.system(f'title NPC • {title}')
    except:
        os.system(f'title NPC')


# Color class
class color:
    """Console color codes."""
    green = c.GREEN
    red = c.RED
    blue = c.BLUE
    yellow = c.LIGHTYELLOW_EX
    reset = c.RESET


# Banner string
banner = """
╔╗╔╔═╗╔═╗
║║║╠═╝║      github/Pandaxyzzz
╝╚╝╩  ╚═╝
"""
banner = fade.purpleblue(banner)

# Console message codes
good = f"[{color.green}!{color.reset}]"
bad = f"[{color.red}*{color.reset}]"
alert = f"[{color.yellow}>{color.reset}]"


# Main function
def main():
    """Main function that checks proxies."""
    clear()
    title('Starting.')
    print(banner)

    proxylist = pystyle.Write.Input(
        "⌈  Paste proxy path  ⌋ : ",
        pystyle.Colors.blue_to_purple,
        interval=0.0035
    )

    clear()
    title('Checking')
    print(banner)

    hits = []
    url = 'http://www.google.com'
    hits_file = 'hits.txt'

    with open(proxylist, 'r') as file:
        proxies = file.readlines()

        for proxy in proxies:
            proxy = proxy.strip()

            if not proxy.startswith('http://'):
                proxy = f'http://{proxy}'

            try:
                response = requests.get(
                    url,
                    proxies={'http': proxy},
                    timeout=10
                )

                if response.status_code == 200:
                    global proxy_hit
                    print(f'{good} {proxy}')
                    hits.append(proxy)
                    proxy_hit = proxy.split('http://')
                    with open(hits_file, 'a') as f:
                        f.write(f'{proxy_hit[1]}\n')
            except:
                print(f'{bad} {proxy}')

    if hits:
        with open(hits_file, 'w') as file:
            for proxy in hits:
                file.write(proxy + '\n')

        print(f'{good} Total proxies: {len(hits)}')
    else:
        print(f'{bad} Total proxies: 0')


if __name__ == '__main__':
    main()
