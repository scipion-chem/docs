'''This script extract a dataframe from a scipion VDS workflow wth the information about all the docking poses
generated, including:
- Original molecule
- Active / Decoy
- Docking software
- Consensus subsets they are contained in

Usage:
    scipion3 python extracData.py <projectName>
'''

import pandas as pd
import pickle
import os, sys

from pyworkflow.project import Manager

PROJECT_NAME = sys.argv[1]
oriPath = os.getcwd()

PRINT_SETS = False
INFO_COLUMNS = ['UniqueName', 'MolName', 'Type', 'ROI_ID', 'PoseFile', 'Energy', 'ODDTScore']

manager = Manager()
project = manager.loadProject(PROJECT_NAME)

def printSets(project):
  protDic = project.getProtocolsDict()
  for protId in protDic:
    protocol = project.getProtocol(protId)
    if 'consensus' in protocol.getObjLabel().lower():
      if PRINT_SETS:
        print()
        print(protId, protocol)
        for inLabel, inPoint in protocol.iterInputPointers():
          print('\t', inLabel, inPoint.get())

        for outLabel, outSet in protocol.iterOutputAttributes():
          print('\t', outLabel, outSet)

def isInConsensus(uniqueName, inConsensus):
  return uniqueName in inConsensus

def parseInputSets(protocolC2, protocolC3):
  '''Return a panda dataframe with molecules as rows and several info as columns, including whether of
  not the molcules remains in the output consensus:

  Columns: UniqueName, MolName, DockType, GridId, PoseFile, Energy, ODDTScore, isInConsensus
  '''

  docks, c = [], INFO_COLUMNS
  for inLabel, inPoint in protocolC2.iterInputPointers():
    for mol in inPoint.get():
      docks += [{c[0]: mol.getUniqueName(), c[1]: mol.getMolName(), c[2]: mol._type.get(), c[3]: mol.getGridId(),
                 c[4]: mol.getPoseFile(), c[5]: mol.getEnergy(), c[6]: mol._oddtScore_1.get()}]

  activeDF = pd.DataFrame(docks)
  inConsensus = parseConsensusSet(protocolC2)
  activeDF['InConsensus_2'] = activeDF['UniqueName'].apply(lambda x: isInConsensus(x, inConsensus))
  inConsensus = parseConsensusSet(protocolC3)
  activeDF['InConsensus_3'] = activeDF['UniqueName'].apply(lambda x: isInConsensus(x, inConsensus))
  
  # print(f'In consensus: ', activeDF['InConsensus'].sum())
  return activeDF

def parseConsensusSet(protocol):
  '''Return a list of the unique molnames of the molecules outputed by a protocol'''
  inConsensus = []
  for outLabel, outSet in protocol.iterOutputAttributes():
    for mol in outSet:
      inConsensus += [mol.getUniqueName()]
  return inConsensus

if PRINT_SETS:
  printSets(project)

consProtDic = {}
pCons2Act, pCons3Act, pCons2Dec, pCons3Dec = None, None, None, None
protDic = project.getProtocolsDict()
for protId in protDic:
  protocol = project.getProtocol(protId)
  protLab = protocol.getObjLabel().lower()
  if 'consensus' in protLab:
    # Parse the results from the 100% consensus protocols
    if 'actives' in protLab:
      if 'n2' in protLab:
        pCons2Act = protocol
      else:
        pCons3Act = protocol
    elif 'decoys' in protLab:
      if 'n2' in protLab:
        pCons2Dec = protocol
      else:
        pCons3Dec = protocol

    elif '%' in protLab:
      # Parse filtered consensus results
      n, p = protLab.split()[-1], protLab.split('%')[0].split()[-1]
      consProtDic[f'{p}_{n}'] = parseConsensusSet(protocol)
      
      
activeDF = parseInputSets(pCons2Act, pCons3Act)
activeDF['Active'] = True
decoyDF = parseInputSets(pCons2Dec, pCons3Dec)
decoyDF['Active'] = False

allDf = pd.concat([activeDF, decoyDF], ignore_index=True)
for consKey in consProtDic:
  allDf[f'InConsensus_{consKey}'] = allDf['UniqueName'].apply(lambda x: isInConsensus(x, consProtDic[consKey]))


outFile = os.path.join(oriPath, f'{PROJECT_NAME}_VDSResults.csv')
print(f'Saving df in {outFile}')
allDf.to_csv(outFile)



