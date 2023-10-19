Workflows
###############################################################

The following sections contain further explanations about the workflows discussed in the VDS Scipion-chem publication.

- :ref:`docs-vds-4erf`: main VDS workflow discussed in "Virtual Drug Screening workflow" section for `4ERF <https://www.rcsb.org/structure/4ERF>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database.
- :ref:`docs-vds-fabp4`: bigger VDS workflow discussed in "Show case" section using `FABP4 <https://dude.docking.org/targets/fabp4>`_ dataset from `DUD-E <https://dude.docking.org/>`_ database.
- :ref:`docs-vds-1a28`: supplementary workflow example similar to 4ERF, with data from `1A28 <https://www.rcsb.org/structure/1A28>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database.

The following workflows are available to download:

.. warning::
   Table of downloadable files is WIP, will be ready in a few days

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :align: center

   * - Dataset
     - Workflow
     - Input files
   * - 4erf
     - `4erf.json <../../../../_static/datasets/scipion-chem_vds/workflows/4erf/4erf.json>`_
     - `4erf.zip <../../../../_static/datasets/scipion-chem_vds/workflows/4erf/4erf.zip>`_
   * - fabp4
     - `fabp4.json <../../../../_static/datasets/scipion-chem_vds/workflows/fabp4/fabp4.json>`_
     - `fabp4.zip <../../../../_static/datasets/scipion-chem_vds/workflows/fabp4/fabp4.zip>`_
   * - 1a28
     - `1a28.json <../../../../_static/datasets/scipion-chem_vds/workflows/1a28/1a28.json>`_
     - `1a28.zip <../../../../_static/datasets/scipion-chem_vds/workflows/1a28/1a28.zip>`_

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :align: center

   * - Dataset
     - Workflow
     - Input files
   * - 4erf
     - :download:`4erf.json </_static/datasets/scipion-chem_vds/workflows/4erf/4erf.json>`
     - `4erf.zip <../../../../_static/datasets/scipion-chem_vds/workflows/4erf/4erf.zip>`_
   * - fabp4
     - `fabp4.json <../../../../_static/datasets/scipion-chem_vds/workflows/fabp4/fabp4.json>`_
     - `fabp4.zip <../../../../_static/datasets/scipion-chem_vds/workflows/fabp4/fabp4.zip>`_
   * - 1a28
     - `1a28.json <../../../../_static/datasets/scipion-chem_vds/workflows/1a28/1a28.json>`_
     - `1a28.zip <../../../../_static/datasets/scipion-chem_vds/workflows/1a28/1a28.zip>`_

A) **Import workflow**
~~~~~~~~~~~~~~~~~~~~~~~~~~
      The workflows are directly importable by Scipion, although, to make them functional, you will need to have all the used plugins installed.
      Because of storage limitations in this GitHub repo, these workflows are data empty, so the protocols are defined but 
      not run, and the results are yet missing. We provide this workflows in case you are interested in rerunning them, either 
      as they are or with any modification.
      To do so, you can import the workflow from a scipion3 project, using "Project -> Import workflow" and selecting the json file.
      
      .. figure:: ../../../_static/images/publications/scipion-chem_vds/importWorkflow.png
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
      
      .. figure:: ../../../_static/images/publications/scipion-chem_vds/importProject.png
         :alt: import project

      In this case, the project is self contained, so all the inputs are included and there is no need to change the paths for the input files.
