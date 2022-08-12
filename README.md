# DIFF-COOKIE
Tool to differentiate two cookie sets.

## Why this tool? 
Many a times , there are certain instance where access is given if the cookie key and value is set. Scenario : Admin user has extra cookie set - admin=base64encoded==; and normal user has - user=base64encoded==;
So this tool compares and differentiate between two cookie sets to output those difference between 'em

For example, below are the two cookie sets:

```
"param1=value1; param2=value2; param6=dddd==; param3=value3;param9=true;" 
"param2=value4; param1=test;param4=hello; param7=fafdfasfs%===; param8=true;"
```
On running diff-cookie.py
This will print out the keys which aren't present in Cookie-1, and also the keys along with the values which aren't present in Cookie-2 like :
```
============================================================
Diff cookie!
------------------------------------------------------------

Cookie key-val pairs not present in first cookie: 
param7 = fafdfasfs%===;
param8 = true;
param4 = hello;

Cookie key-val pairs not present in second cookie: 
param9 = true; 
param3 = value3; 
param6 = dddd==; 

============================================================
```
## Installation
```
$ git clone 
$ pip3 install -r requirements.txt
$ python3 diff.cookie.py
```

## Usage 
```
Usage: python3 cookie-diff.py cookie1 cookie2
Example : python3 cookie-diff.py "param1=value1; param2=value2; param6=dddd==; param3=value3;param9=true;"  "param2=value4; param1=test;param4=hello; param7=fafdfasfs%===; param8=true;"

OR

Usage: python3 cookie-diff.py cookie.txt
Example : python3 cookie-diff.py cookie.txt
```
