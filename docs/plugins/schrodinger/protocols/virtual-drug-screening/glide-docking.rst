:orphan: true

.. _schrodinger-Glide_Docking:

###############################################################
Schrödinger Glide Docking
###############################################################
This protocol uses `Glide <https://www.schrodinger.com/products/glide>`_ for docking a set of ligands to a receptor.
The docking can be performed on the whole protein structure or on specific sites, which can be defines as a ``SetOfStructROIs`` or as a ``SetOfSchrodingerGrids``.

|

|form5_1| |form5_2|

.. |form5_1| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_form5_1.png
   :alt: schrodinger form5_1
   :height: 490

.. |form5_2| image:: ../../../../../_static/images/plugins/schrodinger/schrodinger_form5_2.png
   :alt: schrodinger form5_2
   :height: 490

|

The results of these protocols are a ``SetOfSmallMolecules``, containing the predicted binding poses for the input molecules. 
The user can visualize them using **Analyze Results**, which will display the General SmallMolecules viewer.

| 

.. |testCommand| replace:: schrodingerScipion.tests.main_wf.TestGlideDocking
.. include:: ../../../../templates/plugins/protocol-test.rst

| 
