.. figure:: ../../../_static/images/logo.png
  :alt: pwchem logo

.. _scipion-chem_vds-index:

================================
Scipion-chem VDS Data
================================

This documentation contains all the data discussed in the Scipion-chem paper.

Workflows
###############################################################

The following sections contain further explanations about the workflows discussed in the VDS Scipion-chem publication.

- :ref:`docs-vds-4erf`: main VDS workflow discussed in "Virtual Drug Screening workflow" section for `4ERF <https://www.rcsb.org/structure/4ERF>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database 
- :ref:`docs-vds-fabp4`: bigger VDS workflow discussed in "Show case" section using `FABP4 <https://dude.docking.org/targets/fabp4>`_ dataset from `DUD-E <https://dude.docking.org/>`_ database.
- :ref:`docs-vds-1a28`: supplementary workflow example similar to 4ERF, with data from `1A28 <https://www.rcsb.org/structure/1A28>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database 

| 

In addition, the `GitHub repository <https://github.com/scipion-chem/docs/tree/main/docs/publications/scipion-chem_vds/workflows>`_ contains the actual workflows and data used necessary to run the Scipion workflow and links to the Scipion projects where the original results are stored.

A) **Import workflow**
~~~~~~~~~~~~~~~~~~~~~~~~~~
      The workflows are directly importable by Scipion, although, to make them functional, you will need to have all the used plugins installed.
      Because of storage limitations in this GitHub repo, these workflows are data empty, so the protocols are defined but 
      not run, and the results are yet missing. We provide this workflows in case you are interested in rerunning them, either 
      as they are or with any modification.
      To do so, you can import the workflow from a scipion3 project, using "Project -> Import workflow" and selecting the json file.
      
      .. figure:: ../../../../_static/images/publications/scipion-chem_vds/importWorkflow.png
         :alt: import workflow

      Once you have imported the workflow, remember to redirect the input protocols to the actual paths of the input files contained in this repository.
      For example, the pdb file imported in the "Import PDB" protocols or the sdf or mol2 files in the "Import Small Mols" protocols.

|

B) **Import project**
~~~~~~~~~~~~~~~~~~~~~~~~~~
      The corresponding workflows with the data discussed in the paper, full projects, can be found separatedly in our server:
      
      https://scipion.cnb.csic.es/downloads/scipion/data/tutorials/VirtualDrugScreening/projects/
      
      Scipion can directly recognize the structure of the downloaded folders (once unzipped), so you can directly import the project
      from the project manager window (the one to appear when using the command "scipion3") using the "Import project" button and
      selecting the project folder i.e: 1a28_workflow
      
      .. figure:: ../../../../_static/images/publications/scipion-chem_vds/importProject.png
         :alt: import project

      In this case, the project is self contained, so all the inputs are included and there is no need to change the paths for the input files.

|
|

Data analysis
###############################################################
The results of the "Show case" section for FABP4 workflow are subjected to further analysis outside Scipion in order to obtain the results commented in the pulication.
`Here <https://github.com/scipion-chem/docs/tree/main/docs/publications/scipion-chem_vds/workflows>`_, you can find the scripts python used to parse and analyze the results in the Scipion project. 

1) Data extraction
~~~~~~~~~~~~~~~~~~~~~

First, we extract the results from Scipion in a Pandas data frame object, which contains each of the docked poses as rows with information about its original molecule, whether it is an active or a decoy, the docking software that generated it and a column for each of the consensus docking protocols in the project determining if it is or not included in it.
The user must follow the convention names in the FABP4 workflow provided in order for it to work as expected.

Usage:

    scipion3 python extractData.py <projectName>

Output:
    The output generated is a csv file containing the data frame information


2) Data analysis
~~~~~~~~~~~~~~~~~~~~~

Separately, we code a jupyter notebook that is configured to open and analyze the results extracted in the previous section.
In there, the user can visualize several information extracted from the data frame and the figures in the paper are plotted.

Usage:
    conda activate scipion3 && jupyter notebook analyzeData.ipynb

|
|

Software availability
###############################################################

All the commented Scipion-chem plugins are built on the Scipion workflow engine, which can be found in
https://scipion.i2pc.es/ .

As stated in the paper, `Scipion-chem <https://github.com/scipion-chem>`_ integrates a set of bioinformatic tools and
software inside the platform.
Most of this tools are open, and no license is required for their use, so Scipion-chem installs it automatically,
taking care of properly referencing all the sources.

In the case of the few licensed software, the user must install
either the programs or the license by themselves and tell Scipion-chem where the software is installed. More detailed
guides on how to proceed with the installations can be found in the repositories of each of the plugins.

A complete list of these software, organized by the plugins they are installed on, is described below. The versions
refer to the moment this document is being written, but updates are constantly being made.

1) `Scipion-chem: <https://github.com/scipion-chem/scipion-chem>`_ as the core plugin, it installs a wide set of tools.

    - OpenBabel 2.2 (conda)
    - RDKit 2021.09.4 (conda)
    - MGLTools 1.5.7 (https://ccsb.scripps.edu)
    - Shape-it 2.0.0 (https://github.com/rdkit/shape-it.git)
    - JChemPaint 3.2.0 (https://sourceforge.net/projects/cdk/files/JChemPaint)
    - PyMol 2.5.5 (https://pymol.org/installers)
    - AliView 1.28 (https://ormbunkar.se/aliview)
    - VMD 1.9.3 (conda)
    - MDTraj 1.9.8 (conda)

2) `Scipion-chem-amber: <https://github.com/scipion-chem/scipion-chem-amber>`_

    - AmberTools 21 (conda)

3) `Scipion-chem-autodock: <https://github.com/scipion-chem/scipion-chem-autodock>`_

    - AutoDockSuite 4.2.6 (https://autodock.scripps.edu)
    - AutoDock-GPU (https://github.com/ccsb-scripps/AutoDock-GPU.git as in 2023/04/14)
    - Vina 1.2.3 (https://github.com/ccsb-scripps/AutoDock-Vina.git)
    - ADFRSuite 1.0 (https://ccsb.scripps.edu/adfr)
    - Meeko 0.3.3 (pip)

4) `Scipion-chem-blast: <https://github.com/scipion-chem/scipion-chem-blast>`_

    - BLAST+ 2.12.0 (https://ftp.ncbi.nlm.nih.gov/blast)

5)  `Scipion-chem-fpocket: <https://github.com/scipion-chem/scipion-chem-fpocket>`_

    - FPocket 3.0 (conda)

6) `Scipion-chem-gromacs: <https://github.com/scipion-chem/scipion-chem-gromacs>`_

    - Gromacs 2021.5 (https://ftp.gromacs.org/gromacs)

7) `Scipion-chem-lephar: <https://github.com/scipion-chem/scipion-chem-lephar>`_

    - LeDock - (http://www.lephar.com as in 2023/04/14)
    - LePro - (http://www.lephar.com as in 2023/04/14)

8) `Scipion-chem-modeller: <https://github.com/scipion-chem/scipion-chem-modeller>`_

    - Modeller 10.4 (conda) \*License Key needed

9) `Scipion-chem-p2rank: <https://github.com/scipion-chem/scipion-chem-p2rank>`_

    - P2Rank 2.3 (https://github.com/rdk/p2rank)

10) `Scipion-chem-rosetta: <https://github.com/scipion-chem/scipion-chem-rosetta>`_

    - Rosetta 3.12 (-) \*Need user installation

11) `Scipion-chem-schrodingerScipion: <https://github.com/scipion-chem/scipion-chem-schrodingerScipion>`_

    - Schrödinger Suite 2021-3 (-) \*Need user installation and key
