:orphan: true

.. _schrodinger-ligand-preparation:

###############################################################
Schrödinger Ligand Preparation
###############################################################
This protocol prepares a ``SetOfSmallMolecules`` to make it ready for Schrodinger tools using the `Ligprep <https://www.schrodinger.com/products/ligprep>`_ Schrodinger program.
It includes different options for ionization, building conformers and energy optimization. 

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/schrodinger/virtual-drug-screening/ligand-preparation/form.png
   :alt: Schrödinger Ligand Preparation form
   :height: 400
   :align: center

|

The result of this protocol is another ``SetOfSmallMolecules`` object this time containing the maestro files ready for other Schrodinger tools.

.. |testCommand| replace:: schrodingerScipion.tests.main_wf.TestSchroLigPrep
.. include:: ../../../../templates/plugins/protocol-test.rst
