from collections import namedtuple
from core        import commonFunctions as common
from ROOT import TLorentzVector

class Selection :
    
   
    def __init__(self):
    	self.resetSelectedObjects()
	self.loadPFcand = True
	self.load_qg_tag = False
	self.dphi_ak4pfjets_met = 9999
	self.electronPtCut = 20
	self.muoonPtCut = 20
	self.jet_multiplicity = 3
	#self.btagCut = 0.89
	self.btagCut = 0.8

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
        self.selectedGenJets      = []
        self.ak8selectedJets      = []
        self.ak10selectedJets      = []
	self.pfcands = []
        self.ngoodbtags = 0
	#self.trigger = {}
	self.trigger = {"HLT_IsoMu20":False,"HLT_IsoMu22":False,"HLT_Ele25_eta2p1_WPLoose":False,"HLT_Ele27_eta2p1_WPLoose":False,"HLT_PFMET100_PFMHT100_IDTight":False,"HLT_PFMET170":False}

	self.dphi_ak4pfjets_met = 999

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


    branchesForTrigger = ["trigger_name", "trigger_pass"]

    def FillTriggerInfo(self, event):
        #print "filling trigger info"
	
	trig_name = event.trigger_name
	trig_pass = event.trigger_pass
	
	#for i in xrange(len(trig_name)):
	for i, name in enumerate(trig_name):
		if "HLT_IsoMu20" in name:
			if bool(trig_pass[i]): self.trigger["HLT_IsoMu20"] =  bool(trig_pass[i])
		if "HLT_IsoMu22" in name:
			if bool(trig_pass[i]): self.trigger["HLT_IsoMu22"] =  bool(trig_pass[i])
		if "HLT_Ele25_eta2p1_WPLoose" in name: 
			if bool(trig_pass[i]): self.trigger["HLT_Ele25_eta2p1_WPLoose"] =  bool(trig_pass[i])
		if "HLT_Ele27_eta2p1_WPLoose" in name: 
			if bool(trig_pass[i]): self.trigger["HLT_Ele27_eta2p1_WPLoose"] =  bool(trig_pass[i])
		if "HLT_PFMET170" in name:
			if bool(trig_pass[i]): self.trigger["HLT_PFMET170"] =  bool(trig_pass[i])
		if "HLT_PFMET100_PFMHT100_IDTight" in name:
			if bool(trig_pass[i]): self.trigger["HLT_PFMET100_PFMHT100_IDTight"] =  bool(trig_pass[i])
	
	#print self.trigger


    branchesForGenInfo = ["gen_n", "gen_pt", "gen_eta", "gen_phi", "gen_m", "gen_status", "gen_id", "gen_charge", "gen_index", "gen_mother_index", "gen_daughter_n", "gen_daughter_index", "gen_neutralino_m", "gen_stop_m"]
    branchesForStop = ["gen_neutralino_m", "gen_stop_m"]
    branchesForGenMET = ["metGen_pt", "metGen_phi"]
    branchesForMCTruth = ["mc_truth_tWl1_status", "mc_truth_tWl2_status"]

    
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
    jet    = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'qgtag', 'axis2', 'ptD', 'mult', 'partonFlavour', 'hadronFlavour' , 'PUid', 'bTag', 'looseID' ])
    #jet    = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'qgtag', 'axis2', 'ptD', 'mult', 'partonFlavour', 'PUid', 'bTag', 'looseID' ])
    #to be corrected
    #jet    = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'partonFlavour', 'PUid', 'bTag', 'looseID' ])
    genjet    = namedtuple('genjet',    [ 'E', 'pT', 'eta', 'phi', 'mass'])
    ak8jet = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'softdropMass', 'trimmedMass', 'prunedMass', 'corrprunedMass', 'filteredMass', 'minMass', 'topMass', 'nSubJets', 'tau1', 'tau2', 'tau3' ])
    ak10jet = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSVv2', 'softdropMass', 'trimmedMass', 'prunedMass', 'filteredMass', 'minMass', 'topMass', 'nSubJets', 'tau1', 'tau2', 'tau3' ])
    pfc    = namedtuple('pfcand',    [ 'pT', 'eta', 'phi', 'charge', 'id' ])


    # ####### #
    # pfcanfs #
    # ####### #

    branchesForPfcand = ["pfcand_n", "pfcand_E", "pfcand_pt", "pfcand_eta", "pfcand_phi", "pfcand_dz", "pfcand_charge", "pfcand_id", "pfcand_trackIso"]

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
	#for i in range(n):
	for i in range(len(pt)):
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
    				"tau_decayModeFindingNewDMs",
    				"tau_decayModeFindingOldDMs",
				"tau_byMediumCombinedIsolationDeltaBetaCorr3Hits"]
				#"tau_byMediumIsolationMVA3newDMwLT"] #@EC@ not found in Medusa-patch1-20160615#

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
	#id 	=  event.tau_byMediumIsolationMVA3newDMwLT
	#decayMode = event.tau_decayModeFindingNewDMs
	decayMode = event.tau_decayModeFindingOldDMs #@MJ@ TODO


	lep1 = self.lepton(0,0,0,0,0,0,0,0,0,0)
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
	    if not decayMode[i]: continue
	    if charge[i]*int(lep1.charge)>=0: continue
	    dR = 1
	    if FoundLep1:
	        dR = common.deltaR(phi[i],eta[i],lep1.phi, lep1.eta)
	    if dR>0.4:
	    	#print "tau with pt = ", pt[i], " eta = ", eta[i], " charge = ", charge[i], " id = ", id[i]
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
				 "mu_isLooseMuon", "mu_isMediumMuon", "mu_isTightMuon",
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
            #print "isLooseMuon           =", bool(event.mu_isLooseMuon[i])
            #print "isMediumMuon          =", bool(event.mu_isMediumMuon[i])
            print "isTightMuon           =", bool(event.mu_isTightMuon[i])
            print "miniIso               =", event.mu_miniIso[i]
            #print "SUSYminiIso           =", event.mu_SUSYminiIso[i]
            print "charge	         =", event.mu_charge[i]
	    print "isLooseMuon		 =", bool(event.mu_isLooseMuon[i])



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
	isTightMuon	      = event.mu_isTightMuon


	for i in range(n) :
	    #print "muon with pt = ", pt[i]
	    # Reject muons than can either be veto or selected
	    if abs(eta[i]) >= 2.4  : continue
	    if abs(pt[i]) <= 5  : continue
	    if abs(dxy[i]) >= 0.1 : continue
	    if abs(dz[i]) >= 0.5  : continue	
            if miniIso[i] >= 0.2 : continue
	    if not isLooseMuon[i]: continue

	    #print " > pass"
            # Require tight ID
	    veto = True
	    if isTightMuon[i]  and abs(dxy[i])<0.02 and abs(dz[i])<0.1 and miniIso[i]<0.1:
	        # Selected muon
	    	#print " > here"
		
		
		#CHANGE
		#if abs(eta[i]) < 2.1 and pt[i] >= 30:
		if abs(eta[i]) < 2.1 and pt[i] > self.muonPtCut:
		    #print "sel"
		    veto = False
		    self.selectedLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )
		# Loose selection
		elif pt[i] > 5 and abs(eta[i])<2.4:
		    #print "sel2"
		    veto = False
		    self.selectedLeptons2.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )
	    # Veto muon
	    else:
		#print "veto"
	    #if veto:
	        self.vetoLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], isMediumMuon[i], dz[i], dxy[i], charge[i]) )

	#print "len muon :", len(self.selectedLeptons), len(self.selectedLeptons2), len(self.vetoLeptons)
	# Check DR btw selected good leptons and veto muons
	# for vmuon in self.vetoLeptons)
	

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
                                     "el_vetoStopID", "el_mediumStopID",
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
	vetoStopID     	  = event.el_vetoStopID
	mediumStopID      = event.el_mediumStopID
	

	selected = False
	veto = False

        for i in range(n) :
	    #print "electron with pt = ", pt[i]
            # Loose criteria applied for the veto leptons
	    if pt[i] <= 5  : continue
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
	    #print " > step 1"	    
