:orphan: true

.. _gromacs-System_Modification:

###############################################################
Gromacs system modification
###############################################################
This protocol performs `modifications <https://manual.gromacs.org/documentation/5.1/onlinehelp/gmx-trjconv.html>`_ over a Gromacs System, specially over its trajectory.

The modifications include:
    - **Cleaning**: removing waters and ions
    - **Fitting**: Fit trajectory to initial structure
    - **Dropping**: Cut a trajectory, saving only from first to last specified times
    - **Subsampling**: Subsample trajectory frames
    - **Filtering**: Perform low/high pass filters on trajectory frames

|

.. figure:: ../../../../_static/images/plugins/gromacs/gromacs_form3.png
   :alt: gromacs form3

|


The result of this protocol is a GromacsSystem, containing the modified Gromacs files and trajectory. The user
can visualize the complex using **Analyze Results**.


.. |testCommand| replace:: gromacs.tests.tests.TestGromacsTrajMod
.. include:: ../../../templates/plugins/protocol-test.rst

| 
