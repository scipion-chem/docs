.. _docs-import-database-ids:

###############################################################
Import database IDs
###############################################################
This protocol imports a set of database IDs from a file and stores them as a Scipion object. It save the ID and the
origin database name.

Input
----------------------------------------
All parameters include a help button that gives further information for each of them.

.. image:: ../../../../../_static/images/pwchem/database/import-database-ids/form.png
   :alt: Import database IDs form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfDatabaseIDs`` containing the databases that were defined in the input file.

Test
----------------------------------------
This protocol has an integrated test that can be run using the following command:

.. code-block::

   scipion3 tests pwchem.tests.tests_databases.TestImportDBIDs
