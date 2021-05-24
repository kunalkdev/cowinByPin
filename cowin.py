
"""
Created on Sun May  9 13:42:59 2021

@author: kunal
"""
import requests
#import json
import time
from playsound import playsound
import datetime
import traceback
import sys

headers_dict= {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    };

dates = []
pinCodes = []
dose=1

def check_appointment(pinCode):
    base_url="https://cdn-api.co-vin.in/api/v2"
    session_url="/appointment/sessions/public/findByPin?pincode="
    for checkdate in dates:
        final_url=base_url+session_url+pinCode+"&date="+checkdate;
        #print (final_url)
        time.sleep(3)
        response = requests.get(final_url, headers=headers_dict)
        sessions = response.json()
        for session in sessions["sessions"]:
            if ((session["min_age_limit"] == 18) and 
                (
                (dose == 1 and session["available_capacity_dose1"] > 0)
                or
                (dose == 2 and session["available_capacity_dose2"] > 0)
                )
                ):
                print()
                print ("name: ",session["name"])
                print ("pincode: ",session["pincode"])
                print("available:", session["available_capacity"])
                print("available dose 1:", session["available_capacity_dose1"])
                print("available dose 2:", session["available_capacity_dose2"])
                print("date: ",session["date"])
                #if (session["available_capacity"] > 10):
                playsound("CarAlarm.mp3")


def pinCodeNotValid (pinCodeInput):
    global pinCodes 
    pins = pinCodeInput.split(",")
    
    for pin in pins:
        if (len(pin.strip()) != 6) :
            return True
        if (not pin.strip().isdigit()):
            return True
        pinCodes.append(pin.strip())

def getDates():
    global dates
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days = 1)
    dayAfterTomorrow = today + datetime.timedelta(days = 2)
    d1 = today.strftime("%d-%m-%Y")
    dates.append(d1)
    d2 = tomorrow.strftime("%d-%m-%Y")
    dates.append(d2)
    d3 = dayAfterTomorrow.strftime("%d-%m-%Y")
    dates.append(d3)

try:
    pinCodeInput = input ("Enter the PinCode in comma seperated e.g. single pincode 110011 - more than one 110011,110022,110023  : ")
    if (pinCodeNotValid(pinCodeInput.strip())):
        print ("Invalid pincode(s)")
        sys.exit()
    
    doseDetail = input ("Enter 1 for dose1 2 for dose2 alert : ")
    if (doseDetail.strip().lower() == '1'):
        dose=1
    elif (doseDetail.strip().lower() == '2'):
        dose=2
    else:
        print ("Enter either 1 for dose1 or 2 for dose2")
        sys.exit()
        
    getDates()
    
    print ("Checking for dates "+str(dates)+" dose "+str(dose)+ " pincode(s) "+str(pinCodes))
    
    while (1):
        for pinCode in pinCodes:
            check_appointment(pinCode)
except:
    print ("error occured")
    traceback.print_exc()
finally:
    waitClose = input ("Press enter to exit ...")