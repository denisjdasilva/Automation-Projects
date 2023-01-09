from netaddr import IPRange
from openpyxl import *

wb = load_workbook(filename = 'AG_inputFile.xlsx')
ws = wb['Sheet1']
IP = "10.30.1.1"

for row in ws:
    ip_cell = row[1]
    AG_cell = row[0]
    cell_string = str(ip_cell.value)
    RangeSet = cell_string.split(",")
    for IPset in RangeSet:
        try:
            if "-" in IPset:
                start_address = IPset.split("-")[0]
                end_address = IPset.split("-")[1]
                range = IPRange(f'{start_address}', f'{end_address}')
                if IP in range:
                    print(IP, AG_cell.value)
                else:   
                    continue
            else:
                if IP == IPset:
                    print(IP, AG_cell.value)
                else:
                    continue
        except:
            print("Error on " + str(ip_cell))