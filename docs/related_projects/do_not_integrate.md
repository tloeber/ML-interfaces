# Don't integrate

## FiftyOne

### Goal

- [Promises better data processing](https://towardsdatascience.com/stop-wasting-time-with-pytorch-datasets-17cac2c22fa8)

### Reason for not integrating

Ran into a host of issues, at least some of which seem to be due to bad design:

- Couldn't install package because of a dependency resolution conflict. It has many dependencies...
- After manually resolving conflict (involving a lot of trial and error), I got a "partially initialized module" error when trying to import it. [Presumably, this stems from the fact that it uses relative imports, resulting in a name clash](https://stackoverflow.com/questions/59762996/how-to-fix-attributeerror-partially-initialized-module). I confirmed this hypothesis by installing it into a new project with a different working directory, which worked.
- In the process of debugging these issues, I also witnessed another dangerous coding pattern, namely the repeated use of "import *".
- When I tried to use the package to download a dataset (coco-2017) from the `zoo` submodule, it again failed with another error, after which I gave up.
