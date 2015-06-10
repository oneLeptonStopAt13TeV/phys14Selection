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

	#other variables
	self.M3b = self.computeM3b(event)
	self.Mlb_leadb = self.computeMlb_leadb(event)
        
	#############
	# dphi_Wlep #
        #############
	if len(self.selectedLeptons)>=1:
	    self.dphi_Wlep =  TVector2.Phi_mpi_pi(self.selectedLeptons[0].phi - event.met_phi)
        else: 
	    self.dphi_Wlep = -999.



    ##################
    #      topness   #
    ##################
    def computeTopness(self,event):
        # lepton
        selectedLeptons = self.selectedLeptons
        if len(selectedLeptons) == 0:
	    return -999
	#leadingLepton = TLorentzVector(selectedLeptons[0].pT, selectedLeptons[0].eta, selectedLeptons[0].phi, selectedLeptons[0].E)
	leadingLepton = selectedLeptons[0]
        
        # MEt
	#metp4 = TLorentzVector()
	#metp4.SetPtEtaPhiE(event.met_pt,0,event.met_phi,event.met_pt)

	#find the 2 b-jets candidates
	bJets = []
	selectedJets = self.selectedJets
	#sort the list according to btag
	selectedJets.sort(key=lambda j: j.CSVv2, reverse=True)
	if len(selectedJets)<=2:
	    return -888
	#bjet1 = TLorentzVector(); 
	#bjet1.SetPtEtaPhiE(selectedJets[0].pT, selectedJets[0].eta, selectedJets[0].phi, selectedJets[0].E)
	#bjet2 = TLorentzVector();    
	#bjet2.SetPtEtaPhiE(selectedJets[1].pT, selectedJets[1].eta, selectedJets[1].phi, selectedJets[1].E)
        bjet1 = selectedJets[0]
	bjet2 = selectedJets[1]
	
	#return  topness.computeTopness(leadingLepton, bjet1, bjet2, metp4)
	return topness.computeTopness(\
	    leadingLepton.pT, leadingLepton.eta, leadingLepton.phi, leadingLepton.E,\
	    bjet1.pT, bjet1.eta, bjet1.phi, bjet1.E,\
	    bjet2.pT, bjet2.eta, bjet2.phi, bjet2.E,\
	    event.met_pt, event.met_pt)

    #############
    # Mbl_leadb #
    #############
    def computeMlb_leadb(self,event):
        selectedLeptons = self.selectedLeptons
        if len(selectedLeptons) == 0:
	    return -999
	leadingLepton = TLorentzVector(selectedLeptons[0].pT, selectedLeptons[0].eta, selectedLeptons[0].phi, selectedLeptons[0].E)
        selectedJets = self.selectedJets
	for jet in selectedJets:
	    if jet.bTag:
	        j = TLorentzVector()
		j.SetPtEtaPhiE(jet.pT, jet.eta, jet.phi, jet.E)
	        return (j+leadingLepton).M()

        #if we don't find any bTagged jet
	return -888
    
    #############
    #     M3b   #
    #############
    def computeM3b(self,event):
	
	#avoid to waste time - use local variables
	selectedJets = self.selectedJets
        nJets = len(self.selectedJets)
        	
	
	# if there is not enought jets : return -1
        if (nJets <= 2):
	    return -1.0;

        # no ambiguity if there is only 3 jets
        elif nJets == 3:
	    jet1 = TLorentzVector()
	    jet1.SetPtEtaPhiE(selectedJets[0].pT,selectedJets[0].eta,selectedJets[0].phi,selectedJets[0].E) 
            jet2 = TLorentzVector()
	    jet2.SetPtEtaPhiE(selectedJets[1].pT,selectedJets[1].eta,selectedJets[1].phi,selectedJets[1].E) 
            jet3 = TLorentzVector()
	    jet3.SetPtEtaPhiE(selectedJets[2].pT,selectedJets[2].eta,selectedJets[2].phi,selectedJets[2].E)
	    sum = jet1+jet2+jet3
	    return (jet1+jet2+jet3).M()

	else:
	    # we need to have a lepton
	    if len(self.selectedLeptons) == 0:
	        return -2
            
	    distLeptonJet = []
	    for  jet in selectedJets:
                j = TLorentzVector()
		j.SetPtEtaPhiE(jet.pT,jet.eta,jet.phi,jet.E)
                distLeptonJet.append((TVector2.Phi_mpi_pi(self.selectedLeptons[0].phi -jet.phi),j))
	    
	    # sort the collection according to dPhi
	    distLeptonJet.sort(key=lambda tup: tup[0], reverse=True)

	    #compute the mass based on the 3 most back-to-back to the lepton
	    return (distLeptonJet[0][1] + distLeptonJet[1][1] + distLeptonJet[2][1]).M()

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
            if TVector2.Phi_mpi_pi(event.met_phi -jet.phi) < TMath.Pi()/2.:
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

	#return genLeptonsFound


