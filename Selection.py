from collections import namedtuple
from core        import commonFunctions as common
from ROOT import TLorentzVector

class Selection :
    
    
    # ######################################## #
    # matching leptons with gen prompt lepton  #
    # ######################################## #



    # ############# #
    # Reset objects #
    # ############# #
    

    def resetSelectedObjects(self) :
        self.selectedElectrons = 0
	self.selectedMuons = 0
	self.selectedLeptons   = []
	self.selectedLeptons2   = []
	self.vetoLeptons   = []
        self.selectedJets      = []
	self.pfcands = []
        self.ngoodbtags = 0

	#some default values
	self.PassTrackVeto = True 
	self.PassTauVeto = True 

	# selected pfcands (charged and dz<0.1 and pt>0)
	#self.pf_pt = []
	#self.pf_eta = []
	#self.pf_phi = []
	#self.pf_charge = []
	#self.pf_id = []
	self.pf_isSel = []	
	
	
	#for isoStudy
	self.noIsoSelectedMuons = []
	self.noIsoSelectedElectrons = []
	################################


    branchesForGenInfo = ["gen_n", "gen_pt", "gen_eta", "gen_phi", "gen_m", "gen_status", "gen_id", "gen_charge", "gen_index", "gen_mother_index", "gen_daughter_n", "gen_daughter_index"]

    ############################################################################
    #    ___  _     _           _              _           _                   #
    #   / _ \| |__ (_) ___  ___| |_   ___  ___| | ___  ___| |_ ___  _ __ ___   #
    #  | | | | '_ \| |/ _ \/ __| __| / __|/ _ \ |/ _ \/ __| __/ _ \| '__/ __|  #
    #  | |_| | |_) | |  __/ (__| |_  \__ \  __/ |  __/ (__| || (_) | |  \__ \  #
    #   \___/|_.__// |\___|\___|\__| |___/\___|_|\___|\___|\__\___/|_|  |___/  #
    #             |__/                                                         #
    ############################################################################

    # Define structure for temporary objects storage
    lepton = namedtuple('lepton', ['id', 'E', 'pT', 'eta', 'phi', 'iso', 'passMediumID', 'dz', 'd0', 'charge' ])
    jet    = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'PUid', 'bTag', 'looseID' ])
    pfc    = namedtuple('pfcand',    [ 'pT', 'eta', 'phi', 'charge', 'id' ])


    # ####### #
    # pfcanfs #
    # ####### #

    branchesForPfcand = ["pfcand_n", "pfcand_E", "pfcand_pt", "pfcand_eta", "pfcand_phi", "pfcand_dz", "pfcand_charge", "pfcand_id"]

    def pfCandTupling(self,event):
	
	n	= event.pfcand_n
	#E	= event.pfcand_E
	pt	= event.pfcand_pt
	#eta	= event.pfcand_eta
	#phi	= event.pfcand_phi
	dz	= event.pfcand_dz
	charge	= event.pfcand_charge
	#id	= event.pfcand_id

	#zipped = zip(pt,eta,phi,dz,charge,id)
	# take caution of the indices
	#self.pfcands = [self.pfc(el[0],el[1],el[2],el[4],el[5]) for el in zipped if el[4] != 0 and el[3] < 0.1 and el[0] >0]
	#for el in zipped:
	#    if el[4]==0: continue
	#    if el[3]>0.1: continue
	#    if el[0]<0: continue
	#    self.pfcands.append(self.pfc(el[0],el[1],el[2],el[4],el[5]))
	for i in range(n):
	    if charge[i] == 0: 
	    	self.pf_isSel.append(False)
		continue
	    if dz[i] < 0.1: 
	    	self.pf_isSel.append(False)
		continue
	    if pt[i]>0    : 
	    	self.pf_isSel.append(False)
		continue
	    self.pf_isSel.append(True)
	    #self.pfcands.append(self.pfc(E[i],pt[i],eta[i],phi[i],charge[i],dz[i],id[i]) )
	    #self.pfcands.append(self.pfc(pt[i],eta[i],phi[i],charge[i],id[i]) )
	    
	    
	    #event.pf_pt.append(pt[i])
	    #event.pf_eta.append(eta[i])
	    #event.pf_phi.append(phi[i])
	    #event.pf_charge.append(charge[i])
	    #event.pf_id.append(id[i])
    # ##### #
    # Taus #
    # ##### #
    
    branchesForTauSelection = [ "tau_n", "tau_pt", "tau_eta", "tau_phi", "tau_charge", 
    				"tau_byMediumCombinedIsolationDeltaBetaCorr3Hits"]

    #######################
    # 	Tau Veto          #
    #######################
    ### Return True if it pass TauVeto
    def isTauVeto(self, event):
        n = event.tau_n
	pt 	=  event.tau_pt
	eta 	=  event.tau_eta
	phi 	=  event.tau_phi
	charge	=  event.tau_charge
	id 	=  event.tau_byMediumCombinedIsolationDeltaBetaCorr3Hits

	lep1 = self.lepton
	FoundLep1 = False
	if(len(self.selectedLeptons)>0): 
		lep1 = self.selectedLeptons[0]
		FoundLep1 = True
	elif len(self.selectedLeptons2)>0: 
		lep1 = self.selectedLeptons2[0]
		FoundLep1 = True

	for i in range(n):
	    if pt[i]<20: 	continue
	    if abs(eta[i])>2.4: continue
	    if not id[i]:	continue
	    dR = 1
	    if FoundLep1:
	        dR = common.deltaR(phi[i],eta[i],lep1.phi, lep1.eta)
	    if dR>0.4:
	    	#We've found a tau !!!
	    	return False

	# No tau found - event is not vetoed
	return True

    # ##### #
    # Muons #
    # ##### #

    branchesForMuonSelection = [ "mu_n",
                                 "mu_id", "mu_E", "mu_pt", "mu_eta", "mu_phi", "mu_charge",
                                 "mu_isPFMuon", "mu_isGlobalMuon", "mu_isTrackerMuon",
                                 #"mu_globalTrack_dxy", "mu_globalTrack_dz",
				 "mu_innerTrack_PV_dxy", "mu_innerTrack_PV_dz",
                                 #"mu_pfIso03_sumChargedHadronPt", "mu_pfIso03_sumNeutralHadronEt",
                                 #"mu_pfIso03_sumPhotonEt", "mu_pfIso03_sumPUPt",
                                 #"mu_numberOfMatches",
				 "mu_isLooseMuon", "mu_isMediumMuon", #"mu_isTightMuon",
				 "mu_miniIso"  ]

    def muonDump(self,event):
       for i in range(event.mu_n):
	    print "id                    =", event.mu_id[i]
            print "E                     =", event.mu_E[i]
            print "pt                    =", event.mu_pt[i]
            print "eta                   =", event.mu_eta[i]
            print "phi                   =", event.mu_phi[i]
            print "isPF                  =", event.mu_isPFMuon[i]
            print "isGlobal              =", event.mu_isGlobalMuon[i]
            print "isTracker             =", event.mu_isTrackerMuon[i]
            print "dxy                   =", event.mu_innerTrack_PV_dxy[i]
            print "dz                    =", event.mu_innerTrack_PV_dz[i]
            #print "isoChargedHadron      =", event.mu_pfIso03_sumChargedHadronPt[i]
            #print "isoNeutralHadron      =", event.mu_pfIso03_sumNeutralHadronEt[i]
            #print "isoPhoton             =", event.mu_pfIso03_sumPhotonEt[i]
            #print "isoPU                 =", event.mu_pfIso03_sumPUPt[i]
            print "isLooseMuon           =", event.mu_isLooseMuon[i]
            print "isMediumMuon          =", event.mu_isMediumMuon[i]
            #print "isTightMuon           =", event.mu_isTightMuon[i]
            print "miniIso               =", event.mu_miniIso[i]
            #print "SUSYminiIso           =", event.mu_SUSYminiIso[i]
            print "charge	         =", event.mu_charge[i]




    def muonSelector(self,event, muonSelCode, iso = True) :
    	
	#use also iso cut if iso == True

	#copy info in local variables (avoid retrieved info in the loop: save time)
        n                     = event.mu_n
        id                    = event.mu_id
        E                     = event.mu_E
        pt                    = event.mu_pt
        eta                   = event.mu_eta
        phi                   = event.mu_phi
        charge                = event.mu_charge
        isPF                  = event.mu_isPFMuon
        isGlobal              = event.mu_isGlobalMuon
        isTracker             = event.mu_isTrackerMuon
        dxy                   = event.mu_innerTrack_PV_dxy
        dz                    = event.mu_innerTrack_PV_dz
        #isoChargedHadron      = event.mu_pfIso03_sumChargedHadronPt
        #isoNeutralHadron      = event.mu_pfIso03_sumNeutralHadronEt
        #isoPhoton             = event.mu_pfIso03_sumPhotonEt
        #isoPU                 = event.mu_pfIso03_sumPUPt
        #isTightMuon           = event.mu_isTightMuon
	miniIso		      = event.mu_miniIso
	#miniIso		      = event.mu_SUSYminiIso
	isLooseMuon	      = event.mu_isLooseMuon
	isMediumMuon	      = event.mu_isMediumMuon


	for i in range(n) :
	    # Reject muons than can either be veto or selected
	    if abs(eta[i]) >= 2.4  : continue
	    if abs(pt[i]) <= 10  : continue
	    if abs(dxy[i]) >= 0.1 : continue
	    if abs(dz[i]) >= 0.5  : continue	
            if miniIso[i] >= 0.2 : continue
	    if not isLooseMuon[i]: continue

            # Require tight ID
	    veto = True
	    if isMediumMuon[i]  and abs(dxy[i])<0.02 and abs(dz[i])<0.1 and miniIso[i]<0.1:
	        # Selected muon
		if abs(eta[i]) < 2.1 and pt[i] >= 30:
		    veto = False
		    self.selectedLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )
		# Loose selection
		elif pt[i] >= 20:
		    veto = False
		    self.selectedLeptons2.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )
	    # Veto muon
	    if veto:
	        self.vetoLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )

	

    # ######### #
    # Electrons #
    # ######### #

    branchesForElectronSelection = [ "el_n",
                                     "el_id", "el_E", "el_pt", "el_eta", "el_superCluster_eta", "el_phi", "el_charge",
                                     "el_deltaEtaSuperClusterTrackAtVtx",
                                     "el_deltaPhiSuperClusterTrackAtVtx",
                                     "el_sigmaIetaIeta", "el_hadronicOverEm",
                                     "el_eSuperClusterOverP",
                                     "el_gsfTrack_PV_dxy", "el_gsfTrack_PV_dz", "el_IoEmIoP",
                                     "el_passConversionVeto", "el_numberOfLostHits",
                                     #"el_pfIso_sumChargedHadronPt", "el_pfIso_sumNeutralHadronEt",
                                     #"el_pfIso_sumPhotonEt", "el_pfIso_sumPUPt" ,
				     "ev_rho", 
				     "el_miniIso" ]

    def electronDump( self,event):
        for i in range(event.el_n):
            print "id                 =", event.el_id[i]
            print "E                  =", event.el_E[i]
            print "pt                 =", event.el_pt[i]
            print "eta                =", event.el_eta[i]
            print "scleta             =", event.el_superCluster_eta[i]
            print "phi                =", event.el_phi[i]
            print "dEtaSCTrack        =", event.el_deltaEtaSuperClusterTrackAtVtx[i]
            print "dPhiSCTrack        =", event.el_deltaPhiSuperClusterTrackAtVtx[i]
            print "see                =", event.el_sigmaIetaIeta[i]
            print "hadronicOverEm     =", event.el_hadronicOverEm[i]
            print "eSuperClusterOverP =", event.el_eSuperClusterOverP[i]
            print "dxy                =", event.el_gsfTrack_PV_dxy[i]
            print "dz                 =", event.el_gsfTrack_PV_dz[i]
            print "IoEmIoP            =", event.el_IoEmIoP[i]
            print "passConversionVeto =", event.el_passConversionVeto[i]
            print "numberOfLostHits   =", event.el_numberOfLostHits[i]
            #print "isoChargedHadron   =", event.el_pfIso_sumChargedHadronPt[i]
            #print "isoNeutralHadron   =", event.el_pfIso_sumNeutralHadronEt[i]
            #print "isoPhoton          =", event.el_pfIso_sumPhotonEt[i]
            #print "isoPU              =", event.el_pfIso_sumPUPt[i]
            print "miniIso            =", event.el_miniIso[i]
            print "charge             =", event.el_charge[i]
    
    def electronSelector(self,event,elSelCode, iso = True) :
        n                  = event.el_n
        id                 = event.el_id
        E                  = event.el_E
        pt                 = event.el_pt
        eta                = event.el_eta
        scleta             = event.el_superCluster_eta
        phi                = event.el_phi
        dEtaSCTrack        = event.el_deltaEtaSuperClusterTrackAtVtx
        dPhiSCTrack        = event.el_deltaPhiSuperClusterTrackAtVtx
        see                = event.el_sigmaIetaIeta
        hadronicOverEm     = event.el_hadronicOverEm
        eSuperClusterOverP = event.el_eSuperClusterOverP
        dxy                = event.el_gsfTrack_PV_dxy
        dz                 = event.el_gsfTrack_PV_dz
        charge             = event.el_charge
        IoEmIoP            = event.el_IoEmIoP
        passConversionVeto = event.el_passConversionVeto
        numberOfLostHits   = event.el_numberOfLostHits
        #isoChargedHadron   = event.el_pfIso_sumChargedHadronPt
        #isoNeutralHadron   = event.el_pfIso_sumNeutralHadronEt
        #isoPhoton          = event.el_pfIso_sumPhotonEt
        #isoPU              = event.el_pfIso_sumPUPt
        miniIso   	   = event.el_miniIso
        #miniIso   	   = event.el_SUSYminiIso

	selected = False
	veto = False

        for i in range(n) :

            # Loose criteria applied for the veto leptons
	    if pt[i] <= 10  : continue
	    if abs(eta[i]) >= 2.4: continue
	    if miniIso[i] >= 0.2: continue

            # Remove crack electron
            #if (abs(scleta[i]) > 1.4442) and ((abs(scleta[i]) < 1.566)) : continue

	    ##############
            # Electron ID
	    ##############

	    # Veto Working point
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, revision 19
	    
	    if (abs(scleta[i]) <= 1.479) :
		if (abs(dEtaSCTrack[i]) >= 0.013625 )  : continue
                if (abs(dPhiSCTrack[i]) >= 0.230374 )  : continue
                if (see[i]              >= 0.011586 )  : continue
                if (hadronicOverEm[i]   >= 0.181130 )  : continue
                if (abs(dxy[i])         >= 0.094095 ) : continue
                if (abs(dz[i])          >= 0.713070 )  : continue
                if (IoEmIoP[i]          >= 0.295751 )  : continue
            else :
                if (abs(dEtaSCTrack[i]) >= 0.011932 ) : continue
                if (abs(dPhiSCTrack[i]) >= 0.255450 ) : continue
                if (see[i]              >= 0.031849 ) : continue
                if (hadronicOverEm[i]   >= 0.223870 ) : continue
                if (abs(dxy[i])         >= 0.342293 ) : continue
                if (abs(dz[i])          >= 0.953461 ) : continue
                if (IoEmIoP[i]          >= 0.155501 ) : continue

            if not (passConversionVeto[i] )  : continue
            if (numberOfLostHits[i]   >  3)  : continue


            # Electron ID
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, medium
            # consistent with r19 (r13 in sync' - v1
            
	    passMediumID = False
	    if (abs(scleta[i]) <= 1.479) :
		if((abs(dEtaSCTrack[i]) <  0.008925 )  and 
                   (abs(dPhiSCTrack[i]) <  0.035973 )  and
                   (see[i]              <  0.009996  )  and
                   (hadronicOverEm[i]   <  0.050537 )  and
                   (IoEmIoP[i]          <  0.091942 )  and
                   (abs(dxy[i])         <  0.012235 )  and
                   (abs(dz[i])          <  0.042020 ))  :
		     selected = True
            else :
                if((abs(dEtaSCTrack[i]) <  0.007429  ) and
                   (abs(dPhiSCTrack[i]) <  0.067879  )  and
                   (see[i]              <  0.030135  )  and
                   (hadronicOverEm[i]   <  0.086782  )  and
                   (IoEmIoP[i]          <  0.100683  )  and
                   (abs(dxy[i])         <  0.036719  )  and
                   (abs(dz[i])          <  0.138142  ))  :
		     selected = True


            if not (passConversionVeto[i] )  : selected = False
            if (numberOfLostHits[i]   >  1)  : selected = False
	    passMediumID = selected

	    veto = True
	    if selected:
	       if pt[i] > 40 and abs(eta[i])< 2.1 and miniIso[i]<0.1:
                   veto = False
		   self.selectedLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))
	       elif pt[i] > 20 and abs(eta[i])<2.4 and miniIso[i]<0.1:
                   veto = False
		   self.selectedLeptons2.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))
	    if veto:
              self.vetoLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))



    # #### #
    # Jets #
    # #### #

    branchesForJetSelection = [ "jet_n",
                                "jet_E", "jet_pt", "jet_eta",   "jet_phi",
                                "jet_CSVv2",
                                "jet_pileupJetId" ,
				"jet_looseJetID",
				#"jet_tightJetID"
				]

    
    def jetDump(self,event):
        n   	    = event.jet_n
        E           = event.jet_E
        pt          = event.jet_pt
        eta         = event.jet_eta
        phi         = event.jet_phi
        CSVv2       = event.jet_CSVv2
        looseID     = event.jet_looseJetID

        for i in range(n):
	    j= TLorentzVector ()
	    j.SetPtEtaPhiE(pt[i],eta[i],phi[i],E[i])
	    dr = j.DeltaR(self.leadingLepton)
	    dphi = j.DeltaPhi(self.leadingLepton)
	    dphiMET = j.DeltaPhi(self.METP4)
	    print "jet pt: ", pt[i], " eta: ", eta[i], " phi: ", phi[i], " E: ", E[i], " CSV: ",CSVv2[i], "DR(j,l): ",dr, "dphi(j.l:)",dphi, "dphi(j,MET):", dphiMET
   
    def selJetDump(self,event):
        jets = self.selJetsP4
        for mytuple in jets:
	    j = mytuple[0]
	    dr = j.DeltaR(self.leadingLepton)
	    dphi = j.DeltaPhi(self.leadingLepton)
	    dphiMET = j.DeltaPhi(self.METP4)
	    #print "jet pt: ", j.Pt(), " eta: ", j.Eta(), " phi: ", j.Phi(), " E: ", j.E(), " DR(j,l) : ",dr, " dphi(j,l): ",dphi, " dphi(j,MET): ", dphiMET
	    print "jet pt: ", j.Pt(), " eta: ", j.Eta(), " phi: ", j.Phi(), " E: ", j.E(), "CSVv2: ", mytuple[1]," DR(j,l) : ",dr, " dphi(j,l): ",dphi, " dphi(j,MET): ", dphiMET
            #print "CVS: ", mytuple[1]
	
    def jetSelector(self,event) :

        n           = event.jet_n
        E           = event.jet_E
        pt          = event.jet_pt
        eta         = event.jet_eta
        phi         = event.jet_phi
        CSVv2       = event.jet_CSVv2
        pileupJetId = event.jet_pileupJetId
        looseID     = event.jet_looseJetID
        #tightID     = event.jet_tightJetID

        
	selectedJets = []
	selectedJetsOrg = []

	for i in range(n) :

            # Apply pT and eta requirements
            if (pt[i]       <  30) : continue
            if (abs(eta[i]) > 2.4) : continue
	    if not looseID[i]: continue
	    #if not tightID[i]: continue
            selectedJets.append(self.jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSVv2[i],
                                              pileupJetId[i],
                                              (CSVv2[i] > 0.814),
					      looseID[i]))
           
	# build a collection of leptons (selected, loose and veto)
	leptons = self.selectedLeptons+self.selectedLeptons2+self.vetoLeptons
	    
	# Remove jet overlaping with leptons (the closest one if many)
	tmpCollection = [(j, []) for j in selectedJets]
	for lepton in leptons :
            for jet in tmpCollection:
		dR = common.deltaR(lepton.phi,lepton.eta,jet[0].phi,jet[0].eta)
                jet[1].append(dR)

	for j in tmpCollection:
	    keep_it = True
	    for i in range(len(leptons)):
		if j[1][i]<0.4:
		    # check if it is the closest jet
		    dRs = [tmpCollection[k][1][i] for k in range (len(tmpCollection))] 
	    	    
		    if j[1][i] == min(dRs):
			keep_it = False 
			#print "remove jet: ", j[0].pT, dRs
	    if keep_it:
		self.selectedJets.append(j[0])

	#print "Jets: ", len(selectedJets), len(tmpCollection), len(self.selectedJets), len(selectedJetsOrg)
	#for i in range(len(selectedJets)):
	#   print selectedJets[i]
	#if len(self.selectedJets) != len(selectedJetsOrg):
	#    print "Jets: ", len(selectedJets), len(tmpCollection), len(self.selectedJets), len(selectedJetsOrg)
	self.ngoodbtags = 0
	for jet in self.selectedJets:
	    if jet.bTag:
	        self.ngoodbtags = self.ngoodbtags+1

    ################################	
    # compute TrackIso for each pf
    ################################	
    def TrackIso(self, thispf):

            absIso = 0
   	    for pf in self.pfcands:
	   	 #if pfcands.pT == thispf.pT && pfcands.eta == thispf.eta   
	   	 # do not count the orginal pf
	    	if pf == thispf: continue
	    	# skip neutral particules
    	    	dr = common.deltaR( pf.phi, pf.eta, thispf.phi, thispf.eta)
	        # check size of the code
    	    	if dr > 0.3 : continue # skip pfcands outside the cone
    	    	#already done while computing the tuples
		#if pf.pT >=0.0 and abs(pf.dz) < 0.1:
	    	#if pf.charge == 0: continue
	        absIso += pf.pT
  	 
	    return absIso

    ################################	
    #  Check if a track is Vetoed
    ################################	
    #question here: Should we change that function from 
    #lep1.p4 to all lep.p4?? - might be relevant for control regions.
    #def isVetoTrack(self, pf, lep):
      
