from netaddr import IPRange
from datetime import datetime, date
import os

currenttime = datetime.now()
timestr = currenttime.strftime("%H%M%S")
Current_Directory = os.getcwd()

outfile = open(Current_Directory+"/Results/results" + "_" + str(date.today()) + "_" + str(timestr) + ".txt" , 'w')

with open('inputFile.txt') as inputfile:

    for line in inputfile:
        line = str(line.strip("\n"))
        set = line.split(",")
        for ips in set:
            if "-" in ips:
                start_address = ips.split("-")[0]
                end_address = ips.split("-")[1]
                Range = IPRange(f'{start_address}', f'{end_address}')
                for ip in Range:
                    ip = str(ip)
                    outfile.write(ip)
                    outfile.write('\n')


            else:
                    ip = str(ips)
                    outfile.write(ip)
                    outfile.write('\n')

print("----------------------------")
print("You are DONE SIR!!! ( ͡° ͜ʖ ͡°)")
print("----------------------------")

outfile.close()