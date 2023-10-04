.. _docs-fingerprint-small-molecules-filter:

###############################################################
FingerPrint Small Molecules filter
###############################################################
This protocol uses `RDKit <https://github.com/rdkit/rdkit>`_ to filter a ``SetOfSmallMolecules`` 
by applying fingerprint filters to each of the small molecules stored. 
The user can choose whether to use `Morgan or MACCS fingerprints <https://www.rdkit.org/UGM/2012/Landrum_RDKit_UGM.Fingerprints.Final.pptx.pdf>`_ 
and whether to use `Tanimoto <https://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_similarity_and_distance>`_ or 
`Dice <https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient>`_ similarity coefficients.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/fingerprint-small-molecules-filter/form.png
   :alt: FingerPrint Small Molecules filter form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSmallMolecules`` containing only those small molecules that pass the filter.

.. |testCommand| replace:: pwchem.tests.tests_ligand_filtering.TestFingerprintFiltering
.. include:: ../../../../templates/plugins/protocol-test.rst