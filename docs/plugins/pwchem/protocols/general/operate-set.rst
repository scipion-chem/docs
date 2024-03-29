:orphan: true

.. _pwchem-operate-set:

###############################################################
Operate set
###############################################################
This protocol includes several functionalities to modify any Scipion Set inside the project. It handles the internal
SQLite representation to modify the set object. The user must define a reference attribute of the items which will
determine the function of the protocol:

- **Unique**: Keeps only one of the elements which have the referent attribute repeated.
- **Union**: Merges two sets of the same type. The user can still perform the Unique operation after that.
- **Intersection**: Keeps only the intersection of several sets, using the reference attribute.
- **Difference**: Keeps the elements of the first set that are not repeated in the second set
- **Filter**: Filters the set based on a filter attribute value and a filter operation the user can specify. Keeps only the elements that pass the filter.
- **Remove** columns*: Remove a column or attribute from a Set object.
- **Ranking**: Sorts the elements of a Set based on the filter column and keeps only those elements above/below a defined threshold.

These operations have some shared functionalities with "edit set" and "filter set" protocols from `scipion-em <https://github.com/scipion-em/scipion-em>`_. The user
is free to choose among them.

Input
----------------------------------------
.. include:: ../../../../templates/plugins/input-help.rst

.. image:: ../../../../../_static/images/plugins/pwchem/general/operate-set/form_1.png
   :alt: Operate set form 1
   :height: 400
   :align: center

|

.. image:: ../../../../../_static/images/plugins/pwchem/general/operate-set/form_2.png
   :alt: Operate set form 2
   :height: 400
   :align: center

|

The result of this protocol is object equal to the one in the input, but this time the files inside this object are in
the desired format.

.. |testCommand| replace:: pwchem.tests.tests_general.TestOperateSet
.. include:: ../../../../templates/plugins/protocol-test.rst
