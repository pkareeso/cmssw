import FWCore.ParameterSet.Config as cms

SUSY_HLT_Muon_BJet = cms.EDAnalyzer("SUSY_HLT_Muon_BJet",
  trigSummary = cms.InputTag('hltTriggerSummaryAOD','','HLT'),
  MuonCollection = cms.InputTag("muons"),
  pfJetCollection = cms.InputTag("ak4PFJetsCHS"),
  caloJetCollection = cms.InputTag("ak4CaloJets"),
  TriggerResults = cms.InputTag('TriggerResults','','HLT'),
  HLTProcess = cms.string('HLT'),
  TriggerPath = cms.string('HLT_Mu10_CentralPFJet30_BTagCSV0p5PF_v'),
  TriggerFilterMuon = cms.InputTag('hltL3fL1sMu0L1f0L2f3QL3Filtered10Q','','HLT'),
  TriggerFilterJet = cms.InputTag('hltCSV0p5FilterSingleMu10','','HLT'), #the last filter in the path
  PtThrJet = cms.untracked.double(40.0),
  EtaThrJet = cms.untracked.double(3.0)
)


SUSY_HLT_Muon_BJet_FASTSIM = cms.EDAnalyzer("SUSY_HLT_Muon_BJet",
  trigSummary = cms.InputTag('hltTriggerSummaryAOD','','HLT'),
  MuonCollection = cms.InputTag("muons"),
  pfJetCollection = cms.InputTag("ak4PFJetsCHS"),
  caloJetCollection = cms.InputTag("ak4CaloJets"),
  TriggerResults = cms.InputTag('TriggerResults','','HLT'),
  HLTProcess = cms.string('HLT'),
  TriggerPath = cms.string('HLT_Mu10_CentralPFJet30_BTagCSV0p5PF_v'),
  TriggerFilterMuon = cms.InputTag('hltL3fL1sMu0L1f0L2f3QL3Filtered10Q','','HLT'),
  TriggerFilterJet = cms.InputTag('hltCSV0p5FilterSingleMu10','','HLT'), #the last filter in the path
  PtThrJet = cms.untracked.double(40.0),
  EtaThrJet = cms.untracked.double(3.0)
)


SUSY_HLT_Muon_BJet_POSTPROCESSING = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/SUSYBSM/HLT_Mu10_CentralPFJet30_BTagCSV0p5PF"),
    verbose        = cms.untracked.uint32(2), # Set to 2 for all messages
    resolution     = cms.vstring(""),
    efficiency     = cms.vstring(
       "pfHTTurnOn_eff 'Turn-on vs HT; PFHT (GeV); #epsilon' pfHTTurnOn_num pfHTTurnOn_den",
       "MuTurnOn_eff 'Turn-on vs Mu pT; pT (GeV); #epsilon' MuTurnOn_num MuTurnOn_den",
    )
)


SUSY_HLT_Muon_BJet_FASTSIM_POSTPROCESSING = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/SUSYBSM/HLT_Mu10_CentralPFJet30_BTagCSV0p5PF"),
    verbose        = cms.untracked.uint32(2), # Set to 2 for all messages
    resolution     = cms.vstring(""),
    efficiency     = cms.vstring(
       "pfHTTurnOn_eff 'Turn-on vs HT; PFHT (GeV); #epsilon' pfHTTurnOn_num pfHTTurnOn_den",
       "MuTurnOn_eff 'Turn-on vs Mu pT; pT (GeV); #epsilon' MuTurnOn_num MuTurnOn_den",
    )
)
