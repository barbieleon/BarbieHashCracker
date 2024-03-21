#!/usr/bin/python3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys,crypt

BLUE = "\033[0;34m"
ENDCOLOR = "\033[0m"
RED = "\033[0;31m"

def display_banner():
    banner_text = ''' 



                              .______        ___      .______      .______    __   _______                                      
                              |   _  \      /   \     |   _  \     |   _  \  |  | |   ____|                                     
                              |  |_)  |    /  ^  \    |  |_)  |    |  |_)  | |  | |  |__                                        
                              |   _  <    /  /_\  \   |      /     |   _  <  |  | |   __|                                       
                              |  |_)  |  /  _____  \  |  |\  \----.|  |_)  | |  | |  |____                                      
                              |______/  /__/     \__\ | _| `._____||______/  |__| |_______|                                     
                                                                                                                                
                                                                                                                                
                                                                                                                                
 __    __       ___           _______. __    __       ______ .______           ___        ______  __  ___  _______ .______      
|  |  |  |     /   \         /       ||  |  |  |     /      ||   _  \         /   \      /      ||  |/  / |   ____||   _  \     
|  |__|  |    /  ^  \       |   (----`|  |__|  |    |  ,----'|  |_)  |       /  ^  \    |  ,----'|  '  /  |  |__   |  |_)  |    
|   __   |   /  /_\  \       \   \    |   __   |    |  |     |      /       /  /_\  \   |  |     |    <   |   __|  |      /     
|  |  |  |  /  _____  \  .----)   |   |  |  |  |    |  `----.|  |\  \----. /  _____  \  |  `----.|  .  \  |  |____ |  |\  \----.
|__|  |__| /__/     \__\ |_______/    |__|  |__|     \______|| _| `._____|/__/     \__\  \______||__|\__\ |_______|| _| `._____|

    '''
    print(f"{BLUE}{banner_text}{ENDCOLOR}")
display_banner()

def display_info():
    banner_info = ''' 

BarbieHashCracker V1.0
Coded by Barbie Leon

    '''
    print(f"{banner_info}")
display_info()



if len(sys.argv) <=1:
    print("How to use: ./barbieCrack.py + passwords")
else:
    #Input to capture the salt
    targetHash = input("Enter the target hash: ")
    salt = input("Enter the Salt: ")
    passwordFile = sys.argv[1]


    #Opening a custom file with passwords
    with open(passwordFile, "r") as file:
        for passwords_in_file in file:
            password = passwords_in_file.strip()
            hashed_password = crypt.crypt(password, salt)
            if(targetHash == hashed_password):
                print(f"{RED}Original password: {ENDCOLOR}", password, f"{RED}Hashed Password: {ENDCOLOR}",hashed_password)