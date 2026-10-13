# w mode - open the file for writting or Overwrite a existing file.
# w mode se ham kisi bhi file ko overwrite kar sakte hai but ham usko wapas se reverse nahi kar sakte hai to thoda unsafe hai w mode


fh = open("file03.txt","wt")
fh.write("this file overwriting using 'w' mode in python. \n")
fh.write("Have a nice night!")
fh.close()

# 'w' mai aagar ham kisi bhi file ko ham overwrite karte hai to phir usse ham reverse nahi kar sakte hai
# and most important thing is ki aagar ham kisi aaise file ke sath w mode ka use karte hai
#  jo exist hi nahi karti hai to usse w mode create kar ke write karega.
# yaha pr 'w' mode create or write dono task perform karta hai.

fh = open("file04.txt","wt")
fh.write("this file overwriting & creating using 'w' mode in python. \n")
fh.write("Have a nice night!")
fh.close()