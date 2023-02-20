import os,sys,fade,requests,pystyle;from colorama import Fore as c

#   ⌈ 𝗖𝗹𝗲𝗮𝗿  ⌋ 
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


#   ⌈ 𝗧𝗶𝘁𝗹𝗲  ⌋ 
def title(title=None):
    try:
        os.system(f'title NPC • {title}')
    except:
        os.system(f'title NPC')
title('github/Pandaxyzzz')

#    ⌈ 𝗖𝗼𝗹𝗼𝗿𝘀  ⌋
class color:
    green = c.GREEN
    red = c.RED
    blue = c.BLUE
    yellow = c.LIGHTYELLOW_EX
    reset = c.RESET


#    ⌈ 𝗕𝗮𝗻𝗻𝗲𝗿  ⌋ 
banner = """
╔╗╔╔═╗╔═╗
║║║╠═╝║      github/Pandaxyzzz
╝╚╝╩  ╚═╝
"""
banner = fade.purpleblue(banner)
good = f"[{color.green}!{color.reset}]"
bad = f"[{color.red}*{color.reset}]"
alert = f"[{color.yellow}>{color.reset}]"

#    ⌈ 𝗣𝗮𝘁𝗵𝘀  ⌋ 
clear()
title('Starting.')
print(banner)
proxylist = pystyle.Write.Input("⌈  Paste proxy path  ⌋ : ", pystyle.Colors.blue_to_purple, interval=0.0035)
clear()
title('Checking')
print(banner)

hits = []
url = 'http://www.google.com'
hits_file = f'hits.txt'
with open(proxylist, 'r') as file:
    proxies = file.readlines()

    for proxy in proxies:
        proxy = proxy.strip()

        if not proxy.startswith('http://'):
            proxy = f'http://{proxy}'

        try:
            response = requests.get(url, proxies={'http': proxy}, timeout=10)

            if response.status_code == 200:
                global proxy_hit
                print(f'{good} {proxy}')
                hits.append(proxy)
                proxy_hit = proxy.split('http://')
                f = open('hits.txt', 'w')
                f.write(f'{proxy_hit[1]}\n')
                f.close()
        except:
            print(f'{bad} {proxy}')

if hits:
    with open(hits_file, 'w') as file:
        for proxy in hits:
            file.write(proxy + '\n')
            
    print(f'{good} Total proxies: {len(hits)}')
else:
    print(f'{bad} Total proxies: 0')