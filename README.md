# Water Accounting Plus (WA+) toolbox

Python module for retrieval of hydrologic, atmospheric, and remote sensing data used for [Water Accounting](http://www.wateraccounting.org/).

This module is compatable on Windows 7 computers, for other operating systems a proper operation of the code cannot be guaranteed.

The manual of the Water Accounting Tool box can be found in [docs/ManualWA.md](https://github.com/wateraccounting/wa/blob/master/docs/ManualWA.md)

## Installation

1. Clone the repository
```
git clone https://github.com/az0uz/watools.git
```
2. Install using pip
```
cd watools
pip2 install -e .
```

### Troublshooting
If getting the following message from libcurl:
```
ImportError: pycurl: libcurl link-time ssl backend (openssl) is different from compile-time ssl backend (none/other)
```
Try the following:
```
pip2 uninstall pycurl
export PYCURL_SSL_LIBRARY=openssl
pip2 install pycurl --no-cache-dir
```

## Dowload a dataset

### TRMM
```
from watools.Collect.TRMM.DataAccess import DownloadData

Dir = '~/datasets/TRMM'
Startdate = '2018-01-01' # 'yyyy-mm-dd'
Enddate = '2018-12-31' # 'yyyy-mm-dd'
latlim = [-50, 50] # (values must be between -50 and 50)
lonlim = [-180, 180] (values must be between -180 and 180)
cores = 4 # The number of cores used to run the routine.
          # It can be 'False' to avoid using parallel computing
          # routines.
Waitbar = 1 # will print a waitbar
TimeCase = 'daily' # "daily" or "monthly"
DownloadData(Dir, Startdate, Enddate, latlim, lonlim, Waitbar, cores, TimeCase=TimeCase)
```
