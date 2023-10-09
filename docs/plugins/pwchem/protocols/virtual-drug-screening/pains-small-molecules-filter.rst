:orphan: true
.. _pwchem-pains-small-molecules-filter:

###############################################################
PAINS Small Molecules filter
###############################################################
This protocol uses `RDKit <https://github.com/rdkit/rdkit>`_ to filter a ``SetOfSmallMolecules`` by applying the 
`PAINS (Pan-assay interference compounds) filter <https://en.wikipedia.org/wiki/Pan-assay_interference_compounds>`_ to each of the small molecules stored.
The user can choose whether to use RDKit default PAINS substructures or to provide a custom PAINS file where each line
must contain a first column with a SMARTS string and a second column with a short description.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/pains-small-molecules-filter/form.png
   :alt: PAINS Small Molecules filter form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSmallMolecules`` containing only those small molecules that pass the filter.

.. |testCommand| replace:: pwchem.tests.tests_ligand_filtering.TestPAINSFiltering
.. include:: ../../../../templates/plugins/protocol-test.rst