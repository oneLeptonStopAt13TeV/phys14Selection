   
from math        import sqrt, cos
from inputs.MT2W import MT2W

class Variables() :

    branchesForVariables = [ "met_pt", "met_phi", "gen_n", "gen_id", "gen_mother_index", "gen_status" ]
    
    def computeVariables(self,event) :
        self.MT   = self.computeMT(event)
        self.HT   = self.computeHT(event)
        if len(self.selectedLeptons)>0:
		self.MT2W = MT2W.computeMT2W(self.selectedJets, self.selectedLeptons[0], event.met_pt, event.met_phi)
        else:
		self.MT2W = 0
	self.numberOfGeneratedLeptons = self.getNumberOfGeneratedLeptons(event)

    # ########
    # #  MT  # 
    # ########

    def computeMT(self,event) :

        leadingLeptonPt = self.selectedLeptons[0].pT if len(self.selectedLeptons)>0 else 0
        deltaPhi = self.selectedLeptons[0].phi - event.met_phi if len(self.selectedLeptons)>0 else 0
        
        MT = sqrt(2 * leadingLeptonPt * event.met_pt * (1 - cos(deltaPhi) ))
        
        return MT

    # ########
    # #  HT  #
    # ########

    def computeHT(self,event) :

        HT = 0

        for jet in self.selectedJets :
            HT += jet.pT

        return HT

    # ###############################
    # # Number of generated leptons #
    # ###############################

    def getNumberOfGeneratedLeptons(self, event) :

        genLeptonsFound = 0;

        n      = event.gen_n
        pdgid  = event.gen_id
        mother = event.gen_mother_index
        status = event.gen_status
        
        for i in range(n) :
            
            if ((abs(pdgid[i]) != 11) and (abs(pdgid[i]) != 13) and (abs(pdgid[i]) != 15)) :
                continue;

            mother_pdgid = pdgid[mother[i]]

            if (abs(mother_pdgid) != 24) :
                continue;

            if (status[i] > 3) :
                continue;

            genLeptonsFound += 1

        return genLeptonsFound


