import datetime
from datetime import datetime
from bin.get_data import gateway_health,gateway_set_ble,gateway_start_up
class ggbw100:
    def gateway_startup(data):#gateway start up event processing
        startup_pre_defined_default_keys=sorted(["evt","gateway_id","ble1_count","local_ipv4","powered_by","battery","packet_number","utc_time","access_token","cellular_enabled","mode","imei","sim_ccid","wifi_enabled","ble0_enabled","ble0_count","ble1_enabled","restart_count","firmware_version","hardware_version","gps_enabled","wifi_mode","mod_bus_enabled","communication_mode","mac",'wifi_status',"connected_ap","dhcp","ap_ipv4","static_ip","static_subnet","static_gateway","static_dns1","static_dns2"])
        incoming_data_keys=sorted(data.keys())
        if incoming_data_keys==startup_pre_defined_default_keys:
            for k in data:
                if k=='utc_time':
                    data.update({k:str(datetime.utcfromtimestamp(data[k]))})#converting utc time to gmt time
                #elif data[k]=='':
                    #data.update({k:None})              
            return gateway_start_up(data)
        else:
            not_founded_key_in_incoming_data=[q for q in startup_pre_defined_default_keys if q not in incoming_data_keys ]
            return "this key not found in incoming gateway startup data".title(),not_founded_key_in_incoming_data
    def gateway_ble_config(data):
        ble_config_pre_defined_default_keys=sorted(["evt","count","id_type","ble_port","data","ack_id"])
        incoming_data_keys=sorted(data.keys())

        if incoming_data_keys==ble_config_pre_defined_default_keys:
            for k in data:
               if data[k]=='':
                    data.update({k:None})              
        
            s=data['data'].split(',')
            d=[]
            filtered_data=data
            filtered_data.update({'data':d})
            count=0
            for  x in range(0,len(s),3):
                count+=3
                l={k:v for k,v in zip(['id','sensor_id','time'],s[x:count])}
                d.append(l)
            return gateway_set_ble(filtered_data)
        else:
            not_founded_key_in_incoming_data=[q for q in ble_config_pre_defined_default_keys if q not in incoming_data_keys ]
            return "this key not found in incoming gateway ble config data".title(),not_founded_key_in_incoming_data
            
    def gateway_health(data):
        health_pre_defined_default_keys=sorted(['access_token', 'ap_ipv4', 'battery', 'ble0_count', 'ble0_enabled', 'ble1_count', 'ble1_enabled', 'cellular_enabled', 'communication_mode', 'connected_ap', 'dhcp', 'evt', 'firmware_version', 'gateway_id', 'gps_enabled', 'hardware_version', 'imei', 'local_ipv4', 'mac', 'mod_bus_enabled', 'mode', 'packet_number', 'powered_by', 'present_time', 'restart_count', 'sim_ccid', 'start_time', 'static_dns1', 'static_dns2', 'static_gateway', 'static_ip', 'static_subnet', 'utc_time', 'wifi_enabled', 'wifi_mode', 'wifi_status'])
        incoming_data_keys=sorted(data.keys())
        if incoming_data_keys==health_pre_defined_default_keys:
            for k in data:
                if k=='utc_time':
                    data.update({k:str(datetime.utcfromtimestamp(data[k]))})
                elif k=='present_time':
                    data.update({k:str(datetime.utcfromtimestamp(data[k]))})
                elif k=='start_time':
                    data.update({k:str(datetime.utcfromtimestamp(data[k]))})
        
                #elif str(data[k]).isdigit():
                    #data.update({k:int(data[k])})
            return gateway_health(data)
        else:
            not_founded_key_in_incoming_data=[q for q in health_pre_defined_default_keys if q not in incoming_data_keys]
            return "this key not found in incoming gateway health data".title(),not_founded_key_in_incoming_data
    def input_data(data):
        try:
            if data['evt'].lower()=="START_UP".lower():
                print(ggbw100.gateway_startup(data))
            elif data['evt'].lower()=="SET_BLE_SENSORS".lower():
                print(ggbw100.gateway_ble_config(data))
            elif data['evt'].lower()=="HEALTH".lower():
                print(ggbw100.gateway_health(data))
            else:
                return 'entered evt key value not matching with availble data'.title(),'entered evt key value is : '.title(),data['evt'],'required key values are : SAMPLES,START_UP,HEALTH,SET_BLE_SENSORS'
        except KeyError:
            return 'entered evt key value not matching with availble pre-defined data or evt key not found in entered data '.title(),data