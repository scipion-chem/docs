
.. _docs-chem-modeller:

.. figure:: ../images/modeller_logo.png
   :alt: modeller logo

Welcome to Scipion-chem-modeller's documentation!
=================================================
In order to use this plugin, you need to install first Scipion-chem.
`Scipion-chem <https://github.com/scipion-chem/docs>`_
is the core for the rest of scipion-chem-\* plugins. To do so, you can check the instructions in the
`Scipion-chem README <https://github.com/scipion-chem/scipion-chem/blob/master/README.rst>`_
Similarly, you can find the installation instructions of this plugin in
`Scipion-chem-modeller README <https://github.com/scipion-chem/scipion-chem-modeller/blob/master/README.rst>`_

|

Scipion-chem-modeller overview
========================================
`Modeller <https://salilab.org/modeller/>`_ is a energy-based tool for homology or comparative modeling of protein
three-dimensional structures.

Scipion-chem-p2rank protocols
========================================

**Comparative modelling**
-------------------------------
This protocol follows the `Modeller manual <https://salilab.org/modeller/manual/node15.html>`_ for comparative
modelling of a protein sequence using one or several structure templates. The protocol includes different sections where
you can define the parameters you want to use for the modelling:

1) **Input**: It can either be a protein Sequence (single chain) or a SetOfSequences (multiple chains). You can also
input a initial structure model for the sequence(s).

2) **Output**: The number of output models and whether to model also the hydrogens can be specified

3) **Templates**: You can define the templates from AtomStruct objects in your project or directly from PDB codes. For
each of them, you will need to define the chain(s) to use in the modelling and the sequence indexes to take into
account. You must use the wizards included in the protocol in order to select the desired chains and positions.
Once the chain(s) and positions are selected, use the third wizard to save the template in the list below.

4) **Alignment**: The alignment of the template sequences can be performed using external software included in
Scipion-chem (Mafft, Clustal, Muscle), Modeller (AutoModeller) or inputting a custom alignment from a file or
SetOfSequencesChem object (be aware that a custom alignment not properly prepared will lead to error).

5) **Scoring**: Different scoring fucntions provided by Modeller can be checked to score the resulting model(s).

6) **Optimization**: The quality and number of cycles of modelling can also be tuned.

All parameters include a help button that gives further information on the parameter.

|

.. image:: ../images/modeller_form1_1.png
   :alt: modeller prot1_1
   :width: 45%

.. image:: ../images/modeller_form1_2.png
   :alt: modeller prot1_2
   :width: 50%

|

The result of this protocol is an AtomStruct object for each model generated. In the summary, you can check the score(s)
obtained for each of them. Analyze Results will open all the output models in PyMol for visualization. You can open
them one by one with right click over the object.

|

Get in contact
==================

From the Scipion team we would be happy to hear your doubts and suggestions, do not hesitate to contact us at any
time. To do so, you can either open an issue in the Github repository related to your question or
contact us by mail.

If the question is related to the Scipion framework, try the `contact us <https://scipion.i2pc.es/contact>`_ page.
If it is related to some Scipion-chem plugin or functionality, you can send a mail to
the developer at ddelhoyo@cnb.csic.es


