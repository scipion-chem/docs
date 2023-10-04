.. _docs-generate-variant-sequences:

###############################################################
Generate variant sequences
###############################################################
This protocol generates a set of sequences from a list of specified variants from a ``SequenceVariants`` object.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/generate-variant-sequences/form.png
   :alt: Generate variant sequences form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequences`` which contains all the defined variants or single mutations from the input.

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/generate-variant-sequences/output.png
   :alt: Generate variant sequences output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_sequences.TestGenerateSequences
.. include:: ../../../../templates/plugins/protocol-test.rst
