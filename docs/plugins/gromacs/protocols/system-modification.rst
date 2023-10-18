:orphan: true

.. _gromacs-system-modification:

###############################################################
Gromacs system modification
###############################################################
This protocol performs `modifications <https://manual.gromacs.org/documentation/5.1/onlinehelp/gmx-trjconv.html>`_ over 
a Gromacs System, specially over its trajectory.

The modifications include:
    - **Cleaning**: removing waters and ions
    - **Fitting**: Fit trajectory to initial structure
    - **Dropping**: Cut a trajectory, saving only from first to last specified times
    - **Subsampling**: Subsample trajectory frames
    - **Filtering**: Perform low/high pass filters on trajectory frames

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../_static/images/plugins/gromacs/system-modification/form.png
   :alt: Gromacs system modification form 1
   :height: 400
   :align: center

|

The result of this protocol is a ``GromacsSystem``, containing the modified Gromacs files and trajectory. The user
can visualize the complex using **Analyze Results**.

.. |testCommand| replace:: gromacs.tests.tests.TestGromacsTrajMod
.. include:: ../../../templates/plugins/protocol-test.rst
