Write your code
===============

We have already populated this project with a very simple plugin that allows you to add a constant to each pixel
of an image and then set all pixels with a value below a given threshold to 0.

You will notice the code is organized like this::

    > qgis plugin folder
        > core
        > images
        > interfaces
        my_plugin.py

This is done to keep functionality and interfacing separated:

 - The **core** should be built unaware of file formats. It assumes basic parameters like numpy matrices, integers,
   booleans, etc as input and output variables.
 - The **interfaces** deal with reading and writing files and user interactions (e.g. choosing a value).
 - **my_plugin.py** adds a menu item to the *raster* menu and a new tool to the processing toolbox in QGIS.

We begin with discussing the **core** part of the code. The interfacing is discussed in `Part 2 <step2_ui.html>`_
and the building of the QGIS package is discussed in `Part 6 <step6_qgis_plugin.html>`_.

Now have a look at the code and get familiar with the structure:

.. code-block:: python

    import numpy as np

    class MyCode:

        def __init__(self, image: np.ndarray, normalize: bool = False, quotient: int = 255)

        def add_to_image(self, constant: float) -> np.ndarray

        def execute(self, constant: float, threshold: float, p=None, log: callable = print) -> np.ndarray

This text is no attempt to teach the syntax or even best practices of python.
In the line of this project however, here are some importance practices for you to follow:

 - Please document your code and do it correctly.
 - You can give variable type hints in the definition of your function.

   An example:

   .. code-block:: python

      def my_function(self, parameter_name: float, other_parameter: bool=False) -> int:
          """
          Explain what your function does. Leave a blank line and then explain each input
          and output parameter.

          :param parameter_name: Describe the first parameter
          :param other_parameter: Describe another parameter
          :return: describe the return value
          """

 - If you want your QGIS plugin to have the same look and feel as standard tools, your widget should have a
   progress bar and log window.
   Even though ui is not of concern in the core of your code, you should provide a handle to pass on text messages,
   error codes and progress of your code. We have provided two variables for that. In case there is not ui,
   the text, error messages or progress will simply be printed in the terminal:

   .. code-block:: python

    class MyCode:

        ...

        def execute(self, [...], set_progress: callable = None, log: callable = print)
        -> np.ndarray:
            """
            [...]

            :param set_progress: communicate progress (refer to the progress bar in case of GUI;
                                 otherwise print to console)
            :param log:          communicate messages (refer to the print_log tab in the GUI;
                                 otherwise print to the console)
            [...]
            """

            self.set_progress = set_progress if set_progress else printProgress
            self.print_log = log if log else print

            # example: use self.print_log to issue text output to the user
            self.print_log('Processing started ...')

            # example: use self.set_progress to change the progress bar
            self.set_progress(30)

            [...]

            return [...]


    def printProgress(value: int):
        """ Replacement for the GUI progress bar """

        print('progress: {} %'.format(value))


Before you upload your code to an online platform, make sure you follow the steps
`here <going_public.html>`_ in order not to have incorrect licensing information or author identification.

