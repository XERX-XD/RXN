import os
import platform
print("JOIN FB GROUP")
os.system('clear')
os.system("xdg-open https://facebook.com/groups/460389902592352/")
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import rxn64
    
elif b == '32bit':
    import rxn32
    
