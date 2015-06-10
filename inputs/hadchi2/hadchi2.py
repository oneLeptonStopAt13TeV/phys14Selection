import ctypes
import os
from ROOT import TLorentzVector

lib = os.path.dirname(os.path.realpath(__file__))+'/libHadChi2.so'
chi2wrap = ctypes.CDLL(lib)
Chi2compute_ = chi2wrap.ComputeChi2

# Arguments types
Chi2compute_.argtypes = (ctypes.c_int, 
  ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_bool))

# Return type
Chi2compute_.restype = ctypes.c_double

def computeHadChi2 (jets):
    nJets = len(jets)
    jetsDoubleArray = ctypes.c_double * nJets
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

    
    result = Chi2compute_( ctypes.c_int(nJets), 
                          jetsDoubleArray(*jetsPt), jetsDoubleArray(*jetsPhi), jetsDoubleArray(*jetsEta), jetsDoubleArray(*jetsEnergy), jetsBoolArray(*jetsBTagged))
    return long(result)
