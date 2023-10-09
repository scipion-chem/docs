:orphan: true
.. _pwchem-uniprot-crossref:

###############################################################
UniProt CrossRef
###############################################################
This protocol searches in the `UniProt <https://www.uniprot.org/>`_ cross reference database for related entries of a set of UniProt IDs for
specified databases. The user can choose whether to store the cross reference as a secondary or the main ID and
whether to store also additional properties stored in those IDs.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/database/uniprot-crossref/form.png
   :alt: UniProt CrossRef form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfDatabaseIDs`` containing the information of the cross references. This can also
be checked in a summary file.

.. |testCommand| replace:: pwchem.tests.tests_databases.TestUniProtCrossRef
.. include:: ../../../../templates/plugins/protocol-test.rst
