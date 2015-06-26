from math        import sqrt, cos
from ROOT import TLorentzVector
from ROOT import TVector2
from ROOT import TMath
from inputs.MT2W import MT2W
from inputs.topness import topness    
from inputs.hadchi2 import hadchi2

class Variables() :

    branchesForVariables = [ "met_pt", "met_phi", "gen_n", "gen_id", "gen_mother_index", "gen_status" ]
    
    def computeVariables(self,event) :
        
	self.MT   = self.computeMT(event)
	
	# will compute HT HTSSM HTOSM
        self.computeHTVariables(event)
        
	#MT2W
	if len(self.selectedLeptons)>0:
		self.MT2W = MT2W.computeMT2W(self.selectedJets, self.selectedLeptons[0], event.met_pt, event.met_phi)
        else:
		self.MT2W = 0
	self.numberOfGeneratedLeptons = self.getNumberOfGeneratedLeptons(event)

        #topness
	self.topness = self.computeTopness(event)

	#Chi2
        self.hadchi2 = hadchi2.computeHadChi2(self.selectedJets)
        #print self.hadchi2
	
	#other variables
	self.M3b = self.computeM3b(event)
	self.Mlb_leadb = self.computeMlb_leadb(event)
        
	#############
	# dphi_Wlep #
        #############
	if len(self.selectedLeptons)>=1:
	    self.dphi_Wlep = (self.leadingLepton+self.METP4).DeltaPhi(self.leadingLepton)
	else: 
	    self.dphi_Wlep = -999.



    ##################
    #      topness   #
    ##################
    def computeTopness(self,event):
        # lepton
        #selectedLeptons = self.selectedLeptons
        #if len(selectedLeptons) == 0:
	if self.oneLepton == False:
	    return -999
	# jet
	if len(self.selectedJets)<=2:
	    return -888

	# lepton
	leadingLepton = self.leadingLepton
        

	selJets = self.selectedJets

	#############################
	# create a vector of 
	#############################

	bjets = []
	addjets = []
	jets = self.selJetsP4
	# order with higher CSV jets
	jets.sort(key=lambda j:j[1], reverse = True)
	
	for j in jets:
 	    if j[2] == True:
 	        bjets.append(j[0])
            elif len(bjets)<2 and len(bjets)+len(addjets)<3:
	        addjets.append(j[0])
  
	topnvalues = [];
  	#default value
	topnvalues.append(1000)
	#print "njets = ",len(bjets), len(addjets)
	if len(bjets)>0:
    	    for n in range(len(bjets)):
	        for m in range(n+1,len(bjets)):
		    #print bjets[n].Pt(),bjets[m].Pt()
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		bjets[n].Pt(), bjets[n].Eta(), bjets[n].Phi(), bjets[n].E(),\
	   		bjets[m].Pt(), bjets[m].Eta(), bjets[m].Phi(), bjets[m].E(),\
	    		event.met_pt, event.met_phi)
		    #print n,m,tmptop
		    topnvalues.append(tmptop)
		    # permutation
		    #print "bjet1"
		    #print bjets[m].Px(), bjets[m].Py(),bjets[m].Pz(),bjets[m].E()
		    #print bjets[m].Pt(), bjets[m].Eta(),bjets[m].Phi(),bjets[m].E()
		    #print "bjet2"
		    #print bjets[n].Px(), bjets[n].Py(),bjets[n].Pz(),bjets[n].E()
		    #print bjets[n].Pt(), bjets[n].Eta(),bjets[n].Phi(),bjets[n].E()
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		bjets[m].Pt(), bjets[m].Eta(), bjets[m].Phi(), bjets[m].E(),\
	   		bjets[n].Pt(), bjets[n].Eta(), bjets[n].Phi(), bjets[n].E(),\
	    		event.met_pt, event.met_phi)
		    #print n,m,tmptop
		    topnvalues.append(tmptop)
		
		
      		for m in range(len(addjets)):
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		bjets[n].Pt(), bjets[n].Eta(), bjets[n].Phi(), bjets[n].E(),\
	   		addjets[m].Pt(), addjets[m].Eta(), addjets[m].Phi(), addjets[m].E(),\
	    		event.met_pt, event.met_phi)
		    topnvalues.append(tmptop)
		    #permutation
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		addjets[m].Pt(), addjets[m].Eta(), addjets[m].Phi(), addjets[m].E(),\
	   		bjets[n].Pt(), bjets[n].Eta(), bjets[n].Phi(), bjets[n].E(),\
	    		event.met_pt, event.met_phi)
		    topnvalues.append(tmptop)
		
		
	elif len(addjets)>=2:
	     for m in range(1,len(addjets)):
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		addjets[0].Pt(), addjets[0].Eta(), addjets[0].Phi(), addjets[0].E(),\
	   		addjets[m].Pt(), addjets[m].Eta(), addjets[m].Phi(), addjets[m].E(),\
	    		event.met_pt, event.met_phi)
		    topnvalues.append(tmptop)
		    #permutation
		    tmptop = topness.computeTopness(\
	     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   		addjets[m].Pt(), addjets[m].Eta(), addjets[m].Phi(), addjets[m].E(),\
	   		addjets[0].Pt(), addjets[0].Eta(), addjets[0].Phi(), addjets[0].E(),\
	    		event.met_pt, event.met_phi)
		    topnvalues.append(tmptop)
	
	
	#print "topness values", topness
	return min(topnvalues)



    #############
    # Mbl_leadb #
    #############
    def computeMlb_leadb(self,event):
        selectedLeptons = self.selectedLeptons
        if len(selectedLeptons) == 0:
	    return -999
	leadingLepton = self.leadingLepton
	
	selectedJets = sorted(self.selectedJets, key=lambda j: j.CSVv2, reverse=True)
	
	if len(self.selectedJets)>0:
	    j = TLorentzVector()
	    j.SetPtEtaPhiE(selectedJets[0].pT, selectedJets[0].eta, selectedJets[0].phi, selectedJets[0].E)
	    return (j+leadingLepton).M()

        #if we don't find any bTagged jet
	return -888
    
    #############
    #     M3b   #
    #############
    def computeM3b(self,event):
	
	#avoid to waste time - use local variables
	#selectedJets = self.selectedJets
	selectedJets = 	self.selJetsP4
        nJets = len(selectedJets)
        	
	leadingLepton = self.leadingLepton

	# if there is not enought jets : return -1
        if (nJets <= 2):
	    return -1.0;

        # no ambiguity if there is only 3 jets
        elif nJets == 3:
	    sum = selectedJets[0][0]+selectedJets[1][0]+selectedJets[2][0]
	    return sum.M()

	else:
	    # we need to have a lepton
	    if len(self.selectedLeptons) == 0:
	        return -2
	    
	    # sort the collection according to dPhi
	    selectedJets.sort(key=lambda tup: tup[4], reverse=True)

	    #compute the mass based on the 3 most back-to-back to the lepton
	    return (selectedJets[0][0] + selectedJets[1][0] + selectedJets[2][0]).M()

    # ########
    # #  MT  # 
    # ########

    def computeMT(self,event) :

        leadingLeptonPt = self.selectedLeptons[0].pT if len(self.selectedLeptons)>0 else 0
        deltaPhi = self.selectedLeptons[0].phi - event.met_phi if len(self.selectedLeptons)>0 else 0
        
        MT = sqrt(2 * leadingLeptonPt * event.met_pt * (1 - cos(deltaPhi) ))
        
        return MT

    # ####################
    # #  HT HTSSM HTOSM  #
    # ####################

    def computeHTVariables(self,event) :

        HT = 0
        HT_onTheSideOfMET = 0
        for jet in self.selectedJets :
            HT += jet.pT
            if abs(TVector2.Phi_mpi_pi(event.met_phi -jet.phi)) < TMath.Pi()/2.:
	        HT_onTheSideOfMET += jet.pT

        self.HT = HT
	self.HTSSM = HT_onTheSideOfMET
	self.HTOSM = HT-HT_onTheSideOfMET

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



