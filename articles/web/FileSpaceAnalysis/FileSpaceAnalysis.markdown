
# Analyze Which Files Take The Most Space

I often need to either clean up space on a drive or to shrink a project / notes for archiving. One way to do it is to navigate blindly and to erase big files when found. But this process can be cumbersome. I wrote a small Python script that lists the 150 biggest files contained under the folder in which the script is executed.

## The Code!

    #python 2.6, 3.1

    import os, tempfile
    import misc.search_files

    class FileInfo:
      
      __FullPathFilename = None
      __FileSize = None
      
      def __init__(self, FullPathFilename_, FileSize_):
        self.__FullPathFilename = FullPathFilename_
        self.__FileSize = FileSize_
      
      def __lt__(self, other):
        return (self.__FileSize &lt; other.__FileSize)
      
      def ToRow_NameAndSize(self, SepareAt = 100):
        FullPathStr = self.GetFilename()
        if len(FullPathStr) &gt; SepareAt:
          FullPathStr = FullPathStr[len(FullPathStr)-SepareAt:]
        while len(FullPathStr) &lt; SepareAt:
          FullPathStr+= " "
        return FullPathStr + " : " + str(self.GetFileSize()/1024) + 'k'

      def GetFilename(self):
        return self.__FullPathFilename
      
      def GetFileSize(self):
        return self.__FileSize

    def GetBiggestFileList(SepareAt = 110, MaxNumFilesInReport = 150):
      lAllFilesListIncludingSubDirs = misc.search_files.getAllFilesRecursively(['*.*'], '.')
      
      TotalDiskSpace = 0
      AllFileInfo = []
      
      for file in lAllFilesListIncludingSubDirs:
        try:
          lFileSize = os.path.getsize(file)
          TotalDiskSpace += lFileSize
          AllFileInfo.append( FileInfo(file, lFileSize) )
        #@tag Give a better output of why the file exception occurred
        #except Exception as inst:
        except Exception:
          print ("Error! " + file)
      
      AllFileInfo.sort()
      
      if( len(AllFileInfo)&gt;MaxNumFilesInReport ):
        subAllFileInfo = AllFileInfo[-MaxNumFilesInReport:]
      else:
        subAllFileInfo = AllFileInfo
      
      Report = ''
      Report+= 'Total size: ' + str(TotalDiskSpace/1024) + "k\n"
      for lFileInfo in subAllFileInfo:
        Report += str(lFileInfo.ToRow_NameAndSize(SepareAt)) + "\n"
      
      return Report

    if __name__ == '__main__':
      print (GetBiggestFileList())

## Example

Here is the result of launching the command in c:\windows to find out which files take the most space in the OS.

    python get_space_hoggers_report.py | tee report.txt

