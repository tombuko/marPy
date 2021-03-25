# marPy
A Python library to interact with DC's MAR (master address repository) API

## DC’s Master Address Repository

District of Columbia’s [Master Address Repository
(MAR)](https://dcatlas.dcgis.dc.gov/mar/) provides a [web
service](https://opendata.dc.gov/pages/mar-webservices) with geocoding
and address verification operations. The `marPy` package gives Python users
a set of fuctions to interact with the MAR web service. The MAR web
service is free to use and requies no credentialing.

## What’s Inside?

Currently only the following function is implemented:

  - `getMar()`: Location query for DC addresses, intersections,
    blocks, and place names

## Installation

You can install the development version from GitHub

``` r
$ git clone https://github.com/tombuko/marPy.git
```

## Usage

Below is an example of the output provided by the MAR (in long
format):

``` r
 {'ADDRESS_ID': 233919,
   'MARID': 233919,
   'STATUS': 'ACTIVE',
   'FULLADDRESS': '2009 PARK ROAD NW',
   'ADDRNUM': 2009,
   'ADDRNUMSUFFIX': None,
   'STNAME': 'PARK',
   'STREET_TYPE': 'ROAD',
   'QUADRANT': 'NW',
   'CITY': 'WASHINGTON',
   'STATE': 'DC',
   'XCOORD': 396072.61,
   'YCOORD': 140641.97,
   'SSL': '2617    0094',
   'ANC': 'ANC 1D',
   'PSA': 'Police Service Area 302',
   'WARD': 'Ward 1',
   'NBHD_ACTION': ' ',
   'CLUSTER_': 'Cluster 2',
   'POLDIST': 'Police District - Third District',
   'ROC': 'Police Sector 3D1',
   'CENSUS_TRACT': '002701',
   'VOTE_PRCNCT': 'Precinct 40',
   'SMD': 'SMD 1D03',
   'ZIPCODE': 20010,
   'NATIONALGRID': '18S UJ 22721 11403',
   'ROADWAYSEGID': 9513,
   'FOCUS_IMPROVEMENT_AREA': 'NA',
   'HAS_ALIAS': 'N',
   'HAS_CONDO_UNIT': 'N',
   'HAS_RES_UNIT': 'N',
   'HAS_SSL': 'Y',
   'LATITUDE': 38.9336527,
   'LONGITUDE': -77.04529708,
   'STREETVIEWURL': 'http://maps.google.com/maps?z=16&layer=c&cbll=38.9336527,-77.04529708&cbp=11,83.2110528557177,,0,2.09',
   'RES_TYPE': 'RESIDENTIAL',
   'WARD_2002': 'Ward 1',
   'WARD_2012': 'Ward 1',
   'ANC_2002': 'ANC 1D',
   'ANC_2012': 'ANC 1D',
   'SMD_2002': 'SMD 1D03',
   'SMD_2012': 'SMD 1D03',
   'IMAGEURL': 'http://citizenatlas.dc.gov/mobilevideo',
   'IMAGEDIR': '20040915',
   'IMAGENAME': 'DF133627.jpg',
   'ConfidenceLevel': 80.25}'
```

    
 
