
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
            babyTupleTree.leadingLeptonIso        = self.selectedLeptons[0].iso

        if (len(self.selectedLeptons) >= 2) :
            babyTupleTree.secondLeptonId      = self.selectedLeptons[1].id
            babyTupleTree.secondLeptonPt      = self.selectedLeptons[1].pT
            babyTupleTree.secondLeptonEta     = self.selectedLeptons[1].eta
            babyTupleTree.secondLeptonPhi     = self.selectedLeptons[1].phi
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
