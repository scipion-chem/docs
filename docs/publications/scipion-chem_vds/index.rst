.. figure:: ../../../_static/images/logo.png
  :alt: pwchem logo

.. _scipion-chem_vds-index:

================================
Scipion-chem VDS Data
================================

This documentation contains all the data discussed in the Scipion-chem paper.

.. include:: workflows/index.rst

.. include:: data_analysis/index.rst

Software availability
###############################################################

All the commented Scipion-chem plugins are built on the Scipion workflow engine, which can be found in
https://scipion.i2pc.es/ .

As stated in the paper, `scipion-chem <https://github.com/scipion-chem>`_ integrates a set of bioinformatic tools and
software inside the platform.
Most of this tools are open, and no license is required for their use, so Scipion-chem installs it automatically,
taking care of properly referencing all the sources.

In the case of the few licensed software, the user must install
either the programs or the license by themselves and tell Scipion-chem where the software is installed. More detailed
guides on how to proceed with the installations can be found in the repositories of each of the plugins.

A complete list of these software, organized by the plugins they are installed on, is described below. The versions
refer to the moment this document is being written, but updates are constantly being made.

1) `scipion-chem: <https://github.com/scipion-chem/scipion-chem>`_ as the core plugin, it installs a wide set of tools.

    - OpenBabel 2.2 (conda)
    - RDKit 2021.09.4 (conda)
    - MGLTools 1.5.7 (https://ccsb.scripps.edu)
    - Shape-it 2.0.0 (https://github.com/rdkit/shape-it.git)
    - JChemPaint 3.2.0 (https://sourceforge.net/projects/cdk/files/JChemPaint)
    - PyMol 2.5.5 (https://pymol.org/installers)
    - AliView 1.28 (https://ormbunkar.se/aliview)
    - VMD 1.9.3 (conda)
    - MDTraj 1.9.8 (conda)

2) `scipion-chem-amber: <https://github.com/scipion-chem/scipion-chem-amber>`_

    - AmberTools 21 (conda)

3) `scipion-chem-autodock: <https://github.com/scipion-chem/scipion-chem-autodock>`_

    - AutoDockSuite 4.2.6 (https://autodock.scripps.edu)
    - AutoDock-GPU (https://github.com/ccsb-scripps/AutoDock-GPU.git as in 2023/04/14)
    - Vina 1.2.3 (https://github.com/ccsb-scripps/AutoDock-Vina.git)
    - ADFRSuite 1.0 (https://ccsb.scripps.edu/adfr)
    - Meeko 0.3.3 (pip)

4) `scipion-chem-blast: <https://github.com/scipion-chem/scipion-chem-blast>`_

    - BLAST+ 2.12.0 (https://ftp.ncbi.nlm.nih.gov/blast)

5)  `scipion-chem-fpocket: <https://github.com/scipion-chem/scipion-chem-fpocket>`_

    - FPocket 3.0 (conda)

6) `scipion-chem-gromacs: <https://github.com/scipion-chem/scipion-chem-gromacs>`_

    - Gromacs 2021.5 (https://ftp.gromacs.org/gromacs)

7) `scipion-chem-lephar: <https://github.com/scipion-chem/scipion-chem-lephar>`_

    - LeDock - (http://www.lephar.com as in 2023/04/14)
    - LePro - (http://www.lephar.com as in 2023/04/14)

8) `scipion-chemmodeller: <https://github.com/scipion-chem/scipion-chem-modeller>`_

    - Modeller 10.4 (conda) \*License Key needed

9) `scipion-chemp2rank: <https://github.com/scipion-chem/scipion-chem-p2rank>`_

    - P2Rank 2.3 (https://github.com/rdk/p2rank)

10) `scipion-chemrosetta: <https://github.com/scipion-chem/scipion-chem-rosetta>`_

    - Rosetta 3.12 (-) \*Need user installation

11) `scipion-chemschrodingerScipion: <https://github.com/scipion-chem/scipion-chem-schrodingerScipion>`_

    - Schrödinger Suite 2021-3 (-) \*Need user installation and key
