# programming core with many features and utilities
# alpha-0.0.6v


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
    print('External IP is: {}'.format(ip))


def str_byte(text):
    res = str.encode(text, encoding="utf-8")
    return res


def byte_str(text):
    res = bytes.decode(text, encoding="utf-8")
    return res


def platform():
    import platform
    name = platform.system()
    return name


def processor():
    import platform
    proc = platform.processor()
    return proc


def arch():
    import platform
    arc = platform.architecture()
    return arc


def py_ver():
    import platform
    py_version = platform.python_version()
    return py_version


def machine_info():
    import platform
    proc = platform.processor()
    OS = platform.system()
    arc = platform.architecture()
    py_version = platform.python_version()
    print("OS Name: " + OS)
    print("Processor: " + proc)
    print("Architecture: " + str(arc))
    print("Python version: " + py_version)


def check_ip(ip):
    import requests
    import json
    r = requests.get("http://ipwhois.app/json/" + ip).text
    ip = json.loads(r)
    resource = {ip["ip"],
                ip["success"],
                ip["type"],
                ip["country"],
                ip["continent"],
                ip["country_code"],
                ip["region"],
                ip["city"],
                ip["org"],
                ip["city"],
                ip["latitude"],
                ip["longitude"]}
    return resource


def check_server(ip, port):
    import socket
    s = socket.socket()
    address = ip
    port = int(port)
    try:
        s.connect((address, port))
    except Exception as e:
        print("Something's wrong with %s:%d. Exception is %s" % (address, port, e))
    finally:
        print("Server is available")
        s.close()
