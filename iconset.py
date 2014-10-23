import sys
from subprocess import call

origin_file = ""
def gen_icon(type, sizes):
    print "Icon set for %s"%(type)    
    print origin_file
    for i in sizes:
        icon_name = "%s_icon%s.png"%(type,i)
        icon_name2x = "%s_icon%s@2x.png"%(type,i)
        call(["cp", origin_file, icon_name])
        call(["cp", origin_file, icon_name2x])            
        call(["sips", "-Z" ,str(i), icon_name])            
        call(["sips", "-Z" ,str(i*2), icon_name2x])                    

if len(sys.argv) < 2:
    print "python iconset.py original_file_name"
else:
    origin_file = sys.argv[1]
    ios_sizes = {16,29, 32,40,50, 57,60,58,72, 76, 80,100 ,114,120, 128, 144,152, 256}
    osx_sizes = {29,40,60,76,72,144,512}
    gen_icon("osx", osx_sizes)
    gen_icon("ios", ios_sizes)    
