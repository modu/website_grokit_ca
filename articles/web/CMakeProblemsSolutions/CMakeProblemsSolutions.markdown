
# Common Problems With CMake and Associated Solutions

## Unknown extension ".c" for file

Sometimes CMake will refuse to compile files that one would think it would automatically know what to do with (e.g. C files):

    CMake Error at cmake-2.8/Modules/CheckSymbolExists.cmake:63 (TRY_COMPILE):
      Unknown extension ".c" for file

        plastimatch/src/uno-2-3-reg/build/CMakeFiles/CMakeTmp/CheckSymbolExists.c

      try_compile() works only for enabled languages.  Currently these are:

        CXX RC

      See project() command to enable other languages.
    Call Stack (most recent call first):
      cmake-2.8/Modules/FindQt4.cmake:763 (CHECK_SYMBOL_EXISTS)
      CMakeLists.txt:50 (FIND_PACKAGE)

The solution is to just add the following in the CMakeLists.txt file:

    ENABLE_LANGUAGE(C)
    
For some reason it might be enabled by default on some platforms... but was not on mine!

## Forcing CMake to compile files of a common extension 'as if' they are .cpp files (source code).

This is a common problem when developping ITK projects. The code is split between .h and .txx files, and by default (at least for me), the generate project files in visual studio would not attempt to compile the .txx files, which would result in the project not working.

Here is a solution to force compilation:

    # Instruct MSVC to compile the .txx files as *source files*
    IF(MSVC)
      SET_SOURCE_FILES_PROPERTIES(
        file1.txx
        file2.txx
        PROPERTIES 
        LANGUAGE "CXX" 
        HEADER_FILE_ONLY FALSE
        COMPILE_FLAGS ""
      )
    ENDIF(MSVC)

... this needs to be done for every .txx files to be compiled.

## Get CMake to use absolute path

Just add the following to the CMakeLists.txt:

    SET(BASEPATH "${CMAKE_SOURCE_DIR}")
    INCLUDE_DIRECTORIES("${BASEPATH}")

...you will then be able use includes like '#include "Core/Log.h"' without having to specify the relative path (which is the _right_ thing to do).

## Install Binaries to A Folder Automatically Under Windows

This is not exactly obvious how to tell CMake that it needs to copy the result binary to a specific folder once the target has been built. There are instructions [on the official wiki](http://www.vtk.org/Wiki/CMake:Install_Commands), but there are a lot of different commands and legacy solutions that no longer work. Here is what worked for me.

    CMAKE_MINIMUM_REQUIRED(VERSION 2.4)
    IF(COMMAND CMAKE_POLICY)
      CMAKE_POLICY(SET CMP0003 NEW)
    ENDIF(COMMAND CMAKE_POLICY)

    set(CMAKE_BUILT_TYPE Debug)

    PROJECT(ImageConverters)

    FIND_PACKAGE(ITK REQUIRED)
    INCLUDE(${ITK_USE_FILE})

    ADD_EXECUTABLE(ic SimpleImageConverter.cxx )
    TARGET_LINK_LIBRARIES(ic ITKIO)

    #See http://www.vtk.org/Wiki/CMake:Install_Commands
    SET(INSTALL_PATH "C:/david/sync/app/BashBins")
    INSTALL(TARGETS ic RUNTIME DESTINATION ${INSTALL_PATH})

This is the _CMakeFiles.txt_ for a small application (_ic.exe_) that converts images from ITK formats to whatever. This will result in a project target called 'install' that automatically copies ic.exe (the output of the project) to "C:/david/sync/app/BashBins", where my bash applications are kept on my windows machine.

The two key lines are:

    SET(INSTALL_PATH "C:/david/sync/app/BashBins")
    INSTALL(TARGETS ic RUNTIME DESTINATION ${INSTALL_PATH})

The only non-obvious thing here is that **ic** is the executable file name.
    
## Resources: useful links when stuck

There is a [tutorial](http://www.cmake.org/cmake/help/cmake_tutorial.html), but in my opinion it is not really good. There is also [a manual](http://www.cmake.org/cmake/help/cmake-2-8-docs.html), which states all the commands but does not go in enough details on how and when to use them.

