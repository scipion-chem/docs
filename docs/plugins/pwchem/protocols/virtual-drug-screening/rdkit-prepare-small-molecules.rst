.. _docs-rdkit-prepare-small-molecules:

###############################################################
RDKit Prepare Small Molecules
###############################################################
This protocol prepares a ``SetOfSmallMolecules`` using `RDKit <https://github.com/rdkit/rdkit>`_. 
The user can choose several methods for the charge assignment and conformer generation.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/rdkit-prepare-small-molecules/form.png
   :alt: RDKit Prepare Small Molecules form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSmallMolecules`` prepared by RDKit. 
If the option for generating conformers was chosen, different conformations for each input molecule will be accessible.

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/rdkit-prepare-small-molecules/output.png
   :alt: RDKit Prepare Small Molecules output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_preparations.TestRDKitLigandPreparation
.. include:: ../../../../templates/plugins/protocol-test.rst