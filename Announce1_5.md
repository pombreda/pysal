# PySAL 1.5 Released (2013-01-30) #

On behalf of the PySAL development team, I'm happy to announce the
official release of PySAL 1.5.

PySAL is a library of tools for spatial data analysis and
geocomputation written in Python. PySAL 1.5, the sixth official
release of PySAL brings the following key enhancements:

### spatial regression (spreg) ###

Adding regime classes for all GM methods and OLS available in pysal.spreg,
i.e. OLS, TSLS, spatial lag models, spatial error models and SARAR models. All
tests and heteroskedasticity corrections/estimators currently available in
pysal.spreg apply to regime models (e.g. White, HAC and KP-HET). With the
regimes, it is possible to estimate models that have:

  * Common or regime-specific error variance; Common or regime-specific
  * Coefficients for all variables or for a selection of variables
  * Common or regime-specific constant term


### FileIO ###

  * support for kwt

### contrib modules (sandbox modules, not in core) ###

  * shapely
  * mapping
  * network
  * spatial databases

among the 116 commits and bug fixes since the last release, 6 months ago.

## PySAL modules ##

  * pysal.core — Core Data Structures and IO
  * pysal.cg — Computational Geometry
  * pysal.esda — Exploratory Spatial Data Analysis
  * pysal.inequality — Spatial Inequality Analysis
  * pysal.spatial\_dynamics — Spatial Dynamics
  * pysal.spreg - Regression and Diagnostics
  * pysal.region — Spatially Constrained Clustering
  * pysal.weights — Spatial Weights
  * pysal.FileIO — PySAL FileIO: Module for reading and writing various file types in a Pythonic way

## Downloads ##
Binary installers and source distributions are available for download at
http://code.google.com/p/pysal/downloads/list

PySAL can also be installed with pip or easy\_install.


## Documentation ##
The documentation site is here
http://pysal.geodacenter.org/1.5


## Web sites ##
PySAL's home is here
http://pysal.org/

The developer's site is here
http://code.google.com/p/pysal/

## Mailing Lists ##
Please see the developer's list here
http://groups.google.com/group/pysal-dev

Help for users is here
http://groups.google.com/group/openspace-list

## Bug reports and feature requests ##
To search for or report bugs, as well as request enhancements, please see
http://code.google.com/p/pysal/issues/list

## License information ##
See the file "LICENSE.txt" for information on the history of this
software, terms & conditions for usage, and a DISCLAIMER OF ALL
WARRANTIES.

Many thanks to [all who contributed!](http://code.google.com/p/pysal/source/browse/tags/1.5/THANKS.txt)

Serge, on behalf of the PySAL development team.