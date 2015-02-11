   
from math        import sqrt, cos
from inputs.MT2W import MT2W

class Variables() :

    branchesForVariables = [ "met_pt", "met_phi" ]
    
    def computeVariables(self,event) :
        self.MT   = self.computeMT(event)
        self.MT2W = MT2W.computeMT2W(self.selectedJets, self.selectedLeptons[0], event.met_pt, event.met_phi)

    # ########
    # #  MT  # 
    # ########

    def computeMT(self,event) :
        
        leadingLeptonPt = self.selectedLeptons[0].pT
        deltaPhi = self.selectedLeptons[0].phi - event.met_phi
        
        MT = sqrt(2 * leadingLeptonPt * event.met_pt * (1 - cos(deltaPhi) ))
        
        return MT
