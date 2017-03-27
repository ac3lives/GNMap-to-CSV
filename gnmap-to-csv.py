#!/usr/bin/python
import re
import csv
import argparse

parser = argparse.ArgumentParser(description='Convert GNMap file to CSV by IP address | open ports')
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()

writer = csv.writer(open(args.outputfile, 'wb'), delimiter='\t') 
hostports = {}
for line in open(args.inputfile):
    hostname = ""
    try:
        hostname = re.findall(r'Host: (.+?)\(.+\)\tPorts:', line)[0]
    except: 
        pass
    portslist = re.findall(r'(\d*)/open/',line)
    ports = ', '.join(map(str, portslist))
    if hostname != "":
        outputlist = [hostname, ports]
        writer.writerow(outputlist)
        #print hostname + '\t' + ports

