:orphan: true

.. _pwchem-adme-small-molecules-filter:

###############################################################
ADME Small Molecules filter
###############################################################
This protocol uses `RDKit <https://github.com/rdkit/rdkit>`_ to filter a ``SetOfSmallMolecules`` by applying the ADME (Absortion, Distribution,
Metabolism, Excretion) filter to each of the small molecules stored. The user can choose whether to use the 
`Lipinski's rule of five <https://en.wikipedia.org/wiki/Lipinski%27s_rule_of_five>`_ or the 
`Rule of three <https://en.wikipedia.org/wiki/Lipinski%27s_rule_of_five#:~:text=A%20rule%20of%20three%20compliant,than%203%20hydrogen%20bond%20donors>`_.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/adme-small-molecules-filter/form.png
   :alt: ADME Small Molecules filter form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSmallMolecules`` containing only those small molecules that pass the filter.

.. |testCommand| replace:: pwchem.tests.tests_ligand_filtering.TestADMEFiltering
.. include:: ../../../../templates/plugins/protocol-test.rst