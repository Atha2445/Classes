# f = open("demo.txt","r")
#print(f.read())
# print(f.readline())
# print(f.readline())

# f1 = open("mydemo.txt","w")
# f1.write("This is a file")

# myself = open("mydemo.txt","w")
# myself.write("India is My Country\n.All Indians are My Brothers and Sisters\n.I Love My Country.")

# for i in f:
#     myself.write(i)

# f = open("demo.txt")
# f.close() 

# f = open("Untitled.png","rb")

# f1 = open("Untitled design_copy.png","wb")
# print(f.read())

# for i in f:
#     f1.write(i)

import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File does not exists") 