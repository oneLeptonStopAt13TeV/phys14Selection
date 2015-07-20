
from Selection       import *
from BabyTupleFormat import *
from Variables       import *

saveGenInfo = True
class Analyzer(Selection,BabyTupleFormat,Variables) :
    


    ################
    #  for sync    #
    ################
    # uses a file "evenList"
    # only used for sync' exercise
    # will be remove later
    def loadList(self):
    
        self.eventList=[]
        f = open("eventList");
        for line in f:
           print line
	   print len(line)
	   array = [int(x) for x in line.split()]
	   self.eventList.append(tuple(array))

        #print eventList


    # ####################################### #
    # Define branches needed for the analysis #
    # ####################################### #
        
    requiredBranches = BabyTupleFormat.branchesForMiscInfos   \
                     + Variables.branchesForVariables         \
                     + Selection.branchesForElectronSelection \
                     + Selection.branchesForMuonSelection     \
                     + Selection.branchesForJetSelection      \
                     + Selection.branchesForEventSelection    \
                     + Selection.branchesForPfcand	      \
                     + Selection.branchesForTauSelection
    if saveGenInfo:
    	requiredBranches+= Selection.branchesForGenInfo

    #if saveGenInfo:
      		#BabyTupleFormat.AddGenInfo()
    #self.AddGenInfo()


    # ########### #
    # Constructor #
    # ########### #

    def __init__(self, dataset) :
        self.dataset = dataset
	# only used for sync' exercise
	self.loadList()

    # ############# #
    # Reset objects #
    # ############# #

    def reset(self) :
        self.resetSelectedObjects()


    # ############################## #
    # Dump info about a given event  #
    # ############################## #
    def eventDump(self):
	self.leadingLepton.Print()
	print "gen leptons = ",self.numberOfGeneratedLeptons
	print "Lepton-phi = ", self.leadingLepton.Phi()
	print "M3b = ", self.M3b
	print "topness = ", self.topness
	print "chi2 = ", self.hadchi2
	print "M3b = ", self.M3b
	print "Mlb = ", self.Mlb_leadb
	print "dphi_Wlep = ", self.dphi_Wlep
	print "HT = ", self.HT
	print "HTSSM = ", self.HTSSM
	print "pt lep = ", self.selectedLeptons[0].pT
	print "met_phi = ", event.met_phi
	print "MT = ",self.MT
	print "nof jets = ", len(self.selectedJets)
	print "lepton iso = ",self.leadingLeptonIso 
	self.jetDump(event)
	self.selJetDump(event)
	
	id2 = self.selectedLeptons2[0].id if len(self.selectedLeptons2) else 0 
	idloose = self.vetoLeptons[0].id if len(self.vetoLeptons) else 0 
	numberOfBTaggedJets = 0
        for jet in self.selectedJets :
            if (jet.bTag == True) : numberOfBTaggedJets += 1
	print "### ", event.ev_lumi, event.ev_id,\
	      " - nof leptons sel: ", len(self.selectedLeptons), " lep2: ",len(self.selectedLeptons2), " loose: ",len(self.vetoLeptons),\
	      " - selection Code - ", self.selectionCode[0], " - ", id2, idloose,\
	      " - ", len(self.selectedJets), numberOfBTaggedJets, event.met_pt
	print "Muon dump" 
	self.muonDump(event)
	print "Electron dump" 
	self.electronDump(event)
	if len(self.selectedLeptons2) >=1:
	    print "loose lepton, pt = ", self.selectedLeptons2[0].pT
	if len(self.vetoLeptons) >=1:
	    print "veto lepton, pt = ", self.vetoLeptons[0].pT

    ###################################################################################
    #   _____                 _                                       _               #
    #  | ____|_   _____ _ __ | |_   _ __  _ __ ___   ___ ___  ___ ___(_)_ __   __ _   #
    #  |  _| \ \ / / _ \ '_ \| __| | '_ \| '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |  #
    #  | |___ \ V /  __/ | | | |_  | |_) | | | (_) | (_|  __/\__ \__ \ | | | | (_| |  #
    #  |_____| \_/ \___|_| |_|\__| | .__/|_|  \___/ \___\___||___/___/_|_| |_|\__, |  #
    #                              |_|                                         |___/  #
    ###################################################################################

    def process(self,event,babyTupleTree, isoStudy = False) :

        self.reset()
	#if (event.ev_lumi != 2756 or event.ev_id != 75567):
	#    return

        # Select muons,electrons
        self.muSelCode = []
	self.muonSelector(event, self.muSelCode)
	self.elSelCode = []
        self.electronSelector(event, self.elSelCode)

        # Sort selected leptons by pT
        self.selectedLeptons = sorted(self.selectedLeptons, key=lambda lepton: lepton.pT, reverse=True)
     
        # Selected jets
        self.jetSelector(event)

        # Sort selected jets by pT
        self.selectedJets = sorted(self.selectedJets, key=lambda jet: jet.pT, reverse=True)

	# tupling of pfcands => No, just check for basic selection (charge, pt, dz)
	# required to compute isoTrackVeto
	# should be called before doingn isoTrackVeto
	#self.pfCandTupling(event)

        # Apply event selection
	self.selectionCode  = []
	passEventSelection = self.eventSelector(event, self.selectionCode)
        #print " = ", self.selectionCode[0]
	#if (not passEventSelection) : return False


	# Compute isoTrackVeto
	#self.isoTrackVeto(event)

	# create p4 for met,  leading lepton and jets
	# this is required for the method computeVariables
	self.createTLorentzVector(event)
	
        # Compute variables
	# NB: this part is the most CPU intensive part of the code
	self.computeVariables(event)
      
	#######################
        # for synchronisation #
	#######################
	
	#if (event.ev_lumi == 234 and event.ev_id == 23332):
	#if (event.ev_lumi,event.ev_id)  in self.eventList:
	#	eventDump(event)


        # for iso study
	if isoStudy:
	    self.muonSelector(event,self.muSelCode2, False)
	    self.electronSelector(event,self.elSelCode2, False)
            # Sort selected leptons by pT
            self.noIsoSelectedMuons = sorted(self.noIsoSelectedMuons, key=lambda lepton: lepton['pt'], reverse=True)
            self.noIsoSelectedElectrons = sorted(self.noIsoSelectedElectrons, key=lambda lepton: lepton['pt'], reverse=True)

        # Fill event in babytuple

        if passEventSelection:
	    self.fill(event,babyTupleTree,saveGenInfo)
        
        return True


