
###########################################################################################
#   ____        _           _               _         __                            _     #
#  | __ )  __ _| |__  _   _| |_ _   _ _ __ | | ___   / _| ___  _ __ _ __ ___   __ _| |_   #
#  |  _ \ / _` | '_ \| | | | __| | | | '_ \| |/ _ \ | |_ / _ \| '__| '_ ` _ \ / _` | __|  #
#  | |_) | (_| | |_) | |_| | |_| |_| | |_) | |  __/ |  _| (_) | |  | | | | | | (_| | |_   #
#  |____/ \__,_|_.__/ \__, |\__|\__,_| .__/|_|\___| |_|  \___/|_|  |_| |_| |_|\__,_|\__|  #
#                      |___/          |_|                                                 #
###########################################################################################

doIsoStudy = False

class BabyTupleFormat :

    babyTupleFormat = { 

      #common format
       
	
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
      'ak4pfjets_pt'		:	'F',
      'ak4pfjets_eta'		:	'F',
      'ak4pfjets_phi'		:	'F',
      'ak4pfjets_mass'		:	'F',
      'ak4pfjets_CSV'		:	'F',
      'ak4pfjets_loose_pfid'	:	'B',
      'ak4pfjets_puid'		:	'B',
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


    # Additional input branches needed during the filling of the babytuple
    branchesForMiscInfos = [ "ev_run", "ev_lumi", "ev_id" ]

    def fill(self,event,babyTupleTree) :

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
