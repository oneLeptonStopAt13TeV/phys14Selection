
from collections import namedtuple
from core        import commonFunctions as common

class Selection :

    # ############# #
    # Reset objects #
    # ############# #

    def resetSelectedObjects(self) :
        self.selectedLeptons   = []
        self.selectedJets      = []

    ############################################################################
    #    ___  _     _           _              _           _                   #
    #   / _ \| |__ (_) ___  ___| |_   ___  ___| | ___  ___| |_ ___  _ __ ___   #
    #  | | | | '_ \| |/ _ \/ __| __| / __|/ _ \ |/ _ \/ __| __/ _ \| '__/ __|  #
    #  | |_| | |_) | |  __/ (__| |_  \__ \  __/ |  __/ (__| || (_) | |  \__ \  #
    #   \___/|_.__// |\___|\___|\__| |___/\___|_|\___|\___|\__\___/|_|  |___/  #
    #             |__/                                                         #
    ############################################################################

    # Define structure for temporary objects storage
    lepton = namedtuple('lepton', ['id', 'E', 'pT', 'eta', 'phi', 'iso' ])
    jet    = namedtuple('jet',    [ 'E', 'pT', 'eta', 'phi', 'CSV', 'CSVv2', 'PUid', 'bTag' ])

    # ##### #
    # Muons #
    # ##### #

    branchesForMuonSelection = [ "mu_n",
                                 "mu_id", "mu_E", "mu_pt", "mu_eta", "mu_phi",
                                 "mu_isPFMuon", "mu_isGlobalMuon",
                                 "mu_innerTrack_dxy", "mu_innerTrack_dz",
                                 "mu_pfIso03_sumChargedHadronPt", "mu_pfIso03_sumNeutralHadronEt",
                                 "mu_pfIso03_sumPhotonEt", "mu_pfIso03_sumPUPt",
                                 "mu_isTightMuon" ]

    def muonSelector(self,event) :

        n                     = event.mu_n
        id                    = event.mu_id
        E                     = event.mu_E
        pt                    = event.mu_pt
        eta                   = event.mu_eta
        phi                   = event.mu_phi
        isPF                  = event.mu_isPFMuon
        isGlobal              = event.mu_isGlobalMuon
        dxy                   = event.mu_innerTrack_dxy
        dz                    = event.mu_innerTrack_dz
        isoChargedHadron      = event.mu_pfIso03_sumChargedHadronPt
        isoNeutralHadron      = event.mu_pfIso03_sumNeutralHadronEt
        isoPhoton             = event.mu_pfIso03_sumPhotonEt
        isoPU                 = event.mu_pfIso03_sumPUPt
        isTightMuon           = event.mu_isTightMuon

        for i in range(n) :

            # Require tight ID
            if not (isTightMuon)      : continue

            #if not (isPF[i])       : continue
            #if not (isGlobal[i])   : continue

            # Apply pT and eta critera
            if (pt[i]       <  20)    : continue
            if (abs(eta[i]) > 2.1)    : continue

            # Vertex constrain
            if (abs(dxy[i]) >= 0.02)   : continue
            if (abs(dz[i])  >= 0.1)    : continue

            # Isolation
            absIso = isoChargedHadron[i]         \
                   + max(0.0,isoNeutralHadron[i] \
                           + isoPhoton[i]        \
                     - 0.5 * isoPU[i])
            if (absIso / pt[i]   > 0.15)    : continue

            self.selectedLeptons.append(self.lepton( id[i],
                                                     E[i],
                                                     pt[i],
                                                     eta[i],
                                                     phi[i],
                                                     absIso
                                                     ))


    # ######### #
    # Electrons #
    # ######### #

    branchesForElectronSelection = [ "el_n",
                                     "el_id", "el_E", "el_pt", "el_eta", "el_scleta", "el_phi",
                                     "el_deltaEtaSuperClusterTrackAtVtx",
                                     "el_deltaPhiSuperClusterTrackAtVtx",
                                     "el_see", "el_hadronicOverEm",
                                     "el_eSuperClusterOverP",
                                     "el_dxy", "el_dz", "el_IoEmIoP",
                                     "el_passConversionVeto", "el_numberOfLostHits",
                                     "el_pfIso_sumChargedHadronPt", "el_pfIso_sumNeutralHadronEt",
                                     "el_pfIso_sumPhotonEt", "el_pfIso_sumPUPt" ]

    def electronSelector(self,event) :

        n                  = event.el_n
        id                 = event.el_id
        E                  = event.el_E
        pt                 = event.el_pt
        eta                = event.el_eta
        scleta             = event.el_scleta
        phi                = event.el_phi
        dEtaSCTrack        = event.el_deltaEtaSuperClusterTrackAtVtx
        dPhiSCTrack        = event.el_deltaPhiSuperClusterTrackAtVtx
        see                = event.el_see
        hadronicOverEm     = event.el_hadronicOverEm
        eSuperClusterOverP = event.el_eSuperClusterOverP
        dxy                = event.el_dxy
        dz                 = event.el_dz
        IoEmIoP            = event.el_IoEmIoP
        passConversionVeto = event.el_passConversionVeto
        numberOfLostHits   = event.el_numberOfLostHits
        isoChargedHadron   = event.el_pfIso_sumChargedHadronPt
        isoNeutralHadron   = event.el_pfIso_sumNeutralHadronEt
        isoPhoton          = event.el_pfIso_sumPhotonEt
        isoPU              = event.el_pfIso_sumPUPt

        for i in range(n) :

            # Apply pT and eta critera
            if (pt[i]       <  20) : continue
            if (abs(eta[i]) > 2.1) : continue

            # Remove crack electron
            #if (abs(scleta[i]) > 1.4442) and ((abs(scleta[i]) < 1.566)) : continue

            # Isolation
            # TODO / FIXME : check this is good (deltaBeta correction ?)
            absIso = isoChargedHadron[i]         \
                   + max(0.0,isoNeutralHadron[i] \
                           + isoPhoton[i]        \
                         - 0.5 * isoPU[i])

            relIso = absIso / pt[i]

            # Electron ID
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, medium
            if (abs(scleta[i]) < 1.479) :
                if (relIso              >= 0.097213)  : continue
                if (abs(dEtaSCTrack[i]) >= 0.007641)  : continue
                if (abs(dPhiSCTrack[i]) >= 0.032643)  : continue
                if (see[i]              >= 0.010399)  : continue
                if (hadronicOverEm[i]   >= 0.060662)  : continue
                if (IoEmIoP[i]          >= 0.153897)  : continue
                if (abs(dxy[i])         >= 0.011811)  : continue
                if (abs(dz[i])          >= 0.070775)  : continue
            else :
                if (relIso              >= 0.116708) : continue
                if (abs(dEtaSCTrack[i]) >= 0.009285) : continue
                if (abs(dPhiSCTrack[i]) >= 0.042447) : continue
                if (see[i]              >= 0.029524) : continue
                if (hadronicOverEm[i]   >= 0.104263) : continue
                if (IoEmIoP[i]          >= 0.137468) : continue
                if (abs(dxy[i])         >= 0.051682) : continue
                if (abs(dz[i])          >= 0.180720) : continue

            if not (passConversionVeto[i] )  : continue
            if (numberOfLostHits[i]   >  1)  : continue

            self.selectedLeptons.append(self.lepton(id[i],
                                                    E[i],
                                                    pt[i],
                                                    eta[i],
                                                    phi[i],
                                                    absIso
                                                    ))


    # #### #
    # Jets #
    # #### #

    branchesForJetSelection = [ "jet_n",
                                "jet_E", "jet_pt", "jet_eta",   "jet_phi",
                                "jet_CSV", "jet_CSVv2",
                                "jet_pileupJetId" ]

    def jetSelector(self,event) :

        n           = event.jet_n
        E           = event.jet_E
        pt          = event.jet_pt
        eta         = event.jet_eta
        phi         = event.jet_phi
        phi         = event.jet_phi
        CSV         = event.jet_CSV
        CSVv2       = event.jet_CSVv2
        pileupJetId = event.jet_pileupJetId

        for i in range(n) :

            # Apply pT and eta requirements
            if (pt[i]       <  30) : continue
            if (abs(eta[i]) > 2.4) : continue

            # Remove jet overlaping with leptons
            foundOverlapWithLepton = False
            for lepton in self.selectedLeptons :
                dR = common.deltaR(lepton.phi,lepton.eta,phi[i],eta[i])
                if (dR < 0.4) : foundOverlapWithLepton = True; break

            if (foundOverlapWithLepton) : continue

            self.selectedJets.append(self.jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSV[i],
                                              CSVv2[i],
                                              pileupJetId[i],
                                              (CSVv2[i] > 0.814)))

    ##########################################################################
    #  _____                 _              _           _   _                #
    #  | ____|_   _____ _ __ | |_   ___  ___| | ___  ___| |_(_) ___  _ __    #
    #  |  _| \ \ / / _ \ '_ \| __| / __|/ _ \ |/ _ \/ __| __| |/ _ \| '_ \   #
    #  | |___ \ V /  __/ | | | |_  \__ \  __/ |  __/ (__| |_| | (_) | | | |  #
    #  |_____| \_/ \___|_| |_|\__| |___/\___|_|\___|\___|\__|_|\___/|_| |_|  #
    #                                                                        #
    ##########################################################################

    #syncEventList = [89927, 93353, 94205, 96065, 9766, 89282, 88290, 863, 78438, 78299, 77119, 73828, 73626, 70800, 70761]

    branchesForEventSelection = [ ]
    def eventSelector(self,event) :

        # Debug for synchronization

        #if (event.ev_id in self.syncEventList) :
        #    print "----"
        #    print event.ev_id, event.ev_lumi, len(self.selectedLeptons), len(self.selectedJets)

        # At least on selected lepton
        if (len(self.selectedLeptons) == 0) : return False
        # At least three jets
        if (len(self.selectedJets)     < 3) : return False

        return True




