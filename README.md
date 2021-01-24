
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
Using a single function, one can retrieve data from multiple sources, compare and perform a more complete analysis.


| Source | Status |
| -------|--------|
| understat.com | Beta |
| fbref.com | Tesing |
| whoscored.com | In Progress |
| fantasy.premierleague.com | Planned |
| transfermarkt.us | Planned |


## Installation

The source code is currently [here.](https://github.com/rkaahean/xgpy)

The simplest way to install the package is by pip.
```
pip install xgpy
```

If you want to clone the repository instead:
```
git clone https://github.com/rkaahean/xgpy.git
```

## Usage

**xgpy** has multiple modules, each for every source. For example, in order to get stats from understat:

```python
import xgpy
from xgpy.understat import UnderstatPlayer

player = UnderstatPlayer(1228)
match_data = player.get_player_match_data()
```

And that's it! Look through the documentation and call upon a number of functions.

## Documentation

All the documentation for the functions can be found at [here.](https://xgpy.readthedocs.io/en/latest/)
