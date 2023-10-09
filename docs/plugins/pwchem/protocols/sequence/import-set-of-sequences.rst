.. _pwchem-import-set-of-sequences:

###############################################################
Import set of sequences
###############################################################
This protocol imports a set of sequences from one or several fasta files or from a database like `UniProt <https://www.uniprot.org/>`_ 
using a ``SetOfDatabaseIDs`` as input.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/import-set-of-sequences/form_1.png
   :alt: Import set of sequences form 1
   :height: 400
   :align: center

|

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/import-set-of-sequences/form_2.png
   :alt: Import SetOfSequences form 2
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequences`` with the specified sequences.

.. image:: ../../../../../_static/images/plugins/pwchem/sequence/import-set-of-sequences/output.png
   :alt: Import SetOfSequences output
   :align: center

|

.. |testCommand| replace:: pwchem.tests.tests_imports.TestImportSequences
.. include:: ../../../../templates/plugins/protocol-test.rst
