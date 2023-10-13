.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-blast

.. _docs-chem-blast:

.. figure:: ../../../_static/images/plugins/blast/blast_logo.png
   :alt: blast logo

###############################################################
scipion-chem-blast
###############################################################
`BLAST <https://blast.ncbi.nlm.nih.gov/Blast.cgi>`_ is the well known program for finding regions of similarity between
biological sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the
statistical significance. In this plugin we incorporate functionalities both for local and web-server BLAST.


==========================================
Installation
==========================================
A) Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order to use this plugin, you need to install first :ref:`pwchem-index`.


B) Installation steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. include:: ../../templates/plugins/installation/installation-steps.rst
.. include:: ../../templates/plugins/installation/only-devel.rst

|


==========================================
Protocols
==========================================

- :ref:`blast-NCBI_download`: Predicts the pockets of an atomic structure based on its concavities (using alpha-speheres) and its electrostatics.
- :ref:`blast-create_database`: Predicts the pockets of an atomic structure based on its concavities (using alpha-speheres) and its electrostatics.
- :ref:`blast-blast_search`: Predicts the pockets of an atomic structure based on its concavities (using alpha-speheres) and its electrostatics.

