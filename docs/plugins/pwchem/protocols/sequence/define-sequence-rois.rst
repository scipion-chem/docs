:orphan: true

.. _pwchem-define-sequence-rois:

###############################################################
Define Sequence ROIs
###############################################################
This protocol defines a ``SetOfSequenceROIs`` from a ``Sequence`` or ``SequenceVariants`` object. The user can define a list of
Regions Of Interest from sequence segments, variants or mutations in the input.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/define-sequence-rois/form.png
   :alt: Import set of sequences form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequenceROIs`` with the ROIs defined in the input.

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/define-sequence-rois/output.png
   :alt: Import set of sequences output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_sequences.TestDefineSequenceROIs
.. include:: ../../../../templates/plugins/protocol-test.rst
