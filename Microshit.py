import os
import sys
from modules.menu import *

if __name__=="__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    os.system("alias Microshit='Tool-X'")
    logo.exit()
