:orphan: true

.. _scipion-chem_vds-data_analysis:

Data Analysis
###############################################################
The results of the "Show case" section for FABP4 workflow are subjected to further analysis outside Scipion in order to obtain the results commented in the publication.
`Here <https://github.com/scipion-chem/docs/tree/main/docs/publications/scipion-chem_vds/workflows>`_, you can find the Python scripts used to parse and analyze the results in the Scipion project.

This folder section contains the Python scripts used to analyze the results of the VDS workflow described in section "Show case", regarding the FABP4 dataset.

1) Data extraction
~~~~~~~~~~~~~~~~~~~~~
First, we extract the results from Scipion in a Pandas DataFrame object, which contains each of the docked poses as rows with information about its original molecule, whether it is an active or a decoy, the docking software that generated it and a column for each of the consensus docking protocols in the project determining if it is or not included in it.
The user must follow the convention names in the FABP4 workflow provided in order for it to work as expected.

Usage:

.. parsed-literal::

    scipion3 python extractData.py <projectName>

Output:
    The output generated is a CSV file containing the DataFrame information.

2) Analysis
~~~~~~~~~~~~~~~~~~~~~
Separately, we code a Jupyter notebook that is configured to open and analyze the results extracted in the previous section.
In there, the user can visualize several pieces of information extracted from the DataFrame, and the figures in the paper are plotted.

Usage:

.. parsed-literal::

    conda activate scipion3 && jupyter notebook analyzeData.ipynb
