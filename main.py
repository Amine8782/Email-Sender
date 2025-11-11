import logging
import re
import secrets
import random
import base64
import datetime
import glob
import string
import sys
import time
import os
import pyfiglet
import requests
import socket
import termcolor
import email
import email.utils
from multiprocessing.dummy import Pool
from email.utils import formatdate
from email.utils import make_msgid
import smtplib 
from smtplib import SMTPConnectError
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from termcolor import colored
from random import choice
from colorama import Fore, init
from email.message import EmailMessage
import html
from unidecode import unidecode
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

def banner():
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("Bulk Sender", font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t{cyan}[ {green}Created By ZANZAN {white}] - [V 1.0] @zanzanimax \n")

def send_options():
    user_choice = input(" [?] Select The Sending Speed Mode , Enter 'slow' or 'fast': ")
    if user_choice == 'slow' or user_choice == 's'  or user_choice == 'S':
        delay_time = input(" [?] Enter the delay time (in seconds) between sending emails: ")
        slow_send(delay_time)
    elif user_choice == 'fast' or user_choice == 'f' or user_choice == 'F':
        num_threads = input(" [?] Enter the number of threads for sending emails: ")
        fast_send(num_threads)
    else:
        print(" [!] Invalid option. Please enter 'slow' or 'fast'.")
        send_options()   

def replace_strings(stringtoreplace,email,random_link):
    result = re.search(r'^([\w._-]+)', email)
    name = result.group(1)
    for char in "._-":
        name = name.replace(char,' ')
    stringtoreplace = stringtoreplace.replace('##email##', email)
    stringtoreplace = stringtoreplace.replace('##name##', name)
    stringtoreplace = stringtoreplace.replace('##link##', random_link)
    stringtoreplace = stringtoreplace.replace('##random_number##', str(random.randint(0, 9999999)))
    stringtoreplace = stringtoreplace.replace('##random_string##',''.join(random.sample(string.ascii_lowercase + string.digits, 7)))
    stringtoreplace = stringtoreplace.replace('##time##', datetime.datetime.now().strftime('%H:%M:%S'))
    stringtoreplace = stringtoreplace.replace('##date##', datetime.datetime.now().strftime('%Y-%m-%d'))
    stringtoreplace = stringtoreplace.replace('##date&time##', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return stringtoreplace

def send(email):
        
    email = email.strip()        
    random_link = random.choice(open('settings/links.txt').readlines())
    random_smtp = random.choice(open('settings/smtps.txt').readlines())
    host, port, user, passwd = random_smtp.strip().split("|")
    random_subject = random.choice(open('settings/subjects.txt').readlines())
    random_subject = replace_strings(random_subject,email,random_link)
    random_subject = random_subject.encode('latin-1').decode('utf-8')
        
    try:
        random_from = random.choice(open('settings/froms.txt').readlines())
        random_from = f"{random_from} <{user}>"
    except Exception as e:
        random_from = user
 
    all_tamplates = glob.glob('templates/*.html')
    _temp = choice(all_tamplates)
    with open(_temp, 'r', encoding='utf-8') as (f):
        r_temp = f.read()
        email_template = replace_strings(r_temp,email,random_link)
    try:
        email_detail = " [FROM] " + user 
        server = smtplib.SMTP(host, port)
        server.starttls()
        try:
            server.login(user, passwd)
        except smtplib.SMTPAuthenticationError as e:
            print(f"{red}- "+progress+" [ERROR] authenticating with SMTP server: Invalid username or password :"+email_detail)
            
        email_template = email_template.encode('ascii', 'xmlcharrefreplace')
        msg = MIMEText(email_template, "html", "us-ascii")
        msg["From"] = random_from
        msg["To"] = email
        msg["Subject"] = random_subject
        msg["Date"] = formatdate(localtime=True)
        msg["Message-Id"] = make_msgid()
        
           
        try:
            with SMTP(host, port) as server:
                server.starttls()
                server.login(user, passwd)
                server.sendmail(user, email, msg.as_string())
                print(colored(f"{green}- [SENDTO] " + email + email_detail  , 'green'))
                
        except Exception as e:
            print(f"{red}-  [ERROR] occurred while sending email to "+email_detail )
            print(e)
            
    except (smtplib.SMTPConnectError, socket.timeout) as e:
        print(f"- [ERROR] connecting to SMTP server: "+email_detail , e)
        
    except smtplib.SMTPException as e:
        print(f"{red}-  [ERROR] Unable to send email"+email_detail )
        
    except Exception as e:
        print(f"{red}- [ERROR] Unexpected : [FROM] "+email_detail , e)
        


def fast_send(num_threads):
    with open("settings/emails.txt", 'r', errors="ignore") as (f):
        emails = f.read().split('\n')
        ThreadPool = Pool(int(num_threads))
        Threads = ThreadPool.map(send, emails)





def slow_send(dealytime):

    email_count = 0
    with open("settings/emails.txt") as f:
        for _ in f:
            email_count += 1
    with open("settings/emails.txt") as f:
        email_list = f.readlines()

    email_send_count = 0
    # Iterate through  the email list
    for email in email_list:
        time.sleep(int(dealytime))
        print(f"{white}Waiting for " +dealytime+" seconds")
        email_send_count += 1
        progress = str(email_send_count)+"/"+str(email_count)
        send(email)
        

if __name__ == '__main__':
    banner()
    send_options()