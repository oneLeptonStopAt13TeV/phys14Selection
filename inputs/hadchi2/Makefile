
ROOTCFLAGS    = $(shell root-config --cflags)
ROOTLIBS      = $(shell root-config --libs) -lMinuit2 -lGenVector

CXX           = g++
CXXFLAGS      = -std=c++0x
CXXFLAGS     += -O -Wall -fPIC $(DEFINES) -Wno-unused-result -Wshadow
CXXFLAGS     += $(ROOTCFLAGS) -I./

LD            = g++ 
LDFLAGS       = -g -O3 -Wall -fPIC -Wl,-undefined,error
LDFLAGS      += $(ROOTLIBS)  -lEG -lTMVA 

SOFLAGS       = -shared
LIBS          =  

# Uncomment this line if you want to use a script to parse & colorize gcc output
# (You can also export this variable from your bashrc)
#GCCPARSER     = 2>&1 | python ~/littleScripts/colorGcc.py

#------------------------------------------------------------------------------

lib: libHadChi2.so

clean:
	@echo "Cleaning..."
	@rm -f *.so

#------------------------------------------------------------------------------

#libHadChi2.so: Resolution.cc
libHadChi2.so: chi2.cc
	$(LD) $(CXXFLAGS) $(LDFLAGS) $(SOFLAGS) -o $@ $< $(LIBS) $(GCCPARSER)
