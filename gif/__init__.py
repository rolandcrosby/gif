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

def giphy_translate(phrase):
   response = requests.get("http://api.giphy.com/v1/gifs/translate?api_key=dc6zaTOxFJmzC", params={"s": phrase}).json()
   return (response['meta']['status'], response['data'])

def main():
    parser = argparse.ArgumentParser(description="get a GIF from the Giphy API")
    parser.add_argument("--verbose", "-v", help="show Giphy URL with preview", action="store_true")
    parser.add_argument("subcommand", help="term to search Giphy for")
    parsed, args = parser.parse_known_args()
    args.insert(0, parsed.subcommand)
    status, body = giphy_translate(" ".join(args))
    if status == 200 and body != []:
        if parsed.verbose: print(body['url'])
        url = body['images']['downsized']['url']
        with tempfile.NamedTemporaryFile() as f:
            f.write(requests.get(url).content)
            subprocess.call(["qlmanage", "-c", "com.compuserve.gif", "-p", f.name], stdout=DEVNULL, stderr=DEVNULL)
