.. _docs-import-set-of-sequences:

###############################################################
Import set of sequences
###############################################################
This protocol imports a set of sequences from one or several fasta files or from a database like `UniProt <https://www.uniprot.org/>`_ 
using a ``SetOfDatabaseIDs`` as input.

Input
----------------------------------------
All parameters include a help button that gives further information for each of them.

.. ../../../../../_static/images/pwchem/sequence/import-set-of-sequences/form_1.png
   :alt: Import SetOfSequences form 1
   :height: 400
   :align: center

.. image:: ../../../../../_static/images/pwchem/sequence/import-set-of-sequences/form_2.png
   :alt: Import SetOfSequences form 2
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfSequences`` with the specified sequences.

.. image:: ../../../../../_static/images/pwchem/sequence/import-set-of-sequences/output.png
   :alt: Import SetOfSequences output
   :align: center

|

Test
----------------------------------------
This protocol has an integrated test that can be run using the following command:

.. code-block::

   scipion3 tests pwchem.tests.tests_imports.TestImportSequences
