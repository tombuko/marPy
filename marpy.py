import requests

class marPy:
    '''
    A class used to return a MAR object that returns attributes related to an address in Washington DC
    
    Attributes: 
    -----------
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
    
        Methods
        ---------
        get_MAR()
            fetches the address attributes and makes them available
        '''
    
    
    
    def __init__(self, address = ''):
        '''
        Parameters
        ---------
        address = The DC address string
        
        '''
       
        self.address = address
        
    @property
    def address(self):
#         print('getting address')
        return self._address
    @address.setter
    def address(self, value):
#         print('setting value')
        self._address = value
            
  
       
    def get_MAR(self):
        
        '''
        Parameters
        ---------
        self from the MAR class
        
        Exceptions
        -------
        returns 'non_dc_val' if address can't be resolved
        
        '''
        api_url_base = 'http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx'
        operation = '/findLocation2'
        payload = {'str': self.address, 'f': 'json'}
        target_url = (api_url_base + operation)
        r = requests.get(target_url,  payload)

        try:
            jsondata = r.json()
            self.address_id = jsondata['returnDataset']['Table1'][0]['ADDRESS_ID']
            self.marid = jsondata['returnDataset']['Table1'][0]['MARID']
            self.status = jsondata['returnDataset']['Table1'][0]['STATUS']
            self.fulladdress = jsondata['returnDataset']['Table1'][0]['FULLADDRESS']
            self.addrnum = jsondata['returnDataset']['Table1'][0]['ADDRNUM']
            self.addrnumsuffix = jsondata['returnDataset']['Table1'][0]['ADDRNUMSUFFIX']
            self.stname = jsondata['returnDataset']['Table1'][0]['STNAME']
            self.street_type = jsondata['returnDataset']['Table1'][0]['STREET_TYPE']
            self.quadrant = jsondata['returnDataset']['Table1'][0]['QUADRANT']
            self.city = jsondata['returnDataset']['Table1'][0]['CITY']
            self.state = jsondata['returnDataset']['Table1'][0]['STATE']
            self.xcoord = jsondata['returnDataset']['Table1'][0]['XCOORD']
            self.ycoord = jsondata['returnDataset']['Table1'][0]['YCOORD']
            self.ssl = jsondata['returnDataset']['Table1'][0]['SSL']
            self.anc = jsondata['returnDataset']['Table1'][0]['ANC']
            self.psa = jsondata['returnDataset']['Table1'][0]['PSA']
            self.ward = jsondata['returnDataset']['Table1'][0]['WARD']
            self.nbhd_action = jsondata['returnDataset']['Table1'][0]['NBHD_ACTION']
            self.cluster_ = jsondata['returnDataset']['Table1'][0]['CLUSTER_']
            self.poldist = jsondata['returnDataset']['Table1'][0]['POLDIST']
            self.roc = jsondata['returnDataset']['Table1'][0]['ROC']
            self.census_tract = jsondata['returnDataset']['Table1'][0]['CENSUS_TRACT']
            self.vote_prcnct = jsondata['returnDataset']['Table1'][0]['VOTE_PRCNCT']
            self.smd = jsondata['returnDataset']['Table1'][0]['SMD']
            self.zipcode = jsondata['returnDataset']['Table1'][0]['ZIPCODE']
            self.nationalgrid = jsondata['returnDataset']['Table1'][0]['NATIONALGRID']
            self.roadwaysegid = jsondata['returnDataset']['Table1'][0]['ROADWAYSEGID']
            self.focus_improvement_area = jsondata['returnDataset']['Table1'][0]['FOCUS_IMPROVEMENT_AREA']
            self.has_alias = jsondata['returnDataset']['Table1'][0]['HAS_ALIAS']
            self.has_condo_unit = jsondata['returnDataset']['Table1'][0]['HAS_CONDO_UNIT']
            self.has_res_unit = jsondata['returnDataset']['Table1'][0]['HAS_RES_UNIT']
            self.has_ssl = jsondata['returnDataset']['Table1'][0]['HAS_SSL']
            self.latitude = jsondata['returnDataset']['Table1'][0]['LATITUDE']
            self.longitude = jsondata['returnDataset']['Table1'][0]['LONGITUDE']
            self.streetviewurl = jsondata['returnDataset']['Table1'][0]['STREETVIEWURL']
            self.res_type = jsondata['returnDataset']['Table1'][0]['RES_TYPE']
            self.ward_2002 = jsondata['returnDataset']['Table1'][0]['WARD_2002']
            self.ward_2012 = jsondata['returnDataset']['Table1'][0]['WARD_2012']
            self.anc_2002 = jsondata['returnDataset']['Table1'][0]['ANC_2002']
            self.anc_2012 = jsondata['returnDataset']['Table1'][0]['ANC_2012']
            self.smd_2002 = jsondata['returnDataset']['Table1'][0]['SMD_2002']
            self.smd_2012 = jsondata['returnDataset']['Table1'][0]['SMD_2012']
            self.imageurl = jsondata['returnDataset']['Table1'][0]['IMAGEURL']
            self.imagedir = jsondata['returnDataset']['Table1'][0]['IMAGEDIR']
            self.imagename = jsondata['returnDataset']['Table1'][0]['IMAGENAME']
            self.confidencelevel = jsondata['returnDataset']['Table1'][0]['ConfidenceLevel']
            return(self)
        except:
            self.address_id = 'non_dc_val{}'.format(self.address)
            self.marid = 'non_dc_val{}'.format(self.address)
            self.status = 'non_dc_val{}'.format(self.address)
            self.fulladdress = 'non_dc_val{}'.format(self.address)
            self.addrnum = 'non_dc_val{}'.format(self.address)
            self.addrnumsuffix = 'non_dc_val{}'.format(self.address)
            self.stname = 'non_dc_val{}'.format(self.address)
            self.street_type = 'non_dc_val{}'.format(self.address)
            self.quadrant = 'non_dc_val{}'.format(self.address)
            self.city = 'non_dc_val{}'.format(self.address)
            self.state = 'non_dc_val{}'.format(self.address)
            self.xcoord = 'non_dc_val{}'.format(self.address)
            self.ycoord = 'non_dc_val{}'.format(self.address)
            self.ssl = 'non_dc_val{}'.format(self.address)
            self.anc = 'non_dc_val{}'.format(self.address)
            self.psa = 'non_dc_val{}'.format(self.address)
            self.ward = 'non_dc_val{}'.format(self.address)
            self.nbhd_action = 'non_dc_val{}'.format(self.address)
            self.cluster_ = 'non_dc_val{}'.format(self.address)
            self.poldist = 'non_dc_val{}'.format(self.address)
            self.roc = 'non_dc_val{}'.format(self.address)
            self.census_tract = 'non_dc_val{}'.format(self.address)
            self.vote_prcnct = 'non_dc_val{}'.format(self.address)
            self.smd = 'non_dc_val{}'.format(self.address)
            self.zipcode = 'non_dc_val{}'.format(self.address)
            self.nationalgrid = 'non_dc_val{}'.format(self.address)
            self.roadwaysegid = 'non_dc_val{}'.format(self.address)
            self.focus_improvement_area = 'non_dc_val{}'.format(self.address)
            self.has_alias = 'non_dc_val{}'.format(self.address)
            self.has_condo_unit = 'non_dc_val{}'.format(self.address)
            self.has_res_unit = 'non_dc_val{}'.format(self.address)
            self.has_ssl = 'non_dc_val{}'.format(self.address)
            self.latitude = 'non_dc_val{}'.format(self.address)
            self.longitude = 'non_dc_val{}'.format(self.address)
            self.streetviewurl = 'non_dc_val{}'.format(self.address)
            self.res_type = 'non_dc_val{}'.format(self.address)
            self.ward_2002 = 'non_dc_val{}'.format(self.address)
            self.ward_2012 = 'non_dc_val{}'.format(self.address)
            self.anc_2002 = 'non_dc_val{}'.format(self.address)
            self.anc_2012 = 'non_dc_val{}'.format(self.address)
            self.smd_2002 = 'non_dc_val{}'.format(self.address)
            self.smd_2012 = 'non_dc_val{}'.format(self.address)
            self.imageurl = 'non_dc_val{}'.format(self.address)
            self.imagedir = 'non_dc_val{}'.format(self.address)
            self.imagename = 'non_dc_val{}'.format(self.address)
            self.confidencelevel = 'non_dc_val{}'.format(self.address)
            return(self)