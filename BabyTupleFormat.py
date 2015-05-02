
###########################################################################################
#   ____        _           _               _         __                            _     #
#  | __ )  __ _| |__  _   _| |_ _   _ _ __ | | ___   / _| ___  _ __ _ __ ___   __ _| |_   #
#  |  _ \ / _` | '_ \| | | | __| | | | '_ \| |/ _ \ | |_ / _ \| '__| '_ ` _ \ / _` | __|  #
#  | |_) | (_| | |_) | |_| | |_| |_| | |_) | |  __/ |  _| (_) | |  | | | | | | (_| | |_   #
#  |____/ \__,_|_.__/ \__, |\__|\__,_| .__/|_|\___| |_|  \___/|_|  |_| |_| |_|\__,_|\__|  #
#                      |___/          |_|                                                 #
###########################################################################################

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

      'numberOfGeneratedLeptons' :  'I',
     
      'crossSection'             :  'F',
      'totalNumberOfInitialEvent':  'I'
    }

    # Additional input branches needed during the filling of the babytuple
    branchesForMiscInfos = [ "ev_run", "ev_lumi", "ev_id" ]

    def fill(self,event,babyTupleTree) :

        babyTupleTree.runId                   = event.ev_run
        babyTupleTree.lumiId                  = event.ev_lumi
        babyTupleTree.eventId                 = event.ev_id
        babyTupleTree.numberOfSelectedLeptons = len(self.selectedLeptons)
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

        babyTupleTree.numberOfGeneratedLeptons = self.numberOfGeneratedLeptons

        babyTupleTree.crossSection              = self.dataset.xsection
        babyTupleTree.totalNumberOfInitialEvent = self.dataset.initialNumberOfEvents

