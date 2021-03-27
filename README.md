# marPy
A Python library to interact with DC's MAR (master address repository) API

## DC’s Master Address Repository

District of Columbia’s [Master Address Repository
(MAR)](https://dcatlas.dcgis.dc.gov/mar/) provides a [web
service](https://opendata.dc.gov/pages/mar-webservices) with geocoding
and address verification operations. 

The `marPy` package gives Python users an object that returns MAR attributes
that can be used to enrich an existing data process.
The MAR web service is free to use and requires no credentialing.


## Limitations

Currently this library only returns the highest matching `confidencelevel` , ie. first return, for any ambiguous address. If the address is a non-dc address or not found in the MAR it will resolve with `non_dc_address`

## Installation

You can install the development version from GitHub

``` sh
git clone https://github.com/tombuko/marPy.git
```

## Usage

``` python
from marpy import marPy
# Create the object
lookup_address = marPy()

# Set the address to lookup
lookup_address.address = '2009 PARK ROAD NW'

# Run the address against the MAR
lookup_address = lookup_address.get_MAR()

# Return attributes about the address from the MAR
print(lookup_address.latitude)
print(lookup_address.longitude)

```

Below is an example of the output of `lookup_address.___dict___`:

``` python
{'address': '2009 PARK ROAD NW',
 'address_id': 233919,
 'marid': 233919,
 'status': 'ACTIVE',
 'fulladdress': '2009 PARK ROAD NW',
 'addrnum': 2009,
 'addrnumsuffix': None,
 'stname': 'PARK',
 'street_type': 'ROAD',
 'quadrant': 'NW',
 'city': 'WASHINGTON',
 'state': 'DC',
 'xcoord': 396072.61,
 'ycoord': 140641.97,
 'ssl': '2617    0094',
 'anc': 'ANC 1D',
 'psa': 'Police Service Area 302',
 'ward': 'Ward 1',
 'nbhd_action': ' ',
 'cluster_': 'Cluster 2',
 'poldist': 'Police District - Third District',
 'roc': 'Police Sector 3D1',
 'census_tract': '002701',
 'vote_prcnct': 'Precinct 40',
 'smd': 'SMD 1D03',
 'zipcode': 20010,
 'nationalgrid': '18S UJ 22721 11403',
 'roadwaysegid': 9513,
 'focus_improvement_area': 'NA',
 'has_alias': 'N',
 'has_condo_unit': 'N',
 'has_res_unit': 'N',
 'has_ssl': 'Y',
 'latitude': 38.9336527,
 'longitude': -77.04529708,
 'streetviewurl': 'http://maps.google.com/maps?z=16&layer=c&cbll=38.9336527,-77.04529708&cbp=11,83.2110528557177,,0,2.09',
 'res_type': 'RESIDENTIAL',
 'ward_2002': 'Ward 1',
 'ward_2012': 'Ward 1',
 'anc_2002': 'ANC 1D',
 'anc_2012': 'ANC 1D',
 'smd_2002': 'SMD 1D03',
 'smd_2012': 'SMD 1D03',
 'imageurl': 'http://citizenatlas.dc.gov/mobilevideo',
 'imagedir': '20040915',
 'imagename': 'DF133627.jpg',
 'confidencelevel': 100.0}
```