#	    if (abs(scleta[i]) <= 1.479) :
#                if (see[i]              >= 0.012 )  : continue
#		if (abs(dEtaSCTrack[i]) >= 0.0126 )  : continue
            #    if (abs(dPhiSCTrack[i]) >= 0.107 )  : continue
            #    if (hadronicOverEm[i]   >= 0.186 )  : continue
            #    if (IoEmIoP[i]          >= 0.239 )  : continue
            #    if (abs(dxy[i])         >= 0.0621 ) : continue
            #    if (abs(dz[i])          >= 0.613 )  : continue
            #else :
            #    if (see[i]              >= 0.0339 ) : continue
            #    if (abs(dEtaSCTrack[i]) >= 0.0109 ) : continue
            #    if (abs(dPhiSCTrack[i]) >= 0.219 ) : continue
            #    if (hadronicOverEm[i]   >= 0.0962 ) : continue
            #    if (IoEmIoP[i]          >= 0.141 ) : continue
            #    if (abs(dxy[i])         >= 0.279 ) : continue
            #    if (abs(dz[i])          >= 0.947 ) : continue

            #if not (passConversionVeto[i] )  : continue
            #if (numberOfLostHits[i]   >  3)  : continue
	    
	    
	    #  replace by
	    if not vetoStopID[i]: continue
