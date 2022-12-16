from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = '' # output logs directory
#config.General.workArea = 'crab_reco_step2_benchmark_bgctau10cm'
#config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'flyingtop.py'

config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxJobRuntimeMin = 2630
#$$
config.JobType.inputFiles = ['TMVAClassification_BDTG50cmsansalgo.weights.xml']
#$$

config.section_("Data")
#$$
# config.Data.inputDataset = '/UDD_bgctau10_smu250_snu200/blochd-2018_step2HLT-b403a189a2d057e62e59ed092120c7f4/USER'
#config.Data.inputDataset = '/UDD_bgctau30_smu300_snu250/blochd-2018_step2HLT-b403a189a2d057e62e59ed092120c7f4/USER'
config.Data.inputDataset = '/UDD_bgctau50_smu275_snu225/blochd-2018_step2HLT-b403a189a2d057e62e59ed092120c7f4/USER'
# config.Data.inputDataset = '/UDD_bgctau70_smu250_snu200/blochd-2018_step2HLT-b403a189a2d057e62e59ed092120c7f4/USER'
#$$
config.Data.inputDBS = 'phys03'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits =  -1 

#$$
config.Data.outLFNDirBase = '/store/user/pvaucell/CMSSW_10_6_20_LLP/MC/'
#$$

#$$
config.Data.publication = False
config.Data.outputDatasetTag = '2018_step3_test'
#$$

config.section_("Site")
config.Site.storageSite = 'T2_FR_IPHC'
