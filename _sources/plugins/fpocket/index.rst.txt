.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-fpocket

.. _docs-chem-fpocket:

.. figure:: ../../../_static/images/plugins/fpocket/logo.png
   :alt: fpocket logo

###############################################################
scipion-chem-fpocket
###############################################################
`FPocket <https://github.com/Discngine/fpocket>`_ is one of the most widely known programs for protein pocket detection.
In this plugin we include the main tool for pocket prediction, FPocket, together with the tool for predicting pockets
over a Molecular Dynamics simulation, MDPocket (in devel).

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

- :ref:`fpocket-pocket-prediction`: Predicts the pockets of an atomic structure based on its concavities (using alpha-speheres) and its electrostatics.