#	    if (abs(scleta[i]) <= 1.479) :
#                if (see[i]              >=  0.0114  )  : continue
#		if (abs(dEtaSCTrack[i]) >=  0.0152  )  : continue
#                if (abs(dPhiSCTrack[i]) >=  0.216  )  : continue
#                if (hadronicOverEm[i]   >=  0.181  )  : continue
#                if (IoEmIoP[i]          >=  0.207  )  : continue
#                if (abs(dxy[i])         >=  0.0564  ) : continue
#                if (abs(dz[i])          >=  0.472  )  : continue
#            	if (numberOfLostHits[i]   >  2)  : continue
#            else :
#                if (see[i]              >=  0.0352  ) : continue
#                if (abs(dEtaSCTrack[i]) >=  0.0113  ) : continue
#                if (abs(dPhiSCTrack[i]) >=  0.237  ) : continue
#                if (hadronicOverEm[i]   >=  0.116  ) : continue
#                if (IoEmIoP[i]          >=  0.174   ) : continue
#                if (abs(dxy[i])         >=  0.222  ) : continue
#                if (abs(dz[i])          >=  0.921  ) : continue
#            	if (numberOfLostHits[i]   >  3)  : continue
#
#            if not (passConversionVeto[i] )  : continue
	    #print " > loose sel"	    


            # Electron ID
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, medium
            # consistent with r19 (r13 in sync' - v1
            
	    passMediumID = False
#	    if (abs(scleta[i]) <= 1.479) :
#		if(
#                   (see[i]              <  0.0101  )  and
#		   (abs(dEtaSCTrack[i]) <  0.0094 )  and 
#                   (abs(dPhiSCTrack[i]) <  0.0296 )  and
#                   (hadronicOverEm[i]   <  0.0372 )  and
#                   (IoEmIoP[i]          <  0.118 )  and
#                   (abs(dxy[i])         <  0.0151 )  and
#                   (abs(dz[i])          <  0.238 ))  :
#		     selected = True
#            else :
#                if(
#                   (see[i]              <  0.0287  )  and
#		   (abs(dEtaSCTrack[i]) <  0.00773  ) and
            #       (abs(dPhiSCTrack[i]) <  0.148  )  and
            #       (hadronicOverEm[i]   <  0.0546  )  and
            #       (IoEmIoP[i]          <  0.104  )  and
            #       (abs(dxy[i])         <  0.0535  )  and
            #       (abs(dz[i])          <  0.572  ))  :
	    #	     selected = True
            #if not (passConversionVeto[i] )  : selected = False
            #if (numberOfLostHits[i]   >  1)  : selected = False
	    
	    #replaced by
	    if mediumStopID[i]: selected = True
