:orphan: true

.. _openmm-Receptor_Preparation:

###############################################################
OpenMM Receptor Preparation
###############################################################
This protocol uses PDBFixer to correct most of the common errors encountered in PDB files and prepares it to be used by OpenMM and other programs.

|

.. image:: ../../../../_static/images/plugins/openmm/openmm_form1.png
   :alt: openmm form1

|

The result of this protocol is a ``AtomStruct``, containing the fixed PDB structure, that can be visualized using **Analyze Results**.

|

.. image:: ../../../../_static/images/plugins/openmm/openmm_out1.png
   :alt: openmm out1

|

.. |testCommand| replace:: openmm.tests.test_openmm.TestOpenMMPrepareReceptor
.. include:: ../../../templates/plugins/protocol-test.rst

| 
