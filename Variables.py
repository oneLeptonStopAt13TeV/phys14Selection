from math        import sqrt, cos
from inputs.MT2W import MT2W
#from inputs.topness import topness    

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

    	# ### topness
	# change the way b-jets are choose
        #self.topness = topness.compute(self.selectedLeptons[0], self.selectedJets[0], self.selectedJets[1], event.met_pt, event.met_phi)

	#Chi2
	#M3b
	#ak4_htssm
	#Mlb_leadb
	#dphi_Wlep


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

    # this function is very CPU intensive (40% total time)
    # should be optimzed ?
    
    
    def getNumberOfGeneratedLeptons(self, event) :

        genLeptonsFound = 0;

        n      = event.gen_n
        pdgid  = event.gen_id
        mother = event.gen_mother_index
        status = event.gen_status
       

        #for i in range(n) :

            # put this requirement at the first position
	#    if (status[i] > 3) :
        #        continue;
            
        #    mother_pdgid = pdgid[mother[i]]
	#    if (abs(mother_pdgid) != 24) :
        #        continue;
            
        #    if ((abs(pdgid[i]) != 11) and (abs(pdgid[i]) != 13) and (abs(pdgid[i]) != 15)) :
        #        continue;


        #    genLeptonsFound += 1


	res = [1 for i in range(n) if status[i]<=3 and pdgid[mother[i]] == 24 and ((abs(pdgid[i]) == 11) or (abs(pdgid[i]) == 13) or (abs(pdgid[i]) == 15))]
        return sum(res)

	#return genLeptonsFound


