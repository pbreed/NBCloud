.. 

fronttree
======================

Quickstart
----------

To bootstrap the project::

    #This generates a self contained sandbox environment, so that the server runs in a similar environment
    virtualenv fronttree #first time only

    # activate the environment and enter it.
    source fronttree/bin/activate
    
    # install all of the requirements into your environment to run the website
    pip install -r requirements.txt
    
    # setup and sync the database with the models
    manage.py syncdb

    # run a local server at 127.0.0.1:8000
    python manage.py runserver 
