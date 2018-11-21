# read write file for the exceptions script
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
import sys
import os

exceptionz = ['callback', 'troubleshooting', 'follow up', 'meeting', 'break', 'special project', 'training']
row = 0

def create_client(url):
    print '[+] Loading...'
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cfa-exceptions-a4f72a8677f2.json', scope)
    client = gspread.authorize(creds)
    #headers = gspread.httpsession.HTTPSession(headers={'Connection': 'Keep-Alive'})
    client = gspread.Client(auth=creds)
    client.login()
    sheet = client.open_by_url(url)   
    return sheet

def get_inputs():
    start_time = raw_input('start time: ') #sys.argv[1] to get input from cmd line
    
    if start_time == 'upload':
        exception_code = int(0)
        inc_num = 'null'
        date = 'null'
        full_time = 'null'
        return exception_code, inc_num, date, full_time, start_time

    else:
        exception_code = int(raw_input('Exception Code (0=callback, 1=troubleshooting, 2=follow up, 3=meeting, 4=break, 5=special project, 6=training): '))#int(sys.argv[2])
        inc_num = raw_input('inc number: ')#sys.argv[3] input from cmd
        date =  datetime.date.today().strftime('%m/%d/%Y')
        end_time =  time.strftime('%I:%M:%S')
        full_time = '{0} - {1}'.format(start_time, end_time)
        return exception_code, inc_num, date, full_time, start_time

def next_available_row():
    #str_list = filter(None, worksheet.col_values(1))  # fastest
    global row
    if row == 0:
        row = int(raw_input('Where should I start? >  '))
        row_number = row
    else:
        row += 1
        row_number = row

    #return str(len(str_list)+1)
    return str(row_number)

def get_in_that_cell(client, date, full_time, exception_code, inc_num):
    next_row = next_available_row()
    print '{0}'.format(next_row) 
    client.update_acell("A{}".format(next_row), str(date)) # get date
    client.update_acell("B{}".format(next_row), str(full_time)) # get time
    client.update_acell("C{}".format(next_row), str(exceptionz[exception_code])) # get exception by code (0,1,or2)
    client.update_acell("D{}".format(next_row), str(inc_num)) # get inc number'''
    

def write_and_read(client, exception_code, inc_num, date, full_time, start_time):
    with open("UploadFile.txt", 'r') as _read_file:
         with open("UploadFile.txt", 'a') as _write_file:
             if start_time != 'upload':
                 _write_file.write('{0},{1},{2},{3},\n'.format(date, full_time, exception_code, inc_num))
             else:
                 #upload to google
                for line in _read_file:
                    currentline = line.split(',')
                    try:
                        _date, _full_time, _exception_code, _inc_num = currentline[0], currentline[1], int(currentline[2]), currentline[3]
                        get_in_that_cell(client, _date, _full_time, _exception_code, _inc_num)
                        time.sleep(4)
                        continue
                    except Exception as e:
                        print  e
                        continue