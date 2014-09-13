
# Remove Duplicate Pictures Created by Picasa

Did you ever notice that (the otherwise excellent) [Picasa](http://picasa.google.com/) creates a backup of any picture that has been modified? I could never find an option to suppress that behavior. I mean, I know what I am doing; I do not want to have extra copies of my pictures laying around and taking up all my disk space.

So I built a small application that lists the ".picasaoriginals" folders location under the folder where the Python script is run from. It lists the content of the ".picasaoriginals" and prompts the user for deletion.

## Example of the command-prompt interation with the program

    python DelPicasaOriginalBackups.py

    Folder:
    C:\pics\09-01-03 - Montreal\.picasaoriginals
    Content:
    {IMG_7432.jpg,IMG_7433.jpg,IMG_7434.jpg}

    Do you want to delete the following folder and everything in sub-dirs?
    C:\pics\09-01-03 - Montreal\.picasaoriginals
    N/Y?

## The Code!

    #!/usr/bin/python3.0

    import os, os.path, shutil, code

    PICASA_BACKUP_FOLDER_NAME = ".picasaoriginals"
    TEST_DIR = "./tests/DeletePicasaBackupFolders/"

    def ReturnAllPicasaBackupFolders():
        lPicasaBackupFolders_Fullpath = []
        for root, dirs, files in os.walk('.'):
            for adir in dirs:
                if adir == PICASA_BACKUP_FOLDER_NAME:
                    lPicasaBackupFolders_Fullpath.append( os.path.abspath( os.path.join(root,adir)) )
        return lPicasaBackupFolders_Fullpath

    def ReturnAllFilesInFolder_AsFlat(_Folder):
        "Return a flat array of all files under the dir and subdirs, without directory information."
        lAllFiles = []
        for root, dirs, files in os.walk( _Folder ):
            lAllFiles += files
        return lAllFiles

    def DeleteFolderAndSubIfUserManuallyAgrees(_Folder, IsFakeRun = False):
        print ("Do you want to delete the following folder and everything in sub-dirs?")
        print ("   " + _Folder)
        print("N/Y?")
        u_ans = code.InteractiveConsole.raw_input("")
        if u_ans.upper() == "Y":
            print ("Deleting folder...")
            if not IsFakeRun: shutil.rmtree(_Folder)
        else:
            print ("User chose not to delete the folder.")

    def GetFolderInfo_Str(_Folder):
        lStrFolderInfo = ""
        lStrFolderInfo+= "Folder:\n   " + _Folder + "\n"
        lStrFolderInfo+= "Content:\n"
        lStrFolderInfo+="   {"
        for file in ReturnAllFilesInFolder_AsFlat(_Folder):
            lStrFolderInfo+=file + ","
        lStrFolderInfo = lStrFolderInfo[:-1]
        lStrFolderInfo +="}\n"
        #Somehow does not work:
        #lStrFolderInfo+="Size: " + str(os.path.getsize(_Folder)) + " bytes"
        return lStrFolderInfo

    def Do():
        IsFakeRun = False
        
        lSuspectedBackupFolders = ReturnAllPicasaBackupFolders()
        for lSuspectedFolder in lSuspectedBackupFolders:
            print (GetFolderInfo_Str(lSuspectedFolder) + "\n" )
            DeleteFolderAndSubIfUserManuallyAgrees(lSuspectedFolder, IsFakeRun)
        if len(lSuspectedBackupFolders) ==0:
            print("No folder detected, press a key to exit...")
            code.InteractiveConsole.raw_input("")
        
    if __name__ == "__main__":
        Do()

Hope it is useful. Feel free to post any comment/suggestion.
