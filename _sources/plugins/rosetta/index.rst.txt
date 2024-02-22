.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-rosetta

.. _docs-chem-rosetta:

.. figure:: ../../../_static/images/plugins/rosetta/logo.png
   :alt: rosetta logo

###############################################################
scipion-chem-rosetta
###############################################################
`Rosetta <https://www.rosettacommons.org/software/>`_ includes algorithms for computational modeling and analysis of
protein structures. It has enabled notable scientific advances in computational biology, including de novo protein
design, enzyme design, ligand docking, and structure prediction of biological macromolecules and macromolecular
complexes.

From Scipion-chem, we have mainly integrated protocols for the preparation of the protein receptors and the docking
process, using `DARC <https://pubmed.ncbi.nlm.nih.gov/26181386/>`_.

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

- :ref:`rosetta-receptor-preparation`: Prepares an ``AtomStruct`` object containing a protein file for docking.
- :ref:`rosetta-DARC-docking`: Follows the `DARC <https://pubmed.ncbi.nlm.nih.gov/26181386/>`_ docking procedure.
- :ref:`rosetta-electronic-map-modelling`: Generates a set of possible atomic structures which fit an electronic density map. The protocol has been integrated as the first step for a `global and local Cryo-EM map quality assessment <https://www.sciencedirect.com/science/article/pii/S0969212618303642?via%3Dihub>`_.
