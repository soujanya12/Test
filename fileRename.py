import os
import shutil
import datetime
#img_loc = 'C:\directorypath\logo.png'
datestr = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d'))
print("date:", datestr)
timestr = datetime.datetime.now().strftime("%I-%M-%S")
print("time:",timestr)
folder_loc = datestr+'/'+timestr
print("dirname",folder_loc)
if not os.path.exists(folder_loc):
    os.makedirs(folder_loc)
    print("Directory",folder_loc, "Created")
    #finalfolder = shutil.move(img_loc, folder_loc)
else:
    print("Directory", folder_loc, "already exists")
