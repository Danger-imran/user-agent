import random
logo = (''' 
 Owner by @mr_danger_x 
join our channel https://t.me/we_are_haker
  _____                    _____                    _____                    _____                _____          
         /\    \                  /\    \                  /\    \                  /\    \              |\    \         
        /::\    \                /::\    \                /::\____\                /::\    \             |:\____\        
       /::::\    \              /::::\    \              /:::/    /               /::::\    \            |::|   |        
      /::::::\    \            /::::::\    \            /:::/    /               /::::::\    \           |::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /:::/    /               /:::/\:::\    \          |::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/____/               /:::/__\:::\    \         |::|   |        
    \:::\   \:::\    \      /::::\   \:::\    \      /::::\    \              /::::\   \:::\    \        |::|   |        
  ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\    \   _____    /::::::\   \:::\    \       |::|___|______  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\____\      /::::::::\    \ 
/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\    /::\____\/:::/  \:::\   \:::|    |    /::::::::::\____\
\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::|____|   /:::/~~~~/~~      
 \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/_____/\:::\/:::/    /   /:::/    /         
  \:::\   \:::\    \               \::::::/    /            \::::::/    /            \::::::/    /   /:::/    /          
   \:::\   \:::\____\               \::::/    /              \::::/    /              \::::/    /   /:::/    /           
    \:::\  /:::/    /               /:::/    /               /:::/    /                \::/____/    \::/    /   
Owner by @mr_danger_x 
join our channel https://t.me/we_are_haker         
     \:::\/:::/    /               /:::/    /               /:::/    /                  ~~           \/____/             
      \::::::/    /               /:::/    /               /:::/    /                                                    
       \::::/    /               /:::/    /               /:::/    /                                                     
        \::/    /                \::/    /                \::/    /                                                      
         \/____/                  \/____/                  \/____/                  
''')
print(40*'-')
print('FB PAGE: Mr Danger')
print('GITHUB: Danger-imran')
print(40*'-')
def generate_user_agent():
    cnc = "en_US"  # Example locale; replace with desired value
    tipecnc = "LTE"  # Example connection type; replace with desired value
    models = ["SM-G965F", "SM-N960F", "SM-G975F", "F7", "F9", "A3s", "A5s", "A7", "A9", "R11", "R17", "Reno 2", "Reno 3"]  # Example models; replace with desired models

    density = random.uniform(1.0, 3.0)
    width = random.randint(360, 2600)
    height = random.randint(900, 9999)
    net = random.choice(["6G", "3G", "4G", "5G"])
    com = "com.facebook.katana"  # Example package name; replace with desired value

    ua = (f"[FBAN/FB4A;FBAV/{random.randint(50, 250)}.0.0.{random.randint(10, 300)};"
          f"FBBV/{random.randint(0, 999999999)};"
          f"FBDM/{{density={density:.1f},width={width},height={height}}};"
          f"FBLC/{cnc};FBRV/{random.randint(0, 999999999)};"
          f"FBCR/{net};FBMF/Samsung;FBBD/Samsung;FBPN/{com};"
          f"FBDV/Samsung {random.choice(models)};"
          f"FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]")

    # Checking if the user agent is working
    is_working = random.choice([True, False])
    color_code = '\033[92m' if is_working else '\033[91m'  # Green for working, Red for not working
    status = "Working" if is_working else "Not Working"
    ua = f"{color_code}{ua} ({status})\033[0m"  # Reset color after the user agent

    return ua

n = int(input("Enter the number of user agents to generate: "))
for _ in range(n):
    print(generate_user_agent())