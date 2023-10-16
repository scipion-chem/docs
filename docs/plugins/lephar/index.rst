.. |organization| replace:: scipion-chem
.. |repository| replace:: scipion-chem-lephar

.. _docs-chem-lephar:

.. figure:: ../../../_static/images/lephar/lephar_logo.jpg
   :alt: lephar logo

###############################################################
scipion-chem-lephar
###############################################################
`LePhar <http://www.lephar.com/>`_ is a suite that provides several tools for Virtual Drug Screening. As for today,
only protocols for preparing the target and docking are integrated in Scipion-chem-lephar.

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

- :ref:`lephar-LePro`: prepares the protein receptor for docking using LePro.
- :ref:`lephar-create_database`: performs docking using LeDock on a receptor or regions of interest (ROIs)