#		if common.deltaR(pf.phi, pf.eta, lep.phi, lep.eta) < 0.4: return False
      		#if not electron or muon
#      		if (abs(pf.id)!=11 and abs(pf.id)!=13):
#          		if (pf.pT < 10.):  return False
#			if (pf.charge * lep.charge > 0): return False;
#          		if (self.TrackIso(pf)/pf.pT >0.1): return False
#      		else:
#			if (pf.pT < 5.): return False
#          		if (self.TrackIso(pf)/pf.pT >0.2): return False;
#      		return True


 	################################	
 	#  Main function ot be called 
	#   to check if the event pass
	#  the Track Veto
	################################	

    def isoTrackVeto(self, event):
		#load inf
		n = len(event.pfcand_pt)
		pf_pt = event.pfcand_pt
		pf_eta = event.pfcand_eta
		pf_phi = event.pfcand_phi
		pf_charge = event.pfcand_charge
		pf_id = event.pfcand_id
    		pf_isSel = self.pf_isSel	

		lep1 = self.lepton 
		#lep2 = self.lepton
		FoundLep1 = False
		#FoundLep2 = False
    		if (len(self.selectedLeptons)>0): 
			lep1 = self.selectedLeptons[0]
			FoundLep1 = True
		elif (len(self.selectedLeptons2)>0): 
			lep1 = self.selectedLeptons2[0]
	        	FoundLep1 = True
		#if (len(self.vetoLeptons)>0):
		#	lep2 = self.vetoLeptons[0]
		#	FoundLep2 = True
		vetotracks = 0
		for i in range(n):
		#for pf in self.pfcands:
		    # cut already applied during the producion of the tuples
		    if not pf_isSel[i]: continue
		    #if pf.charge == 0 :		continue
		    if pf_pt[i] < 5: 		continue
		    # cut already applied during the producion of the tuples
		    #if abs(pf.dz) > 0.1: 	continue
		    if (FoundLep1):   
		    	dR = common.deltaR(pf_phi[i], pf_eta[i], lep1.phi, lep1.eta)
			if dR < 0.1: continue  
     		    	#if self.isVetoTrack(ipf, lep1):
			## inline computation of isVetoTrack
			isVeto = True
			if dR < 0.4: isVeto =  False
      		        #if not electron or muon
      		        if (abs(pf_id[i])!=11 and abs(pf_id[i])!=13):
          			if (pf_pt[i] < 10.):  isVeto = False
				if (pf_charge[i] * lep.charge > 0): isVeto = False
            
	    			absIso = 0
	    			# compute isolation
   	    			for j in range(n):
	   	 			#if pfcands.pT == thispf.pT && pfcands.eta == thispf.eta   
	   	 			# do not count the orginal pf
	    				if i == j: continue
		    			if not pf_isSel[j]: continue
	    				# skip neutral particules
    	    				dr = common.deltaR( pf_phi[i], pf_eta[i], pf_phi[j], pf_eta[j])
	       				# check size of the code
    	    				if dr > 0.3 : continue # skip pfcands outside the cone
    	   			 	#already done while computing the tuples
					#if pf.pT >=0.0 and abs(pf.dz) < 0.1:
	   			 	#if pf.charge == 0: continue
	        			absIso += pf.pT
  	 
          			if (absIso/pf_pt[i] >0.1): isVeto =  False
          			#if (self.TrackIso(pf)/pf_pt[i] >0.1): isVeto =  False
      			else:
				if (pf_pt[i] < 5.): return False
	    			# compute isolation
				absIso = 0
   	    			for j in range(n):
	   	 			#if pfcands.pT == thispf.pT && pfcands.eta == thispf.eta   
	   	 			# do not count the orginal pf
	    				if i == j: continue
	    				# skip neutral particules
    	    				dr = common.deltaR( pf_phi[i], pf_eta[i], pf_phi[j], pf_eta[j])
	       				# check size of the code
    	    				if dr > 0.3 : continue # skip pfcands outside the cone
	        			absIso += pf.pT
          			if (self.TrackIso(pf)/pf_pt[i] >0.2): isVeto =  False;
        		if isVeto:		
				vetotracks+=1;
     		    #if (FoundLep2):
         #		if common.deltaR(pf.phi, pf.eta, lep2.phi, lep2.eta) < 0.1: continue
     	#	    	if self.isVetoTrack(pf, lep2):
        #			vetotracks+=1;

        		#isoTracks_isVetoTrack.push_back(true);
     		   #else isoTracks_isVetoTrack.push_back(false);
   
   		#if vetotracks<1 :	self.PassTrackVeto = True;
   		#else: 			self.PassTrackVeto = False;
   		if vetotracks<1 :	
		     return True;
   		return False
  

    ##########################################################################
    #  _____                 _              _           _   _                #
    #  | ____|_   _____ _ __ | |_   ___  ___| | ___  ___| |_(_) ___  _ __    #
    #  |  _| \ \ / / _ \ '_ \| __| / __|/ _ \ |/ _ \/ __| __| |/ _ \| '_ \   #
    #  | |___ \ V /  __/ | | | |_  \__ \  __/ |  __/ (__| |_| | (_) | | | |  #
    #  |_____| \_/ \___|_| |_|\__| |___/\___|_|\___|\___|\__|_|\___/|_| |_|  #
    #                                                                        #
    ##########################################################################


    #branchesForPVSelection = []
    def pvSelection(self,event):
        if abs(event.pv_z) >24 : return False
	if event.pv_rho > 2 : return False 
        if event.pv_ndof <= 4 : return False
        if event.pv_isFake : return False
        return True

    def pvDump( self,event):
    	print "pv_rho = ", event.pv_rho
    	print "pv_z = ", event.pv_z
    	print "pv_ndof = ", event.pv_ndof
    	print "pv_isFake = ", event.pv_isFake

    
    branchesForEventSelection = [ 'pv_z', 'pv_rho', 'pv_ndof', 'pv_isFake' ]
    def eventSelector(self,event, sCode ) :

	selectionCode = 0
	returnBool = True

	#PV selection
	if self.pvSelection(event) == False: 
	    returnBool =  False
        else : 
	    selectionCode+=1

        # At least on selected lepton
        if (len(self.selectedLeptons) != 1) :
	    returnBool = False
	else : 
	    selectionCode+=10
	# new    
	if len(self.selectedLeptons2) != 0 :
	    returnBool = False
        if len(self.vetoLeptons)!=  0:
	    returnBool = False
	
	##############
	# At least three jets
        if (len(self.selectedJets)     < 3) : 
	    returnBool =  False
        else : 
	    selectionCode+=100

        #print "sel-Code = ", selectionCode
        sCode.append(selectionCode)

	########################################
	# The following methods should be called 
	# once we've selected the leptons
	########################################

	#to reduce time - only comute this for event passing the selection:
	if returnBool:
	# tupling of pfcands => No, just check for basic selection (charge, pt, dz)
	# required to compute isoTrackVeto
	# should be called before doingn isoTrackVeto
	    self.pfCandTupling(event)
	
	    # Test TrackVeto
	    self.PassTrackVeto  = self.isoTrackVeto(event)


	###########################

	# Test TauVeto
	self.PassTauVeto  = self.isTauVeto(event)

        return returnBool

    ##################################################
    # this method should be called before computing 
    # variables ..
    # will write METP4, leadingLepton and selJetsP4
    # selJetsP4BtagOrdered (max b-tagged first)
    ##################################################
    
    def createTLorentzVector(self, event):
	
	#MET
	self.METP4 = TLorentzVector()
	self.METP4.SetPtEtaPhiE(event.met_pt,0,event.met_phi,event.met_pt)
        
	# leading Lepton
	self.oneLepton = False
	self.leadingLepton = TLorentzVector()
	if len(self.selectedLeptons) >0:
	    self.oneLepton = True
	    self.leadingLepton.SetPtEtaPhiE(self.selectedLeptons[0].pT, self.selectedLeptons[0].eta, self.selectedLeptons[0].phi, self.selectedLeptons[0].E)
	    self.leadingLeptonIso = self.selectedLeptons[0].iso

        # selectedJets
	# create tuple (TLorentzVector, btagDiscri, btagBool, DR(l,jet), DPhi(l,jet), DPhi(jet, MET)
	self.selJetsP4 = []
	selectedJets = self.selectedJets
	for jet in selectedJets:
	    j = TLorentzVector()
	    j.SetPtEtaPhiE(jet.pT, jet.eta, jet.phi, jet.E)
	    dr = j.DeltaR(self.leadingLepton)
	    dphi = abs(j.DeltaPhi(self.leadingLepton))
	    dphiMET = abs(j.DeltaPhi(self.METP4))
	    self.selJetsP4.append((j, jet.CSVv2,jet.bTag, dr, dphi, dphiMET))

	self.selJetsBtagOrdered = [i[0] for i in sorted(self.selJetsP4, key=lambda j: j[2], reverse=True)]
	#self.selJetPtOrdered = [i[0] for i in sorted(self.selJetsP4, key=lambda j: j[2], reverse=True)]

