socialcrawl
=========

Script for fetching profile information from social networks

## Installation

Python 2.7.x is required, plus some python packages which can be installed by typing:

    pip install -r requirements.txt


## Configuration

Create a file for social network authentication at `socialcrawl/auth.py`. A sample file can be
found at `socialcrawl/auth_sample.py`. 

### Twitter

You will need to register an application, generate an OAuth access token for it and define `TWITTER_ACCESS_TOKEN`

### Facebook

You will need to register an app, generate an OAuth access token and define `FACEBOOK_ACCESS_TOKEN`

### Cache

The maximum staleness of the cached data is defined in `settings.CACHE_MAX_AGE`, in minutes.

Per default a local `data.db` sqlite DB is used for caching, which can be installed in debian based systems by typing:

    sudo apt-get install sqlite

You will need to create the DB:

    python manage.py syncdb

If you want to use another SQL DB or otherwise change the defaults edit `settings.DATABASES`.

## Running the scripts

### Client scripts

To get twitter profile info for the user 'twitter':

    PYTHONPATH=. python socialcrawl/clients/twitter.py twitter

For the Facebook 'zuck' user:

    PYTHONPATH=. python socialcrawl/clients/facebook.py zuck

### Cached scripts

You can use a cached version of the scripts that use Django's ORM to cache data locally:

    python manage.py twitter twitter
    python manage.py facebook zuck

## Tests

Test dependencies can be installed by typing:

    pip install -r test_requirements.txt

To run the test suite:

    python manage.py test -v 2 -s socialcrawl