#	    if (abs(scleta[i]) <= 1.479) :
#		if(
#            	   (numberOfLostHits[i]   <=  2)  and 
#                   (see[i]              <   0.0101   )  and
#		   (abs(dEtaSCTrack[i]) <   0.0103  )  and 
#                   (abs(dPhiSCTrack[i]) <   0.0336  )  and
#                   (hadronicOverEm[i]   <   0.0876  )  and
#                   (IoEmIoP[i]          <   0.0174   )  and
#                   (abs(dxy[i])         <   0.0118   )  and
#                   (abs(dz[i])          <   0.373  ))  :
#		     selected = True
#            else :
#                if(
#            	   (numberOfLostHits[i] <= 1)  and 
#                   (see[i]              <   0.0287  )  and
#		   (abs(dEtaSCTrack[i]) <   0.00773  ) and
#                   (abs(dPhiSCTrack[i]) <   0.114   )  and
#                   (hadronicOverEm[i]   <   0.0678   )  and
#                   (IoEmIoP[i]          <   0.0898   )  and
#                   (abs(dxy[i])         <   0.0739   )  and
#                   (abs(dz[i])          <   0.602   ))  :
#		     selected = True
#
#            if not (passConversionVeto[i] )  : selected = False
#	    passMediumID = selected

	    veto = True
	    if selected:
	       #CHANGE
	       #if pt[i] > 40 and abs(eta[i])< 2.1 and miniIso[i]<0.1:
	       if pt[i] > self.electronPtCut and abs(eta[i])< 1.4442 and miniIso[i]<0.1:
                   veto = False
		   self.selectedLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))
	       elif pt[i] > 5 and abs(eta[i])<2.4 and miniIso[i]<0.2:
                   veto = False
		   self.selectedLeptons2.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))
	    #if veto:
            else:
	    	self.vetoLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i], passMediumID, dz[i], dxy[i], charge[i]))
	    
	    #print " > veto, selected: ", veto, selected
	
	#print "leptons collection size: ", len(self.selectedLeptons), len(self.selectedLeptons2), len(self.vetoLeptons)




    # ############### #
    # Lepton cleaning #
    # ############### #

   

    def leptonCleaning(self):
    	
	# make a copy
	vetoLeptons = self.vetoLeptons
	# reset the collection
	self.vetoLeptons = []

	#print "cleaning"
	for vlep in vetoLeptons:
	    minDr = 9999
	    # computing minDR with selected leptons
	    for rlep in self.selectedLeptons:
		dR = common.deltaR(vlep.phi,vlep.eta,rlep.phi,rlep.eta)
	    	if dR < minDr : dr = minDr	
	    # computing minDR with selected leptons 2
	    for rlep in self.selectedLeptons2:
		dR = common.deltaR(vlep.phi,vlep.eta,rlep.phi,rlep.eta)
	    	if dR < minDr : dr = minDr	
	    #print "dr = ", minDr
	    if minDr>0.01:
	    	self.vetoLeptons.append(vlep)


    # #### #
    # Jets #
    # #### #

   

    branchesForAk8JetSelection = ["ak8jet_n",
                                  "ak8jet_E", "ak8jet_pt", "ak8jet_eta",   "ak8jet_phi",
                                  "ak8jet_CSVv2",
                                  "ak8jet_tau1" , "ak8jet_tau2", "ak8jet_tau3",
				  "ak8jet_softdrop_mass", "ak8jet_trimmed_mass", "ak8jet_pruned_mass", "ak8jet_corrpruned_mass", "ak8jet_filtered_mass",
				  "ak8jet_minMass", "ak8jet_topMass",
				  "ak8jet_nSubJets"
				 ]
    
    def ak8jetSelector(self,event) :

        n           = event.ak8jet_n
        E           = event.ak8jet_E
        pt          = event.ak8jet_pt
        eta         = event.ak8jet_eta
        phi         = event.ak8jet_phi
        CSVv2       = event.ak8jet_CSVv2
	softdrop_mass	 = event.ak8jet_softdrop_mass
	trimmed_mass	 = event.ak8jet_trimmed_mass
	filtered_mass  	= event.ak8jet_filtered_mass
	pruned_mass	= event.ak8jet_pruned_mass
	corrpruned_mass	= event.ak8jet_corrpruned_mass
	minMass 	= event.ak8jet_minMass
	topMass 	= event.ak8jet_minMass
	tau1 		= event.ak8jet_tau1
	tau2 		= event.ak8jet_tau2
	tau3 		= event.ak8jet_tau3
	nSubJets	= event.ak8jet_nSubJets
        
	selectedJets = []
	selectedJetsOrg = []


	for i in range(n) :

            # No selection for the moment (Apply pT and eta later)
	    self.ak8selectedJets.append(self.ak8jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSVv2[i],
					      softdrop_mass[i], trimmed_mass[i], pruned_mass[i], corrpruned_mass[i], filtered_mass[i],
					      minMass[i], topMass[i],
					      nSubJets[i],
					      tau1[i], tau2[i], tau3[i]
					      ))


    branchesForAk10JetSelection = ["ak10jet_n",
                                  "ak10jet_E", "ak10jet_pt", "ak10jet_eta",   "ak10jet_phi",
                                  "ak10jet_CSVv2",
                                  "ak10jet_tau1" , "ak10jet_tau2", "ak10jet_tau3",
				  "ak10jet_softdrop_mass", "ak10jet_trimmed_mass", "ak10jet_pruned_mass", "ak10jet_filtered_mass",
				  "ak10jet_minMass", "ak10jet_topMass",
				  "ak10jet_nSubJets"
				 ]
    
    def ak10jetSelector(self,event) :
        
        n           = event.ak10jet_n
        E           = event.ak10jet_E
        pt          = event.ak10jet_pt
        eta         = event.ak10jet_eta
        phi         = event.ak10jet_phi
        CSVv2       = event.ak10jet_CSVv2
	softdrop_mass	 = event.ak10jet_softdrop_mass
	trimmed_mass	 = event.ak10jet_trimmed_mass
	filtered_mass  	= event.ak10jet_filtered_mass
	pruned_mass	= event.ak10jet_pruned_mass
	minMass 	= event.ak10jet_minMass
	topMass 	= event.ak10jet_minMass
	tau1 		= event.ak10jet_tau1
	tau2 		= event.ak10jet_tau2
	tau3 		= event.ak10jet_tau3
	nSubJets	= event.ak10jet_nSubJets
        
	selectedJets = []
	selectedJetsOrg = []


	for i in range(len(E)) :

            # No selection for the moment (Apply pT and eta later)
	    self.ak10selectedJets.append(self.ak10jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSVv2[i],
					      softdrop_mass[i], trimmed_mass[i],  pruned_mass[i], filtered_mass[i],
					      minMass[i], topMass[i],
					      nSubJets[i],
					      tau1[i], tau2[i], tau3[i]
					      ))

    # ######### #
    #  Gen Jets #
    # ######### #
    branchesForGenJetSelection = [ "genJet_n",
                                   "genJet_E", "genJet_pt", "genJet_eta",   "genJet_phi",
                                   "genJet_m",
				   ]

    def genJetDump(self,event):
        gj_n    = event.genJet_n
        gj_E    = event.genJet_E
        gj_pt   = event.genJet_pt
        gj_eta  = event.genJet_eta
        gj_phi  = event.genJet_phi
        gj_m    = event.genJet_m
    
    def genJetSelector(self,event) :

        gj_n    = event.genJet_n
        gj_E    = event.genJet_E
        gj_pt   = event.genJet_pt
        gj_eta  = event.genJet_eta
        gj_phi  = event.genJet_phi
        gj_m    = event.genJet_m

        #print "number of gen jets: %d" %gj_n
        
	selectedGenJets = []
	
        for i in range(gj_n) :

            #print "gen get pt: %d" % gj_pt[i]
	    selectedGenJets.append(self.genjet(gj_E[i],
                                              gj_pt[i],
                                              gj_eta[i],
                                              gj_phi[i],
					      gj_m[i]))

        #print "size of selectedgenjet in selector %d" % len(selectedGenJets)
        self.selectedGenJets = selectedGenJets
        #print "size of self selectedgenjet in selector %d" % len(self.selectedGenJets)
        
           

    # #### #
    # Jets #
    # #### #



    branchesForJetSelection = [ "jet_n",
                                "jet_E", "jet_pt", "jet_eta",   "jet_phi",
                                "jet_CSVv2",
				"jet_pileupJetId" ,
				"jet_looseJetID",
				"jet_partonFlavour",
				"jet_hadronFlavour"
				#"jet_tightJetID"
				]

    branchesForQGJetSelection = [
                                "jet_qgtag",
                                "jet_qgtag_axis2",
                                "jet_qgtag_ptD",
                                "jet_qgtag_mult",
				]
    
    def jetDump(self,event):
        n   	    = event.jet_n
        E           = event.jet_E
        pt          = event.jet_pt
        eta         = event.jet_eta
        phi         = event.jet_phi
        CSVv2       = event.jet_CSVv2
        looseID     = event.jet_looseJetID
	qgtag = [-999]*n
	axis2 = [-999]*n
	ptD = [-999]*n
	mult = [-999]*n
        if self.load_qg_tag:
	    qgtag	    = event.jet_qgtag
	    axis2	    = event.jet_qgtag_axis2
	    ptD	    = event.jet_qgtag_ptD
	    mult	    = event.jet_qgtag_mult
	partonFlavour = event.jet_partonFlavour
	hadronFlavour = event.jet_hadronFlavour

        for i in range(n):
	    j= TLorentzVector ()
	    j.SetPtEtaPhiE(pt[i],eta[i],phi[i],E[i])
	    dr = j.DeltaR(self.leadingLepton)
	    dphi = j.DeltaPhi(self.leadingLepton)
	    dphiMET = j.DeltaPhi(self.METP4)
	    #print "jet pt: ", pt[i], " eta: ", eta[i], " phi: ", phi[i], " E: ", E[i], " CSV: ",CSVv2[i], "QGT: ", qgtag[i], "DR(j,l): ",dr, "dphi(j.l:)",dphi, "dphi(j,MET):", dphiMET
   

   
    def selJetDump(self,event):
        jets = self.selJetsP4
        for mytuple in jets:
	    j = mytuple[0]
	    dr = j.DeltaR(self.leadingLepton)
	    dphi = j.DeltaPhi(self.leadingLepton)
	    dphiMET = j.DeltaPhi(self.METP4)
	    #print "jet pt: ", j.Pt(), " eta: ", j.Eta(), " phi: ", j.Phi(), " E: ", j.E(), " DR(j,l) : ",dr, " dphi(j,l): ",dphi, " dphi(j,MET): ", dphiMET
	    #print "jet pt: ", j.Pt(), " eta: ", j.Eta(), " phi: ", j.Phi(), " E: ", j.E(), "CSVv2: ", mytuple[1], "QGT: ", qgtag[i], " DR(j,l) : ",dr, " dphi(j,l): ",dphi, " dphi(j,MET): ", dphiMET
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
	qgtag = [-999]*n
	axis2 = [-999]*n
	ptD = [-999]*n
	mult = [-999]*n
        if self.load_qg_tag:
	    qgtag	    = event.jet_qgtag
	    axis2	    = event.jet_qgtag_axis2
	    ptD	    = event.jet_qgtag_ptD
	    mult	    = event.jet_qgtag_mult
	partonFlavour	 = event.jet_partonFlavour
	hadronFlavour	 = event.jet_hadronFlavour
        
	selectedJets = []
	selectedJetsOrg = []

	self.dphi_ak4pfjets_met = 9999
	for i in range(n) :

            # Apply pT and eta requirements
            if (pt[i]       <  30) : continue
            if (abs(eta[i]) > 2.4) : continue
	    if not looseID[i]: continue
	    #if not tightID[i]: continue
            
	    #compute self.dphi_ak4pfjets_met
	    #j = TLorentzVector ()
	    #j.SetPtEtaPhiE(pt[i],eta[i],phi[i],E[i])
	    #self.METP4 = TLorentzVector()
	    #self.METP4.SetPtEtaPhiE(event.met_pt,0,event.met_phi,event.met_pt)
	    #dphiM = j.DeltaPhi(self.METP4)
	    #if abs(dphiM) < self.dphi_ak4pfjets_met:
	    	#print "final old dphi: ", abs(dphiM)

	    #end

	    selectedJets.append(self.jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSVv2[i],
					      qgtag[i],
                                              axis2[i],
                                              ptD[i],
                                              mult[i],
                                              partonFlavour[i],
                                              hadronFlavour[i],
					      pileupJetId[i],
                                              (CSVv2[i] > self.btagCut),
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


        counter = 0
	for jts in self.selectedJets:
	    #compute self.dphi_ak4pfjets_met
            if counter == 0 or counter == 1:
	        j= TLorentzVector ()
	        j.SetPtEtaPhiE(jts.pT, jts.eta, jts.phi, jts.E)
	        self.METP4 = TLorentzVector()
	        self.METP4.SetPtEtaPhiE(event.met_pt,0,event.met_phi,event.met_pt)
	        dphiMET = j.DeltaPhi(self.METP4)
                #print "counter: ", counter
                #print "dphi: ", dphiMET
                counter += 1
	        if abs(dphiMET) < self.dphi_ak4pfjets_met:
	    	    self.dphi_ak4pfjets_met = abs(dphiMET)
                    #print "dphi final: ", self.dphi_ak4pfjets_met


	
	#print "jet collections: ", len(selectedJets), len(self.selectedJets), len(event.jet_pt)
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


    def dumpPFCand(self, event):
		n = int(event.pfcand_pt.size())
		pf_pt = event.pfcand_pt
		pf_eta = event.pfcand_eta
		pf_phi = event.pfcand_phi
		pf_charge = event.pfcand_charge
		pf_id = event.pfcand_id
		pf_trackIso =  event.pfcand_trackIso
		print "#### dump pf cand ##"
		#print event.pfcand_id
		print n
		for i in range(n):
			print i
			print "pt = ", pf_pt[i], " eta = ", pf_eta[i] , " charge = ", pf_charge[i], " id = ", pf_id[i], " trackIso = ", pf_trackIso[i]


    def isoTrackVeto(self, event):
		#load inf
		n = len(event.pfcand_pt)
		#print "nof pf cand: ", n
		pf_pt = event.pfcand_pt
		pf_eta = event.pfcand_eta
		pf_phi = event.pfcand_phi
		pf_dz = event.pfcand_dz
		pf_charge = event.pfcand_charge
		pf_id = event.pfcand_id
		pf_trackIso =  event.pfcand_trackIso


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
		
		#print "found lep1", FoundLep1
		vetotracks = 0
		for i in range(n):
	 	    #pt, eta, dz, iso has been applied on production
		    if pf_pt[i]< 10: continue
		    if abs(pf_eta[i])>2.4: continue
		    if abs(pf_dz[i]) >0.1: continue

		    #print i, " over ", n
		    if (FoundLep1): 
		    	#print "found"
			dR = common.deltaR(pf_phi[i], pf_eta[i], lep1.phi, lep1.eta)
			#if dR < 0.1: continue  
			## inline computation of isVetoTrack
			isVeto = True
			#print "charge, pt", lep1.charge, lep1.pT
			#print "pf pt = ", pf_pt[i]," dr = ", dR, " id = ", pf_id[i], "charge*charge = ", pf_charge[i]," *  ", #lep1.charge, pf_trackIso[i]
			if dR < 0.4: isVeto =  False
      		        # if not electron or muon
      		        #solve a bug here !! - requirement was inverted
			#print "here"
			if abs(pf_id[i])==11 or abs(pf_id[i])==13:  
				continue
				#break
			# opposite chrage requirement btw sel lepton and pfcand
			#print "here"
			if (pf_charge[i] * lep1.charge > 0): isVeto = False
           		 
        		if isVeto:		
				#print "pt = ", pf_pt[i], " eta = ", pf_eta[i], " id = ", pf_id[i], " dR = ", dR, " charge = ", pf_charge[i], pf_charge[i] * lep1.charge 
			        #print "isotrack" ", pf pt = ", pf_pt[i]," dr = ", dR, " id = ", pf_id[i], "charge*charge = ", pf_charge[i]," *  ", lep1.charge, pf_trackIso[i] 
				vetotracks+=1;

			#print "n-pf: ", n, "vetotracks = ", vetotracks
		
		
		#print "what's going on"
		#print "n-pf: ", n, "vetotracks = ", vetotracks
		if vetotracks<1 :	
		     return True;
   		return False


    def isoTrackVetoOld(self, event):
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
		for i in range(len(pf_isSel)):
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

	# commented only for Marketa study //@MJ@ TODO use this again!!!!

        # At least on selected lepton
        #if (len(self.selectedLeptons) != 1) :
	#    returnBool = False
	#else : 
	#    selectionCode+=10
	# new    
	
	#if len(self.selectedLeptons2) != 0 :
	#    returnBool = False
        #if len(self.vetoLeptons)!=  0:
	#    returnBool = False
	
	##############
	# At least three jets
        # CHANGE
	#if (len(self.selectedJets)     < 2) : 
        #if (len(self.selectedJets)     < self.jet_multiplicity) : 
	#    returnBool =  False
        #else : 
	#    selectionCode+=100

        #print "sel-Code = ", selectionCode
        sCode.append(selectionCode)

	########################################
	# The following methods should be called 
	# once we've selected the leptons
	########################################

	#to reduce time - only comute this for event passing the selection:
	if returnBool and self.loadPFcand:
	# tupling of pfcands => No, just check for basic selection (charge, pt, dz)
	# required to compute isoTrackVeto
	# should be called before doingn isoTrackVeto
            #print "this should not be called"
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

        # selectedGenJets
	#selectedGenJets = self.selectedGenJets
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

