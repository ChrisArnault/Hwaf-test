Hwaf-test
=========

Little environment to generate a (set of) project(s)

Each project contains a set of packages

Each package offers:
- a C++ class with its C++ headers
- a library implementing the class
- a test program to instantiate some objects
- a hscript.yml HWAF configuration script

The packages are structured to form a use graph.

Each package using one or several other packages will instantiate objects of the used classes.

One python script 'generator.py' automates the testbed as follows: 

- it creates a new "test" directory
- there, it creates a set of projects
- it generates one random set of packages into each project
- the use graph of the projects is computed on the basis of the complete use graph of packages
- then it traverses the graph of projects, following the use relationships 
- for each project:
  - it configures the project using HWAF
  - it builds the project using the general HWAF conventions 
  - it tests all test programs

Operation:

1) get the generator:

```sh
> (cd /my/dev; git clone https://github.com/ChristianArnault/Hwaf-test.git)
```

2) produce the testbed:

```sh
> (cd /my/dev; python /my/dev/Hwaf-test/generator.py project=[1] packages=[5])
```


