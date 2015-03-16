
from core import genericDataset

Dataset = genericDataset.Dataset
datasets = [
    Dataset("T2tt_850_100",   "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/crab_T2tt_850_100/150314_225910/0000/",          xsection=-1),
    Dataset("T2tt_425_325",   "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_425_325/150314_225747/0000/",          xsection=-1),
    Dataset("T2tt_500_325",   "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_500_325/150314_225814/0000/",          xsection=-1),
    Dataset("T2tt_650_325",   "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_650_325/150314_225841/0000/",          xsection=-1),
    
    Dataset("ttbar-madgraph", "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/crab_ttbar-madgraph/150314_230009/0000/",          xsection=-1),
    Dataset("ttbar-pythia8",  "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TT_Tune4C_13TeV-pythia8-tauola/crab_ttbar-pythia8/150314_230037/0000/",          xsection=-1),
    
    Dataset("Wjets",          "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/WJetsToLNu_13TeV-madgraph-pythia8-tauola/crab_Wjets/150314_230201/0000/",          xsection=-1),
   
    Dataset("singleTopbar_s", "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTop_s/150314_230257/0000/",          xsection=-1),
    Dataset("singleTopbar_t", "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola/crab_singleTop_t/150314_230228/0000/",          xsection=-1),
    Dataset("singleTop_s",    "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTopbar_s/150314_230354/0000/",          xsection=-1),
    Dataset("singleTop_t",    "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TToLeptons_t-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/crab_singleTopbar_t/150314_230326/0000/",          xsection=-1),

    Dataset("DY",             "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/DYJetsToLL_M-50_13TeV-madgraph-pythia8/crab_DY/150314_230421/0000/",          xsection=-1),
    Dataset("ttW",            "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTWJets_Tune4C_13TeV-madgraph-tauola/crab_ttW/150314_230105/0000/",          xsection=-1),
    Dataset("ttZ",            "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTZJets_Tune4C_13TeV-madgraph-tauola/crab_ttZ/150314_230132/0000/",          xsection=-1),
    Dataset("WZ",             "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/crab_WZ/150314_230516/0000/",          xsection=-1),
    Dataset("ZZ",             "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/ZZTo4L_Tune4C_13TeV-powheg-pythia8/crab_ZZ/150314_230449/0000/", xsection=-1)
    
    #Dataset("ttH",           "dpm:/aaubin/FlatTrees/v20150314-WildBeast-v2/TTbarH_M-125_13TeV_amcatnlo-pythia8-tauola/crab_ttH/150314_225940/0000/",          xsection=-1),
]
