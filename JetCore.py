# programming core with many features and utilities
# alpha-0.0.1v


def check_site(site):
    from colorama import Fore, init
    init()
    import requests
    s = requests.get(site)
    r = s.status_code
    if r == 200:
        print(Fore.GREEN + "Site is available!")
    else:
        print(Fore.RED + "Site is not available!")


def check_ping(ip):
    import os
    res = os.system("ping " + ip)
    print(res)


def thread(target, count):
    import threading
    for i in range(int(count)):
        th = threading.Thread(target=target)
        th.start()


def get_ip():
    import requests
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print('External IP address is: {}'.format(ip))

