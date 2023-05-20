import os,platform
os.system('git pull')
 
hacker=platform.architecture()[0]
if hacker=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif hacker=="64bit":
    #print('Command is in update wait we will fix it soon !')
    __import__("hacker")
