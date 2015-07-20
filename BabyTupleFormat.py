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

doIsoStudy = False
addGenInfo = True

class BabyTupleFormat :

    babyTupleFormat = { 

      ##################
      # common format  #
      ##################

      ######## global quantites   ###
      'run'                    :  'I',
      'ls'   	               :  'I',
      'event'                  :  'I',

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
      'ak4_htssm'		 :  'F',
      'ak4_htosm'		 :  'F',
      'M3b'			 :  'F',
      'Mlb_leadb'		 :  'F',
      'dphi_Wlep'		 :  'F',
      'topness'			 :  'F',
      'hadronic_top_chi2'        :  'F',

      #added: pv
      'pv_ndof'			 :   'F',
      'pv_isFake'                :   'I',
      'pv_rho'                	 :   'F',
      'pv_z'                	 :   'F',

      'numberOfGeneratedLeptons' :  'I',
     
      'crossSection'             :  'F',
      'totalNumberOfInitialEvent':  'I',
	
      'numberOfSelectedElectrons' : 'I',
      'numberOfSelectedMuons' : 'I'
   }
    #for isolation study
    # store info for leading and second leading leptons (for each flavor)
    if doIsoStudy:
   	# for electrons
   	babyTupleFormat['el_miniIso']  =  'F[2]'
        babyTupleFormat['el_relIsoDB']  =  'F[2]'
        babyTupleFormat['el_relIsoEA']  =  'F[2]'
        babyTupleFormat['el_pt']  =  'F[2]'
        babyTupleFormat['el_eta']  =  'F[2]'
        # for muons
        babyTupleFormat['mu_miniIso']  =  'F[2]'
        babyTupleFormat['mu_relIsoDB']  =  'F[2]'
        babyTupleFormat['mu_pt']  =  'F[2]'
        babyTupleFormat['mu_eta']  =  'F[2]'

    #for synchronisation
    babyTupleFormat['selectionCode'] = 'F'
     

    def AddGenInfo(self):
        setattr(self, 'gen_n', 'I')
        setattr(self,'gen_pt',	 "vector<float>")
        setattr(self,'gen_eta',	 "vector<float>")
        setattr(self,'gen_phi',	 "vector<float>")
        setattr(self,'gen_m',	 "vector<float>")
        setattr(self,'gen_status',	 "vector<int>")
        setattr(self,'gen_id',	 "vector<int>")
        setattr(self,'gen_charge',	 "vector<int>")
        setattr(self,'gen_index',	 "vector<int>")
        setattr(self,'gen_mother_index',	 "vector<int>")
        setattr(self,'gen_daughter_n',	 "vector<int>")
        setattr(self,'gen_daughter_index',	 "vector<vector<int> >")
        
    if addGenInfo:
        babyTupleFormat['gen_n'] =	 'I'
        babyTupleFormat['gen_pt'] =	 "vector<float>"
        babyTupleFormat['gen_eta'] =	 "vector<float>"
        babyTupleFormat['gen_phi'] =	 "vector<float>"
        babyTupleFormat['gen_m'] =	 "vector<float>"
        babyTupleFormat['gen_status'] =	 "vector<int>"
        babyTupleFormat['gen_id'] =	 "vector<int>"
        babyTupleFormat['gen_charge'] =	 "vector<int>"
        babyTupleFormat['gen_index'] =	 "vector<int>"
        babyTupleFormat['gen_mother_index'] =	 "vector<int>"
        babyTupleFormat['gen_daughter_n'] =	 "vector<int>"
        babyTupleFormat['gen_daughter_index'] =	 "vector<vector<int> >"




    # Additional input branches needed during the filling of the babytuple
    branchesForMiscInfos = [ "ev_run", "ev_lumi", "ev_id" ]

    def fill(self,event,babyTupleTree,saveGenInfo = False) :
        ############################
        #  common format           #
        ############################
      
	
        babyTupleTree.run              = event.ev_run
        babyTupleTree.ls               = event.ev_lumi
        babyTupleTree.event            = event.ev_id

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
	lepton2 = []
	if len(self.selectedLeptons) > 1:
	    lepton2 = self.selectedLeptons[1]
	    babyTupleTree.lep2_passVeto = True	# by definition
	if len(self.selectedLeptons2) > 0:
	    lepton2 = self.selectedLeptons2[0]
	    babyTupleTree.lep2_passVeto = True	# by definition
	if len(self.vetoLeptons) > 0:
	    lepton2 = vetoLeptons[0]
	    babyTupleTree.lep2_passVeto = False	# by definition

	if lepton2 != []:
	    babyTupleTree.lep2_pdgid = lepton.id
	    babyTupleTree.lep2_pt = lepton.pT
	    babyTupleTree.lep2_eta = lepton.eta
	    babyTupleTree.lep2_phi = lepton.phi
	    # compute Mass
	    lep = TLorentzVector()
	    lep.SetPtEtaPhiE(lepton.pT, lepton.eta, lepton.phi, lepton.E)
	    babyTupleTree.lep2_mass = lep.M()
	    babyTupleTree.lep2_dz = lepton.dz
	    babyTupleTree.lep2_d0 = lepton.d0
	    babyTupleTree.lep2_MiniIso = leptonm.iso
	    babyTupleTree.lep2_pdgid = lepton.id
	    babyTupleTree.lep2_passMediumID = lepton.passMediumID
	   
	babyTupleTree.runId                   = event.ev_run
      
        # vector of jets are pt ordered
        v_jet_pt = stl.vector('float')()
        v_jet_eta = stl.vector('float')()
        v_jet_phi = stl.vector('float')()
        v_jet_mass = stl.vector('float')()
        v_jet_CSV = stl.vector('float')()
        v_jet_loose_pfid = stl.vector('bool')()
        v_jet_puid = stl.vector('float')()
	for jet in self.selectedJets:
	    v_jet_pt.push_back(jet.pT)
	    v_jet_eta.push_back(jet.eta)
	    v_jet_phi.push_back(jet.phi)
	    jetp4 = TLorentzVector()
	    jetp4.SetPtEtaPhiE(jet.pT, jet.eta, jet.phi, jet.E)
	    v_jet_mass.push_back(jetp4.M())
	    v_jet_CSV.push_back(jet.CSVv2)
	    v_jet_loose_pfid.push_back(jet.looseID)
	    v_jet_puid.push_back(jet.PUid)
        babyTupleTree.ak4pfjets_pt	 =  v_jet_pt
        babyTupleTree.ak4pfjets_eta	 =  v_jet_eta
        babyTupleTree.ak4pfjets_phi	 =  v_jet_phi
        babyTupleTree.ak4pfjets_mass	 =  v_jet_mass
        babyTupleTree.ak4pfjets_CSV	 =  v_jet_CSV
        babyTupleTree.ak4pfjets_loose_pfid	 =  v_jet_loose_pfid
        babyTupleTree.ak4pfjets_puid	 =  v_jet_puid
        
	#'dphi_ak4pfjets_met'	:	'F',

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
        babyTupleTree.HLT_SingleMu	= True #
        babyTupleTree.HLT_SingleE	= True # default

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
            babyTupleTree.jetsCSV[i]          = jet.CSV
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


        #isoStudy
	if doIsoStudy:
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


        #for synchronization
	#babyTupleTree.selectionCode = self.selectionCode

	#Add gen info
        if saveGenInfo:
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
