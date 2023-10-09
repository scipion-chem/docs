:orphan: true
.. _pwchem-openbabel-prepare-small-molecules:

###############################################################
OpenBabel Prepare Small Molecules
###############################################################
This protocol prepares a ``SetOfSmallMolecules`` using `OpenBabel <https://github.com/openbabel/openbabel>`_. 
The user can choose several methods for the charge assignment and conformer generation.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/openbabel-prepare-small-molecules/form.png
   :alt: OpenBabel Prepare Small Molecules form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSmallMolecules`` prepared by OpenBabel. 
If the option for generating conformers was chosen, different conformations for each input molecule will be accessible.

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/openbabel-prepare-small-molecules/output.png
   :alt: OpenBabel Prepare Small Molecules output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_preparations.TestOBLigandPreparation
.. include:: ../../../../templates/plugins/protocol-test.rst