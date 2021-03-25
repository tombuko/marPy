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

  - `find_location()`: Location query for DC addresses, intersections,
    blocks, and place names

## Installation

You can install the development version from GitHub

``` r
remotes::install_github("tombuko/marPy")
```

## Usage

Below is an example of the output provided by the MAR (in long
format):

``` r
find_location(address = "1600 Pennsylvania Ave NW") %>% tidyr::gather() %>% print(n=Inf)
```

    ## # A tibble: 43 x 2
    ##    key                    value                                 
    ##    <chr>                  <chr>                                 
    ##  1 ADDRESS_ID             293211                                
    ##  2 MARID                  293211                                
    ##  3 STATUS                 ACTIVE                                
    ##  4 FULLADDRESS            1600 PENNSYLVANIA AVENUE NW           
    ##  5 ADDRNUM                1600                                  
    ##  6 STNAME                 PENNSYLVANIA                          
    ##  7 STREET_TYPE            AVENUE                                
    ##  8 QUADRANT               NW                                    
    ##  9 CITY                   WASHINGTON                            
    ## 10 STATE                  DC                                    
    ## 11 XCOORD                 396829.87                             
    ## 12 YCOORD                 136646.99                             
    ## 13 SSL                    0187S   0800                          
    ## 14 ANC                    ANC 2A                                
    ## 15 PSA                    Police Service Area 207               
    ## 16 WARD                   Ward 2                                
    ## 17 NBHD_ACTION            " "                                   
    ## 18 POLDIST                Police District - Second District     
    ## 19 ROC                    Police Sector 2D3                     
    ## 20 CENSUS_TRACT           006202                                
    ## 21 VOTE_PRCNCT            Precinct 2                            
    ## 22 SMD                    SMD 2A01                              
    ## 23 ZIPCODE                20500                                 
    ## 24 NATIONALGRID           18S UJ 23390 07392                    
    ## 25 ROADWAYSEGID           2522                                  
    ## 26 FOCUS_IMPROVEMENT_AREA NA                                    
    ## 27 HAS_ALIAS              Y                                     
    ## 28 HAS_CONDO_UNIT         N                                     
    ## 29 HAS_RES_UNIT           N                                     
    ## 30 HAS_SSL                Y                                     
    ## 31 LATITUDE               38.89766766                           
    ## 32 LONGITUDE              -77.03654468                          
    ## 33 RES_TYPE               MIXED USE                             
    ## 34 WARD_2002              Ward 2                                
    ## 35 WARD_2012              Ward 2                                
    ## 36 ANC_2002               ANC 2A                                
    ## 37 ANC_2012               ANC 2A                                
    ## 38 SMD_2002               SMD 2A05                              
    ## 39 SMD_2012               SMD 2A01                              
    ## 40 IMAGEURL               http://citizenatlas.dc.gov/mobilevideo
    ## 41 IMAGEDIR               NO_IMAGE                              
    ## 42 IMAGENAME              No_Image_Available.JPG                
    ## 43 ConfidenceLevel        100

## Next Steps

  - Testing
  - Implementing additional functions: [all available endpoints for the
    MAR
    webservice](https://citizenatlas.dc.gov/newwebservices/locationverifier.asmx)
