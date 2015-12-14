from ROOT import TLorentzVector, std
import rootpy.stl as stl

###########################################################################################
#   ____        _           _               _         __                            _     #
#  | __ )  __ _| |__  _   _| |_ _   _ _ __ | | ___   / _| ___  _ __ _ __ ___   __ _| |_   #
#  |  _ \ / _` | '_ \| | | | __| | | | '_ \| |/ _ \ | |_ / _ \| '__| '_ ` _ \ / _` | __|  #
#  | |_) | (_| | |_) | |_| | |_| |_| | |_) | |  __/ |  _| (_) | |  | | | | | | (_| | |_   #
#  |____/ \__,_|_.__/ \__, |\__|\__,_| .__/|_|\___| |_|  \___/|_|  |_| |_| |_|\__,_|\__|  #
#                      |___/          |_|                                                 #
###########################################################################################


class BabyTupleFormat :

    def __init__(self):
	self.doIsoStudy = False
	self.saveGenInfo = True
    	self.saveAK8 = False	
	self.saveGenMET = False

    	self.babyTupleFormat = { 
	
	      ##################
	      # common format  #
	      ##################
	
	      ######## global quantites   ###
	      'run'                    :  'I',
	      'ls'   	               :  'I',
	      'event'                  :  'I',
	      'mc_weight'              :  'D',
	
	      'PassTrackVeto'	:	'B',
	      'PassTauVeto'	:	'B',
	
	      ## lepton 1: leading lepton
	      'lep1_pdgid'		:	'I',
	      'lep1_pt'			:	'F',
	      'lep1_eta'		:	'F',
	      'lep1_phi'		:	'F',
	      'lep1_mass'		:	'F',
	      'lep1_passVeto'		:	'F',
	      'lep1_passMediumID'	:	'F',
	      'lep1_dz'			:	'F',
	      'lep1_d0'			:	'F',
	      'lep1_MiniIso'		:	'F',
	      
	      ## lepton 2: second leading lepton
	      'lep2_pdgid'		:	'I',
	      'lep2_pt'			:	'F',
	      'lep2_eta'		:	'F',
	      'lep2_phi'		:	'F',
	      'lep2_mass'		:	'F',
	      'lep2_passVeto'		:	'F',
	      'lep2_passMediumID'	:	'F',
	      'lep2_dz'			:	'F',
	      'lep2_d0'			:	'F',
	      'lep2_MiniIso'		:	'F',
	      
	      # vector of jets are pt ordered
	      'ak4pfjets_pt'		: 'vector<float>',
	      'ak4pfjets_eta'		: 'vector<float>',
	      'ak4pfjets_phi'		: 'vector<float>',
	      'ak4pfjets_mass'		: 'vector<float>',
	      'ak4pfjets_CSV'		: 'vector<float>',
	      'ak4pfjets_loose_pfid'	: 'vector<bool>',
	      'ak4pfjets_puid'		: 'vector<float>',
	      'ak4pfjets_qgtag'		: 'vector<float>',
	      'ak4pfjets_partonFlavour'	: 'vector<float>',
	      'dphi_ak4pfjets_met'	:	'F',
	
	      #Store the following event variables: 
	      'ak4pfjets_rho'		:	'F',
	      #pf - type1 corrected
	      'pfmet'			:	'F',
	      'pfmet_phi'		:	'F',
	      'mt_met_lep'		:	'F',
	      'ngoodjets'		:	'I',	#number of selected jets 
	      'ngoodbtags'		:	'I',	#number of selected btag jets 
	      'ngoodleps'		:	'I',	#number of selected leptons 
	      'nvetoleps'		:	'I',	#number of leptons that pass the veto selection 
	      'genlepsfromtop'		:	'I',	
	      #inumber of gen-level leptons (e, mu,tau) from top decays; used to classify ttbar=>1lep+Jets, ttbar=>2lep mc events
	
	      # discriminating variables
	      'MT2W'		:	'F',
	      'chi2'		:	'F',  #hadronic chi2 
	      'topness'		:	'F',
	      'dphi_Wlep'	:	'F',  #DeltaPhi(l,W) using lep1 
	      'ak4_HT'		:	'F',  # HT of selected jets 
	      'ak4_htssm'	:	'F',  # HT of selected jets on same hemisphere as met 
	      'ak4_htosm'	:	'F',  # HT of selected jets on opposite hemisphere as met 
	      'Mlb'		:	'F',  # M(lb), mass of lep1 + closest b 
	      'Mjjj'		:	'F',  # M3b, mass of 3 jets most back to back to lep1 
	      'dR_lep_leadb'	:	'F',  # DeltaR(l,lead_b)  
	
	      #triggers
	      'HLT_SingleMu'	:	'B',
	      'HLT_SingleE'	:	'B',
	
	      # weights
	      'pu_weight'	:	'F',
	      'scale1fb'	:	'F',
	      'lep_sf'		:	'F',
	      'btag_sf'		:	'F',
	
	      ############################################
	      ## END COMMON FORMAT
	      ############################################
	      
	      
	      
	      'runId'                    :  'I',
	      'lumiId'                   :  'I',
	      'eventId'                  :  'I',
	
	      'numberOfSelectedLeptons'  :  'I',
	      
	      'leadingLeptonId'          :  'I',
	      'leadingLeptonPt'          :  'F',
	      'leadingLeptonPhi'         :  'F',
	      'leadingLeptonEta'         :  'F',
	      'leadingLeptonIso'         :  'F',
	      
	      'secondLeptonId'           :  'I',
	      'secondLeptonPt'           :  'F',
	      'secondLeptonPhi'          :  'F',
	      'secondLeptonEta'          :  'F',
	      'secondLeptonIso'          :  'F',
	
	      'numberOfSelectedJets'     :  'I',
	      'numberOfBTaggedJets'      :  'I',
	      'jetsPt'                   :  'F[6]',
	      'jetsPhi'                  :  'F[6]',
	      'jetsEta'                  :  'F[6]',
	      'jetsCSV'                  :  'F[6]',
	      'jetsCSVv2'                :  'F[6]',
	      'jetsPUid'                 :  'F[6]',
	
	      'ETmiss'                   :  'F',
	      'ETmissPhi'                :  'F',
	      'MT'                       :  'F',
	      'MT2W'                     :  'F',
	      'HT'                       :  'F',
	      'ak4_htosm'		 :  'F',
	      'M3b'			 :  'F',
	      'Mlb_leadb'		 :  'F',
	      'dphi_Wlep'		 :  'F',
	      'topness'			 :  'F',
	      'hadronic_top_chi2'        :  'F',
	      
	      'met_sig'                  :  'F',
	
	      #added: pv
	      'pv_ndof'			 :   'F',
	      'pv_isFake'                :   'I',
	      'pv_rho'                	 :   'F',
	      'pv_z'                	 :   'F',
	
	      'numberOfGeneratedLeptons' :  'I',
	     
	      'crossSection'             :  'F',
	      'totalNumberOfInitialEvent':  'I',
		
	      'numberOfSelectedElectrons' : 'I',
	      'numberOfSelectedMuons' : 'I',
	
	      'metGen_pt' : 'F',
	      'metGen_phi': 'F'
	}
	#for synchronisation
	self.babyTupleFormat['selectionCode'] = 'F'
	#for isolation study
    
    	# Additional input branches needed during the filling of the babytuple
    	self.branchesForMiscInfos = [ "ev_run", "ev_lumi", "ev_id", "mc_weight" ]
    
    ##############################
    # 	END OF CONSTRUCTOR       #
    ##############################
	
    def UpdateFormat(self):
	
	# store info for leading and second leading leptons (for each flavor)
	if self.doIsoStudy:
	   	# for electrons
	   	self.babyTupleFormat['el_miniIso']  =  'F[2]'
	        self.babyTupleFormat['el_relIsoDB']  =  'F[2]'
	        self.babyTupleFormat['el_relIsoEA']  =  'F[2]'
	        self.babyTupleFormat['el_pt']  =  'F[2]'
	        self.babyTupleFormat['el_eta']  =  'F[2]'
	        # for muons
	        self.babyTupleFormat['mu_miniIso']  =  'F[2]'
	        self.babyTupleFormat['mu_relIsoDB']  =  'F[2]'
	        self.babyTupleFormat['mu_pt']  =  'F[2]'
	        self.babyTupleFormat['mu_eta']  =  'F[2]'
	
     

        
    	if self.saveGenInfo:
	      	self.babyTupleFormat['gen_n'] =	 'I'
	        self.babyTupleFormat['gen_pt'] =	 "vector<float>"
	        self.babyTupleFormat['gen_eta'] =	 "vector<float>"
	        self.babyTupleFormat['gen_phi'] =	 "vector<float>"
	        self.babyTupleFormat['gen_m'] =	 "vector<float>"
	        self.babyTupleFormat['gen_status'] =	 "vector<int>"
	        self.babyTupleFormat['gen_id'] =	 "vector<int>"
	        self.babyTupleFormat['gen_charge'] =	 "vector<int>"
	        self.babyTupleFormat['gen_index'] =	 "vector<int>"
	        self.babyTupleFormat['gen_mother_index'] =	 "vector<int>"
	        self.babyTupleFormat['gen_daughter_n'] =	 "vector<int>"
	        self.babyTupleFormat['gen_daughter_index'] =	 "vector<vector<int> >"
	   

        if self.saveAK8:
       		self.babyTupleFormat['ak8pfjets_pt'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_eta'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_phi'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_mass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_CSV'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_softdrop_mass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_trimmed_mass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_pruned_mass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_filtered_mass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_minMass'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_topMass'] = "vector<float>"
       		self.babyTupleFormat['ak8pfjets_nSubJets'] =  "vector<int>"
       		self.babyTupleFormat['ak8pfjets_tau1'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_tau2'] =  "vector<float>"
       		self.babyTupleFormat['ak8pfjets_tau3'] =  "vector<float>"
   


    



    def fill(self,event,babyTupleTree) : #,saveGenInfo = False) :
        ############################
        #  common format           #
        ############################
      
	
        babyTupleTree.run              = event.ev_run
        babyTupleTree.ls               = event.ev_lumi
        babyTupleTree.event            = event.ev_id
        babyTupleTree.mc_weight        = event.mc_weight

        babyTupleTree.PassTrackVeto = self.PassTrackVeto
        babyTupleTree.PassTauVeto = self.PassTauVeto

        # filling lepton1
	if len(self.selectedLeptons) > 0 :
	    lepton = self.selectedLeptons[0]
	    babyTupleTree.lep1_pdgid = lepton.id
	    babyTupleTree.lep1_pt = lepton.pT
	    babyTupleTree.lep1_eta = lepton.eta
	    babyTupleTree.lep1_phi = lepton.phi
	    # compute Mass
	    lep = TLorentzVector()
	    lep.SetPtEtaPhiE(lepton.pT, lepton.eta, lepton.phi, lepton.E)
	    babyTupleTree.lep1_mass = lep.M()
	    babyTupleTree.lep1_passVeto = True	# by definition
	    babyTupleTree.lep1_passMediumID = True	# by definition
	    babyTupleTree.lep1_dz = lepton.dz
	    babyTupleTree.lep1_d0 = lepton.d0
	    babyTupleTree.lep1_MiniIso = lepton.iso
	    babyTupleTree.lep1_pdgid = lepton.id

	# filling lepton2
	lepton2 = self.lepton(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	foundLep2 = False
	if len(self.selectedLeptons) > 1:
	    lepton2 = self.selectedLeptons[1]
	    babyTupleTree.lep2_passVeto = True	# by definition
	    foundLep2 = True
	if len(self.selectedLeptons2) > 0:
	    lepton2 = self.selectedLeptons2[0]
	    babyTupleTree.lep2_passVeto = True	# by definition
	    foundLep2 = True
	if len(self.vetoLeptons) > 0:
	    lepton2 = vetoLeptons[0]
	    babyTupleTree.lep2_passVeto = False	# by definition
	    foundLep2 = True

	if foundLep2 :
	    babyTupleTree.lep2_pdgid = lepton2.id
	    babyTupleTree.lep2_pt = lepton2.pT
	    babyTupleTree.lep2_eta = lepton2.eta
	    babyTupleTree.lep2_phi = lepton2.phi
	    # compute Mass
	    lep = TLorentzVector()
	    lep.SetPtEtaPhiE(lepton2.pT, lepton2.eta, lepton2.phi, lepton2.E)
	    babyTupleTree.lep2_mass = lep.M()
	    babyTupleTree.lep2_dz = lepton2.dz
	    babyTupleTree.lep2_d0 = lepton2.d0
	    babyTupleTree.lep2_MiniIso = lepton2.iso
	    #babyTupleTree.lep2_passMediumID = lepton2.passMediumID
	else:
	    babyTupleTree.lep2_pdgid = 0
	    babyTupleTree.lep2_pt = 0
	    babyTupleTree.lep2_eta = -999
	    babyTupleTree.lep2_phi = 0
	    babyTupleTree.lep2_mass = 0
	    babyTupleTree.lep2_dz = 9999
	    babyTupleTree.lep2_d0 = 9999
	    babyTupleTree.lep2_MiniIso = 9999
	    #babyTupleTree.lep2_passMediumID = lepton2.passMediumID

	babyTupleTree.runId                   = event.ev_run
      
        # vector of jets are pt ordered
        v_jet_pt = stl.vector('float')()
        v_jet_eta = stl.vector('float')()
        v_jet_phi = stl.vector('float')()
        v_jet_mass = stl.vector('float')()
        v_jet_CSV = stl.vector('float')()
        v_jet_loose_pfid = stl.vector('bool')()
        v_jet_puid = stl.vector('float')()
        v_jet_qgtag = stl.vector('float')()
        v_jet_partonFlavour = stl.vector('float')()
	for jet in self.selectedJets:
	    v_jet_pt.push_back(jet.pT)
	    v_jet_eta.push_back(jet.eta)
	    v_jet_phi.push_back(jet.phi)
	    jetp4 = TLorentzVector()
	    jetp4.SetPtEtaPhiE(jet.pT, jet.eta, jet.phi, jet.E)
	    v_jet_mass.push_back(jetp4.M())
	    v_jet_CSV.push_back(jet.CSVv2)
	    v_jet_loose_pfid.push_back(bool(jet.looseID))
	    v_jet_puid.push_back(jet.PUid)
	    v_jet_qgtag.push_back(jet.qgtag)
	    v_jet_partonFlavour.push_back(jet.partonFlavour)
        babyTupleTree.ak4pfjets_pt	 =  v_jet_pt
        babyTupleTree.ak4pfjets_eta	 =  v_jet_eta
        babyTupleTree.ak4pfjets_phi	 =  v_jet_phi
        babyTupleTree.ak4pfjets_mass	 =  v_jet_mass
        babyTupleTree.ak4pfjets_CSV	 =  v_jet_CSV
        babyTupleTree.ak4pfjets_loose_pfid	 =  v_jet_loose_pfid
        babyTupleTree.ak4pfjets_puid	 =  v_jet_puid
        babyTupleTree.ak4pfjets_qgtag	 =  v_jet_qgtag
        babyTupleTree.ak4pfjets_partonFlavour	 =  v_jet_partonFlavour
       

	#ak8 jets
        # vector of jets are pt ordered
        
	v_ak8jet_E = stl.vector('float')()
        v_ak8jet_pt = stl.vector('float')()
        v_ak8jet_eta = stl.vector('float')()
        v_ak8jet_phi = stl.vector('float')()
        v_ak8jet_mass = stl.vector('float')()
        v_ak8jet_CSV = stl.vector('float')()
        v_ak8jet_tau1 = stl.vector('float')()
        v_ak8jet_tau2 = stl.vector('float')()
        v_ak8jet_tau3 = stl.vector('float')()
        v_ak8jet_softdrop_mass = stl.vector('float')()
        v_ak8jet_trimmed_mass = stl.vector('float')()
        v_ak8jet_pruned_mass = stl.vector('float')()
        v_ak8jet_filtered_mass = stl.vector('float')()
        v_ak8jet_minMass = stl.vector('float')()
        v_ak8jet_topMass = stl.vector('float')()
        v_ak8jet_nSubJets = stl.vector('int')()
	for jet in self.ak8selectedJets:
		v_ak8jet_pt.push_back(jet.pT)
		v_ak8jet_eta.push_back(jet.eta)
		v_ak8jet_phi.push_back(jet.phi)
	        jetp4.SetPtEtaPhiE(jet.pT, jet.eta, jet.phi, jet.E)
	        v_ak8jet_mass.push_back(jetp4.M())
		v_ak8jet_CSV.push_back(jet.CSVv2)
		v_ak8jet_softdrop_mass.push_back(jet.softdropMass)
		v_ak8jet_trimmed_mass.push_back(jet.trimmedMass)
		v_ak8jet_pruned_mass.push_back(jet.prunedMass)
		v_ak8jet_filtered_mass.push_back(jet.filteredMass)
		v_ak8jet_minMass.push_back(jet.minMass)
		v_ak8jet_topMass.push_back(jet.topMass)
		v_ak8jet_nSubJets.push_back(jet.nSubJets)
		v_ak8jet_tau1.push_back(jet.tau1)
		v_ak8jet_tau2.push_back(jet.tau2)
		v_ak8jet_tau3.push_back(jet.tau3)



        if self.saveAK8:
        	babyTupleTree.ak8pfjets_pt	 =  v_ak8jet_pt
        	babyTupleTree.ak8pfjets_eta	 =  v_ak8jet_eta
        	babyTupleTree.ak8pfjets_phi	 =  v_ak8jet_phi
        	babyTupleTree.ak8pfjets_mass	 =  v_ak8jet_mass
        	babyTupleTree.ak8pfjets_CSV	 =  v_ak8jet_CSV
        	babyTupleTree.ak8pfjets_softdrop_mass	 =  v_ak8jet_softdrop_mass
        	babyTupleTree.ak8pfjets_trimmed_mass	 =  v_ak8jet_trimmed_mass
        	babyTupleTree.ak8pfjets_pruned_mass	 =  v_ak8jet_pruned_mass
        	babyTupleTree.ak8pfjets_filtered_mass	 =  v_ak8jet_filtered_mass
        	babyTupleTree.ak8pfjets_minMass	 =  v_ak8jet_minMass
        	babyTupleTree.ak8pfjets_topMass	 =  v_ak8jet_topMass
        	babyTupleTree.ak8pfjets_nSubJets	 =  v_ak8jet_nSubJets
        	babyTupleTree.ak8pfjets_tau1	 =  v_ak8jet_tau1
        	babyTupleTree.ak8pfjets_tau2	 =  v_ak8jet_tau2
        	babyTupleTree.ak8pfjets_tau3	 =  v_ak8jet_tau3

	babyTupleTree.dphi_ak4pfjets_met	 = self.dphi_ak4pfjets_met

        #Store the following event variables: 
        babyTupleTree.ak4pfjets_rho  =	event.ev_rho
      
        #pf - type1 corrected
        babyTupleTree.pfmet		 = 	event.met_pt
        babyTupleTree.pfmet_phi		 = 	event.met_phi
        babyTupleTree.mt_met_lep	 = 	self.MT
        babyTupleTree.ngoodjets	 = len(self.selectedJets)	#number of selected jets 
        #to be changed
	#babyTupleTree.ngoodbtags	 = len(self.selectedLeptons)	#number of selected btag jets 
	babyTupleTree.ngoodbtags	 = self.ngoodbtags	#number of selected btag jets 
        babyTupleTree.ngoodleps	 = len(self.selectedLeptons)	#number of selected leptons 
        babyTupleTree.nvetoleps	 = len(self.vetoLeptons)	#number of leptons that pass the veto selection 
        babyTupleTree.genlepsfromtop	 = self.numberOfGeneratedLeptons

        # discriminating variables
        babyTupleTree.MT2W		= self.MT2W
        babyTupleTree.chi2		= self.hadchi2
        babyTupleTree.topness		= self.topness
        babyTupleTree.dphi_Wlep		= self.dphi_Wlep
        babyTupleTree.ak4_HT		= self.HT
        babyTupleTree.ak4_htosm		= self.HTOSM
        babyTupleTree.Mlb		= self.Mlb_leadb
        babyTupleTree.Mjjj		= self.M3b
        # not yet computed 
	babyTupleTree.dR_lep_leadb	= 0 #self.
        
	#triggers
	# will have to be filled
        #babyTupleTree.HLT_SingleMu	= True #
        #babyTupleTree.HLT_SingleE	= True # default
	#print self.trigger
	babyTupleTree.HLT_SingleMu = self.trigger.setdefault("HLT_IsoMu17_eta2p1_v2",False) or self.trigger.setdefault("HLT_IsoMu20_v2",False) or self.trigger.setdefault("HLT_IsoMu17_eta2p1_v1",False) or self.trigger.setdefault("HLT_IsoMu20_v1",False)
	babyTupleTree.HLT_SingleE = self.trigger.setdefault("HLT_Ele27_eta2p1_WPLoose_Gsf_v1",False) or self.trigger.setdefault("HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v1",False) or self.trigger.setdefault("HLT_Ele27_eta2p1_WPLoose_Gsf_v1",False)

        # weights
	# will have to be filled
        babyTupleTree.pu_weight		= 1.0
        babyTupleTree.scale1fb		= 1.0
        babyTupleTree.lep_sf		= 1.0
        babyTupleTree.btag_sf		= 1.0


	##################################
	#  end common format
	##################################

        babyTupleTree.runId                   = event.ev_run
        babyTupleTree.lumiId                  = event.ev_lumi
        babyTupleTree.eventId                 = event.ev_id
        
	babyTupleTree.numberOfSelectedMuons = self.selectedMuons
	babyTupleTree.numberOfSelectedElectrons = self.selectedElectrons
	babyTupleTree.numberOfSelectedLeptons = len(self.selectedLeptons)
	if len(self.selectedLeptons)>0:
            babyTupleTree.leadingLeptonId         = self.selectedLeptons[0].id
            babyTupleTree.leadingLeptonPt         = self.selectedLeptons[0].pT
            babyTupleTree.leadingLeptonEta        = self.selectedLeptons[0].eta
            babyTupleTree.leadingLeptonPhi        = self.selectedLeptons[0].phi
            #babyTupleTree.leadingLeptonIso        = self.selectedLeptons[0].miniIso
            babyTupleTree.leadingLeptonIso        = self.selectedLeptons[0].iso

        if (len(self.selectedLeptons) >= 2) :
            babyTupleTree.secondLeptonId      = self.selectedLeptons[1].id
            babyTupleTree.secondLeptonPt      = self.selectedLeptons[1].pT
            babyTupleTree.secondLeptonEta     = self.selectedLeptons[1].eta
            babyTupleTree.secondLeptonPhi     = self.selectedLeptons[1].phi
            #babyTupleTree.secondLeptonIso     = self.selectedLeptons[1].miniIso
            babyTupleTree.secondLeptonIso     = self.selectedLeptons[1].iso
        else :
            babyTupleTree.secondLeptonId      = 0
            babyTupleTree.secondLeptonPt      = -1
            babyTupleTree.secondLeptonEta     = -9
            babyTupleTree.secondLeptonPhi     = -9
            babyTupleTree.secondLeptonIso     = -1

        babyTupleTree.numberOfSelectedJets    = len(self.selectedJets)

        # FIXME this is a C++ way of thinking, rewrite it in python
        babyTupleTree.numberOfBTaggedJets     = 0
        for jet in self.selectedJets :
            if (jet.bTag == True) : babyTupleTree.numberOfBTaggedJets += 1


        for i, jet in enumerate(self.selectedJets) :
            if (i >= 6) : break;
            babyTupleTree.jetsPt[i]           = jet.pT
            babyTupleTree.jetsPhi[i]          = jet.phi
            babyTupleTree.jetsEta[i]          = jet.eta
            babyTupleTree.jetsCSVv2[i]        = jet.CSVv2
            babyTupleTree.jetsPUid[i]         = jet.PUid

        babyTupleTree.ETmiss                  = event.met_pt
        babyTupleTree.ETmissPhi               = event.met_phi
        babyTupleTree.MT                      = self.MT
        babyTupleTree.MT2W                    = self.MT2W
        babyTupleTree.HT                      = self.HT
        babyTupleTree.ak4_htssm  = self.HTSSM
        babyTupleTree.ak4_htosm  = self.HTOSM
        babyTupleTree.M3b   	= self.M3b
        babyTupleTree.Mlb_leadb 	= self.Mlb_leadb
        babyTupleTree.dphi_Wlep 	= self.dphi_Wlep
        babyTupleTree.topness   	= self.topness
        babyTupleTree.hadronic_top_chi2 = self.hadchi2
        babyTupleTree.met_sig	        = event.met_sig


        #isoStudy
	if self.doIsoStudy:
	    for i in range(2):
	        #electrons
		babyTupleTree.el_miniIso[i] = self.noIsoSelectedElectrons[i]['miniIso'] if len (self.noIsoSelectedElectrons)> i else -999
	        babyTupleTree.el_relIsoDB[i] = self.noIsoSelectedElectrons[i]['relIsoDB'] if len (self.noIsoSelectedElectrons) > i else -999
	        babyTupleTree.el_relIsoEA[i] = self.noIsoSelectedElectrons[i]['relIsoEA'] if len (self.noIsoSelectedElectrons) > i else -999
	        babyTupleTree.el_pt[i] = self.noIsoSelectedElectrons[i]['pt'] if len (self.noIsoSelectedElectrons) > i else -999
	        babyTupleTree.el_eta[i] = self.noIsoSelectedElectrons[i]['eta'] if len (self.noIsoSelectedElectrons) > i else -999
          	#muons
		babyTupleTree.mu_miniIso[i] = self.noIsoSelectedMuons[i]['miniIso'] if len (self.noIsoSelectedMuons)> i else -999
	        babyTupleTree.mu_relIsoDB[i] = self.noIsoSelectedMuons[i]['relIsoDB'] if len (self.noIsoSelectedMuons) > i else -999
	        babyTupleTree.mu_pt[i] = self.noIsoSelectedMuons[i]['pt'] if len (self.noIsoSelectedMuons) > i else -999
	        babyTupleTree.mu_eta[i] = self.noIsoSelectedMuons[i]['eta'] if len (self.noIsoSelectedMuons) > i else -999


	#added: pv
	babyTupleTree.pv_z                   = event.pv_z
	babyTupleTree.pv_rho                 = event.pv_rho
	babyTupleTree.pv_ndof                = event.pv_ndof
	babyTupleTree.pv_isFake              = event.pv_isFake

        babyTupleTree.numberOfGeneratedLeptons = self.numberOfGeneratedLeptons

        babyTupleTree.crossSection              = self.dataset.xsection
        babyTupleTree.totalNumberOfInitialEvent = self.dataset.initialNumberOfEvents

	
        if self.saveGenMET:	
		babyTupleTree.metGen_pt = event.metGen_pt
		babyTupleTree.metGen_phi = event.metGen_phi
	else: 
		babyTupleTree.metGen_pt  = -999
		babyTupleTree.metGen_phi = -999

        #for synchronization
	#babyTupleTree.selectionCode = self.selectionCode

	#Add gen info
        if self.saveGenInfo:
        	babyTupleTree.gen_n =				event.gen_n 
        	babyTupleTree.gen_pt = 			event.gen_pt
        	babyTupleTree.gen_eta = 			event.gen_eta
        	babyTupleTree.gen_phi = 			event.gen_phi
        	babyTupleTree.gen_m = 			event.gen_m
        	babyTupleTree.gen_status = 			event.gen_status
        	babyTupleTree.gen_id = 			event.gen_id
        	babyTupleTree.gen_charge = 			event.gen_charge
        	babyTupleTree.gen_index = 			event.gen_index
        	babyTupleTree.gen_mother_index = 			event.gen_mother_index
        	babyTupleTree.gen_daughter_n = 			event.gen_daughter_n
        	babyTupleTree.gen_daughter_index = 			event.gen_daughter_index

	#Add pfcand. info
