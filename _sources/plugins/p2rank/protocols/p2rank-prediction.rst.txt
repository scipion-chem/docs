:orphan: true

.. _p2rank-prediction:

###############################################################
P2Rank pocket prediction
###############################################################
The main program of the `P2Rank <https://github.com/rdk/p2rank>`_ package is P2Rank and it is integrated in Scipion-chem-p2rank as a protocol.

.. image:: ../../../../_static/images/plugins/p2rank/prediction/protocol.png
   :alt: P2Rank pocket prediction protocol
   :align: center

|

Input
----------------------------------------
This protocol takes a ``AtomStruct`` as an input and predicts its pockets based on a machine learning model over its surface. 

.. include:: ../../../templates/plugins/input-help.rst

If you need more information, we recommend you to check the `P2Rank page <https://github.com/rdk/p2rank>`_.

.. image:: ../../../../_static/images/plugins/p2rank/prediction/form.png
   :alt: P2Rank pocket prediction form
   :height: 400
   :align: center

|

The result of this protocol is a ``SetOfStructROIs`` object, containing the predicted pockets. You can inspect this pockets
using the **Analyze results** button or if you want to directly see the related files you will be able to find them
in the protocol's folder.

.. |testCommand| replace:: p2rank.tests.test_p2rank.TestP2Rank
.. include:: ../../../templates/plugins/protocol-test.rst

Viewer
----------------------------------------
The viewer for p2rank results include the Pymol General Viewer for ``SetOfStructROIs`` objects plus an specific viewer of
the surface points visualization they provide.

|

|viewer|  |surface|

|

.. |viewer| image:: ../../../../_static/images/plugins/p2rank/prediction/viewer.png
   :alt: P2Rank pocket prediction viewer
   :width: 45%

.. |surface| image:: ../../../../_static/images/plugins/p2rank/prediction/vmd.png
   :alt: P2Rank pocket prediction vmd
   :width: 50%

As for the rest of the Scipion object, you can also check **Table view** to visualize the stored parameters for each of
the items in the set.
