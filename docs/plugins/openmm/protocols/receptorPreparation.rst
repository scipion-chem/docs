:orphan: true

.. _openmm-Receptor_Preparation:

###############################################################
OpenMM receptor preparation
###############################################################
================================
This protocol uses PDBFixer to correct most of the common errors encountered in PDB files and prepares it to be used by OpenMM and other programs.

|

.. image:: ../../../../_static/images/plugins/gromacs/gromacs_form1.png
   :alt: gromacs form1

|

The result of this protocol is a ``AtomStruct``, containing the fixed PDB structure, that can be visualized using **Analyze Results**.

|

.. |testCommand| replace:: gromacs.tests.tests.TestGromacsPrepareSystem
.. include:: ../../../../templates/plugins/protocol-test.rst

| 
