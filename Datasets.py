
from core import genericDataset

Dataset = genericDataset.Dataset
datasets = [

#Dataset("SingleElectron",wildcard="dpm:echabert/FlatTree/triggerV1/SingleElectron/Run2016B_PromptReco_v2_MINIAOD/160622_212229/0000/")
#Dataset("SingleMuon",wildcard="dpm:echabert/FlatTree/triggerV1/SingleMuon/Run2016B_PromptReco_v2_MINIAOD/160622_212210/0000/")

#Dataset("SMS_T2tt_850_100", wildcard="dpm:mjansova/FlatTree/sync0616-v2/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160614_141121/0000/merged")

#Dataset("sync", wildcard="local:/opt/sbg/data/data1/cms/echabert/Stop2015/Prod1Nov/CMSSW_7_4_12_patch4/src/IPHCFlatTree/FlatTreeProducer/test/sync/output3.root"),
#Dataset("sync", wildcard="local:/opt/sbg/data/data1/cms/echabert/Stop2015/Prod1Nov/CMSSW_7_4_12_patch4/src/IPHCFlatTree/FlatTreeProducer/test/output0.root"),
#Dataset("sync", wildcard="local:/opt/sbg/data/data1/cms/echabert/Stop2015/Prod1Nov/CMSSW_7_4_12_patch4/src/IPHCFlatTree/FlatTreeProducer/test/output_miniIso.root"),
#Dataset("sync", wildcard="local:/opt/sbg/data/data1/cms/echabert/Stop2015/Prod1Nov/CMSSW_7_4_12_patch4/src/IPHCFlatTree/FlatTreeProducer/test/output_debug.root"),
#Dataset("sync", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_083845/0000"),
#Dataset("ST_s", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151217_233558/0000"),
#Dataset("ST_t-top", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151217_233820/0000"),

#Dataset("TTjets", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180950/0000"),

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#DATA
Dataset("SE_1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleElectron/Run2016B_PromptReco_v2_MINIAOD/160725_204148/0001"),
Dataset("SE_0", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleElectron/Run2016B_PromptReco_v2_MINIAOD/160725_204148/0000"),
Dataset("SE_C", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleElectron/Run2016C_PromptReco_v2_MINIAOD/160725_204218/0000"),
Dataset("SE_D", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleElectron/Run2016D_PromptReco_v2_MINIAOD/160725_204242/0000"),

#kskovpen/FlatTree/Medusa-patch4-v20160726/SingleElectron/Run2016B_PromptReco_v2_MINIAOD/160726_20d4148/0001"
Dataset("SM_0", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleMuon/Run2016B_PromptReco_v2_MINIAOD/160725_204321/0000"),
Dataset("SM_1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleMuon/Run2016B_PromptReco_v2_MINIAOD/160725_204321/0001"),
Dataset("SM_C", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleMuon/Run2016C_PromptReco_v2_MINIAOD/160725_204345/0000"),
Dataset("SM_D", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SingleMuon/Run2016D_PromptReco_v2_MINIAOD/160725_204404/0000"),


#Dataset("MET_0", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/MET/Run2016B_PromptReco_v2_MINIAOD/160725_203926/0000"),
#Dataset("MET_1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/MET/Run2016B_PromptReco_v2_MINIAOD/160725_203926/0001"),

##MC
#Dataset("WJetsToLNuTune",                   wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_182216/0000"),
#Dataset("WJetsToLNuPt100to250", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160729_123952/0000"),
#Dataset("WJetsToLNuPt250to400", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160729_124016/0000"),
#Dataset("WJetsToLNuPt400to600", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160728_165026/0000"),
#Dataset("WJetsToLNuPt600toInf", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160728_165053/0000"),
#Dataset("WJetsToLNuHT100To200ext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1_v2_MINIAODSIM/160726_183703/0000"),
#Dataset("WJetsToLNuHT200To400ext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1_v1_MINIAODSIM/160726_183833/0000"),
#Dataset("WJetsToLNuHT200To400v3v2", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v2_MINIAODSIM/160726_183811/0000"),
#Dataset("WJetsToLNuHT400To600ext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1_v1_MINIAODSIM/160727_135345/0000"),
#Dataset("WJetsToLNuHT400To600v3v2", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v2_MINIAODSIM/160726_184004/0000"),
#Dataset("WJetsToLNuHT600To800v3v2", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v2_MINIAODSIM/160726_184110/0000"),
#Dataset("WJetsToLNuHT800To1200ext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1_v1_MINIAODSIM/160726_184226/0000"),
#Dataset("WJetsToLNuHT800To1200v3v1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160726_184150/0000"),
#Dataset("WJetsToLNuHT1200To2500ext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1_v1_MINIAODSIM/160726_183745/0000"),
#Dataset("WJetsToLNuHT1200To2500v3v2", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v2_MINIAODSIM/160726_183723/0000"),
#Dataset("WJetsToLNuHT2500ToInfv3v1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160727_135527/0000"),
#Dataset("W1JetsToLNuTune", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160726_184246/0000"),
#Dataset("W2JetsToLNuTune", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160726_184308/0000"),
#Dataset("W3JetsToLNuTune", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160726_184335/0000"),
#Dataset("W4JetsToLNuTune", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160726_184356/0000"),
#Dataset("W1JetsToLNuPt200", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W1JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160728_165117/0000"),
#Dataset("W2JetsToLNuPt200", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W2JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160728_165139/0000"),
#Dataset("W3JetsToLNuPt200", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W3JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160728_165205/0000"),
#Dataset("W4JetsToLNuPt200", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/W4JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160729_123930/0000"),
#
#Dataset("TTJetsSLtop", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180843/0000"),
#Dataset("TTJetsSLatopv1", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180903/0000"),
#Dataset("TTJetsSLatopext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1_v1_MINIAODSIM/160726_180929/0000"),
#Dataset("TTJetsDLv0v4", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v4_MINIAODSIM/160726_180756/0000"),
#Dataset("TTJetsDLext", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1_v1_MINIAODSIM/160726_180821/0000"),
#
#Dataset("ST_s", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160727_143227/0000"),
#Dataset("ST_tW_top", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180521/0000"),
#Dataset("ST_tW_atop", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180432/0000"),
#Dataset("ST_t", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_180411/0000"),
#
#Dataset("TTWtoQQ", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_190306/0000"),
#Dataset("TTWtoLNu", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_190231/0000"),
#Dataset("TTT", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/TTToSemiLeptonic_13TeV-powheg/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1_v2_MINIAODSIM/160726_181358/0000"),
#Dataset("ttZ", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ttZJets_13TeV_madgraphMLM/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_190600/0000"),
#Dataset("VV", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_182237/0000"),
#Dataset("tZq", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_183614/0000"),
#Dataset("WZ", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_182856/0000"),
#Dataset("ZZ", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_183321/0000"),
#
#Dataset("T2tt_150to250", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_184449/0000"),
#Dataset("T2tt_250to350", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_184513/0000"),
#Dataset("T2tt_350to400", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_184534/0000"),
#Dataset("T2tt_400to1200", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0_v1_MINIAODSIM/160726_184600/0000"),


#------------------OLD------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Dataset("Wjets", wildcard="dpm:kskovpen/FlatTree/Medusa-patch4-v20160726/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v2_MINIAODSIM/160726_183723/0000"),
#Dataset("W1Jets", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_Asympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160511_134915/0000"),
#Dataset("W2Jets", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160422_121518/0000"),
#Dataset("W3Jets", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_Asympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160422_121532/0000"),
#Dataset("W4Jets", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_Asympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160422_121549/0000"),

##first merge needed
#Dataset("T2bW_625to950_0to300", wildcard="dpm:mjansova/MantaRay-patch7-v16022016/SMS-T2bW_X05_mStop-625to950_0to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160420_082553/0000/merged"),

#Dataset("100-125_1to50", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-100-125_mLSP-1to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/160125_102519/0000"),
#Dataset("200_1to125", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-200_mLSP-1to125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102535/0000"),
#Dataset("225_25to150", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-225_mLSP-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102549/0000"),
#Dataset("250_1to175", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-250_mLSP-1to175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102609/0000"),
#Dataset("275_75to200", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-275_mLSP-75to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102624/0000"),
#Dataset("400-475_1to400", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-400to475_mLSP-1to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102638/0000"),
#Dataset("SMS_T2tt_850_100", wildcard="dpm:echabert/FlatTree/sync0616-v1/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1_PUSpring16_80X_mcRun2_asymptotic_2016_v3_v1_MINIAODSIM/160606_154027/0000/")
#Dataset("TTjets_M5_0", wildcard="dpm:mjansova/MantaRay-patch7-v16022016/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_124452/0000/merged"),
#Dataset("TTjets_M5_1", wildcard="dpm:mjansova/MantaRay-patch7-v16022016/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_124452/0000/merged"),
#Dataset("600-950_1to450_0", wildcard="dpm2:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0000" , min = 0, max = 200),
#Dataset("600-950_1to450_2", wildcard="dpm2:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0000" , min =201, max = 500),
#Dataset("600-950_1to450_3", wildcard="dpm2:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0000" , min =501, max = 750),
#Dataset("600-950_1to450_4", wildcard="dpm2:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0000" , min =751, max = 907),
#Dataset("600-950_1to450_5", wildcard="dpm2:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0000" , min =909, max = 999),
#Dataset("WJetsToLNu_HT-100To200", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085653/0000"),
#Dataset("WJetsToLNu_HT-1200To2500", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103607/0000"),
#Dataset("WJetsToLNu_HT-200To400", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085726/0000"),
#Dataset("WJetsToLNu_HT-2500ToInf", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103628/0000"),
#Dataset("WJetsToLNu_HT-400To600", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103502/0000"),
#Dataset("WJetsToLNu_HT-600To800", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103524/0000"),
#Dataset("WJetsToLNu_HT-800To1200", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103544/0000"),

#Dataset("TTZ_ll", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151218_085236/0000/"), 
#Dataset("ST_tW-atop", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_103717/0000"),
#Dataset("600-950_1to450_1", wildcard="dpm:/mjansova/MantaRay-patch7-v16022016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160216_141121/0001"),
#Dataset("TTjets_M5_1", wildcard="dpm:mjansova/MantaRay-patch7-v16022016/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160217_124452/0001"),
#Dataset("400to475_1to400", wildcard="dpm:/mjansova/MantaRay-patch7-v09022016/SMS-T2tt_mStop-400to475_mLSP-1to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160209_134225/0000"),
#Dataset("500-525-550_1to425-300to450", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-500-525-550_mLSP-1to425-325to450-1to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102654/0000"),
#Dataset("600-950_1to450", wildcard="dpm:/mjansova/MantaRay-patch7-v25012016/SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160125_102714/0000"),

#Dataset("signal_test", wildcard="dpm:/mjansova/MantaRay-patch7-v20150822/SMS-T2tt_mStop-400to475_mLSP-1to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_FastAsympt25ns_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/160121_140418/0000"),
#Dataset("ST_atop", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151217_233802/0000/"),
#Dataset("ST_tW-atop", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151217_233858/0000"),
#Dataset("ST_tW-top", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151217_234037/0000"),
#Dataset("SingleElectron_RunD", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/SingleElectron/Run2015D_05Oct2015_v1_MINIAOD/151217_173917/0000"),
#Dataset("SingleElectron_RunD_prompt", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/SingleElectron/Run2015D_PromptReco_v4_MINIAOD/151217_140234/0000"),
#Dataset("SingleMuon_RunD", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/SingleMuon/Run2015D_05Oct2015_v1_MINIAOD/151217_173933/0000"),
#Dataset("SingleMuon_RunD_prompt", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/SingleMuon/Run2015D_PromptReco_v4_MINIAOD/151217_140254/0000"),
#Dataset("TTjets_M5", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_084124/0000"),
#Dataset("WJetsToLNu_HT-100To200", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085653/0000"),
#Dataset("WJetsToLNu_HT-1200To2500", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085708/0000"),
#Dataset("WJetsToLNu_HT-200To400", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085726/0000"),
#Dataset("WJetsToLNu_HT-2500ToInf", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085741/0000"),
#Dataset("WJetsToLNu_HT-400To600", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085802/0000"),
#Dataset("WJetsToLNu_HT-600To800", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085836/0000"),
#Dataset("WJetsToLNu_HT-800To1200", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151218_085913/0000"),
#Dataset("TTZ_ll", wildcard="dpm:/kskovpen/FlatTree/Akoula-patch1-v20151217/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151218_085236/0000/"), 

#  Dataset("TTJets-FXFX", xsection=831.76  ,
#	wildcard="dpm:/echabert/FlatTrees/test-ak10/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_TTjets/151020_151326/0000/"),
#  Dataset("WJets", xsection=61466  ,
#	wildcard="dpm:/echabert/FlatTrees/test-ak10/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_Wjets/151021_093821/0000/")


#Dataset("T2tt_425_325", wildcard="dpm:/mjansova/MantaRay-patch7-v20150822/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR_PU20bx25_tsg_PHYS14_25_V1_v1_MINIAODSIM/160115_143036/0000"),
#Dataset("T2tt_500_325", wildcard="dpm:/mjansova/MantaRay-patch7-v20150822/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR_PU20bx25_tsg_PHYS14_25_V1_v1_MINIAODSIM/160115_143052/0000"),
#Dataset("T2tt_650_325", wildcard="dpm:/mjansova/MantaRay-patch7-v20150822/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR_PU20bx25_tsg_PHYS14_25_V1_v1_MINIAODSIM/160115_143123/0000/"),
#Dataset("T2tt_850_100", wildcard="dpm:/mjansova/MantaRay-patch7-v20150822/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR_PU20bx25_tsg_PHYS14_25_V1_v1_MINIAODSIM/160115_143141/0000/"),

#Dataset("WJetsToLNu_HT-100To200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_100To200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213910/0000/"), 
#Dataset("WJetsToLNu_HT-1200To2500", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_1200To2500_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213925/0000/"), 
#Dataset("WJetsToLNu_HT-200To400", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_200To400_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213940/0000/"), 
#Dataset("WJetsToLNu_HT-2500ToInf", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_2500ToInf_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_213955/0000/"), 
#Dataset("WJetsToLNu_HT-400To600", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_400To600_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214018/0000/"), 
#Dataset("WJetsToLNu_HT-600To800", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_600To800_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214040/0000/"), 
#Dataset("WJetsToLNu_HT-600ToInf", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_600ToInf_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214054/0000/"), 
#Dataset("WJetsToLNu_HT-800To1200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT_800To1200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_214110/0000/"), 



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


#Dataset("SingleElectron_RunD_prompt", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/SingleElectron/Run2015D_PromptReco_v4_MINIAOD/151105_132608/0000/"),
#Dataset("SingleElectron_RunD", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/SingleElectron/Run2015D_05Oct2015_v1_MINIAOD/151105_132551/0000/"),
#Dataset("SingleMuon_RunD_prompt", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/SingleMuon/Run2015D_PromptReco_v4_MINIAOD/151105_132652/0000/"),
#Dataset("SingleMuon_RunD", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG/SingleMuon/Run2015D_05Oct2015_v1_MINIAOD/151105_132630/0000/"),


#Dataset("ST_s", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101751/0000/"),
#Dataset("ST_t-atop", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101818/0000/"),
#Dataset("ST_t-top", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151104_101805/0000/"),
#Dataset("ST_tW-atop", wildcard="dpm:/echabert//FlatTree/MantaRay-patch7-v20150822_QG/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151105_105250/0000/"),
#Dataset("ST_tW-top", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v2_MINIAODSIM/151104_101901/0000/"),
#Dataset("TTjets_aMC", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v3_MINIAODSIM/151104_101915/0000/"),
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

#Dataset("QCD_HT100to200", wildcard="dpm:/echabert/FlatTree/MantaRay-patch7-v20150822_QG//QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCD_HT100to200_TuneCUETP8M1_13TeV_madgraphMLM_pythia8_RunIISpring15MiniAODv2_74X_mcRun2_asymptotic_v2_v1_MINIAODSIM/151109_165939/0000/"),
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
