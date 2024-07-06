:orphan: true

.. _schrodinger-binding-site-prediction:

###############################################################
Schrödinger Binding Site Prediction (SiteMap)
###############################################################
This protocol predicts the most promising binding sites on the structure using `SiteMap <https://www.schrodinger.com/products/sitemap>`_.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/schrodinger/virtual-drug-screening/binding-site-prediction/form.png
   :alt: Schrödinger Binding Site Prediction form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfStructROIs`` (Structural Regions Of Interest), containing the predicted binding sites. 
The user can visualize them using **Analyze Results**, which will display the General StructROIs viewer.

.. |testCommand| replace:: pwchemSchrodinger.tests.main_wf.TestSitemap
.. include:: ../../../../templates/plugins/protocol-test.rst
