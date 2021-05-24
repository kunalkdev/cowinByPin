RUN SAMPLE:<br />
<br />
python .\cowin.py <br />
Enter the PinCode in comma seperated e.g. single pincode 110011 - more than one 110011,110022,110023  : 122001 <br />
Vaccine preference - 0 for any, 1 for covishield, 2 for covaxin, 3 for sputnik : 1<br />
Cost Preference - 0 for any, 1 for paid only, 2 for free only : 0<br />
Enter 1 for dose1, 2 for dose2 alert : 2<br />
Checking for dates -['24-05-2021', '25-05-2021', '26-05-2021'] dose -2 pincode(s) -['122001'] vaccine-COVISHIELD cost preference-any<br />

2021-05-24 21:31:21.267308<br />
name:  Max Hospital<br />
pincode:  122001<br />
vaccine:  COVISHIELD<br />
fee_type:  Paid<br />
available: 19<br />
available dose 1: 0<br />
available dose 2: 19<br />
date:  26-05-2021<br />
!!!Plays sound for alert!!! <br />


SETUP:
1. place mp3 file put in same folder with python script - cowin.py.
2. If you don't have setup of python, recommend downloading anaconda package - https://www.anaconda.com/products/individual
3. install playsound playsound - Ananconda powershell prompt - $ pip install playsound 
4. Go to folder having cowin.py - run python cowin.py
5. Recommended to change power option to disable sleep - set sleep timer to never. So, that script always get cpu and keep running in case of inactivity of system too.


LIMITATIONS:
1. There is a limit of 100 api calls per 5 mins per IP. As script run after every 3 seconds. Please run it only in 1 machine in one wifi.
2. This is currently only for under 45 age category.