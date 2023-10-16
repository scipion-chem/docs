
.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-gromacs
   
.. _docs-chem-gromacs:

.. figure:: ../../../_static/images/plugins/gromacs/gromacs_logo.png
   :alt: gromacs logo

###############################################################
scipion-chem-gromacs
###############################################################
`Gromacs <https://www.gromacs.org/>`_ is a free and open-source software suite for high-performance Molecular
Dynamics (MD) and output analysis. In Scipion-chem-gromacs, we have integrated tools for preparing MD systems,
running simulations and modifying and analyzing the output trajectories.

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

- :ref:`gromacs-System_Preparation`: prepares a Gromacs MD system prior to its simulation from a ``AtomStruct`` object.
- :ref:`gromacs-MD_Simulation`: takes the prepared Gromacs system and use it to run a defined simulation.
- :ref:`gromacs-System_Modification`: performs `modifications <https://manual.gromacs.org/documentation/5.1/onlinehelp/gmx-trjconv.html>`_ over a Gromacs System, specially over its trajectory.
