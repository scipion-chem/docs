:orphan: true
.. _pwchem-operate-sequence-rois:

###############################################################
Operate Sequence ROIs
###############################################################
This protocol allows the user to operate sets of sequence ROIs, similarly to the operate sets. In this protocol however,
the overlap of the ROIs is the attribute taken into account for the set operations.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/operate-sequence-rois/form.png
   :alt: Operate Sequence ROIs form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequenceROIs`` with the operated regions.

.. |testCommand| replace:: pwchem.tests.tests_sequences.TestOperateSeqROIs
.. include:: ../../../../templates/plugins/protocol-test.rst
