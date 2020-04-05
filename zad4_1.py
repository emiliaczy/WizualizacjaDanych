file = open("file.txt", "w")
for i in range(1,30):
    if (i%4==0):
        file.write(str(i))
        file.write("\n")

file.close()
        

        
        
        