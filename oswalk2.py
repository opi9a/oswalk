# coding: utf-8
files = []
for f,x,y in os.walk("testdir/"):
    for g in y:
        files.append(os.path.join(f,g))
    
