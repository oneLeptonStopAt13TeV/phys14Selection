
from core import genericDataset

Dataset = genericDataset.Dataset
datasets = [

#    Dataset("ttbar-madgraph", xsection=831.76,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/crab_ttbar-madgraph/150314_230009/0000/"),          
#    Dataset("ttbar-pythia8", xsection=831.76,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TT_Tune4C_13TeV-pythia8-tauola/crab_ttbar-pythia8/150314_230037/0000/"),          

    Dataset("T2tt_850_100",   xsection=0.01896,
            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/crab_T2tt_850_100/150314_225910/0000/"),
#    Dataset("T2tt_425_325",   xsection=1.31169,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_425_325/150314_225747/0000/"),
#   Dataset("T2tt_500_325",   xsection=0.51848,
#           wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_500_325/150314_225814/0000/"),
   Dataset("T2tt_650_325",   xsection=0.107045,
           wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_650_325/150314_225841/0000/"),          
   #Dataset("T2tt_650_325",   xsection=0.107045,
   #        wildcard="local:/opt/sbg/data/data2/cms/aaubin/stopPhys14/store/FlatTrees_T2tt_650_325/*.root"),

#    Dataset("Wjets", xsection=61466,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/WJetsToLNu_13TeV-madgraph-pythia8-tauola/crab_Wjets/150314_230201/0000/"),          
#
#    Dataset("singleTopbar_s", xsection=4.16,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTop_s/150314_230257/0000/"),
#    Dataset("singleTopbar_t", xsection=80.95,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola/crab_singleTop_t/150314_230228/0000/"),
#    Dataset("singleTop_s", xsection=7.20,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTopbar_s/150314_230354/0000/"),
#    Dataset("singleTop_t", xsection=136.02,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TToLeptons_t-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTopbar_t/150314_230326/0000/"),
#
#    Dataset("DY",  xsection=6024,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/DYJetsToLL_M-50_13TeV-madgraph-pythia8/crab_DY/150314_230421/0000/"),          
#    Dataset("ttW", xsection=0.70,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTWJets_Tune4C_13TeV-madgraph-tauola/crab_ttW/150314_230105/0000/"),          
#    Dataset("ttZ", xsection=0.62,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTZJets_Tune4C_13TeV-madgraph-tauola/crab_ttZ/150314_230132/0000/"),
#    Dataset("WZ",  xsection=48.4,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/crab_WZ/150314_230516/0000/"),          
#    Dataset("ZZ",  xsection=15.4,
#            wildcard="dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/ZZTo4L_Tune4C_13TeV-powheg-pythia8/crab_ZZ/150314_230449/0000/")
]
