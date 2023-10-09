.. _pwchem-import-database-ids:

###############################################################
Import database IDs
###############################################################
This protocol imports a set of database IDs from a file and stores them as a Scipion object. It save the ID and the
origin database name.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/database/import-database-ids/form.png
   :alt: Import database IDs form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfDatabaseIDs`` containing the databases that were defined in the input file.

.. |testCommand| replace:: pwchem.tests.tests_databases.TestImportDBIDs
.. include:: ../../../../templates/plugins/protocol-test.rst
