
<p align="center">
  <h1 align="center">
    xgpy: a powerful python wrapper for football data
  </h1>
</p>
<p align="center">
   <a href="https://travis-ci.com/rkaahean/xgpy"><img src="https://travis-ci.com/rkaahean/xgpy.svg?branch=main"></a>
   <a href="https://xgpy.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/xgpy/badge/?version=latest"></a>
</p>

## What is it?

**xgpy** is a Python package that aims to aggregate multiple football data sources into a single python module.
Using a single function, one can retrieve data from multple places, compare and perform a more complete analysis.


| Source | Status |
| -------|--------|
| understat.com | Beta |
| fbref.com | In Progress |
| fantasy.premierleague.com | Planned |
| whoscored.com | Planned |

## Installation

The source code is currently [here.](https://github.com/rkaahean/xgpy)

The simplest way to install the package is by pip.
```
pip install xgpy
```

## Usage

**xgpy** has multiple modules, each for every source. For example, in order to get stats from understat:

```
import xgpy
from xgpy.understat import UnderstatPlayer

player = UnderstatPlayer(1228)
```

And that's it! Look through the documentation and call upon a number of functions.

### Troubleshooting

There is a known issue of pandas not installing correctly. Please make sure you have pandas
installed before installing xgpy.

```
pip install pandas
pip install xgpy
```
