# marPy
A Python library to interact with DC's MAR (master address repository) API

## DC’s Master Address Repository

District of Columbia’s [Master Address Repository
(MAR)](https://dcatlas.dcgis.dc.gov/mar/) provides a [web
service](https://opendata.dc.gov/pages/mar-webservices) with geocoding
and address verification operations. 

The `marPy` package gives Python users
a set of fuctions to interact with the MAR web service. 
The MAR web service is free to use and requies no credentialing.


## Limitations

Currently this library only returns the highest matching, first return, for an abiguous address. If the address is a non-dc address or not found in the mar it will resolve with `non_dc_address`

## Installation

You can install the development version from GitHub

``` sh
git clone https://github.com/tombuko/marPy.git
```

## Usage

``` python
address = marpy('2009 PARK ROAD NW').get_MAR()
print(address.latitude)
print(address.longitude)

```

Below is an example of the output provided by the MAR (in long
format):

``` python
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
The callable MAR objects in `marPy` are:

```python
    address_id
    marid
    status
    fulladdress
    addrnum
    addrnumsuffix
    stname
    street_type
    quadrant
    city
    state
    xcoord
    ycoord
    ssl
    anc
    psa
    ward
    nbhd_action
    cluster_
    poldist
    roc
    census_tract
    vote_prcnct
    smd
    zipcode
    nationalgrid
    roadwaysegid
    focus_improvement_area
    has_alias
    has_condo_unit
    has_res_unit
    has_ssl
    latitude
    longitude
    streetviewurl
    res_type
    ward_2002
    ward_2012
    anc_2002
    anc_2012
    smd_2002
    smd_2012
    imageurl
    imagedir
    imagename
    confidencelevel
```
 
