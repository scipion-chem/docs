
.. _docs-chem-blast:


###############################################################
Importable workflows
###############################################################

This directory contain the workflows discussed in this section in json format. They are directly importable 
by Scipion, although, to make them functional, you will need to have all the used plugins installed.

**Import workflow**
      Because of storage limitations in this GitHub repo, these workflows are data empty, so the protocols are defined but 
      not run, and the results are yet missing. We provide this workflows in case you are interested in rerunning them, either 
      as they are or with any modification.
      To do so, you can import the workflow from a scipion3 project, using "Project -> Import workflow" and selecting the json file.
      
      .. figure:: ../../../../_static/images/publications/scipion-chem_vds/importWorkflow.png
         :alt: import workflow

Once you have imported the workflow, remember to redirect the input protocols to the actual paths of the input files contained in this repository.
For example, the pdb file imported in the "Import PDB" protocols or the sdf or mol2 files in the "Import Small Mols" protocols.

|

**Import project**
      The corresponding workflows with the data discussed in the paper, full projects, can be found separatedly in our server:
      
      https://scipion.cnb.csic.es/downloads/scipion/data/tutorials/VirtualDrugScreening/projects/
      
      Scipion can directly recognize the structure of the downloaded folders (once unzipped), so you can directly import the project
      from the project manager window (the one to appear when using the command "scipion3") using the "Import project" button and
      selecting the project folder i.e: 1a28_workflow
      
      .. figure:: ../../../../_static/images/publications/scipion-chem_vds/importProject.png
         :alt: import project
