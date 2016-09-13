import ROOT
from Selection       import *
from BabyTupleFormat import *
from Variables       import *
import ConfigParser

saveGenInfo = False
loadGenInfo = False
loadStop = False
loadAK8 = True
loadAK10 = True
loadTriggerBranches = True
load_qg_tag = False

class Analyzer(Selection,BabyTupleFormat,Variables) :
    


    ################
    #  for sync    #
    ################
    # uses a file "evenList"
    # only used for sync' exercise
    # will be remove later
    def loadList(self):
    
        self.eventList=[]
        #f = open("eventList"); #@MJ@ TODO different name
        #f = open("RijuRestAfterCutInvest"); #@MJ@ TODO different name
        #for line in f:
        #   print line
	#   print len(line)
	#   array = [int(x) for x in line.split()]
	#   self.eventList.append(tuple(array))

        #print eventList

    # ########### #
    # Constructor #
    # ########### #

    def __init__(self, dataset) :
        
	# ################################## #
	# Call constructor of mother classes #
	# ################################## #
	BabyTupleFormat.__init__(self)
	Variables.__init__(self)
	Selection.__init__(self)

	################################
	#  LOAD CONFIG FILE            #
	################################

	config = ConfigParser.ConfigParser()
	config.read('config/config_mc.init')
	#config.read('config/config_data.init')

	self.dataset = dataset
	# only used for sync' exercise
	self.loadList()

	# saving some information (need first to load them)
	# member of BabyTupleFormat class
	#self.doIsoStudy = False
	#self.saveGenInfo = True
	self.saveAK8 = True
	self.saveAK10 = True
	self.isData 		= config.getboolean('DEFAULT','isData')
	self.doIsoStudy 	= config.getboolean('DEFAULT','doIsoStudy')
	self.saveGenInfo 	= config.getboolean('DEFAULT','saveGenInfo')
	self.saveAK8 		= config.getboolean('DEFAULT','saveAK8')
	self.saveAK10 		= config.getboolean('DEFAULT','saveAK10')
    	self.computeVar		= config.getboolean('DEFAULT','computeVar')

	# loading of certain branches
	# member of Analyze class
	#self.loadAK8 = True	
	#self.loadGenMET = True
	self.loadAK8 		= config.getboolean('DEFAULT','loadAK8')
	self.loadAK10 		= config.getboolean('DEFAULT','loadAK10')
	self.loadGenInfo 	= config.getboolean('DEFAULT','loadGenInfo')
	self.loadStop   	= config.getboolean('DEFAULT','loadStop')
    	#self.loadGenInfo = False
	#print 'value = ', config.get('DEFAULT','loadGenInfo',12)
	#print "GenInfo = ", self.loadGenInfo
	self.loadGenMET		= config.getboolean('DEFAULT','loadGenMET')
	self.UpdateVarBranchLoad()
	
	# member of Selection
	#self.loadPFcand = False
	self.loadPFcand 	= config.getboolean('DEFAULT','loadPFcand')
        self.load_qg_tag        = config.getboolean('DEFAULT', 'load_qg_tag')

	#do not forget to update the format once the boolean have been set
	self.UpdateFormat()
	self.loadGenInfo_Var = self.loadGenInfo
	#self.loadMCTruth_Var = False
	self.loadMCTruth_Var = config.getboolean('DEFAULT','loadMCTruth_Var')

	self.loadTriggerBranches = config.getboolean('DEFAULT','loadTriggerBranches')
	self.saveTriggerInfos = config.getboolean('DEFAULT','saveTriggerInfo')

	# Configuable selection variable
	self.electronPtCut = config.getfloat('SELECTION','electronPtCut')
	self.muonPtCut = config.getfloat('SELECTION','muonPtCut')
	self.jet_multiplicity = config.getint('SELECTION','jet_multiplicity')

	# Branches for trigger study
	branchesForTrigger = ['trigger_name', 'trigger_pass']


    	# ####################################### #
   	# Define branches needed for the analysis #
    	# ####################################### #
    	self.requiredBranches = self.branchesForMiscInfos   \
                     + self.branchesForVariables         \
		     + Selection.branchesForElectronSelection \
                     + Selection.branchesForMuonSelection     \
                     + Selection.branchesForJetSelection      \
                     + Selection.branchesForEventSelection    \
                     + Selection.branchesForTauSelection
    	if self.loadGenInfo:
    		#print "here or not "
		self.requiredBranches+= Selection.branchesForGenInfo
                self.requiredBranches+= Selection.branchesForGenJetSelection  #@MJ@ TODO make special requirement for this
        if self.loadGenMET:
		self.requiredBranches+= Selection.branchesForGenMET  
        if self.loadMCTruth_Var:
                #print "reading truth var"
		self.requiredBranches+= Selection.branchesForMCTruth
	if self.loadAK8:
    		self.requiredBranches +=  Selection.branchesForAk8JetSelection
	if self.loadAK10:
    		self.requiredBranches +=  Selection.branchesForAk10JetSelection
	if self.loadPFcand:
		self.requiredBranches += Selection.branchesForPfcand
    	if self.loadTriggerBranches:
		self.requiredBranches += Selection.branchesForTrigger
	if not self.isData:
		self.requiredBranches += self.branchesMC_PU
        if self.load_qg_tag: 
		self.requiredBranches += Selection.Selection.branchesForQGJetSelection
    	if self.loadStop:
    		#print "here or not "
		self.requiredBranches+= Selection.branchesForStop


    	self.hWeights = ROOT.TH1D("hWeights","Sum of weights",1,0.5,1.5)
    	self.hWeightsPlus = ROOT.TH1D("hWeightsPlus","Sum of positive  weights",1,0.5,1.5)
    	self.hWeightsMinus = ROOT.TH1D("hWeightsMinus","Sum of negative weights",1,0.5,1.5)
    	self.hStopNeutralino = ROOT.TH2F("hStopNeutralino","Weights for cross section computation",2000,0,2000,1000,0,1000)



    # ############# #
    # Reset objects #
    # ############# #

    def reset(self) :
        self.resetSelectedObjects()




    # ############################## #
    #  Event dump for sync exercise  #
    # ############################## #
    def syncDump(self, event):
    		prec = 4
		print event.ev_run, ":", \
		event.ev_lumi, ":", \
		event.ev_id, ":", \
		round(self.selectedLeptons[0].pT, prec), ":", \
		self.selectedLeptons[0].id, ":", \
		round(event.met_pt, prec), ":", \
		round(self.MT, prec), ":", \
		self.PassTrackVeto, ":", \
		len(self.selectedJets), ":", \
		self.ngoodbtags, ":", \
		self.numberOfGeneratedLeptons, ":", \
		round(self.dphi_Wlep, prec), ":", \
		round(self.HTSSM, prec), ":", \
		round(self.Mlb_leadb, prec), ":", \
		round(self.M3b, prec), ":", \
		round(self.MT2W,prec), ":", \
		round(self.topness,prec), ":", \
		round(self.hadchi2,prec) \


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
	if self.loadMCTruth_Var:
            self.genJetDump(event)
	
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

    def process(self,event,babyTupleTree,isoStudy = False) :

        self.reset()

	#fill the weight (treat separately positive and negative - needed for correction stat. uncert.
	self.hWeights.Fill(1,event.mc_weight)
	if event.mc_weight>0:   
		self.hWeightsPlus.Fill(1,event.mc_weight)
	else:
		self.hWeightsMinus.Fill(1,-event.mc_weight)

        if event.met_pt < 200:
            return False
        if len(event.gen_neutralino_m) > 0:
            #print "neutralino m %d" % event.gen_neutralino_m[1]
            self.hStopNeutralino.Fill(event.gen_stop_m[0], event.gen_neutralino_m[0]);
	#if (event.ev_lumi != 2756 or event.ev_id != 75567):
	#    return

        # Select muons,electrons
        self.muSelCode = []
	self.muonSelector(event, self.muSelCode)
	self.elSelCode = []
        self.electronSelector(event, self.elSelCode)

	# Make a cleaning
	self.leptonCleaning()

        # Sort selected leptons by pT
        self.selectedLeptons = sorted(self.selectedLeptons, key=lambda lepton: lepton.pT, reverse=True)
     
        # Selected gen jets
        if self.loadGenInfo:
            self.genJetSelector(event)
        
            #print "gen jet length in Analyzer: %d" % len(self.selectedGenJets)
            # Sort selected gen jets by pT
            self.selectedGenJets = sorted(self.selectedGenJets, key=lambda genjet: genjet.pT, reverse=True)
        
        # Selected jets
        self.jetSelector(event)

        # Sort selected jets by pT
        self.selectedJets = sorted(self.selectedJets, key=lambda jet: jet.pT, reverse=True)


	# Selected AK8 jets
	if(self.loadAK8):  self.ak8jetSelector(event)
	
        # Selected AK10 jets
	if(self.loadAK10):  self.ak10jetSelector(event)

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
	if self.computeVar: self.computeVariables(event)
  
  	# Retrieve gen lost leptons
	self.genLostLeptons = self.getGenLostLeptons(event, self.leadingLepton)

	#print "##@@ sync exec'"
 	###   sync exercise   ####
