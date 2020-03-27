#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from io import StringIO
import csv, json

data = urlopen("https://raw.githubusercontent.com/Unanimad/hummingbird_brazil_covid19/master/data/brazil_covid19.csv").read().decode('ascii', 'ignore')
datafile = StringIO(data)
cvsReader = csv.reader(datafile)

for row in cvsReader:
    print(row[1], row[2], row[3])