import os

for files in os.listdir(os.getcwd()):
    if files.endswith('.ui'):

        infile = files
        output = files[:len(files)-3] + ".py"
        bashCommand = "pyuic5 " + files + " -o ../gui_files/" + output
        os.system(bashCommand)
        print("Command " + "'"+bashCommand+"'" +" completed")


