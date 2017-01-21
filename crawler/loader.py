#!/usr/local/bin/python3

from urllib.request import Request, urlopen

id_list = open(input("> ")[0:-1]).read()[0:-1].split(",")
link_list = ["https://www.wattpad.com/" + c_id for c_id in id_list]
for link in link_list:
	print(urlopen(Request(link, headers={'User-Agent': 'H4X0R/6.6.6'})).read())