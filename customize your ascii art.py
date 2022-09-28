# Variable changing Ascii Art of APS

aps="""
  /$$$$$$  /$$$$$$$   /$$$$$$ 
 /$$__  $$| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$$| $$$$$$$/|  $$$$$$ 
| $$__  $$| $$____/  \____  $$
| $$  | $$| $$       /$$  \ $$
| $$  | $$| $$      |  $$$$$$/
|__/  |__/|__/       \______/ 
                              
                              """
print(f"Original ASCII Art: {aps}")
userinput=input("To change the dollar to any other symbol type that symbol and press enter: ")

print(aps.replace('$' , userinput ))
