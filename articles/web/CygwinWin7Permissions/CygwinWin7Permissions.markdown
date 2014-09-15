
# Get Full Access Right to A Folder Using Cygwin Under Windows 7

It can be pretty hard to get full access rights to a directory and all its contents recursively when using cygwin under windows 7. In theory a simple `chmod 777 -R "c:\path_to\target\folder` should do the trick, but it just isn't so. Here is the most 'bulletproof' way I found to make sure I get proper ownership of a folder:

    takeown /F "C:\path_to\target\folder" /R
    icacls "C:\path_to\target\folder" /grant Everyone:\(F\) /T
    icacls "C:\path_to\target\folder"
    chmod 777 -R "c:\path_to\target\folder"

Or for the current dir:
    
    takeown /F "." /R
    icacls "." /grant Everyone:\(F\) /T
    icacls "."
    chmod 777 -R "."
    
[icacls.exe](http://en.wikipedia.org/wiki/Icacls) is window's command-line tools to modify the [Access Control List](http://en.wikipedia.org/wiki/Access_Control_List) and 'takeown.exe' "`allows an administrator to recover access to a file that was denied by re-assigning file ownership`". I guess doing all three commands subsequently (takeown, icacls and chmod) is the blunt solution that has o be used until the cygwin team gets around to get `chmod` to work properly on windows 7.

