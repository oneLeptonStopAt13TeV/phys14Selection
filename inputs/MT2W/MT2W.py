import ctypes
import os

lib = os.path.dirname(os.path.realpath(__file__))+'/libMT2W.so'
MT2Wwrap = ctypes.CDLL(lib)

MT2Wwrap.computeMT2W.argtypes = (ctypes.c_int, 
                             ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), 
                             ctypes.POINTER(ctypes.c_bool),
                             ctypes.c_float,                 ctypes.c_float,                 ctypes.c_float,                 ctypes.c_float, 
                             ctypes.c_float,                 ctypes.c_float)

MT2Wcompute_ = MT2Wwrap.computeMT2W

def computeMT2W(jets, lepton, MET, METphi):
    global MT2Wwrap
    
    nJets = len(jets)
    jetsFloatArray = ctypes.c_float * nJets
    jetsBoolArray  = ctypes.c_bool * nJets
    jetsPt      = [ ]
    jetsPhi     = [ ]
    jetsEta     = [ ] 
    jetsEnergy  = [ ]
    jetsBTagged = [ ]
    for jet in jets :
        jetsPt     .append(jet.pT)
        jetsPhi    .append(jet.phi)
        jetsEta    .append(jet.eta)
        jetsEnergy .append(jet.E)
        jetsBTagged.append(jet.bTag)

    result = MT2Wcompute_(ctypes.c_int(nJets), 
                          jetsFloatArray(*jetsPt), jetsFloatArray(*jetsPhi), jetsFloatArray(*jetsEta), jetsFloatArray(*jetsEnergy), jetsBoolArray(*jetsBTagged),
                          ctypes.c_float(lepton.pT), ctypes.c_float(lepton.phi), ctypes.c_float(lepton.eta), ctypes.c_float(lepton.E),
                          ctypes.c_float(MET), ctypes.c_float(METphi))

    return float(result)
