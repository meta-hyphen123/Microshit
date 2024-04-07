red=""
green=""
yellow=""
blue=""
purple=""
cyan=""
violate=""
nc=""

class logo:
  @classmethod
  def tool_header(self):
    print(f'''Microshit Shiter [Version 1]
(c) Microshit Corporation。 All rights reserved.''')

  @classmethod
  def tool_footer(self):
    print(f'''''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
  [ + ]  {red}We can't install Microshit
  [ + ]  {red}There are some error.
  [ + ]  {red}Please try again after some time!''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print (f'''
  [ + ] Use It At Your Own Risk.
  [ + ] No Warranty.
  [ + ] Use it legal purpose only.
  [ + ] We are not responsible for your actions.
  [ + ] Do not do things that are forbidden.

If you are installing this tool.
that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print (f'''
Microshit installed successfully.
To run Microshit,
Type Microshit in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print (f'''
{yellow}  [ 1 ] {green}Update your Microshit.
{yellow}  [ 0 ] {green}For Back.{nc}''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print (f'''
Microshit Updated Successfully.
Press Enter to continue.{nc}''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print (f'''
No network connection?
Are you offline?
Please try again after some time.''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print (f'''
We can't Update Microshit.
Please try again after some time.{nc}''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
Tool Name :Microshit
Tools :- total  tools.

Microshit is automatic tool installer.
Made for termux and linux based system.
Note :- Use this tool at your own risk.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print (f"""""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
Sorry ??
'{name}'is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
Installed Successfully !!
'{name}' is Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
Sorry ??
{name}' is not installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print (f"""""")

  @classmethod
  def updating(self):
    print (f"""updating Microshit """)

  @classmethod
  def installing(self):
    print (f"""Installing""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print (f'''
Thanks for using Microshit
Good Bye.....! ){nc}''')
    self.tool_footer()
