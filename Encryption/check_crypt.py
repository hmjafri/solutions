from urllib.request import urlopen
import rdft160crypt as crypt
import sys

sub_type = ["substitution", "ceaser", "block"]

# Select a cipher
encryption_type = sub_type[0]

textfile = urlopen("http://textfiles.com/stories/13chil.txt")
#sys.exit(0)

encrypted = ""
if encryption_type == "substitution":
    for line in textfile:
        encrypted += crypt.sub_encrypt(line.decode())
    
    print(crypt.sub_decrypt(encrypted))
elif encryption_type == "ceaser":
    for line in textfile:
        encrypted += crypt.ceaser_encrypt(line.decode(), 8)

    print(crypt.ceaser_decrypt(encrypted, 8))
elif encryption_type == "block":
    for line in textfile:
        encrypted += crypt.block_encrypt(line.decode(), "mykey")
        
    print(crypt.block_decrypt(encrypted, "mykey"))
        
    


    
    