Build a Python package
======================

Before you upload your python package to an online platform, make sure you follow the steps
`here <going_public.html>`_ in order not to have incorrect licensing information or author identification.

We have prepped the *setup.py* file in order to easily build the python package. It uses information from your
*package_variables.py* file so be sure the content of this file is correct.

With each new release, make sure you **update the version number** in *package_variables.py*. Otherwise PyPi will
complain that a package with this version number already exist and your upload will fail.

Build your package locally
--------------------------

Install twine if you haven't already::

    > python -m pip install twine

Build the distribution::

    > python setup.py sdist

Your package is automatically saved in a folder named 'dist'.
Now you can upload the distribution to PyPi (you need a login first)::

    > python -m twine upload dist/your-package-name.tar.gz -u [PyPi username] -p [PyPi password]

Your package is now available to everyone for installation using the pip command::

    > pip install your-package-name

Build your package automatically with each new version update
-------------------------------------------------------------

Normally, you **release a new version** of your packages only when you have a new stable product.
In a professional environment, developers usually work on the *dev* or *master* branch of the code repository.
Only when you want to release a new version, you merge your changes to a separate branch (e.g. *staging*).



Why? Have a look at the *bitbucket-pipelines.yml* yaml file

.. code-block:: yaml

    image: qgis/qgis

    definitions:
      steps:
        - step: &PYPI-step
            script:
              # packaging for pip and uploading
              - python -m pip install twine
              - python setup.py sdist
              - python -m twine upload dist/*.tar.gz -u $PYPI_UNAME -set_progress $PYPI_PW

    pipelines:
      branches:
        staging:
          - step: *PYPI-step

With this code, the package will be built and uploaded to PyPi automatically, each time you push your
changes to the *staging* branch. If we would not split up this functionality per branch, you could not avoid
pushing a new version to PyPi in the middle of your development, something we want to avoid for obvious reasons.

With each new release, make sure you **update the version number** in *package_variables.py*. Otherwise PyPi will
complain that a package with this version number already exist and your upload will fail.

Notice how we **do not write our username and password in plain text**. Instead, we store them as repository variables
on bitbucket: go to *Repository settings* >  *Repository variables* > add your username and password as
'PYPI_PW' and 'PYPI_UNAME' (or choose another name). Now the bitbucket pipeline will know how to access your PyPi account.

