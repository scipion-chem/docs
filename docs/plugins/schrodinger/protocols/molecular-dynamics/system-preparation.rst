:orphan: true

.. _schrodinger-System_Preparation:

###############################################################
Schrödinger System Preparation (Desmond)
###############################################################
This protocol prepares a Schrodinger MD system using `Desmond <https://www.schrodinger.com/products/desmond>`_ prior to its simulation from a AtomStruct or a SmallMolecule object.
We recommend you to input the protein or ligand structures from a previous Schrodinger protocol. If the structure comes from another plugin or a raw pdb, conversions will be attempted to adapt them to the Schrodinger format.

This protocol allows the user to create a solute boundary box, define the force field and finally specify the ions in the solute, which can be set to neutralize the charges, or manually add the desired number.

This protocol also includes the functionality for preparing complexes containing non-protein atoms, such as ligands, as Schrodinger takes care of the ligand parametrization itself.

|

|form6_1| |form6_2|

.. |form6_1| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_form6_1.png
   :alt: schrodinger form6_1
   :height: 490

.. |form6_2| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_form6_2.png
   :alt: schrodinger form6_2
   :height: 490

|

The result of this protocol is a ``SchrodingerSystem``, containing the Schrodinger structural files. 
The user can visualize the complex with Maestro using **Analyze Results**.

|

|out6_1| |out6_2|

.. |out6_1| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_out6_1.png
   :alt: schrodinger out6_1
   :height: 425

.. |out6_2| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_out6_2.png
   :alt: schrodinger out6_2
   :height: 425

| 

.. |testCommand| replace:: schrodingerScipion.tests.md_wf.TestDesmondSysPrep
.. include:: ../../../../templates/plugins/protocol-test.rst

| 
