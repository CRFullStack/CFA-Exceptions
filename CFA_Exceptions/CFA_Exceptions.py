from oauth2client.service_account import ServiceAccountCredentials
from CFA_Exceptions_RW import *
import gspread
import datetime
import time
import sys
import os

#----------------------------------Make instance---------------------------------
#create_client('https://docs.google.com/spreadsheets/d/1kmoJVYan14-XL5XIjxM1T9WsMfcbCO9z0_RZSnRB2mE/edit?usp=sharing').worksheet('C. Hobdy')
#monet_link = https://docs.google.com/spreadsheets/d/14hBiTS_pUEWdjT3JOq8OxtmhoQnhq4HSEPa6brEPFXA/edit?usp=sharing
client_url = raw_input('What is the url? > ')
client_name = raw_input('What is the name? (Type it exactly as it appears on the exception sheet ie J.Doe) > ')
client = create_client(client_url).worksheet(client_name)

#-------------------------------------------------- Start Main ------------------------------------------

print '[+] File Loaded...'
time.sleep(1)
os.system('cls')

while True:
    print ' CFA Exceptions Script! v1.6'
    print ' If you need to upload to google, just type upload in the "start time" field!'
    print '---------------------------------------------------------------------------------'
    try:
        exception_code, inc_num, date, full_time, start_time = get_inputs()
        write_and_read(client, exception_code, inc_num, date, full_time, start_time)
        print '[+] processing...'
    except:
        print '[!] logging back in...'
        client = create_client(client_url).worksheet(client_name)
        write_and_read(client, exception_code, inc_num, date, full_time, start_time)
        print '[+] processing...'
        
    print '[+] Added successfully...'
    time.sleep(1)
    os.system('cls')