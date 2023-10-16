
.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-openmm
   
.. _docs-chem-gromacs:

.. figure:: ../../../../_static/images/plugins/openmm/openmm_logo.png
   :alt: openmm logo

###############################################################
scipion-chem-openmm
###############################################################
`OpenMM <https://openmm.org/>`_ is a high-performance toolkit for molecular simulation. 

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

- :ref:`openmm-Receptor_Preparation`: prepares a protein ``AtomStruct`` object using PDBFixer to prepare it for posterior analysis.
This Plugin is currently under development and more protocols will be available soon.