And here is the result:

    Total size: 18528928k
    orms\9c6fe9d44d22834993e9aa23cc9dc272\System.Windows.Forms.ni.dll : 12139k
    31bf3856ad364e35_6.0.6001.18000_none_c0a3fbb5ef29fe27\Mahjong.dll : 12261k
    31bf3856ad364e35_6.0.6002.18005_none_c28f74c1ec4bc973\Mahjong.dll : 12261k
    orms\17e020ae92d7fab33bcc1c98b25019d0\System.Windows.Forms.ni.dll : 12701k
    Entity\642a7b3d47828fb0070a55cfeb58f42b\System.Data.Entity.ni.dll : 12962k
    load\41bec7591f57a2b41248a2c1d4189ab0\Windows6.0-KB944036-x86.cab : 13073k
    c:\Windows\Fonts\gulim.ttc                                        : 13207k
    6ad364e35_6.0.6000.16386_none_4355a8715fa423d5_gulim.ttc_7c526737 : 13207k
    m_31bf3856ad364e35_6.0.6000.16386_none_4355a8715fa423d5\gulim.ttc : 13207k
    s\System32\DriverStore\FileRepository\nvdj.inf_d1096b58\nvcpl.dll : 13234k
    s\System32\DriverStore\FileRepository\nvdj.inf_e166b159\nvcpl.dll : 13234k
    s\System32\DriverStore\FileRepository\nvdj.inf_f4eaea07\nvcpl.dll : 13234k
    a_31bf3856ad364e35_6.0.6001.18000_none_03ed68ae2c4994ef\dicjp.bin : 13259k
    c:\Windows\System32\xlivefnt.dll                                  : 13322k
    c:\Windows\System32\nvcpl.dll                                     : 13363k
    c:\Windows\Fonts\simsun.ttc                                       : 13424k
    ad364e35_6.0.6000.16386_none_f8d25d0e72c3c090_simsun.ttc_eba56c14 : 13424k
    _31bf3856ad364e35_6.0.6000.16386_none_f8d25d0e72c3c090\simsun.ttc : 13424k
    d_31bf3856ad364e35_6.0.6000.16386_none_770bd33f8d44346e\ehcir.ird : 13575k
    ache$\Managed\00002109030000000000000000F01FEC\12.0.4518\OART.DLL : 13819k
    c:\Windows\System32\xlive.dll                                     : 13976k
    wo#\b89f584d5b315c16d4e57e747158cb69\PresentationFramework.ni.dll : 13992k
    wo#\0832f9155d800cb802e70409447c1128\PresentationFramework.ni.dll : 13993k
    0319_32\mscorlib\246f1a5abb686b9dcdf22d3505b08cea\mscorlib.ni.dll : 14078k
    c:\Windows\Fonts\msjhbd.ttf                                       : 14169k
    ad364e35_6.0.6000.16386_none_5c79d760afbbb312_msjhbd.ttf_176cee86 : 14169k
    _31bf3856ad364e35_6.0.6000.16386_none_5c79d760afbbb312\msjhbd.ttf : 14169k
    c:\Windows\Logs\CBS\CBS.log                                       : 14280k
    e$\Managed\00002109030000000000000000F01FEC\12.0.4518\XL12CNV.EXE : 14330k
    _31bf3856ad364e35_6.0.6000.16386_none_0c8ed16bb707d3be\msyhbd.ttf : 14341k
    c:\Windows\Fonts\msyhbd.ttf                                       : 14343k
    ad364e35_6.0.6002.18005_none_10b10c73b114afde_msyhbd.ttf_16e5cd4d : 14343k
    _31bf3856ad364e35_6.0.6002.18005_none_10b10c73b114afde\msyhbd.ttf : 14343k
    c:\Windows\Fonts\msjh.ttf                                         : 14368k
    56ad364e35_6.0.6000.16386_none_6309f686e329e15f_msjh.ttf_ea675e5c : 14368k
    ei_31bf3856ad364e35_6.0.6000.16386_none_6309f686e329e15f\msjh.ttf : 14368k
    c:\Windows\Fonts\msyh.ttf                                         : 14691k
    ei_31bf3856ad364e35_6.0.6000.16386_none_389c8034332e39c5\msyh.ttf : 14691k
    c:\Windows\IME\IMEJP10\DICTS\IMJPST.DIC                           : 14726k
    _31bf3856ad364e35_6.0.6000.16386_none_7e4e5681ddf0010b\IMJPST.DIC : 14726k
    c:\Windows\Installer\1aac20a.msp                                  : 14834k
    c:\Windows\System32\nvoglv32.dll                                  : 14878k
    ystem32\DriverStore\FileRepository\nvdj.inf_59384ced\nvoglv32.dll : 14878k
    c:\Windows\Fonts\simsunb.ttf                                      : 15045k
    d364e35_6.0.6000.16386_none_8ec3c7fa1f04c342_simsunb.ttf_08f71e3f : 15045k
    31bf3856ad364e35_6.0.6000.16386_none_8ec3c7fa1f04c342\simsunb.ttf : 15045k
    c:\Windows\Installer\24fce6d.msp                                  : 15342k
    c:\Windows\IME\IMETC10\DICTS\IMTCS.IMD                            : 15444k
    y_31bf3856ad364e35_6.0.6000.16386_none_8c1c51f402c169d0\IMTCS.IMD : 15444k
    c:\Windows\System32\imageres.dll                                  : 15450k
    364e35_6.0.6000.16386_none_da86e136fafaf563_imageres.dll_44f44625 : 15450k
    1bf3856ad364e35_6.0.6000.16386_none_da86e136fafaf563\imageres.dll : 15450k
    1FEC\12.0.4518\msmdlocal.dll.5DF9D670_534C_4AB2_B0C6_FF0B0C448C29 : 15489k
    93892-1000\65AE474ADBD51814280308A67426AEF7\6.2.7000\Combi.04.psi : 15611k
    c:\Windows\Fonts\batang.ttc                                       : 15883k
    ad364e35_6.0.6000.16386_none_b5b2ca1d695fce16_batang.ttc_949601ce : 15883k
    _31bf3856ad364e35_6.0.6000.16386_none_b5b2ca1d695fce16\batang.ttc : 15883k
    ndows\System32\spool\drivers\w32x86\PCC\prnhp001.inf_2ade4966.cab : 16103k
    c:\Windows\ehome\ehcir.ird                                        : 16170k
    d_31bf3856ad364e35_6.0.6000.16663_none_771e77eb8d36a7fc\ehcir.ird : 16170k
    d_31bf3856ad364e35_6.0.6000.20804_none_77e9f66ea622b69e\ehcir.ird : 16170k
    d_31bf3856ad364e35_6.0.6001.18043_none_791a56698a4d010b\ehcir.ird : 16170k
    d_31bf3856ad364e35_6.0.6001.22147_none_79a7f45ca3670631\ehcir.ird : 16170k
    d_31bf3856ad364e35_6.0.6002.18005_none_7b2e0e478751108e\ehcir.ird : 16170k
    c:\Windows\Fonts\meiryo.ttc                                       : 16318k
    ad364e35_6.0.6002.18130_none_76259f2c44aeed75_meiryo.ttc_ab0401d6 : 16318k
    _31bf3856ad364e35_6.0.6000.16945_none_72531e3e4a65a4dd\meiryo.ttc : 16318k
    _31bf3856ad364e35_6.0.6000.21148_none_72df94096380c3ee\meiryo.ttc : 16318k
    _31bf3856ad364e35_6.0.6001.18349_none_743d5e0c47889b2a\meiryo.ttc : 16318k
    _31bf3856ad364e35_6.0.6001.22550_none_74b32a3760b66ffd\meiryo.ttc : 16318k
    _31bf3856ad364e35_6.0.6002.18130_none_76259f2c44aeed75\meiryo.ttc : 16318k
    _31bf3856ad364e35_6.0.6002.22252_none_769b9cb35ddaf7cf\meiryo.ttc : 16318k
    c:\Windows\System32\wbem\Logs\WMITracing.log                      : 16384k
    c:\Windows\System32\config\COMPONENTS.SAV                         : 16452k
    Cache$\Managed\00002109030000000000000000F01FEC\12.0.4518\MSO.DLL : 16475k
    c:\Windows\Fonts\meiryob.ttc                                      : 16757k
    d364e35_6.0.6002.18130_none_cf13a97974e4cf1c_meiryob.ttc_d9ebd964 : 16757k
    31bf3856ad364e35_6.0.6000.16945_none_cb41288b7a9b8684\meiryob.ttc : 16757k
    31bf3856ad364e35_6.0.6000.21148_none_cbcd9e5693b6a595\meiryob.ttc : 16757k
    31bf3856ad364e35_6.0.6001.18349_none_cd2b685977be7cd1\meiryob.ttc : 16757k
    31bf3856ad364e35_6.0.6001.22550_none_cda1348490ec51a4\meiryob.ttc : 16757k
    31bf3856ad364e35_6.0.6002.18130_none_cf13a97974e4cf1c\meiryob.ttc : 16757k
    31bf3856ad364e35_6.0.6002.22252_none_cf89a7008e10d976\meiryob.ttc : 16757k
    000\65AE474ADBD51814280308A67426AEF7\6.2.7000\Le_Petit_Druide.psi : 16829k
    Model\52cbaee4e94489731096be5ecc320958\System.ServiceModel.ni.dll : 16996k
    che$\Managed\00002109030000000000000000F01FEC\12.0.4518\WWLIB.DLL : 17073k
    wo#\7f91eecda3ff7ce478146b6458580c98\PresentationFramework.ni.dll : 17216k
    che$\Managed\00002109030000000000000000F01FEC\12.0.4518\EXCEL.EXE : 17471k
    Model\250b525aa8c17327216e102569c0d766\System.ServiceModel.ni.dll : 17499k
    c:\Windows\Installer\fe5e2c.msi                                   : 17755k
    c:\Windows\System32\WDI\LogFiles\BootCKCL.etl                     : 17792k
    c:\Windows\System32\IME\IMETC10\applets\MSHWCHTR.dll              : 19522k
    1bf3856ad364e35_6.0.6001.18000_none_fb2914a7fb7f05d4\MSHWCHTR.dll : 19522k
    1bf3856ad364e35_6.0.6002.18005_none_fd148db3f8a0d120\MSHWCHTR.dll : 19522k
    1bf3856ad364e35_6.0.6001.18000_none_fd48368c658afbaa\mshwchtr.dll : 19522k
    ache$\Managed\68AB67CA7DA73301B7449A0300000010\9.3.0\AcroRd32.dll : 19957k
    _msige52\program files\Google\Google Earth\client\googleearth.exe : 20428k
    c:\Windows\System32\winevt\Logs\Security.evtx                     : 20484k
    c:\Windows\System32\winevt\Logs\System.evtx                       : 20484k
    c:\Windows\Installer\1aac08e.msp                                  : 20889k
    c:\Windows\System32\IME\IMEJP10\APPLETS\mshwjpnr.dll              : 20959k
    1bf3856ad364e35_6.0.6000.16386_none_29bd61de3dbf60e5\mshwjpnr.dll : 20959k
    1bf3856ad364e35_6.0.6001.18000_none_03ed68ae2c4994ef\mshwjpnr.dll : 20959k
    c:\Windows\System32\IME\imekr8\applets\mshwkorr.dll               : 21316k
    1bf3856ad364e35_6.0.6000.16386_none_4e1eb5b4af3fbd40\mshwkorr.dll : 21316k
    1bf3856ad364e35_6.0.6001.18000_none_03ed2a082c4a1514\mshwkorr.dll : 21316k
    1bf3856ad364e35_6.0.6001.18000_none_fd484d54658ae209\mshwchsr.dll : 21448k
    c:\Windows\System32\wbem\repository\OBJECTS.DATA                  : 22528k
    c:\Windows\Fonts\ARIALUNI.TTF                                     : 22730k
    c:\Windows\Speech\Engines\SR\en-US\t1033.ngr                      : 22858k
    _31bf3856ad364e35_6.0.6000.16386_en-us_cbfb04a3abf30016\t1033.ngr : 22858k
    e52\program files\Google\Google Earth\plugin\googleearth_free.dll : 22880k
    naged\00002109F10090400000000000F01FEC\12.0.4518\NLSDATA.DLL_1033 : 23818k
    0002109030000000000000000F01FEC\12.0.4518\INSTALLED_RESOURCES.XSS : 24288k
    c:\Windows\inf\setupapi.dev.log                                   : 24433k
    c:\Windows\System32\config\RegBack\SYSTEM.OLD                     : 25552k
    c:\Windows\Fonts\mingliu.ttc                                      : 26851k
    31bf3856ad364e35_6.0.6000.16386_none_b8e3a7d58b1249ca\mingliu.ttc : 26851k
    c:\Windows\Speech\Engines\SR\en-US\l1033.ngr                      : 27833k
    _31bf3856ad364e35_6.0.6000.16386_en-us_cbfb04a3abf30016\l1033.ngr : 27833k
    3856ad364e35_6.0.6001.18000_none_062b7e7afe71e492\PurblePlace.dll : 27994k
    3856ad364e35_6.0.6002.18005_none_0816f786fb93afde\PurblePlace.dll : 27994k
    s_31bf3856ad364e35_6.0.6001.18000_none_74d4a1cd7e673a2e\Chess.dll : 28321k
    s_31bf3856ad364e35_6.0.6002.18005_none_76c01ad97b89057a\Chess.dll : 28321k
    1bf3856ad364e35_6.0.6000.16386_none_0d44c2d7a6e22754\M1033DSK.CSD : 29099k
    c:\Windows\System32\config\RegBack\COMPONENTS.OLD                 : 31148k
    c:\Windows\System32\mrt.exe                                       : 31710k
    c:\Windows\Fonts\mingliub.ttc                                     : 32999k
    364e35_6.0.6000.16386_none_c6eae5a23b4a0d1e_mingliub.ttc_b8743970 : 32999k
    1bf3856ad364e35_6.0.6000.16386_none_c6eae5a23b4a0d1e\mingliub.ttc : 32999k
    32\DriverStore\FileRepository\nvdj.inf_05fd020f\NvCplSetupInt.exe : 37308k
    93892-1000\65AE474ADBD51814280308A67426AEF7\6.2.7000\Combi.01.psi : 38261k
    32\DriverStore\FileRepository\nvdj.inf_59384ced\NvCplSetupInt.exe : 39343k
    c:\Windows\ehome\en-US\Intro.wmv                                  : 45166k
    _31bf3856ad364e35_6.0.6000.16386_en-us_35933539ffce9bad\Intro.wmv : 45166k
    c:\Windows\System32\config\RegBack\SOFTWARE.OLD                   : 45532k
    5_6.0.6000.16386_none_3264f7ee9b82c6e1\Jewels of Caribbean.dvr-ms : 45830k
    856ad364e35_6.0.6000.16386_none_3264f7ee9b82c6e1\Apollo 13.dvr-ms : 48902k
    c:\Windows\Installer\4dac3f.msp                                   : 49713k
    f3856ad364e35_6.0.6000.16386_none_3264f7ee9b82c6e1\Vertigo.dvr-ms : 51846k
    c:\Windows\Speech\Engines\SR\en-GB\l2057.ngr                      : 55999k
    _31bf3856ad364e35_6.0.6000.16386_en-gb_857893b11436ae5f\l2057.ngr : 55999k
    c:\Windows\IME\IMESC5\DICTS\PINTLGT.IMD                           : 65408k
    31bf3856ad364e35_6.0.6000.16386_none_b4aaff4041e28397\PINTLGT.IMD : 65408k
    c:\Windows\Logs\CBS\CBS.persist.log                               : 68341k
    c:\Windows\SoftwareDistribution\DataStore\DataStore.edb           : 77832k
    c:\Windows\Installer\13ea212.msp                                  : 99335k
    crosoft.NET\Framework\v4.0.30319\SetupCache\Client\netfx_core.mzz : 113164k
    c:\Windows\winsxs\ManifestCache\6.0.6002.18005_001c11ba_blobs.bin : 188770k
    c:\Windows\Installer\1aac1e6.msp                                  : 335018k

