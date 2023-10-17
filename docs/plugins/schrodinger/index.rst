.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-schrodinger

.. _docs-chem-schrodinger:

.. figure:: ../../../_static/images/plugins/schrodinger/schrodinger_logo.png
   :alt: schrodinger logo

###############################################################
scipion-chem-schrodinger
###############################################################
`Schrodinger <https://www.schrodinger.com/>`_ is a platform that platform leverages a deep understanding of physics,
chemistry, and predictive modeling to accelerate innovation. It contains numerous tools for molecular modelling,
including drug discovery and molecular dynamics.

|

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

Notice that Schrodinger is a license software, so from Scipion-chem we only provide tools for using their programs, but we do not provide the software itself, which must be separately installed by the user.

==========================================
Protocols
==========================================

A) Virtual Drug Screening
~~~~~~~~~~~~~~~~~~~~~~~~~~~
It includes several tools from Schrodinger for Virtual Drug Screening. 
The user will be able to prepare both the target and the ligands, predict or define the binding sites and perform a docking analysis.

- :ref:`schrodinger-Receptor_Preparation`: prepares an ``AtomStruct`` object containing a protein file to make it ready for Schrodinger tools using the `Prepwizard <https://www.schrodinger.com/science-articles/protein-preparation-wizard>`_ Schrodinger utility.
- :ref:`schrodinger-Ligand_Preparation`: prepares a ``SetOfSmallMolecules`` to make it ready for Schrodinger tools using the `Ligprep <https://www.schrodinger.com/products/ligprep>`_ Schrodinger program.
- :ref:`schrodinger-Binding_Site_Prediction`: predicts the most promising binding sites on the structure using `SiteMap <https://www.schrodinger.com/products/sitemap>`_ .
- :ref:`schrodinger-Grid_Preparation`: generates the grids used by the docking Schrodinger program: `Glide <https://www.schrodinger.com/products/glide>`_. 
- :ref:`schrodinger-Glide_Docking`: uses `Glide <https://www.schrodinger.com/products/glide>`_ for docking a set of ligands to a receptor.

| 

B) Molecular Dynamics
~~~~~~~~~~~~~~~~~~~~~~~~~~~
It includes protocols able to handle Molecular Dynamics simulations in Schrodinger. 
The following protocols allow the user to prepare, run and analyze these simulations.

- :ref:`schrodinger-System_Preparation`: prepares a Schrodinger MD system using `Desmond <https://www.schrodinger.com/products/desmond>`_ prior to its simulation from a AtomStruct or a SmallMolecule object.
- :ref:`schrodinger-Desmond_MD_Simulation`: takes the prepared Schrodinger system and uses `Desmond <https://www.schrodinger.com/products/desmond>`_ to run a defined simulation. 

| 

C) Utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~
It includes other util protocols that can be used in any of the previous fields.

- :ref:`schrodinger-Format_Conversion`: uses Schrodinger scripts to convert an ``AtomStruct`` or a ``SetOfSmallMolecules`` to the desired format.
- :ref:`schrodinger-Fix_Structure`: allows the user to use `Prime <https://www.schrodinger.com/products/prime>`_ for fixing an atomic structure. 
- :ref:`schrodinger-Split_Structure`: allows the user to use the *split_structure.py* script from Schrodinger mmShare. 
