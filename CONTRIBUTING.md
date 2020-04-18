# Using the Python dependency manager - Poetry

* [Poetry Documentation](https://python-poetry.org/)

Within each "service" or "fexapi" package, type the following commands in the terminal:
```
poetry env use 3.8
poetry shell
poetry update
```

# Generating changelogs correctly - Towncrier

* [Link Pypi Towncrier](https://pypi.org/project/towncrier/)

The towncrier has some standard types of news fragments, signified by the file extension. These are:
```
.feature: meaning a new feature.
.bugfix: meaning a bug fix.
.doc: meaning an improvement in the documentation.
.removal: meaning a discontinuation or removal of the public API.
.misc: a ticket has been closed, but it does not interest users.
```    
Example: a file named 25.feature, where "25" represents the issue number and ".feature" 
represents what type of issue it is about, the content of the issue can be inserted into the
archive.

To generate the changelog, type the following command:
```
towncrier --name namepackage "Service" or "Fexapi"
```
The name of the package for which the changelog is being generated  
Is it okay if I remove those files? [Y/n]: Choose no "n"

---
# __Atention__: follow versioning and semantic releases

* [Guide on how to do a semantic versioning](https://semver.org/lang/pt-BR/)