:orphan: true

.. _pwchem-consensus-structural-rois:

###############################################################
Consensus Structural ROIs
###############################################################
This protocol performs a consensus operation over several ``SetOfStructROIs``, studying which of them are shared among all
or a subset of the input sets. The protocol can be used for example to extract the most relevant and robust results
from different methods that predict protein pockets, or to extract which pockets predicted by a certain software overlap
with some interesting regions defined manually.

The protocol works by clustering the structural ROIs from the different inputs and filtering those that are not repeated
sufficiently among the inputs. For a pair of structural ROIs to be considered overlapping, they must share a certain
proportion of their involved residues.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/virtual-drug-screening/consensus-structural-rois/form.png
   :alt: Consensus Structural ROIs form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfStructROIs`` containing the consensus structural ROIs.

.. |testCommand| replace:: pwchem.tests.tests_structROIs.TestConsensusStructROIs
.. include:: ../../../../templates/plugins/protocol-test.rst