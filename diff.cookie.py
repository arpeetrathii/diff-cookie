import os
import re
import sys
from termcolor import colored

cookie_params1=[]
cookie_params2=[]
cookie_values1=[]
cookie_values2=[]
cookie_params =[]
cookie_values =[]


def split_cookie(line,cookie_params,cookie_values):
    regex = list(re.split(";",line))
    for x in regex:
        spl = x.split("=",1)
        for attr in range(0,len(spl)):
            if attr % 2== 0: 
                cookie_params.append(spl[attr].strip())
            else:
                cookie_values.append(spl[attr].strip())

def cookie_combine_and_render(cookie_params,cookie_params1,cookie_params2,cookie_values,cookie_values1,cookie_values2):
    cookie_params = list(set(cookie_params1 + cookie_params2))
    cookie_params = [i for i in cookie_params if i != None and i != '']
    cookie_values= list(set(cookie_values1 + cookie_values2))
    cookie_values = [i for i in cookie_values if i != None and i != '']
    print(colored("Cookie key-val pairs not present in first cookie: ","red"))
    for params in cookie_params:
        if params not in cookie_params1:
            print(colored(f"{params} = {cookie_values2[cookie_params2.index(params)]};","green"))
    print()
    print(colored("Cookie key-val pairs not present in second cookie: ","red"))
    for params in cookie_params:
        if params not in cookie_params2:
            print(colored(f"{params} = {cookie_values1[cookie_params1.index(params)]}; ","green"))
    
    
    

# def split_cookie_in_args(arg1,arg2):
if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    split_cookie(arg1,cookie_params1,cookie_values1)
    split_cookie(arg2,cookie_params2,cookie_values2)
    
    print()
    print("============================================================")
    print(colored("Diff cookie!","blue",attrs=['bold']))
    print("------------------------------------------------------------")
    print()
    cookie_combine_and_render(cookie_params,cookie_params1,cookie_params2,cookie_values,cookie_values1,cookie_values2)
    print()
    print("============================================================")

elif len(sys.argv) == 2:
    if(sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "-help"):
        print("Usage: python cookie-diff.py cookie1 cookie2 ")
        print("OR")
        print("Usage: python cookie-diff.py cookie.txt")
    #Reading line 1 - Cookie 1
    
    else:
        try:
            cwd = os.getcwd()
            def_loc = sys.argv[1]
            if (os.path.exists(def_loc)):
                loc=sys.argv[1]
            elif(os.path.exists(cwd+"/"+def_loc)):
                loc=cwd+"/"+def_loc
            cookie_file = open(loc,"r")
            line1=cookie_file.readline()
            split_cookie(line1,cookie_params1,cookie_values1)

            #Reading line 2 - Cookie 2
            line2=cookie_file.readline()
            split_cookie(line2,cookie_params2,cookie_values2)
            
            print()
            print("============================================================")
            print(colored("Diff cookie!","blue",attrs=['bold']))
            print("------------------------------------------------------------")
            print()
            cookie_combine_and_render(cookie_params,cookie_params1,cookie_params2,cookie_values,cookie_values1,cookie_values2)
            print()
            print("============================================================")
        except:
            print("Some error occured, file doesn't exists maybe! ")
            print("Or maybe if you are seeing result. Cookie isn't formatted well.")

else : 
    print("Usage: python cookie-diff.py cookie1 cookie2 ")
    print("OR")
    print("Usage: python cookie-diff.py cookie.txt")
