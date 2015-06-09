
from Selection       import *
from BabyTupleFormat import *
from Variables       import *

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
                     + Selection.branchesForEventSelection

    # ########### #
    # Constructor #
    # ########### #

    def __init__(self, dataset) :
        self.dataset = dataset
	# only used for sync' exercise
	#self.loadList()

    # ############# #
    # Reset objects #
    # ############# #

    def reset(self) :
        self.resetSelectedObjects()

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

        # Select muons,electrons
        self.muSelCode = []
	self.muonSelector(event, self.muSelCode)
	#print "self.mSelcode = ", self.muSelCode[0] if len(self.muSelCode) else -1
	self.elSelCode = []
        self.electronSelector(event, self.elSelCode)

        # Sort selected leptons by pT
        self.selectedLeptons = sorted(self.selectedLeptons, key=lambda lepton: lepton.pT, reverse=True)
     
        # Selected jets
        self.jetSelector(event)

        # Sort selected jets by pT
        self.selectedJets = sorted(self.selectedJets, key=lambda jet: jet.pT, reverse=True)

        # Apply event selection
	self.selectionCode  = []
        #setattr(event,'selectionCode',0)
	passEventSelection = self.eventSelector(event, self.selectionCode)
        #print " = ", self.selectionCode[0]
	#if (not passEventSelection) : return False

        # Compute variables
	# NB: this part is the most CPU intensive part of the code
	self.computeVariables(event)
      
	#######################
        # for synchronisation #
	#######################
	#if (event.ev_lumi,event.ev_id)  in self.eventList:
	#if event.ev_lumi == 229 and event.ev_id == 22840: 
	#    print "### ", event.ev_lumi, event.ev_id
	#    print "- electron -"
	#    self.electronDump(event)
	#    print "- muon -"
	#    self.muonDump(event)
	#    print "- pv - "
	#    self.pvDump(event)
	#    print " - selection Code - ", self.selectionCode[0]
	#    print " - muon sele Code - ", self.muSelCode[0] if len(self.muSelCode)>0 else -1
	#    print " - elec sele Code - ", self.elSelCode[0] if len(self.elSelCode)>0 else -1

        # for iso study
	if isoStudy:
	    self.muonSelector(event,self.muSelCode2, False)
	    self.electronSelector(event,self.elSelCode2, False)
            # Sort selected leptons by pT
            self.noIsoSelectedMuons = sorted(self.noIsoSelectedMuons, key=lambda lepton: lepton['pt'], reverse=True)
            self.noIsoSelectedElectrons = sorted(self.noIsoSelectedElectrons, key=lambda lepton: lepton['pt'], reverse=True)

        # Fill event in babytuple

        self.fill(event,babyTupleTree)
        
        return True


