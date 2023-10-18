:orphan: true

.. _openmm-receptor-preparation:

###############################################################
Receptor Preparation
###############################################################
This protocol uses PDBFixer to correct most of the common errors encountered in PDB files and prepares it to be used by OpenMM and other programs.

Input
----------------------------------------
.. include:: ../../../templates/plugins/input-help.rst

.. image:: ../../../../_static/images/plugins/openmm/receptor-preparation/form.png
   :alt: Receptor Preparation form
   :height: 400
   :align: center

|

The result of this protocol is a ``AtomStruct``, containing the fixed PDB structure, that can be visualized using **Analyze Results**.

.. image:: ../../../../_static/images/plugins/openmm/receptor-preparation/output.png
   :alt: Receptor Preparation output
   :height: 400
   :align: center

|

.. |testCommand| replace:: openmm.tests.test_openmm.TestOpenMMPrepareReceptor
.. include:: ../../../templates/plugins/protocol-test.rst
