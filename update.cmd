rem python27 "%DTG_ROOT%\app\google_app_engine\appcfg.py" update ws_root
rem python regenerate_webdoc.py
c:\python27\python.exe regenerate_webdoc.py
c:\python27\python.exe "app\google_app_engine\appcfg.py" update ws_root
