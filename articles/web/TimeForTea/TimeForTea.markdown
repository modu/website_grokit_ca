
# Time For Tea

A small program that alerts your when your tea (or anything else) is done. Extremely small. Does only one thing, and one thing right.

![](../../static/TimeForTea_sshot_v1-2.png)

## The Code!

Project on [google code](http://code.google.com/p/timefortea/); can be cloned using:

    hg clone https://timefortea.googlecode.com/hg/ timefortea 

## Note On Running Under Linux

The application can also be compiled and run by [mono](http://www.mono-project.com/Main_Page). Here is how to get a linux machine dev ready, compile and run the program (assuming a ubuntu distribution):

    sudo apt-get install -y mono-gmcs
    sudo apt-get install -y mono-devel
    hg clone https://timefortea.googlecode.com/hg/ timefortea
    cd timefortea
    gmcs -pkg:dotnet -target:winexe -out:TimeForTea.exe AppMain.cs TeaCounter.cs TeaCounter.Designer.cs TeaIsReadyPopUp.cs TeaIsReadyPopUp.Designer.cs Utils.cs
    chmod +x TimeForTea.exe
    ./TimeForTea.exe

![](../../static/TimeForTea_sshot_v1-2_linux.png)
![](../../static/TimeForTea_sshot_v1-2_linux_popup.png)

The application does not look as nice as in windows and there are few quirks (UI is a bit messed-up) but it works with no code modification :).

**Note: TimeForTea.exe is a _.exe_ file, but it is work under _Linux_ (is it .NET bytecode that the mono project can run).**

## Download

[Windows binary](../../static/TimeForTea_1.2_win.zip)

**Note:** you may need to install `libmono-winforms2.0-cil' (sudo apt-get install -y libmono-winforms2.0-cil on ubuntu) in order to run the linux version.




