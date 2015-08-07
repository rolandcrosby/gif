#!/usr/bin/env python

import requests
import argparse
import tempfile
import subprocess
try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


def main():
    parser = argparse.ArgumentParser(description="get a GIF from the Giphy API")
    parser.add_argument("subcommand", help="term to search Giphy for")
    args = parser.parse_args()
    r = requests.get("http://api.giphy.com/v1/gifs/translate?s={}&api_key=dc6zaTOxFJmzC".format(args.subcommand)).json()
    if r['meta']['status'] == 200 and r['data'] != []:
        url = r['data']['images']['downsized']['url']
        with tempfile.NamedTemporaryFile() as f:
            f.write(requests.get(url).content)
            subprocess.call(["qlmanage", "-c", "com.compuserve.gif", "-p", f.name], stdout=DEVNULL, stderr=DEVNULL)
            
if __name__ == "__main__":
    main()
