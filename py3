##f = open("example.txt","w")
##for i in range(1,4):
##    f.write("Line %d\n" %i)
##f.close()
##
##f = open("example.txt","a")
##alphabet = ['A','B','C','D','E']
##for c in alphabet :
##    f.write(c)
##f.close()
##
##f = open("example.txt","r")
##data = f.read()
##print(data)
##f.close()
##
##f = open("example.txt","r")
##while True :
##    line = f.readline()
##    if not line : break
##    print(line,end = '')
##f.close()
##
##f = open("example.txt","r")
##data = f.readlines()
##for line in data :
##    print(line,end = '')
##f.close()
####f = open("profile.txt","w")
####name = input("Name : ")
####age = input("Age : ")
####f.write("Name : %s\n" % name)
####f.write("Age : %s\n"% age)
####f.close()
##f = open("profile.txt","a")
##school = input("School  :")
##f.write("School : %s\n" % school)
##f.close()
##f = open("profile.txt","r")
##data = f.read()
##print(data)
##f.close()
##f = open("profile.txt","r")
##data = f.readlines()[2]
##print(data)
##f.close()
##f = open("profile.txt", "w")
##name = input("Name : ")
##age = input("Age : ")
##f.write("Name : %s\n" % name)
##f.write("Age : %s\n" % age)
##f.close()
##f = open("profile.txt","r")
##
##print(f.read())
##
##f.close()
##f = open("alphabet.txt","w")
##f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##f.close()
##f = open("alphabet.txt","r")
##n=int(input(" index : "))
##f.seek(n)
##print(f.read())
##f.close()
##f = open("fruit.txt","r")
##data = f.readlines()
##
##for i in data:
##    if len(i) >= 11:
##        print(i)
##
##
##
##f.close()
##f = open("anna.txt","r")
##data = f.read()
##data = data.split()
##
##for i in data :
##    if 'b' in i :
##        print(i)
##    elif 'B' in i :
##        print(i)
##f.close()
def read_file(file_name) :
    f = open(file_name,"r")
    print(f.read())


def write_file(file_name,mode) :
    f = open(file_name,mode)
    print("input(input(Enter 'q' to exit input) :")
    while True :
        a = input()
        if a == "q":
            break
        f.write(a)






file_name = input("File name : ")
mode = input("file mode(r\w\a) : " )

if mode == "r" :
    read_file(file_name)
else :
    write_file(file_name, mode)
