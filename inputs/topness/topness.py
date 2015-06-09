import ctypes
import os

lib = os.path.dirname(os.path.realpath(__file__))+'/libTopness.so'
Topnesswrap = ctypes.CDLL(lib)
Topnesscompute_ = Topnesswrap.topnessMinimization

# Arguments types
Topnesscompute_.argtypes = (
  ctypes.c_double lep_pt, ctypes.c_double lep_eta, ctypes.c_double lep_phi, ctypes.c_double lep_e,
  ctypes.c_double bjet1_pt, ctypes.c_double bjet1_eta, ctypes.c_double bjet1_phi, ctypes.c_double bjet1_e,
  ctypes.c_double bjet2_pt, ctypes.c_double bjet2_eta, ctypes.c_double bjet2_phi, ctypes.c_double bjet2_e,
  ctypes.c_double met, ctypes.c_double met_phi)

# Return type
Topnesscompute_.restype = ctypes.c_float


def computeTopness( lepton, bjet1, bjet2,  MET, METphi):
    
    result = Topnesscompute_(
   	ctypes.double(lepton.pT),  ctypes.double(lepton.eta),  ctypes.double(lepton.phi),  ctypes.double(lepton.E),
   	ctypes.double(bjet1.pT) ,  ctypes.double(bjet1.eta) ,  ctypes.double(bjet1.phi) ,  ctypes.double(bjet1.E),
   	ctypes.double(bjet2.pT) ,  ctypes.double(bjet2.eta) ,  ctypes.double(bjet2.phi) ,  ctypes.double(bjet2.E),
	ctypes.double(met), ctypes.double(met_phi))
    
    return float(result)
