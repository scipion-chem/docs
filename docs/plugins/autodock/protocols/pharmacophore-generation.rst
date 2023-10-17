:orphan: true

.. _autodock-pharmacophore_generation:

###############################################################
AutoSite Pharmacophore Generation
###############################################################
This protocol generates a Pharmacophore object RDKit compatible from a resulting binding site of AutoSite. 
This pharmacophore objects can later be modified or used to filter compatible molecules using pharmacophore Scipion-chem protocols.

|

.. image:: ../../../../_static/images/plugins/autodock/autodock_form_pharm.png
   :alt: autodock pharm

|

The result of this protocol is an Pharmacophore object containing the hydrophobic, H-donor and H-acceptor cluster centers described in the AutoSite output.

|

.. |testCommand| replace:: autodock.tests.test_autodock.TestAutoSitePharmacophore
.. include:: ../../../templates/plugins/protocol-test.rst