count=0
with open('Ex_Files_Python_Automation/Exercise Files/inputFile.txt','r') as f:
    with open('Ex_Files_Python_Automation/Exercise Files/Passppl.txt','w') as p:
        for line in f:
            if 'P' in line.split()[2]:
                p.write(line)
print(count)