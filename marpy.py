class MAR:
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
    
    
    
    def __init__(self, address):
        '''
        Parameters
        ---------
        address = The DC address string
        
        '''
        self.u_address = address
       
    def get_MAR(self):
        
           '''
        Parameters
        ---------
        self from the MAR class
        
        Exceptions
        -------
        returns 'non_dc_val' if address can't be resolved
        
        '''
        api_url_base = 'http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx';
        operation = '/findLocation2';
        payload = {'str': self.u_address, 'f': 'json'}
        target_url = (api_url_base + operation)
        r = requests.get(target_url,  payload)

        try:
            jsondata = r.json()

            if (jsondata['returnDataset'] is not None):
                # assigning the values to the object
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
            return('non_dc_val') 
