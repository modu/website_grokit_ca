# C++ Linker Errors Debugging

C++ compilers generally do not produce very helpful error messages (it is part of the training of a C++ code to learn to _interpret_ the error messages -- one needs to understand that the error message is a _symptom_ that can lead to the error and rarely the error itself, except in the most trivial cases). C++ linkers are worse.

I had the really funny error today that the linker could not find a function I knew very well was in the library that I was providing. This is what I was getting from the C++ compiler:

		error LNK2019: unresolved external symbol "public: bool __thiscall imageRead::seqStart(char *,class ATL::CStringT<wchar_t,class StrTraitMFC_DLL<wchar_t,class ATL::ChTraitsCRT<wchar_t> > >)" 

The function outlined was _definitely_ in the library, which was properly linked. I checked 10 times.

## dumpbin.exe to The Rescue

Visual studio comes with the very handy __dumpbin.exe__ utility. It allows one to see the functions inside a _.obj_ or _.lib_ file. It is usually contained in the following directory:

		C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin

Here is [the microsoft help page for the tool](http://support.microsoft.com/kb/177429). Here is the usage that helped me find my problem:

    dumpbin.exe /SYMBOLS foo.lib
    dumpbin.exe /SYMBOLS foo.obj

By using dumpbin and grepping for ‘seqStart’, I got the following:

		public: bool __thiscall imageRead::seqStart(char *,class ATL::CStringT<char,class StrTraitMFC_DLL<char,class ATL::ChTraitsCRT<char> > >))

The linker error indicates that it is looking for the following function:

		public: bool __thiscall imageRead::seqStart(char *,class ATL::CStringT<wchar_t,class StrTraitMFC_DLL<wchar_t,class ATL::ChTraitsCRT<wchar_t> > >)

… which means that the only difference is that the library code somehow generated wchar CString, and the linker is looking for char CString. My guess is that there is a #define somewhere that defines the behavior of CString, and that it was somehow different in the two libraries. I just replaced a few to those CString with std::string and then the linker error disappeared.

