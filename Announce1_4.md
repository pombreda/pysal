## PySAL 1.4 Released (2012-07-31) ##

On behalf of the PySAL development team, I'm happy to announce the
official release of PySAL 1.4.

PySAL is a library of tools for spatial data analysis and
geocomputation written in Python. PySAL 1.4, the fifth official
release of PySAL brings the following key enhancements:

  * spatial regression (spreg):
    * Integration of scipy.sparse structures in all the regression classes
    * Probit
    * Probit with diagnostics for spatial effects

  * exploratory spatial data analysis (esda):
    * Generalized Gamma statistics for spatial autocorrelation

  * spatial dynamics (spatial\_dynamics):
    * O(n log n) algorithm for spatial tau (spatial rank correlation)
    * LISA Markov transitions and tests for spatial dynamics

  * computational geometry (cg) and spatial networks
    * efficient point to nearest LineSegment search
    * generate network topology from shapefiles
    * utilities for interfacing with networkx
    * integration of network cluster code (beta)

among the 155 commits and bug fixes since the last release, 6 months ago.

PySAL modules

---

  * pysal.core — Core Data Structures and IO
  * pysal.cg — Computational Geometry
  * pysal.esda — Exploratory Spatial Data Analysis
  * pysal.inequality — Spatial Inequality Analysis
  * pysal.spatial\_dynamics — Spatial Dynamics
  * pysal.spreg - Regression and Diagnostics
  * pysal.region — Spatially Constrained Clustering
  * pysal.weights — Spatial Weights
  * pysal.FileIO — PySAL FileIO: Module for reading and writing various file types in a Pythonic way

Downloads

---

Binary installers and source distributions are available for download at
http://code.google.com/p/pysal/downloads/list

Documentation

---

The documentation site is here
http://pysal.geodacenter.org/1.4


Web sites

---

PySAL's home is here
http://pysal.org/

The developer's site is here
http://code.google.com/p/pysal/

Mailing Lists

---

Please see the developer's list here
http://groups.google.com/group/pysal-dev

Help for users is here
http://groups.google.com/group/openspace-list

Bug reports and feature requests

---

To search for or report bugs, as well as request enhancements, please see
http://code.google.com/p/pysal/issues/list

License information

---

See the file "LICENSE.txt" for information on the history of this
software, terms & conditions for usage, and a DISCLAIMER OF ALL
WARRANTIES.

Many thanks to [all who contributed!](http://code.google.com/p/pysal/source/browse/tags/1.4/THANKS.txt)

Serge, on behalf of the PySAL development team.