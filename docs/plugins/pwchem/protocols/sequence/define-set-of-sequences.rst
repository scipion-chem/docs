.. _docs-define-set-of-sequences:

###############################################################
Define set of sequences
###############################################################
This protocol allows the user to manually build a set of small molecules from individual elements, which can be either
``Sequence``, ``AtomStruct`` objects or even PDB codes. In the case of structures and PDB, the chain must be specified. Also,
the user can always select just a segment of the total sequence to be added.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/pwchem/sequence/define-set-of-sequences/form.png
   :alt: Define set of sequences form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequences`` with each of the defined sequences in the input.

.. |testCommand| replace:: pwchem.tests.tests_sequences.TestDefineSetSequences
.. include:: ../../../../templates/plugins/protocol-test.rst
