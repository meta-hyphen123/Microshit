import os
import sys
import subprocess
from time import sleep
from modules.logo import *
from modules.system import *

yellow=""
blue=""
nc=""


        
class tool:
  @classmethod

  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"Do you want to install Microshit [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Microshit"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Microshit")
          os.system(system.sudo+" cp -r modules core Microshit.py "+system.conf_dir+"/Microshit")
          os.system(system.sudo+" cp -r core/Microshit "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/microshit")
          os.system("cd .. && "+system.sudo+" rm -rf Microshit")
          if os.path.exists(system.bin+"/Microshit") and os.path.exists(system.conf_dir+"/Microshit"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Microshit{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Microshit{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/Microshit"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Micorshit")
          os.system("cp -r modules core Microshit.py "+system.conf_dir+"/Microshit")
          os.system("cp -r core/Microshit "+system.bin)
          os.system("chmod +x "+system.bin+"/Microshit")
          os.system("cd .. && rm -rf Microshit")
          if os.path.exists(system.bin+"/Microshit") and os.path.exists(system.conf_dir+"/Microshit"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Microshit{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"Microshit{nc}@{blue}space {yellow}$ {nc}")
            os.system("alias Microshit='Tool-X'")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
