
.. _docs-chem-fpocket:

.. figure:: ../../../../_static/images/fpocket/fpocket_logo.png
   :alt: fpocket logo


###############################################################
scipion-chem-fpocket
###############################################################
`FPocket <https://github.com/Discngine/fpocket>`_ is one of the most widely known programs for protein pocket detection.
In this plugin we include the main tool for pocket prediction, FPocket, together with the tool for predicting pockets
over a Molecular Dynamics simulation, MDPocket (in devel).


==========================================
Installation
==========================================
In order to use this plugin, you need to install first Scipion-chem.
`Scipion-chem <https://github.com/scipion-chem/docs>`_
is the core for the rest of scipion-chem-\* plugins. To do so, you can check the instructions in the
`Scipion-chem README <https://github.com/scipion-chem/scipion-chem/blob/master/README.rst>`_.

Similarly, you can find the installation instructions of this plugin in
`Scipion-chem-fpocket README <https://github.com/scipion-chem/scipion-chem-fpocket/blob/master/README.rst>`_

|


==========================================
Protocols
==========================================

- :ref:`fpocket-fpocket-prediction`: Predicts the pockets of an atomic structure based on its concavities (using alpha-speheres) and its electrostatics.



