:orphan: true

.. _schrodinger-split-structure:

###############################################################
Schrödinger Split Structure
###############################################################
This protocol allows the user to use the ``split_structure.py`` script from Schrodinger mmShare. 

It can be used to split proteins, ligands or different chains inside the structure.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/schrodinger/utils/split-structure/form.png
   :alt: Schrödinger Split Structure form
   :height: 400
   :align: center

|

The result of this protocol is an ``AtomStruct`` containing the splitted structure file in Maestro format.

.. |testCommand| replace:: pwchemSchrodinger.tests.test_utils.TestSplitSchro
.. include:: ../../../../templates/plugins/protocol-test.rst
