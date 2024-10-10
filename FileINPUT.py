s= "rajnish is a good boy "

# with open("test.txt","r") as f:
#   s =  f.read()
#   print(s)

fp = open("test2.txt","r")
s=fp.read()
print(s)
fp.close()

with open("test.txt ", "a") as f:
    f.write("yes he is best ")