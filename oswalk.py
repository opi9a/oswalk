# coding: utf-8
def fprint(topdir):
    for rawdir in os.listdir(topdir):
        if rawdir[-1]=="~":
            print("Couldn't process ", rawdir)
            print("Please clear up temp files etc")
            return
        dir = os.path.join(topdir, rawdir)
        print("looking at ", dir, ".. ", end="")
        if os.path.isfile(dir):
            print(dir, " is a file")
            with open(dir, "r") as f:
                print(f.read())
        elif os.path.isdir(dir):
            print(dir, "is a directory")
            fprint(dir)
        else:
            print("Don't know what ", dir, " is")
           
