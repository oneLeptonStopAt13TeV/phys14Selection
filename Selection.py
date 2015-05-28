
from collections import namedtuple
from core        import commonFunctions as common

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
        self.selectedJets      = []
	#for isoStudy
	self.noIsoSelectedMuons = []
	self.noIsoSelectedElectrons = []
	################################

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
                                 "mu_globalTrack_dxy", "mu_globalTrack_dz",
				 "mu_innerTrack_dxy", "mu_innerTrack_dz",
                                 "mu_pfIso03_sumChargedHadronPt", "mu_pfIso03_sumNeutralHadronEt",
                                 "mu_pfIso03_sumPhotonEt", "mu_pfIso03_sumPUPt",
                                 "mu_numberOfMatches",
				 "mu_isTightMuon","mu_miniIso" ]

    def muonDump(self,event):
       for i in range(event.mu_n):
	    print "id                    =", event.mu_id[i]
            print "E                     =", event.mu_E[i]
            print "pt                    =", event.mu_pt[i]
            print "eta                   =", event.mu_eta[i]
            print "phi                   =", event.mu_phi[i]
            print "isPF                  =", event.mu_isPFMuon[i]
            print "isGlobal              =", event.mu_isGlobalMuon[i]
            print "dxy                   =", event.mu_innerTrack_dxy[i]
            print "dz                    =", event.mu_innerTrack_dz[i]
            print "isoChargedHadron      =", event.mu_pfIso03_sumChargedHadronPt[i]
            print "isoNeutralHadron      =", event.mu_pfIso03_sumNeutralHadronEt[i]
            print "isoPhoton             =", event.mu_pfIso03_sumPhotonEt[i]
            print "isoPU                 =", event.mu_pfIso03_sumPUPt[i]
            print "isTightMuon           =", event.mu_isTightMuon[i]


    def muonSelector(self,event,mSelCode, iso = True) :
    	#use also iso cut if iso == True

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

        muSelCode = 0
	for i in range(n) :

            isSel = True
            # Require tight ID
            if isTightMuon[i] != 1     :
	        #continue
                isSel = False
	    else:
	        muSelCode+=1
	    # The following cuts are need
	    if not (isPF[i])       : 
	        #continue
                isSel = False
            else:
	        muSelCode+=10
	    if not (isGlobal[i])   : 
	        #continue
                isSel = False
	    else: 
	        muSelCode+=100
	    if event.mu_numberOfMatches[i] < 2 : 
	        #continue
                isSel = False
	    else: 
	        muSelCode+=1000
	    #print dxy[i], dz[i]
	    if abs(dxy[i]) >= 0.02 : 
	        #continue
                isSel = False
	    else:
	        muSelCode+=10000
	    if abs(dz[i]) >= 0.1 : 
	        #continue	
                isSel = False
	    else:
	        muSelCode+=100000
	    #if event.mu_globalTrack_dxy[i] >= 0.02 : continue
	    #if event.mu_globalTrack_dz[i] >= 0.1 : continue	
            # Apply pT and eta critera
            if (pt[i]       <  20)    : 
	        #continue
                isSel = False
            else:
	        muSelCode+=1000000
	    if (abs(eta[i]) > 2.1)    : 
	        #continue
	        isSel = False	
	    else:
	        muSelCode+=10000000
            # Vertex constrain
            # Already present in tight-id
	    #if (abs(dxy[i]) >= 0.02)   : continue
            #if (abs(dz[i])  >= 0.1)    : continue

            # Isolation
            absIso = isoChargedHadron[i]         \
                   + max(0.0,isoNeutralHadron[i] \
                           + isoPhoton[i]        \
                     - 0.5 * isoPU[i])
            
	    if iso:
	        rIso = 99999 
		if pt[i] !=0:
		   rIso = absIso / pt[i] 
		#or (absIso / pt[i]   > 0.15)    : 
		if (rIso  > 0.15)    : 
		    #continue
	            isSel = False	
                else:
		    muSelCode+=100000000
		    if isSel:
		        self.selectedMuons = self.selectedMuons + 1
	                self.selectedLeptons.append(self.lepton( id[i],
                                                     E[i],
                                                     pt[i],
                                                     eta[i],
                                                     phi[i],
                                                     absIso
                                                     ))
            	#print "y a des muons!"
	    else :
	        if isSel:
	            self.noIsoSelectedMuons.append(
			{'miniIso':event.mu_miniIso[i],
			'relIsoDB':absIso/pt[i],
			'pt':pt[i],
			'eta':eta[i]})
	
	    if i == 0 : 
	        mSelCode.append(muSelCode)
                #print "muSelCode = ", muSelCode

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
                                     "el_pfIso_sumPhotonEt", "el_pfIso_sumPUPt" ,
				     "ev_rho", "el_miniIso"]

    def electronDump( self,event):
        for i in range(event.el_n):
            print "id                 =", event.el_id[i]
            print "E                  =", event.el_E[i]
            print "pt                 =", event.el_pt[i]
            print "eta                =", event.el_eta[i]
            print "scleta             =", event.el_scleta[i]
            print "phi                =", event.el_phi[i]
            print "dEtaSCTrack        =", event.el_deltaEtaSuperClusterTrackAtVtx[i]
            print "dPhiSCTrack        =", event.el_deltaPhiSuperClusterTrackAtVtx[i]
            print "see                =", event.el_see[i]
            print "hadronicOverEm     =", event.el_hadronicOverEm[i]
            print "eSuperClusterOverP =", event.el_eSuperClusterOverP[i]
            print "dxy                =", event.el_dxy[i]
            print "dz                 =", event.el_dz[i]
            print "IoEmIoP            =", event.el_IoEmIoP[i]
            print "passConversionVeto =", event.el_passConversionVeto[i]
            print "numberOfLostHits   =", event.el_numberOfLostHits[i]
            print "isoChargedHadron   =", event.el_pfIso_sumChargedHadronPt[i]
            print "isoNeutralHadron   =", event.el_pfIso_sumNeutralHadronEt[i]
            print "isoPhoton          =", event.el_pfIso_sumPhotonEt[i]
            print "isoPU              =", event.el_pfIso_sumPUPt[i]
    
    def electronSelector(self,event,elSelCode, iso = True) :
    	#use also iso cut if iso == True

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
            #else : elSelCode+=1
	    if (abs(eta[i]) > 2.1) : continue
            #else : elSelCode+=10

            # Remove crack electron
            #if (abs(scleta[i]) > 1.4442) and ((abs(scleta[i]) < 1.566)) : continue

            # Isolation
            # TODO / FIXME : check this is good (deltaBeta correction ?)
            
	    #taken form https://indico.cern.ch/event/367861/contribution/2/material/slides/0.pdf (slide 7)
	    effAreaList = [ (0.8,0.1013), (1.3,0.0988), (2.0,0.0572), (2.2,0.0842), (2.5,0.1530)] 
	    #effArea = 0
	    for eff_eta,eff_val in effAreaList:
	    	if abs(eta[i]) < eff_eta: 
			effArea = eff_val
			break;

	    absIso = isoChargedHadron[i]         \
                   + max(0.0,isoNeutralHadron[i] \
                           + isoPhoton[i]        \
                         #- 0.5 * isoPU[i])
                         - event.ev_rho * effArea)

            relIso = absIso / pt[i]


	    relIsoDB = (isoChargedHadron[i]         \
                   + max(0.0,isoNeutralHadron[i] \
                           + isoPhoton[i]        \
                         - 0.5 * isoPU[i])) / pt[i]

            # Electron ID
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, medium
            # consistent with r16
	    if (abs(scleta[i]) <= 1.479) :
                if iso:
		    if (relIsoDB              >= 0.097213)  : continue
                if (abs(dEtaSCTrack[i]) >= 0.007641)  : continue
                if (abs(dPhiSCTrack[i]) >= 0.032643)  : continue
                if (see[i]              >= 0.010399)  : continue
                if (hadronicOverEm[i]   >= 0.060662)  : continue
                if (IoEmIoP[i]          >= 0.153897)  : continue
                if (abs(dxy[i])         >= 0.011811)  : continue
                if (abs(dz[i])          >= 0.070775)  : continue
            else :
                if iso:
                    if (relIsoDB              >= 0.116708 ) : continue
                if (abs(dEtaSCTrack[i]) >= 0.009285 ) : continue
                if (abs(dPhiSCTrack[i]) >= 0.042447 ) : continue
                if (see[i]              >= 0.029524 ) : continue
                if (hadronicOverEm[i]   >= 0.104263 ) : continue
                if (IoEmIoP[i]          >= 0.137468 ) : continue
                if (abs(dxy[i])         >= 0.051682 ) : continue
                if (abs(dz[i])          >= 0.180720 ) : continue

	   #https://twiki.cern.ch/twiki/bin/rdiff/CMS/CutBasedElectronIdentificationRun2 - r17
           # if (abs(scleta[i]) <= 1.479) :
           #     if (relIso              >= 0.107587 )  : continue
           #     if (abs(dEtaSCTrack[i]) >= 0.007641)  : continue
           #     if (abs(dPhiSCTrack[i]) >= 0.032643 )  : continue
           #     if (see[i]              >= 0.009996 )  : continue
           #     if (hadronicOverEm[i]   >= 0.050537 )  : continue
           #     if (IoEmIoP[i]          >= 0.091942  )  : continue
           #     if (abs(dxy[i])         >= 0.0118110.012235 )  : continue
           #     if (abs(dz[i])          >= 0.070775 )  : continue
           # else :
           #     if (relIso              >= 0.116708) : continue
           #     if (abs(dEtaSCTrack[i]) >= 0.007429 ) : continue
           #     if (abs(dPhiSCTrack[i]) >= 0.067879 ) : continue
           #     if (see[i]              >= 0.030135 ) : continue
           #     if (hadronicOverEm[i]   >= 0.086782 ) : continue
           #     if (IoEmIoP[i]          >= 0.100683 ) : continue
           #     if (abs(dxy[i])         >= 0.036719 ) : continue
           #     if (abs(dz[i])          >= 0.138142 ) : continue


            if not (passConversionVeto[i] )  : continue
            if (numberOfLostHits[i]   >  1)  : continue

            if iso:
	        self.selectedElectrons = self.selectedElectrons + 1
                self.selectedLeptons.append(self.lepton(id[i],
                                                    E[i],
                                                    pt[i],
                                                    eta[i],
                                                    phi[i],
                                                    absIso
                                                    ))
	    else :
	        self.noIsoSelectedElectrons.append(
			{'miniIso':event.el_miniIso[i],
			'relIsoEA':absIso/pt[i],
			'relIsoDB':relIsoDB,
			'pt':pt[i],
			'eta':eta[i]})
		


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

    #branchesForPVSelection = []
    def pvSelection(self,event):
        #variables are missing in the tuples for the moment
	if event.pv_rho > 2 : return False 
        if abs(event.pv_z) >24 : return False
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

        # Debug for synchronization

        #if (event.ev_id in self.syncEventList) :
        #    print "----"
        #    print event.ev_id, event.ev_lumi, len(self.selectedLeptons), len(self.selectedJets)

        #event.setattr(event,'selectionCode',0)
	selectionCode = 0
	returnBool = True

	#PV selection
	if self.pvSelection(event) == False: 
	    returnBool =  False
        else : 
	    selectionCode+=1

        # At least on selected lepton
        if (len(self.selectedLeptons) == 0) :
	    returnBool = False
	else : 
	    selectionCode+=10
        # At least three jets
        if (len(self.selectedJets)     < 3) : 
	    returnBool =  False
        else : 
	    selectionCode+=100

        #print "sel-Code = ", selectionCode
        sCode.append(selectionCode)

        return returnBool




