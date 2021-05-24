RUN SAMPLE:

python .\cowin.py
Enter the PinCode in comma seperated e.g. single pincode 110011 - more than one 110011,110022,110023  : 122017
Enter 1 for dose1 2 for dose2 alert : 2
Checking for dates ['24-05-2021', '25-05-2021', '26-05-2021'] dose 2 pincode(s) ['122017']

2021-05-24 16:58:11.223592
name:  Columbia Asia
pincode:  122017
available: 298
available dose 1: 0
available dose 2: 298
date:  24-05-2021
<<Plays sound for alert>>


SETUP:
1. place mp3 file put in same folder with python script - cowin.py.
2. If you don't have setup of python, recommend downloading anaconda package - https://www.anaconda.com/products/individual
3. install playsound playsound - Ananconda powershell prompt - $ pip install playsound 
4. Go to folder having cowin.py - run python cowin.py
5. Recommended to change power option to disable sleep - set sleep timer to never. So, that script always get cpu and keep running in case of inactivity of system too.


LIMITATIONS:
1. There is a limit of 100 api calls per 5 mins per IP. As script run after every 3 seconds. Please run it only in 1 machine in one wifi.
2. This is currently only for under 45 age category.