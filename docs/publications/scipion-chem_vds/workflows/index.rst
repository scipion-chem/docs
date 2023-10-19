Workflows
###############################################################

The following sections contain further explanations about the workflows discussed in the VDS Scipion-chem publication.

- :ref:`docs-vds-4erf`: main VDS workflow discussed in "Virtual Drug Screening workflow" section for `4ERF <https://www.rcsb.org/structure/4ERF>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database.
- :ref:`docs-vds-fabp4`: bigger VDS workflow discussed in "Show case" section using `FABP4 <https://dude.docking.org/targets/fabp4>`_ dataset from `DUD-E <https://dude.docking.org/>`_ database.
- :ref:`docs-vds-1a28`: supplementary workflow example similar to 4ERF, with data from `1A28 <https://www.rcsb.org/structure/1A28>`_ PDB structure, using `D-COID <https://data.mendeley.com/datasets/8czn4rxz68/1>`_ database.

The following workflows are available to download:

.. list-table::
   :widths: 50 50
   :header-rows: 1
   :align: center

   * - Dataset
     - Download Links
   * - 1a28
     - `Workflow </_static/datasets/scipion-chem_vds/workflows/1a28/workflow.json>`_ | `Inputs <path/to/your/data1>`_
   * - 4erf
     - `Workflow <path/to/your/workflow2>`_ | `Inputs <path/to/your/data2>`_
   * - fabp4
     - `Workflow <path/to/your/workflow3>`_ | `Inputs <path/to/your/data3>`_
   * - inha
     - `Workflow <path/to/your/workflow3>`_ | `Inputs <path/to/your/data3>`_

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
