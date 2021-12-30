import send2trash,shutil,os
top=os.getcwd()
for parent,sub,filename in os.walk(top, topdown=False):
    #
    #print(filename)
    for fname in filename:
        name, extension = os.path.splitext(fname)
        if extension =='.txt':
            #print(fname)
            size = os.path.getsize(fname)
            print(size)
            if size>104857600:
                send2trash.send2trash(fname)