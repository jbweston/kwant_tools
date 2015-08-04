Kwant Tools
===========

A small set of utilities for use with the [Kwant](http://kwant-project.org/)
package for quantum transport simulations.

Kwant is a very general and powerful library. Part of its design philosophy
is to keep it reasonably lean so as not to burden the user with
a load of functionality that they don't need. In this way it is a framework
in which to implement quantum transport simulations, rather than a
plug-and-play simulation package. The downside of this design philosophy
is that there are often common idioms that have to be implemented and
re-implemented by the users themselves, because the concepts are not
sufficiently general to be included in Kwant.

`kwant_tools` is a set of utilities that I have personally found useful
for working with Kwant, as such it is in no way meant to be "complete".
That being said, anyone who finds it useful is free to use it under the
MIT licence, the conditions of which are stated in the LICENSE file.

Contents
========

+ **lattice.py**: utilities for working with Kwant lattices. Includes
  functions for connecting sites in a system from arbitrary lattices
  subject to some criterion, and some functionality for more easily
  working with symmetries

+ **spin.py**: utilities for working with spin as an internal degree
  of freedom (i.e. matrix onsite/hoppings, as opposed to separate
  lattices)


Contributing
------------
I'd be happy to accept pull/merge requests if anyone else has any tools
they'd like to add to this collection.
