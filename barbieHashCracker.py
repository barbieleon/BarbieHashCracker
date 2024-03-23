#!/usr/bin/python3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys,crypt

# Define console colors
BLUE = "\033[0;34m"
ENDCOLOR = "\033[0m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"




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



if len(sys.argv) <= 1:
    print("Usage: ./barbieCrack.py <password_file>")
else:
    # Capture the hash and salt input
    target_hash = input(f"{CYAN}Enter the target hash: {ENDCOLOR}")
    salt = input(f"{CYAN}Enter the salt: {ENDCOLOR}")
    password_file = sys.argv[1]
    found = False

    # Try to find the password in the provided file
    try:
        with open(password_file, "r") as file:
            for password_in_file in file:
                password = password_in_file.strip()
                hashed_password = crypt.crypt(password, salt)
                if target_hash == hashed_password:
                    print(f"{GREEN}Original password: {ENDCOLOR}", password, f"{GREEN}Hashed Password: {ENDCOLOR}", hashed_password)
                    found = True
                    break
    except UnicodeDecodeError as err:
        print(f"{RED}Error reading the file: the file may contain non-text elements{ENDCOLOR}")
        print(f"{RED}Error detail: {err}{ENDCOLOR}")

    if not found:
        print(f"{RED}Password not found. Try using another password list{ENDCOLOR}")

    # Ask to try a different file if the password was not found
    if not found:
        new_pass_file = input(f"Try a different file? (y/n): ").lower().strip()
        if new_pass_file == "y":
            new_pass_file = input("Enter the filename: ").strip()
            try:
                with open(new_pass_file, "r") as new_file:
                    for new_pass in new_file:
                        password = new_pass.strip()
                        hashed_password = crypt.crypt(password, salt)
                        if target_hash == hashed_password:
                            print(f"{GREEN}Original password: {ENDCOLOR}", password, f"{GREEN}Hashed Password: {ENDCOLOR}", hashed_password)
                            found = True
                            break
                    if not found:
                        print(f"{RED}Password not found in the new file.{ENDCOLOR}")
            except FileNotFoundError:
                print(f"{RED}The file '{new_pass_file}' was not found. Please check the filename and try again.{ENDCOLOR}")
            except UnicodeDecodeError as err:
                print(f"{RED}Error reading the file: the file may contain non-text elements{ENDCOLOR}")
                print(f"{RED}Error detail: {err}{ENDCOLOR}")
        else:
            print("Program exited.")
