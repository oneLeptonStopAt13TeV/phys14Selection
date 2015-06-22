
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
                                 "mu_isPFMuon", "mu_isGlobalMuon", "mu_isTrackerMuon",
                                 #"mu_globalTrack_dxy", "mu_globalTrack_dz",
				 "mu_innerTrack_dxy", "mu_innerTrack_dz",
                                 #"mu_pfIso03_sumChargedHadronPt", "mu_pfIso03_sumNeutralHadronEt",
                                 #"mu_pfIso03_sumPhotonEt", "mu_pfIso03_sumPUPt",
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
            print "isTracker             =", event.mu_isTrackerMuon[i]
            print "dxy                   =", event.mu_innerTrack_dxy[i]
            print "dz                    =", event.mu_innerTrack_dz[i]
            #print "isoChargedHadron      =", event.mu_pfIso03_sumChargedHadronPt[i]
            #print "isoNeutralHadron      =", event.mu_pfIso03_sumNeutralHadronEt[i]
            #print "isoPhoton             =", event.mu_pfIso03_sumPhotonEt[i]
            #print "isoPU                 =", event.mu_pfIso03_sumPUPt[i]
            print "isTightMuon           =", event.mu_isTightMuon[i]
            print "miniIso               =", event.mu_miniIso[i]




    def muonSelector(self,event, muonSelCode, iso = True) :
    	
	#use also iso cut if iso == True

	#copy info in local variables (avoid retrieved info in the loop: save time)
        n                     = event.mu_n
        id                    = event.mu_id
        E                     = event.mu_E
        pt                    = event.mu_pt
        eta                   = event.mu_eta
        phi                   = event.mu_phi
        isPF                  = event.mu_isPFMuon
        isGlobal              = event.mu_isGlobalMuon
        isTracker             = event.mu_isTrackerMuon
        dxy                   = event.mu_innerTrack_dxy
        dz                    = event.mu_innerTrack_dz
        #isoChargedHadron      = event.mu_pfIso03_sumChargedHadronPt
        #isoNeutralHadron      = event.mu_pfIso03_sumNeutralHadronEt
        #isoPhoton             = event.mu_pfIso03_sumPhotonEt
        #isoPU                 = event.mu_pfIso03_sumPUPt
        isTightMuon           = event.mu_isTightMuon
	miniIso		      = event.mu_miniIso



	for i in range(n) :
	    # Reject muons than can either be veto or selected
	    
	    if abs(eta[i]) >= 2.4  : continue
	    if abs(pt[i]) <= 10  : continue
	    if abs(dxy[i]) >= 0.1 : continue
	    if abs(dz[i]) >= 0.5  : continue	
            if miniIso[i] >= 0.2 : continue
	    if not (isPF[i])       : continue
	    if (not isTracker[i]) and (not isGlobal[i]) : continue
	    # we miss if it is a track muon

            # Require tight ID
	    if isTightMuon[i] == 1 and event.mu_numberOfMatches[i] >=2 and abs(dxy[i])<0.02 and abs(dz[i])<0.1 and miniIso[i]<0.1:
	        # Selected muon
		if abs(eta[i]) < 2.1 and pt[i] >= 30:
		    self.selectedLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]) )
		# Loose selection
		elif pt[i] >= 20:
		    self.selectedLeptons2.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]) )
	    # Veto muon
	    else:
	        self.vetoLeptons.append( self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]) )

	

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
            print "miniIso            =", event.el_miniIso[i]
    
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
        miniIso   	   = event.el_miniIso

	selected = False
	veto = False

        for i in range(n) :

            # Loose criteria applied for the veto leptons
	    if pt[i] <= 10  : continue
	    if abs(eta[i]) >= 2.4: continue
	    if miniIso[i] >= 0.2: continue
	    # Isolation
	    if iso:
	        if miniIso[i] >= 0.1: continue

            # Apply pT and eta critera
            #if (pt[i]       <  20) : continue
	    #if (abs(eta[i]) > 2.1) : continue

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

	    veto = True

            # Electron ID
            # Taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
            # Phys14, PU20, bx25, medium
            # consistent with r19 (r13 in sync' - v1
            
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


	    if selected:
	       if pt[i] > 40 and abs(eta[i])< 2.1:
                   self.selectedLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]))
	       elif pt[i] > 20 and abs(eta[i])<2.4:
                   #print "SECOND LEPTON"
		   self.selectedLeptons2.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]))
	    else:
	      #print "LOOSE LEPTON"
              self.vetoLeptons.append(self.lepton(id[i], E[i], pt[i], eta[i], phi[i], miniIso[i]))



    # #### #
    # Jets #
    # #### #

    branchesForJetSelection = [ "jet_n",
                                "jet_E", "jet_pt", "jet_eta",   "jet_phi",
                                "jet_CSV", "jet_CSVv2",
                                "jet_pileupJetId" ]

    
    def jetDump(self,event):
        n   	    = event.jet_n
        E           = event.jet_E
        pt          = event.jet_pt
        eta         = event.jet_eta
        phi         = event.jet_phi
        CSVv2       = event.jet_CSVv2

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
        CSV         = event.jet_CSV
        CSVv2       = event.jet_CSVv2
        pileupJetId = event.jet_pileupJetId

        
	selectedJets = []
	selectedJetsOrg = []

	for i in range(n) :

            # Apply pT and eta requirements
            if (pt[i]       <  30) : continue
            if (abs(eta[i]) > 2.4) : continue

            selectedJets.append(self.jet(E[i],
                                              pt[i],
                                              eta[i],
                                              phi[i],
                                              CSV[i],
                                              CSVv2[i],
                                              pileupJetId[i],
                                              (CSVv2[i] > 0.814)))
           
	# build a collection of leptons (selected, loose and veto)
	leptons = self.selectedLeptons+self.selectedLeptons2+self.vetoLeptons
	    
	# Remove jet overlaping with leptons (the closest one if many)
	tmpCollection = [(j, []) for j in selectedJets]
	for lepton in leptons :
            for jet in tmpCollection:
		dR = common.deltaR(lepton.phi,lepton.eta,jet[0].phi,jet[0].eta)
                #print "loop ", jet[0].pT, dR
                jet[1].append(dR)

	for j in tmpCollection:
	    keep_it = True
	    for i in range(len(leptons)):
		#print j[0].pT, j[1][i]
		if j[1][i]<0.4:
		    # check if it is the closest jet
		    dRs = [tmpCollection[k][1][i] for k in range (len(tmpCollection))] 
	    	    
		    if j[1][i] == min(dRs):
			keep_it = False 
	    if keep_it:
		self.selectedJets.append(j[0])

	#if len(self.selectedJets) != len(selectedJetsOrg):
	#    print "Jets: ", len(selectedJets), len(tmpCollection), len(self.selectedJets), len(selectedJetsOrg)


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
        #if (len(self.selectedLeptons) == 0) :
        if (len(self.selectedLeptons) != 1) :
	    returnBool = False
	else : 
	    selectionCode+=10
	# new    
	#print returnBool, len(self.selectedLeptons2), len(self.vetoLeptons)
	if len(self.selectedLeptons2) != 0 :
	    returnBool = False
        if len(self.vetoLeptons)!=  0:
	    returnBool = False
	#print "answer = ",returnBool
	##############
	# At least three jets
        if (len(self.selectedJets)     < 3) : 
	    returnBool =  False
        else : 
	    selectionCode+=100

        #print "sel-Code = ", selectionCode
        sCode.append(selectionCode)

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

