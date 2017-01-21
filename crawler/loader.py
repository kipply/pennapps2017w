#!/usr/local/bin/python3

from urllib.request import Request, urlopen

id_list = open("ids.txt").read()[0:-1].split(",")
link_list = ["https://www.wattpad.com/" + c_id for c_id in id_list]

counter = 0
with open("teen-fic.txt", "w+") as output:
	for link in link_list:
		counter += 1
		print(str(counter) + "/" + str(len(link_list)))
		f.write(urlopen(Request(link, headers={'User-Agent': 'H4X0R/6.6.6'})).read())