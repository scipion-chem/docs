Automatic testing tool
========================================
Scipion chem also integrates a tool aimed at running every test in a plugin taking advantage of the full potential of the 
machine they are being run on.

Requisites
------------------------------------------
In order to use this tool, both :ref:`pwchem-index` and the plugin to be tested must be installed.

Usage
------------------------------------------
Basic usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are usually two ways of using the automatic test tool.

 1. The first and easiest one usually is to call the script directly from the scipion-chem directory.
    To command to use is:

    .. parsed-literal::

        python /path/to/scipion-chem/pwchem/runTests.py /path/to/scipion/scipion3 modulename
    
    Where ``/path/to/scipion-chem/`` is the path to your scipion-chem repository, ``/path/to/scipion/`` is the current path to your Scipion3 installation, 
    effectively providing the script the scipion binary file to launch, and ``modulename`` must be replaced with the module name of the 
    plugin to use. That name can be found inside Scipion, when searching for protocols of a plugin.

    For example, the module name for scipion-chem is ``pwchem``, as shown in the image below:

    .. image:: ../../../_static/images/tools/automatic-tests/pwchem_modulename.png
        :alt: Pwchem module name
        :height: 300
        :align: center

    |

    So, as an example, if I want to run all tests for scipion-chem plugin, my scipion-chem repository has been downloaded in the path 
    ``/home/chemuser/software``, and scipion is also in the path ``/home/chemuser/software``, the command I would need to run would be:

    .. parsed-literal::

        python /home/chemuser/software/scipion-chem/pwchem/runTests.py /home/chemuser/software/scipion/scipion3 pwchem

 2. It is not always possible and / or easy to use the first method, specially if scipion-chem has been installed in production mode.
    So, for such reason, all plugins which deppend on scipion-chem, are bundled with a small script that imports and calls the script from scipion-chem.
    To use it, use the following commands:

    .. parsed-literal::

        conda activate scipion3
        python /path/to/scipion-chem-plugin/modulename/runTests.py /path/to/scipion/scipion3 modulename

    Where ``/path/to/scipion-chem-plugin/modulename/`` must be replaced with the path of the plugin to test, and, inside it, the folder with the module name 
    of that plugin. The rest of arguments must also be replaced as explained in the previous way.

    .. warning:
        For the second way to work, it is necessary to activate ``scipion3`` conda enviroment first as shown in the command above.

    So, as an example, if I want to run all tests for scipion-chem-autodock plugin, my scipion-chem-autodock repository has been downloaded in 
    the path ``/home/chemuser/software``, and scipion is also in the path ``/home/chemuser/software``, the command I would need to run would be:

    .. parsed-literal::

        conda activate scipion3
        python /home/chemuser/software/scipion-chem-autodock/autodock/runTests.py /home/chemuser/software/scipion/scipion3 autodock
    
    .. note:
        Take into account that, from every plugin, you can access the automatic test tool entirely, which means that you can also run tests for plugins 
        other than the one you are calling it from.

        For example:

        ``conda activate scipion3 && python /home/chemuser/software/scipion-chem-autodock/autodock/runTests.py /home/chemuser/software/scipion/scipion3 rosetta``

        This command would run all tests for ``scipion-chem-rosetta`` plugin.

Additional Flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
