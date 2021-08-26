#!/usr/bin/python
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    4chan image downloader
    usage ./imgDownload threadurl directory
"""
import re
from sys import argv, stdout
#import os
import requests

count = 0 #count of images

if len(argv)<2:
    print( "Usage: ./spider4chan thread_url optional_destination_directory")
else:
    inurl = argv[1]
    directory=""
    if len(argv)>2:
        directory=argv[2]
    infile = requests.get(inurl).text.split(' ')
    images=[]
    for i in infile:
        imgs = re.findall('i[.]4cdn[.]org.*[.](?:(?:jpg)|(?:png)|(?:jpeg)|(?:gif)|(?:webm))', i)
        if imgs:
            for p in imgs:
                imgUrl=re.findall('\w+[.].*[.][a-z]{3}[^s]*[.](?:(?:jpg)|(?:png)|(?:jpeg)|(?:gif)|(?:webm))',p)
                if imgUrl:
                    images.append("http://"+imgUrl[0])

    stdout.write("Downloading images:\n")
    stdout.flush()
    for url in images:
        stdout.write("\r" + str(count))
        count+=1
        stdout.flush()
        picname=re.findall("[0-9a-zA-Z]+[.](?:(?:jpg)|(?:png)|(?:jpeg)|(?:gif)|(?:webm))", url)[0]
        image=requests.get(url)
        with open(directory+picname, 'wb') as f:
            f.write(image.content)
    stdout.write("\n")