You can see that by clearing the last two files (which seem to just be cache files that were not deleted for whatever reason) one would free ~500Mb.

I bundled the Python script compiled as a win32 binary. It is for my own personal need when I am on a (windows) computer in a lab which does not have Python installed and I need to hunt down a few big files.

## Example on Linux

    Total size: 3132993k
    /usr/lib/libpython2.6.so.1                                   : 2340k
    /usr/lib/libpython2.6.so.1.0                                 : 2340k
    /usr/lib/python2.6/config/libpython2.6.so                    : 2340k
    /usr/lib/dri/r128_dri.so                                     : 2342k
    /usr/lib/dri/i810_dri.so                                     : 2350k
    apt/archives/xserver-xorg-core_2%3a1.7.6-2ubuntu7.2_i386.deb : 2352k
    /var/cache/apt/archives/evolution_2.28.3-0ubuntu10_i386.deb  : 2370k
    /usr/lib/dri/savage_dri.so                                   : 2386k
    /usr/lib/dri/tdfx_dri.so                                     : 2394k
    /usr/bin/python3.1                                           : 2407k
    /usr/lib/dri/sis_dri.so                                      : 2410k
    /usr/lib/dri/mach64_dri.so                                   : 2414k
    /usr/lib/openoffice/basis3.2/program/libchartcontrollerli.so : 2420k
    /usr/lib/dri/r600_dri.so                                     : 2430k
    /usr/lib/dri/mga_dri.so                                      : 2442k
    /var/cache/apt/archives/libgtk2.0-0_2.20.1-0ubuntu1_i386.deb : 2455k
    /usr/lib/dri/radeon_dri.so                                   : 2455k
    /usr/lib/openoffice/basis3.2/program/libscfiltli.so          : 2467k
    /usr/lib/dri/r200_dri.so                                     : 2489k
    /usr/lib/dri/r300_dri.so                                     : 2491k
    /usr/lib/openoffice/basis3.2/program/libfrmli.so             : 2502k
    le-content/Ubuntu_Free_Culture_Showcase/UbuntuIsHumanity.ogv : 2503k
    /usr/lib/mono/2.0/mscorlib.dll                               : 2508k
    /usr/lib/vmware-tools/configurator/XOrg/7.6/vmwgfx_dri.so    : 2522k
    /usr/lib/vmware-tools/configurator/XOrg/7.5/vmwgfx_dri.so    : 2535k
    /var/lib/aspell/en-common.rws                                : 2589k
    /usr/lib/aspell/en-common.rws                                : 2589k
    /usr/lib/dri/i915_dri.so                                     : 2610k
    /usr/lib/openoffice/basis3.2/program/libfwkli.so             : 2655k
    /usr/lib/dri/i965_dri.so                                     : 2701k
    /usr/lib/vmware-tools/configurator/XOrg/7.5_64/vmwgfx_dri.so : 2706k
    /usr/lib/vmware-tools/configurator/XOrg/7.6_64/vmwgfx_dri.so : 2730k
    /var/lib/defoma/gs.d/dirs/fonts/UnDotumBold.ttf              : 2744k
    /lib/defoma/x-ttcidfont-conf.d/dirs/TrueType/UnDotumBold.ttf : 2744k
    /usr/share/fonts/truetype/unfonts/UnDotumBold.ttf            : 2744k
    r/cache/apt/archives/libgl1-mesa-dri_7.7.1-1ubuntu3_i386.deb : 2799k
    /usr/lib/openoffice/basis3.2/program/libtkli.so              : 2880k
    usr/lib/vmware-tools/lib32/libconf/gtk-2.0/modules/libgail.a : 2894k
    /boot/grub/unicode.pf2                                       : 2898k
    /usr/share/grub/unicode.pf2                                  : 2898k
    /usr/lib/libc.a                                              : 2960k
    /var/cache/apt/archives/emacs23_23.1+1-4ubuntu7_i386.deb     : 2966k
    /home/david/.dropbox-dist/libwx_gtk2ud_core-2.8.so.0         : 2968k
    /usr/lib/xen/libc.a                                          : 3063k
    ink/PxpMisc/CodeTests/c++/monitor_memory_allocation/test.ncb : 3147k
    cache/apt/archives/evolution-common_2.28.3-0ubuntu10_all.deb : 3157k
    us.archive.ubuntu.com_ubuntu_dists_lucid_main_source_Sources : 3169k
    /usr/lib/gcc/i486-linux-gnu/4.4/libgcc.a                     : 3183k
    /usr/lib/openoffice/basis3.2/program/libsvxli.so             : 3294k
    /usr/lib/perl5/auto/Gtk2/Gtk2.so                             : 3323k
    /usr/lib/libpython3.1.a                                      : 3361k
    /apt/archives/gnome-do-plugins_0.8.2.1+dfsg-2ubuntu1_all.deb : 3371k
    /usr/lib/libgtkmm-2.4.so.1.1.0                               : 3389k
    /usr/lib/libgtkmm-2.4.so.1                                   : 3389k
    /usr/lib/libgucharmap.so.7                                   : 3442k
    /usr/lib/libgucharmap.so.7.0.0                               : 3442k
    /var/cache/apt/archives/python3.1_3.1.2-0ubuntu2_i386.deb    : 3463k
    /usr/share/hplip/data/pcl/colorcal1_450.pcl.gz               : 3506k
    ives/openoffice.org-style-human_1%3a3.2.0-7ubuntu4.1_all.deb : 3584k
    /var/lib/defoma/gs.d/dirs/fonts/UnBatang.ttf                 : 3592k
    var/lib/defoma/x-ttcidfont-conf.d/dirs/TrueType/UnBatang.ttf : 3592k
    /usr/share/fonts/truetype/unfonts/UnBatang.ttf               : 3592k
    /var/cache/apt/archives/humanity-icon-theme_0.5.2.1_all.deb  : 3602k
    /usr/lib/libflite_cmu_us_kal16.so.1                          : 3617k
    /usr/lib/libflite_cmu_us_kal16.so.1.3                        : 3617k
    /usr/lib/xen/libc_pic.a                                      : 3672k
    /var/cache/apt/archives/libc6_2.11.1-0ubuntu7.1_i386.deb     : 3690k
    /usr/lib/openoffice/basis3.2/program/libcuili.so             : 3886k
    /cache/apt/archives/libavcodec52_4%3a0.5.1-1ubuntu1_i386.deb : 3904k
    /usr/lib/libgtk-x11-2.0.so.0                                 : 3916k
    /usr/lib/libgtk-x11-2.0.so.0.2000.1                          : 3916k
    /usr/lib/libflite_cmu_time_awb.so.1                          : 3925k
    /usr/lib/libflite_cmu_time_awb.so.1.3                        : 3925k
    /vmlinuz.old                                                 : 3935k
    /boot/vmlinuz-2.6.32-21-generic                              : 3935k
    /boot/vmlinuz-2.6.32-22-generic                              : 3935k
    /var/lib/defoma/gs.d/dirs/fonts/UnBatangBold.ttf             : 3977k
    lib/defoma/x-ttcidfont-conf.d/dirs/TrueType/UnBatangBold.ttf : 3977k
    /usr/share/fonts/truetype/unfonts/UnBatangBold.ttf           : 3977k
    /var/lib/mlocate/mlocate.db                                  : 3981k
    r/lib/vmware-tools/lib32/libgtkmm-2.4.so.1/libgtkmm-2.4.so.1 : 4057k
    ache/apt/archives/gnome-screensaver_2.30.0-0ubuntu2_i386.deb : 4078k
    /tmp/VMwareDnD/c3f93485/scripts/sa_utils/dist/library.zip    : 4115k
    /usr/lib/openoffice/basis3.2/program/libsvtli.so             : 4124k
    /usr/lib/openoffice/basis3.2/program/libsfxli.so             : 4257k
    b/vmware-tools/lib32/libgtk-x11-2.0.so.0/libgtk-x11-2.0.so.0 : 4315k
    /usr/lib/openoffice/basis3.2/program/libvclli.so             : 4336k
    /usr/lib/vmware-tools/icu/icudt38l.dat                       : 4496k
    t/archives/openoffice.org-calc_1%3a3.2.0-7ubuntu4.1_i386.deb : 4538k
    /usr/lib/openoffice/basis3.2/program/libooxli.so             : 4627k
    /usr/lib/openoffice/basis3.2/program/libxoli.so              : 4634k
    b/vmware-tools/lib64/libgtk-x11-2.0.so.0/libgtk-x11-2.0.so.0 : 4673k
    /usr/lib/libsmbclient.so.0                                   : 4698k
    /var/cache/apt/archives/libc6-dev_2.11.1-0ubuntu7.1_i386.deb : 4726k
    /var/cache/apt/archives/g++-4.4_4.4.3-4ubuntu5_i386.deb      : 4833k
    /usr/lib/openoffice/basis3.2/program/libwriterfilterli.so    : 4839k
    /usr/share/fonts/truetype/wqy/wqy-microhei.ttc               : 5056k
    /usr/share/icons/hicolor/icon-theme.cache                    : 5181k
    r/lib/vmware-tools/lib64/libgtkmm-2.4.so.1/libgtkmm-2.4.so.1 : 5247k
    /usr/lib/i686/cmov/libavcodec.so.52                          : 5328k
    /usr/lib/i686/cmov/libavcodec.so.52.20.1                     : 5328k
    /usr/lib/libavcodec.so.52                                    : 5336k
    /usr/lib/libavcodec.so.52.20.1                               : 5336k
    /var/lib/openoffice/basis3.2/program/services.rdb            : 5408k
    /usr/lib/openoffice/basis3.2/program/services.rdb            : 5408k
    /cache/apt/archives/vim-runtime_2%3a7.2.330-1ubuntu3_all.deb : 5572k
    /usr/share/openoffice/basis3.2/share/config/images_human.zip : 5827k
    /usr/lib/openoffice/basis3.2/program/libsdli.so              : 5946k
    /usr/bin/net.samba3                                          : 5949k
    archives/openoffice.org-writer_1%3a3.2.0-7ubuntu4.1_i386.deb : 5983k
    /etc/alternatives/ttf-japanese-gothic.ttf                    : 6088k
    /usr/share/fonts/truetype/ttf-japanese-gothic.ttf            : 6088k
    /usr/share/fonts/truetype/takao/TakaoPGothic.ttf             : 6088k
    /usr/lib/openoffice/basis3.2/program/offapi.rdb              : 6368k
    /usr/share/icons/gnome/icon-theme.cache                      : 7081k
    ar/cache/apt/archives/libflite1_1.3-release-2build1_i386.deb : 7103k
    aves_via_symlink/PxpMisc/CodeTests/c++/win_os_layer/test.ncb : 7243k
    /initrd.img                                                  : 7778k
    /boot/initrd.img-2.6.32-22-generic                           : 7778k
    /initrd.img.old                                              : 7790k
    /boot/initrd.img-2.6.32-21-generic                           : 7790k
    /home/david/.dropbox-dist/library.zip                        : 7867k
    hive.ubuntu.com_ubuntu_dists_lucid_main_binary-i386_Packages : 8396k
    /usr/lib/libgs.so.8                                          : 8487k
    /usr/lib/libgs.so.8.71                                       : 8487k
    /usr/lib/openoffice/basis3.2/program/libsvxcoreli.so         : 9191k
    /var/cache/cups/ppds.dat                                     : 9230k
    /usr/lib/openoffice/basis3.2/program/libscli.so              : 9584k
    he/apt/archives/linux-headers-2.6.32-22_2.6.32-22.36_all.deb : 9636k
    /usr/lib/openoffice/basis3.2/program/libswli.so              : 11390k
    /opt/google/chrome/libgcflashplayer.so                       : 11511k
    avid/.mozilla/firefox/g9eit4ej.default/urlclassifier3.sqlite : 12472k
    /usr/lib/xulrunner-1.9.2.3/libxul.so                         : 13332k
    rchive.ubuntu.com_ubuntu_dists_lucid_universe_source_Sources : 13563k
    /var/lib/apt-xapian-index/index.1/termlist.DB                : 13648k
    /var/cache/apt/srcpkgcache.bin                               : 13956k
    /var/cache/apt/pkgcache.bin                                  : 13976k
    /usr/lib/firefox-3.6.3/libxul.so                             : 14113k
    /usr/lib/libwebkit-1.0.so.2                                  : 14502k
    /usr/lib/libwebkit-1.0.so.2.17.2                             : 14502k
    /usr/lib/libicudata.so.42.1                                  : 15636k
    /usr/lib/libicudata.so.42                                    : 15636k
    /archives/openoffice.org-common_1%3a3.2.0-7ubuntu4.1_all.deb : 17854k
    ar/cache/apt/archives/emacs23-common_23.1+1-4ubuntu7_all.deb : 20145k
    .ubuntu.com_ubuntu_dists_lucid_universe_binary-i386_Packages : 26179k
    t/archives/openoffice.org-core_1%3a3.2.0-7ubuntu4.1_i386.deb : 27214k
    /var/cache/apt/archives/freepats_20060219-1_all.deb          : 28285k
    archives/linux-image-2.6.32-22-generic_2.6.32-22.36_i386.deb : 30204k
    pbox/misc_saves_via_symlink/PxpMisc/Backups/cygwin_backup.7z : 30643k
    /var/lib/apt-xapian-index/index.1/postlist.DB                : 40624k

## Python Compile To Exe

On a side note [py2exe](http://www.py2exe.org) is an amazing tool that works quite well. It takes about 5 min to download, install and compile your script into a standalone windows application. For your reference here is the small script that uses py2exe:

    #Launch with: python27 make_bin.py py2exe
    from distutils.core import setup
    import py2exe

    setup(
        console=['get_space_hoggers_report.py'],
        options={"py2exe":{"bundle_files":1}}    
        )

The script creates the standalone .exe of the next section. [To be accurate I used py2exe-0.6.9.win64](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win64-py2.7.amd64.exe/download) but without the 'bundle_files' option because it is not yet supported for win64 :(. Works quite well on win32 though.

## Download

Standalone win64: [get_space_hoggers_report_win64bin.zip](../../static/get_space_hoggers_report_win64bin.zip)

Source (same as copy/paste above): [get_space_hoggers_report.py.zip](../../static/get_space_hoggers_report.py.zip)


Happy hunting!
