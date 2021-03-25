def getMarResult(cellvalue):
    api_url_base = 'http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx';
    operation = '/findLocation2';
    payload = {'str': cellvalue, 'f': 'json'}
    target_url = (api_url_base + operation)
    r = requests.get(target_url,  payload)

    try:
        jsondata = r.json()
        if(jsondata['returnDataset'] is not None):
            # print('FULL_ADDRESS: ', cellvalue)
            # Assign the json values to a variable
            vADDRESS_ID = jsondata['returnDataset']['Table1'][0]['ADDRESS_ID']
            vADDRNUM = jsondata['returnDataset']['Table1'][0]['ADDRNUM']
            vADDRNUMSUFFIX = jsondata['returnDataset']['Table1'][0]['ADDRNUMSUFFIX']
            vSTNAME = jsondata['returnDataset']['Table1'][0]['STNAME']
            vSTREET_TYPE = jsondata['returnDataset']['Table1'][0]['STREET_TYPE']
            vQUADRANT = jsondata['returnDataset']['Table1'][0]['QUADRANT']
            vZIPCODE = jsondata['returnDataset']['Table1'][0]['ZIPCODE']
            vFULLADDRESS = jsondata['returnDataset']['Table1'][0]['FULLADDRESS']
            vSSL = jsondata['returnDataset']['Table1'][0]['SSL']
            vWARD = jsondata['returnDataset']['Table1'][0]['WARD']
            vANC = jsondata['returnDataset']['Table1'][0]['ANC']
            vSMD = jsondata['returnDataset']['Table1'][0]['SMD']
            vLONGITUDE = jsondata['returnDataset']['Table1'][0]['LONGITUDE']
            vLATITUDE = jsondata['returnDataset']['Table1'][0]['LATITUDE']
            vCLUSTER = jsondata['returnDataset']['Table1'][0]['CLUSTER_']

    #         print('\nADDRESS_ID:', '"'+str(vADDRESS_ID)+'"')
    #         print('ADDRNUM:', '"'+str(vADDRNUM)+'"')
    #         print('ADDRNUMSUFFIX:', '"'+str(vADDRNUMSUFFIX)+'"')
    #         print('STNAME:', '"'+str(vSTNAME)+'"')
    #         print('STREET_TYPE:', '"'+str(vSTREET_TYPE)+'"')
    #         print('QUADRANT:', '"'+str(vQUADRANT)+'"')
    #         print('ZIPCODE:', '"'+str(vZIPCODE)+'"')
    #         print('FULLADDRESS:', '"'+str(vFULLADDRESS)+'"')
    #         print('SSL:', '"'+str(vSSL)+'"')
    #         print('WARD:', '"'+str(vWARD)+'"')
    #         print('ANC:', '"'+str(vANC)+'"')
    #         print('SMD:', '"'+str(vSMD)+'"')
    #         print('LONGITUDE:', '"'+str(vLONGITUDE)+'"')
    #         print('LATITUDE:', '"'+str(vLATITUDE)+'"')
    #         print('CLUSTER:', '"'+str(vCLUSTER)+'"')

        return (vLONGITUDE, vLATITUDE)
    except:
        return('non_dc_val','non_dc_val')
