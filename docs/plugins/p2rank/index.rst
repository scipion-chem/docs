.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-p2rank

.. _docs-chem-p2rank:

.. figure:: ../../../_static/images/plugins/p2rank/logo.png
   :alt: p2rank logo

###############################################################
scipion-chem-p2rank
###############################################################
`P2Rank <https://github.com/rdk/p2rank>`_ is one of the most widely known programs for protein pocket detection based
on machine learning. In this plugin we include the main tool for pocket prediction, P2Rank.

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

==========================================
Protocols
==========================================

- :ref:`p2rank-prediction`: Predicts the pockets of an atomic structure based on a machine learning model over the protein surface.
