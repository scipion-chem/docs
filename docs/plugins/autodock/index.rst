.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-autodock

.. figure:: ../../../_static/images/plugins/autodock/logo.png
   :alt: autodock logo

.. _autodock-index:

###############################################################
scipion-chem-autodock
###############################################################
`AutoDock <https://autodocksuite.scripps.edu/adt/>`_ is a suite of automated docking tools. It is designed to predict how 
small molecules, such as substrates or drug candidates, bind to a receptor of known 3D structure. Over the years, it has
been modified and improved to add new functionalities, and multiple engines have been developed.

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

C) Packages & enviroments
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. include:: ../../templates/plugins/installation/packages-header.rst

**TODO: COMPLETE THIS PART**

.. include:: ../../templates/plugins/installation/packages-footer.rst

==========================================
Protocols
==========================================
A) Receptor preparation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-receptor-preparation`: prepares an ``AtomStruct`` object containing a protein file to make it ready for `AutoDock tools <https://autodocksuite.scripps.edu/adt/>`_, such as docking with AutoDock or Vina.

B) Ligand preparation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-ligand-preparation`: uses the script *prepare_ligand4.py* in the utilities of AutoDock Tools to prepare a ``SetOfSmallMolecules``.
- :ref:`autodock-ligand-preparation-meeko`: uses the new `Meeko <https://github.com/forlilab/Meeko>`_ functionality as a Python module to prepare a ``SetOfSmallMolecules``.

C) Grid generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-grid-generation`: generates the grids used by the different AutoDock programs using autogrid4. 

D) Binding site identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-roi-autoligand`: uses `AutoLigand <https://autodock.scripps.edu/resources/autoligand/>`_ tool to predict the binding sites on a protein receptor.
- :ref:`autodock-roi-autosite`: uses `AutoSite <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5048065/>`_ tool to predict the binding sites on a protein receptor.

E) Pharmacophore generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-pharmacophore-generation`: generates a Pharmacophore object RDKit compatible from a resulting binding site of `AutoSite <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5048065/>`_. 

F) Docking
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-autodock4-docking`: uses `AutoDock4: <https://autodock.scripps.edu/download-autodock4/>`_ tool to predict the binding poses for a set of small molecules over the receptor. 
- :ref:`autodock-autodockGPU-docking`: uses `AutoDock-GPU: <https://github.com/ccsb-scripps/AutoDock-GPU>`_, the GPU implementation of AutoDock. 
- :ref:`autodock-vina-docking`: uses `AutoDock Vina: <https://vina.scripps.edu/>`_ docking engine to predict the binding poses for a set of small molecules over the receptor.

G) Docking Rescoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- :ref:`autodock-autodock4-dock-scoring`: scores a ``SetOfSmallMolecules`` that has been already docked by any docking program using `AutoDock4: <https://autodock.scripps.edu/download-autodock4/>`_ scoring function.
