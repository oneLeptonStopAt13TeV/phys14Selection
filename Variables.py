from math        import sqrt, cos
from ROOT import TLorentzVector
from ROOT import TVector2
from ROOT import TMath
from inputs.MT2W import MT2W
from inputs.topness import topness    
from inputs.hadchi2 import hadchi2

loadGenInfo = True
loadMCTruth = True
loadStop = True

class Variables() :
    

    def __init__(self):
   	self.loadGenInfo_Var = False
	self.loadMCTruth_Var = False
	self.branchesForVariables = []
        #put default value
        self.MT = 0
        self.MT2W = 0
        self.topness = 0
        self.hadchi2 = 0
        self.M3b = 0
        self.Mlb_leadb = 0
        self.dphi_Wlep = 0
	self.numberOfGeneratedLeptons = 0
	self.HT = 0
	self.HTOSM = 0
	self.HTSSM = 0
	self.ST = 0 
	self.LP = 0
	self.Meff = 0 
	self.MTdeco_Q = 0 
	self.DeltaPtbb = 0


    def UpdateVarBranchLoad(self):
    	self.branchesForVariables = [ "met_pt", "met_phi", "met_sig"]
    	if (self.loadGenInfo_Var):
    		self.branchesForVariables.extend( ["gen_n", "gen_id", "gen_mother_index", "gen_status" ])

    	if(self.loadMCTruth_Var): 
    		self.branchesForVariables.extend( ["mc_truth_tWl1_status", "mc_truth_tWl2_status"])

    def computeVariables(self,event) :
        
	self.MT   = self.computeMT(event)
	
	# will compute HT HTSSM HTOSM
        self.computeHTVariables(event)
        
	#MT2W
	if len(self.selectedLeptons)>0:
		self.MT2W = MT2W.computeMT2W(self.selectedJets, self.selectedLeptons[0], event.met_pt, event.met_phi)
        else:
		self.MT2W = 0
	
	self.numberOfGeneratedLeptons = -999
	if (self.loadGenInfo_Var):
		self.numberOfGeneratedLeptons = self.getNumberOfGeneratedLeptons(event)
                #print "filling from loadGenInfo"

	if (self.loadMCTruth_Var):
		self.numberOfGeneratedLeptons = 0
                #print "loadMCtruthVAR"
		if event.mc_truth_tWl1_status >=0 : self.numberOfGeneratedLeptons+=1
		if event.mc_truth_tWl2_status >=0 : self.numberOfGeneratedLeptons+=1

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


	###################
	# new variables   #
	###################
	if len(self.selectedLeptons)>=1:
	   self.ST = self.leadingLepton.Pt()+event.met_pt
	   self.LP = self.computeLP(event)
	   self.Meff = self.computeMeff(event) 
	   self.MTdeco_Q = sqrt(self.leadingLepton.Pt()*self.METP4.Pt()) 
	else:
	   self.ST = -999. 
	   self.LP = -999.
	   self.Meff = -999.
	   self.MTdeco_Q = -999.
	self.DeltaPtbb = self.computeDeltaPtbb(event)
	

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
	if len(self.selectedJets)<2:
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
            #elif len(bjets)<1 and len(addjets)<3:
	    #    addjets.append(j[0])
  
	topnvalues = [];
  	#default value
	topnvalues.append(1000)
	#print "njets = ",len(bjets), len(addjets)
	if len(bjets)>0:
    	    for n in range(len(bjets)):
		#print bjets[n].Pt(),bjets[m].Pt()
		tmptop = topness.computeTopness(\
	     	 leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	   	 bjets[n].Pt(), bjets[n].Eta(), bjets[n].Phi(), bjets[n].E(),\
	    	 event.met_pt, event.met_phi)
		    #print n,m,tmptop
		topnvalues.append(tmptop)
        
	else:
            return -1111

	return min(topnvalues)
		
	#elif len(bjets)==0 and len(addjets)>0:
	#     for m in range(1,len(addjets)):
	#	    tmptop = topness.computeTopness(\
	#     		leadingLepton.Pt(), leadingLepton.Eta(), leadingLepton.Phi(), leadingLepton.E(),\
	#   		addjets[m].Pt(), addjets[m].Eta(), addjets[m].Phi(), addjets[m].E(),\
	#    		event.met_pt, event.met_phi)
	#	    topnvalues.append(tmptop)
	
	
	#print "topness values", topness



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

    # ###########
    # # DPtbb   #
    # ###########
    def computeDeltaPtbb(self, event):
        if len(self.selJetsBtagOrdered)>=2:	  
	  return (abs(self.selJetsBtagOrdered[0].Pt()-self.selJetsBtagOrdered[1].Pt()))/(self.selJetsBtagOrdered[0].Pt()+self.selJetsBtagOrdered[1].Pt())
	else: 
	  return -999.

    # ########
    # #  MT  # 
    # ########

    def computeMT(self,event) :

        leadingLeptonPt = self.selectedLeptons[0].pT if len(self.selectedLeptons)>0 else 0
        deltaPhi = self.selectedLeptons[0].phi - event.met_phi if len(self.selectedLeptons)>0 else 0
        
        MT = sqrt(2 * leadingLeptonPt * event.met_pt * (1 - cos(deltaPhi) ))
        
        return MT
  

    # ######
    # # LP #
    # ######

    def computeLP(self, event):
	Wcand = self.METP4+self.leadingLepton
	LP = -999.
	if Wcand.Pt()!=0:
	  LP = (self.leadingLepton.Pt()*Wcand.Pt()*cos(self.leadingLepton.Phi()-Wcand.Phi()))/(Wcand.Pt()*Wcand.Pt())
	return LP


    # ############
    # # Meff     #
    # ############
    
    def computeMeff(self, event):
    	cand = TLorentzVector();
	cand+=self.leadingLepton
	cand+=self.METP4
	for jet in self.selJetsP4:
	  cand+=jet[0]

        return cand.M()

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
        tmp = 0

        #for i in range(n) :
            # put this requirement at the first position
	#    if (status[i]!=1) :
        #        continue;
        #    mother_pdgid = pdgid[mother[i]]
	#    if (abs(mother_pdgid) != 24) :
        #        continue;
        #    if ((abs(pdgid[i]) != 11) and (abs(pdgid[i]) != 13) and (abs(pdgid[i]) != 15)) :
        #        continue;
        #    tmp += 1
            #print "id %d" % event.gen_id[i]
            #print "index %d" % event.gen_index[i]
            #print "mother index %d" % event.gen_mother_index[i]
            #print "status %d" % event.gen_status[i]
            #print "i: %d" % i

        #print "sum result 1: %d" % tmp

	res = [1 for i in range(n) if (status[i]==1 and abs(pdgid[mother[i]]) == 24 and ((abs(pdgid[i]) == 11) or (abs(pdgid[i]) == 13) or (abs(pdgid[i]) == 15)))]
        #print "sum result 2: %d" % sum(res)
        return sum(res)


     # return a list of tuple (pt, eta, pdgid)
    def getGenLostLeptons(self, event, leadingLepton):
        n      = event.gen_n
	pt     = event.gen_pt
	eta    = event.gen_eta
	phi    = event.gen_phi
	m      = event.gen_m
        pdgid  = event.gen_id
        mother = event.gen_mother_index
        status = event.gen_status
	
	output = []

	res = [(pt[i],eta[i], phi[i], m[i],pdgid[i])for i in range(n) if(status[i]==1 and abs(pdgid[mother[i]]) == 24 and ((abs(pdgid[i]) == 11) or (abs(pdgid[i]) == 13) or (abs(pdgid[i]) == 15)))]
	for p in res:
	   if(p[0]>=5 and abs(p[1])<2.4):
	     p4 = TLorentzVector()
	     p4.SetPtEtaPhiM(p[0],p[1], p[2], p[3]) 
	     if(p4.DeltaR(leadingLepton)>0.1):
		 output.append((p[0], p[1], p[4]))

        return output
