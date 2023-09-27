
.. _docs-chem-blast:

.. figure:: ../../_static/images/blast/blast_logo.png
   :alt: blast logo

###############################################################
scipion-chem-blast
###############################################################
In order to use this plugin, you need to install first Scipion-chem.
`Scipion-chem <https://github.com/scipion-chem/docs>`_
is the core for the rest of scipion-chem-\* plugins. To do so, you can check the instructions in the
`Scipion-chem README <https://github.com/scipion-chem/scipion-chem/blob/master/README.rst>`_.

Similarly, you can find the installation instructions of this plugin in
`Scipion-chem-blast README <https://github.com/scipion-chem/scipion-chem-blast/blob/master/README.rst>`_

|

Scipion-chem-blast overview
******************************************
`BLAST <https://blast.ncbi.nlm.nih.gov/Blast.cgi>`_ is the well known program for finding regions of similarity between
biological sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the
statistical significance. In this plugin we incorporate functionalities both for local and web-server BLAST.

Scipion-chem-blast protocols
******************************************

**NCBI download**
================================
This protocol access the NCBI API using the `Entrez module <https://biopython.org/docs/1.75/api/Bio.Entrez.html>`_
of the Biopython package. The protocol is prepared to fetch protein or nucleotide sequences from the NCBI databases and
small molecules from PubChem.

The user can perform a search using NCBI IDs, where the specific objects they refer will be directly fetched; or
a broader search using keywords which will return a set of objects which are returned by the esearch functionality.
The user must be aware of this functionality, since the outputs might not be those expected.

All parameters include a help button that gives further information for each of them.

|

.. figure:: ../../_static/images/blast/blast_form1.png
   :alt: blast form1

|

The result of this protocol is either a SetOfSequences (for protein or nucletides sequences) or a SetOfSmallMolecules
for PubChem downloads.

A test for this protocol can be run using::
    scipion3 tests blast.tests.test_blast.TestNCBIDownload

|

**Create local database**
================================
This protocol creates a local database in BLAST format and stores it in the plugin folder. The user can create
databases either from a SetOfSequences or from default databases in BLAST. The user must be aware of this last option,
since most of the BLAST databases are quite big and downloading them will expend high amounts of time and storage.

|

This protocol does not output any object, but it saves the database in the plugin folder.

A test for this protocol can be run using::
    scipion3 tests blast.tests.test_blast.TestDatabaseBLAST

|

.. figure:: ../../_static/images/blast/blast_form2.png
   :alt: blast form2

|

**BLAST search**
================================
This protocol performs a BLAST search over a database, which can be local or a web-server BLAST database.
The input of the protocol is a sequence, which can be from a protein or nucleotide, and the user will be able to define
the type of search (blastp, blastn, blastx, ...).

In the second parameters tab, different parameters for the search can be tuned. If you are
not sure of which parameters to use, click on the wizard and the default parameters for the search type will be set.

|

.. figure:: ../../_static/images/blast/blast_form3.png
   :alt: blast form3

|

The result of this protocol is a SetOfSequences containing the BLAST hits. The analyze results button will open these
sequences in AliViewer.

A test for this protocol can be run using::
    scipion3 tests blast.tests.test_blast.TestBLAST

|

Get in contact
******************************************

From the Scipion team we would be happy to hear your doubts and suggestions, do not hesitate to contact us at any
time. To do so, you can either open an issue in the Github repository related to your question or
contact us by mail.

If the question is related to the Scipion framework, try the `contact us <https://scipion.i2pc.es/contact>`_ page.
If it is related to some Scipion-chem plugin or functionality, you can send a mail to
the developer at ddelhoyo@cnb.csic.es


