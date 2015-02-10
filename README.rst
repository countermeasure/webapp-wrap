webapp-wrap
===========

**Turn you webapp into a desktop app in a few minutes.**


Contents
--------

`1. What is this thing?
<https://github.com/countermeasure/webapp-wrap#1-what-is-this-thing>`_

`2. Dependencies
<https://github.com/countermeasure/webapp-wrap#2-dependencies>`_

`3. Installation
<https://github.com/countermeasure/webapp-wrap#3-installation>`_

`4. Configuration
<https://github.com/countermeasure/webapp-wrap#4-configuration>`_

`5. Use
<https://github.com/countermeasure/webapp-wrap#5-use>`_


1. What is this thing?
----------------------

``webapp-wrap`` configures a lightweight browser and a server so that you
can run your webapp as a desktop app.

The browser uses the WebKit engine and Qt4.

The server is Gunicorn.

It was built with Python-based webapps in mind.


2. Dependencies
---------------

PyQt4 is required.

Not sure if you have it?

::

    $ python
    >>> import PyQt4

If the next line that you see is this, you have PyQt4:

::

    >>>

If the next line that you see is this, you don't have PyQt4:

::

    ImportError: No module named PyQt4


3. Installation
---------------

3.1 Install pip, virtualenv and virtualenvwrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may already have these installed. If so, skip this step.

::

    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv virtualenvwrapper

Add these lines to the end of your ``~/.bashrc`` file:

::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Projects
    source /usr/local/bin/virtualenvwrapper.sh

Reload ``~/.bashrc``:

::

    $ source ~/.bashrc

3.2 Set up a virtualenv
^^^^^^^^^^^^^^^^^^^^^^^

You may already have a virtualenv set up for your webapp. If so, skip
this step.

::

    $ mkvirtualenv your_virtualenv_name

3.3 Clone the repo
^^^^^^^^^^^^^^^^^^

For these instructions we'll clone the repo to ``~/Projects``, but you can put
it anywhere you like.

::

    $ mkdir -p ~/Projects
    $ cd ~/Projects
    $ git clone https://github.com/countermeasure/webapp-wrap.git

3.4 Install requirements (Gunicorn)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ cd ~/Projects/webapp-wrap
    $ pip install -r requirements.txt


4. Configuration
----------------

4.1 Edit the browser script
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open ``browser.py``.

Set the ``TITLE`` variable to the text string you want to see in the window's
title bar.

Set the ``HORIZONTAL_SIZE`` and ``VERTICAL_SIZE`` variables to the size in
pixels that you went the window to be when it opens.

Set the ``STARTING_URL`` variable to your webapp's local URL, remembering to
include the port.

4.2 Edit the server script
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open ``start_server.sh``.

Set the ``PROJECT_NAME`` variable to the name of your project in lower case.

Set the ``PROJECT_DIR`` variable to the directory which your project is in.

Set the ``VIRTUALENVWRAPPER_DIR`` variable to the directory containing your
``virtualenvwrapper.sh`` file.

Set the ``VIRTUALENVWRAPPER_NAME`` variable to the name of your virtualenv.

Set the ``PORT`` variable to the port which the Gunicorn server is using. Port
``8001`` is the default.


5. Use
------

At the moment, starting ``webapp-wrap`` is quite crude.

In a terminal window execute these commands, and leave the window
open:

::

    $ cd ~/Projects/webapp-wrap
    $ source start_server.sh
    $ python browser.py
