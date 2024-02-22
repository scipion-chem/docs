.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-amber

.. _docs-chem-amber:

.. figure:: ../../../_static/images/plugins/amber/logo.png
   :alt: amber logo

###############################################################
scipion-chem-amber
###############################################################
`AMBER <https://ambermd.org/>`_ is a suite of biomolecular simulation programs.
Amber is distributed in two parts: AmberTools23 (which is free) and Amber22 (which requires a license).

.. warning::
   This plugin is currently under first-stage development, so you may encounter errors or some options may not be available. 
   Sorry for the inconvenience.

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

- :ref:`amber-ligand-parametrization`: Parametrizes and prepares a ligand to be used in Amber simulations using pdb4amber and Antechamber. 
- :ref:`amber-system-preparation`: Prepares a system for Amber MD simulation, cleaning the input PDB for further analysis and generating topology and coordinate files necessary.
- :ref:`amber-md-simulation`: Defines and executes a Amber MD simulation. 
