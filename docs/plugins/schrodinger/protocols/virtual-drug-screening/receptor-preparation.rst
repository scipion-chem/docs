:orphan: true

.. _schrodinger-Receptor_Preparation:

###############################################################
Schrödinger Receptor Preparation
###############################################################
This protocol prepares an ``AtomStruct`` object containing a protein file to make it ready for Schrodinger tools using the `Prepwizard <https://www.schrodinger.com/science-articles/protein-preparation-wizard>`_ Schrodinger utility.
The protocol contains 4 sections with different parameters that define the receptor preparation, including protonation, energy minimization, ionization and tautomerization. 

From Scipion-chem, we also provide the option of cleaning the structure from HETATM atoms and selecting specific chains from the input structure.

An additional option is included to manually perform this receptor preparation using prepwizard from Schrodinger's GUI.

|

.. image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_form1.png
   :alt: schrodinger form1

|

The result of this protocol is an ``AtomStruct`` object containing the resulting maestro file of the receptor, ready for other Schrodinger tools.

| 

.. |testCommand| replace:: schrodingerScipion.tests.main_wf.TestSchroProtPrep
.. include:: ../../../../templates/plugins/protocol-test.rst

| 
