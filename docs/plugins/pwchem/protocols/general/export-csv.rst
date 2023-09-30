.. _docs-export-csv:

###############################################################
Export CSV
###############################################################
This protocol allows the user to export the SQLite table of a set as a CSV file, containing the values of each attribute
for each column and each item in a row. This protocol might be useful for further exploring the attributes of a Set.

Input
----------------------------------------
All parameters include a help button that gives further information for each of them.

.. image:: ../../../../../_static/images/pwchem/general/export-csv/form.png
   :alt: Export CSV form
   :height: 400
   :align: center

|

The result of this protocol is a ``CSV`` file in the protocol folder. It has no Scipion output object.

.. image:: ../../../../../_static/images/pwchem/general/export-csv/output.png
   :alt: Export CSV output
   :align: center

|

Test
----------------------------------------
This protocol has an integrated test that can be run using the following command:

.. code-block::

   scipion3 tests pwchem.tests.tests_general.TestExportcsv