# 	if self.pvSelection(event) 			\
#		and len(self.selectedLeptons) == 1	\
#		and len(self.selectedJets) >=4		\
#		and event.met_pt > 50			\
#		and len(self.selectedLeptons2) == 0 	\
#		and len(self.vetoLeptons)==0	\
#		and self.isoTrackVeto(event)	\
#		and self.isTauVeto(event):
#		self.syncDump(event)	
		#print "debug: ",len(self.selectedLeptons2), len(self.vetoLeptons), self.isoTrackVeto(event), self.isTauVeto(event)

	# fill trigger info
	if self.saveTriggerInfos and self.isData:
		self.FillTriggerInfo(event)

	#######################
        # for synchronisation #
	#######################
	
	#if (event.ev_lumi == 234 and event.ev_id == 23332):
	if (event.ev_lumi,event.ev_id)  in self.eventList:
		print "##################"
		print event.ev_lumi,event.ev_id \
		      ,"n-lep:", len(self.selectedLeptons), "n-jets:", len(self.selectedJets), "n-lep2:", len(self.selectedLeptons2), "n-veto:", len(self.vetoLeptons) \
		      ,"met:", event.met_pt, "isTrackVeto:", self.isoTrackVeto(event), "isTauVeto:", self.isTauVeto(event)
		self.dumpPFCand(event)
		print self.selectedLeptons
		print self.selectedLeptons2
	 	print self.vetoLeptons
		#print "muon Dump"
		#self.muonDump(event)
		#print "electron Dump"
		#self.electronDump(event)
	#self.eventDump(event)


        # for iso study
	if isoStudy:
	    self.muonSelector(event,self.muSelCode2, False)
	    self.electronSelector(event,self.elSelCode2, False)
            # Sort selected leptons by pT
            self.noIsoSelectedMuons = sorted(self.noIsoSelectedMuons, key=lambda lepton: lepton['pt'], reverse=True)
            self.noIsoSelectedElectrons = sorted(self.noIsoSelectedElectrons, key=lambda lepton: lepton['pt'], reverse=True)



        # Fill event in babytuple
        if passEventSelection:
	    self.fill(event,babyTupleTree) #,self.addGenInfo)
	#just for synchronization	
	if (event.ev_lumi,event.ev_id)  in self.eventList:
            print "lost event found"
	    #self.fill(event,babyTupleTree) #,self.addGenInfo) #@MJ@ TODO commented this
        
        #return True
        return passEventSelection


