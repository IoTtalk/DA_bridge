IoTtalk_v1_url = ''
IoTtalk_v2_url = ''

dname = "DA_bridge"
dm = "DA_bridge"

device_v1_settings = {
    'IoTtalkURL': IoTtalk_v1_url,
    'd_name': dname,
    'dm_name': dm,
    'u_name': '',
    'is_sim': False,
    'Reg_addr': "C860008BD252",
    'df_list': [''],
    'idf_list': [''],
    'odf_list':[]
}

device_v2_settings = {
    'IoTtalkURL': IoTtalk_v2_url,
    'id': "00000000-0000-0000-0000-000000000000",
    "idf_list": [],
    "odf_list": [('', [''])],
    "name": dname,
    "profile":{
        'model': dm,
    }
}
