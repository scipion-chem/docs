.. _pwchem-pairwise-alignment:

###############################################################
Pairwise Alignment
###############################################################
This protocol performs a pairwise alignment using clustal omega over two input sequences.
These sequences can be input either from a ``Sequence`` or an ``AtomStruct`` object, in the later,
the chain must also be specified.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/pairwise-alignment/form.png
   :alt: Pairwise Alignment form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequences`` with the two input sequences aligned.

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/pairwise-alignment/output.png
   :alt: Pairwise Alignment output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_sequences.TestPairwiseAlign
.. include:: ../../../../templates/plugins/protocol-test.rst
