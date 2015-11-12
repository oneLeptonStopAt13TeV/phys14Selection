
from core import genericDataset

Dataset = genericDataset.Dataset
datasets = [
#  Dataset("TTJets-FXFX", xsection=831.76  ,
#	wildcard="dpm:/echabert/FlatTrees/test-ak10/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TTjets/151020_151326/0000/"),
#  Dataset("WJets", xsection=61466  ,
#	wildcard="dpm:/echabert/FlatTrees/test-ak10/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_Wjets/151021_093821/0000/")


#Dataset("T2tt_425_325", wildcard="dpm:/echabert/FlatTrees/test-ak10/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_425_325/151023_162425/0000"),
#Dataset("T2tt_500_325", wildcard="dpm:/echabert/FlatTrees/test-ak10//SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_500_325/151023_162445/0000"),
#Dataset("T2tt_650_325", wildcard="dpm:/echabert/FlatTrees/test-ak10//SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_650_325/151023_162504/0000/"),
#Dataset("T2tt_850_325", wildcard="dpm:/echabert/FlatTrees/test-ak10//SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/crab_T2tt_850_100/151023_162703/0000/"),



#Dataset("MuonEG_RunD", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//MuonEG/Run2015D_05Oct2015_v2_MINIAOD/151025_193306/0000/"), 
#Dataset("MuonEG_RunD_prompt", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//MuonEG/Run2015D_PromptReco_v4_MINIAOD/151025_192834/0000/"), 
#Dataset("ST_s", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153213/0000/"), 
#Dataset("ST_t-atop", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153252/0000/"), 
#Dataset("ST_t-top", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153238/0000/"), 
#Dataset("ST_tW-atop", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153308/0000/"), 
#Dataset("ST_tW-top", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151025_153323/0000/"), 
#Dataset("SingleElectron_RunD", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//SingleElectron/Run2015D_05Oct2015_v1_MINIAOD/151025_193322/0000/"), 
#Dataset("SingleElectron_RunD_prompt", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//SingleElectron/Run2015D_PromptReco_v4_MINIAOD/151025_192855/0000/"), 
#Dataset("SingleMuon_RunD", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//SingleMuon/Run2015D_05Oct2015_v1_MINIAOD/151025_193337/0000/"), 
#Dataset("SingleMuon_RunD_prompt", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//SingleMuon/Run2015D_PromptReco_v4_MINIAOD/151025_192910/0000/"), 
###Dataset("TTjets_aMC", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v3_MINIAODSIM/151025_153359/0000/"), 
#Dataset("TTjets_M5", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153415/0000/"), 
#Dataset("TTjets_pow", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTTo2L2Nu_13TeV-powheg/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153453/0000/"), 
#Dataset("TTW_ln", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_140352/0000/"), 
#Dataset("TTW_qq", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_140408/0000/"), 
#Dataset("TTZ_ll", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151025_140422/0000/"), 
#Dataset("TTZ_qq", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_140437/0000/"), 
#Dataset("TT_pow", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153430/0000/"), 
#Dataset("Wjets_aMC", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153508/0000/"), 
#Dataset("WW_aMC", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153525/0000/"), 
#Dataset("WW_pow", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//WWTo2L2Nu_13TeV-powheg/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153542/0000/"), 
#Dataset("WZ", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153608/0000/"), 
#Dataset("ZZ_2l2n", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring15MiniAODv2_Asympt50ns_74X_mcRun2_asymptotic50ns_v0_v1_MINIAODSIM/151025_153639/0000/"), 
#Dataset("ZZ", wildcard="dpm:/kskovpen/FlatTree/MantaRay-patch8-v20151025//ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151025_153623/0000/")

#################################################
# new samples with AK8 - MC info - QG - pfcand  #
#################################################

#Dataset("T2tt_425_325", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_425_325/151108_154559/0000/"),
#Dataset("T2tt_500_325", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_500_325/151108_154623/0000/"),
#Dataset("T2tt_650_325", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/crab_T2tt_650_325/151108_154642/0000/"),
#Dataset("T2tt_850_325", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/crab_T2tt_850_100/151108_154703/0000/"),
#
Dataset("SingleElectron_RunD_prompt", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/SingleElectron/Run2015D_PromptReco_v4_MINIAOD/151105_132608/0000/"),
Dataset("SingleElectron_RunD", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/SingleElectron/Run2015D_05Oct2015_v1_MINIAOD/151105_132551/0000/"),
Dataset("SingleMuon_RunD_prompt", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/SingleMuon/Run2015D_PromptReco_v4_MINIAOD/151105_132652/0000/"),
Dataset("SingleMuon_RunD", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/SingleMuon/Run2015D_05Oct2015_v1_MINIAOD/151105_132630/0000/"),
#
#Dataset("ST_s", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101751/0000/"),
#Dataset("ST_t-atop", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101818/0000/"),
#Dataset("ST_t-top", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101805/0000/"),
#Dataset("ST_tW-atop", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151105_105250/0000/"),
#Dataset("ST_tW-top", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151104_101901/0000/"),
##Dataset("TTjets_aMC", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v3_MINIAODSIM/151104_101915/0000/"),
#Dataset("TTjets_M5", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101932/0000/"),
#Dataset("TTW_ln", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102022/0000/"),
#Dataset("TTW_qq", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102037/0000/"),
#Dataset("TTZ_ll", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151104_102052/0000"),
#Dataset("TTZ_qq", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102108/0000/"),
#Dataset("Wjets_aMC", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_TuneCUETP8M1_13TeV_amcatnloFXFX_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151108_162520/0000/"),
#Dataset("WW_aMC", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102140/0000/"),
#Dataset("WW_pow", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WWTo2L2Nu_13TeV-powheg/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102156/0000/"),
#Dataset("WZ", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102214/0000/"),
#Dataset("ZZ", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_102231/0000/"),
#
##Dataset("QCD_HT100to200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT100to200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165939/0000/"),
#Dataset("QCD_HT200to300", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT200to300_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_170025/0000/"),
#Dataset("QCD_HT300to500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT300to500_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_170042/0000/"),
#Dataset("QCD_HT500to700", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT500to700_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_220519/0000/"), 
#Dataset("QCD_HT700to1000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT700to1000_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_170112/0000/"),
#Dataset("QCD_HT1000to1500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT1000to1500_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165920/0000/"),
#Dataset("QCD_HT1500to2000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT1500to2000_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165956/0000/"),
#Dataset("QCD_HT2000toInf", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT2000toInf_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_170012/0000/"),
#Dataset("WToENu_M-1000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/WToENu_M-1000_TuneCUETP8M1_13TeV-pythia8/crab_WToENu_M_1000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165622/0000/"),
#Dataset("WToENu_M_200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToENu_M-200_TuneCUETP8M1_13TeV-pythia8/crab_WToENu_M_200_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165639/0000/"),
#Dataset("WToENu_M_3000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToENu_M-3000_TuneCUETP8M1_13TeV-pythia8/crab_WToENu_M_3000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165653/0000/"),
#Dataset("WToENu_M_500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToENu_M-500_TuneCUETP8M1_13TeV-pythia8/crab_WToENu_M_500_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165707/0000/"),
#Dataset("WToMuNu_M_1000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToMuNu_M-1000_TuneCUETP8M1_13TeV-pythia8/crab_WToMuNu_M_1000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165726/0000/"),
#Dataset("WToMuNu_M-200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/WToMuNu_M-200_TuneCUETP8M1_13TeV-pythia8/crab_WToMuNu_M_200_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165739/0000/"),
#Dataset("WToMuNu_M-3000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/WToMuNu_M-3000_TuneCUETP8M1_13TeV-pythia8/crab_WToMuNu_M_3000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165752/0000/"),
#Dataset("WToMuNu_M-500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/WToMuNu_M-500_TuneCUETP8M1_13TeV-pythia8/crab_WToMuNu_M_500_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165805/0000/"),
#Dataset("WToTauNu_M_1000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToTauNu_M-1000_TuneCUETP8M1_13TeV-pythia8/crab_WToTauNu_M_1000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165818/0000/"),
#Dataset("WToTauNu_M_200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToTauNu_M-200_TuneCUETP8M1_13TeV-pythia8/crab_WToTauNu_M_200_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165833/0000/"),
#Dataset("WToTauNu_M_3000", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToTauNu_M-3000_TuneCUETP8M1_13TeV-pythia8/crab_WToTauNu_M_3000_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165846/0000/"),
#Dataset("WToTauNu_M_500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WToTauNu_M-500_TuneCUETP8M1_13TeV-pythia8/crab_WToTauNu_M_500_TuneCUETP8M1_13TeV_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165859/0000/"),
#
#Dataset("WJetsToLNu_HT-100to200_P14", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis//WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/crab_WJets_HT-100-200/151109_213341/0000"),
#Dataset("WJetsToLNu_HT-200to400_14", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis//WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/crab_WJets_HT-200-400/151109_213401/0000/"),
#Dataset("WJetsToLNu_HT-400to600_14", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis//WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/crab_WJets_HT-400-600/151109_213422/0000/"),
#Dataset("WJetsToLNu_HT-600toInf_P14", wildcard="dpm:/echabert/FlatTrees/test-ak10-bis//WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/crab_WJets_HT-600-inf/151109_213450/0000/"),
#
#Dataset("WJetsToLNu_HT-100To200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_100To200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213910/0000/"), 
#Dataset("WJetsToLNu_HT-1200To2500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_1200To2500_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213925/0000/"), 
#Dataset("WJetsToLNu_HT-200To400", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_200To400_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213940/0000/"), 
#Dataset("WJetsToLNu_HT-2500ToInf", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_2500ToInf_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213955/0000/"), 
#Dataset("WJetsToLNu_HT-400To600", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_400To600_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214018/0000/"), 
#Dataset("WJetsToLNu_HT-600To800", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_600To800_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214040/0000/"), 
#Dataset("WJetsToLNu_HT-600ToInf", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_600ToInf_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214054/0000/"), 
#Dataset("WJetsToLNu_HT-800To1200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_800To1200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214110/0000/"), 

#Dataset("DYJetsToNuNu", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToNuNu_TuneCUETP8M1_13TeV_amcatnloFXFX_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151110_140310/0000/"),
]
