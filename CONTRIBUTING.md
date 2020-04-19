# Using the Python dependency manager - Poetry

* [Poetry Documentation](https://python-poetry.org/docs/)

Within each package __fexapi__ or __service__:
```
poetry env use 3.8
poetry shell
poetry install 
```

# Generating changelog - Towncrier

* [Link Pypi Towncrier](https://pypi.org/project/towncrier/)

Towncrier has a few standard types of news fragments, signified by the file extension. These are:
```
.feature: Signifying a new feature.
.bugfix: Signifying a bug fix.
.doc: Signifying a documentation improvement.
.removal: Signifying a deprecation or removal of public API.
.misc: A ticket has been closed, but it is not of interest to users.
```
Example a 25.feature file, where 25 is the issue number and .feature and the type of issue, the issue commit goes inside the file.
The version will be read from __init__ within changes

in terminal:
```
towncrier --name packagename
Is it okay if I remove those files? [Y/n]: n
```

# Attention: to always __follow__ the versioning and semantic releases
* [Guide to semantically versioning code](https://semver.org/)
