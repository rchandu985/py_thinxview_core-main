from py_thinxview_core.ggbw100_gateway import *
from py_thinxview_core.ble_temperature_humidity_sensor import Ble_TH_Sensor_Data_Processing,Get_Ble_TH_Sensor_Duplicate_Data
from py_thinxview_core.one_wire_temperature_sensor import Notification_Alert_Processing,One_Wire_Temperature_Sensor_Data_Processing,Get_One_Wire_Temperature_Sensor_Duplicate_Data
from py_thinxview_core.door_sensor import Door_Sensor_Data_Processing,Get_Door_Sensor_Duplicate_Data
import json

#from py_thinxview_core.ble_temperature_humidity_sensor import 
startup=json.loads('{"evt":"START_UP","gateway_id":"GS00000004","powered_by":"battery","battery":1,"packet_number":12001,"utc_time":1669023964,"access_token":"asdfghjklasdfghjk","cellular_enabled":1,"mode":"wifi","imei":"860987053931736","sim_ccid":"89910273304011072774","wifi_enabled":1,"ble0_enabled":1,"ble0_count":2,"ble1_enabled":0,"ble1_count":0,"restart_count":0,"firmware_version":"1.15","hardware_version":"1.1","gps_enabled":0,"mod_bus_enabled":0,"communication_mode":"Plain_MQTT","mac":"","wifi_status":"Connected","wifi_mode":"AP+Station","connected_ap":"","dhcp":"","local_ipv4":"","ap_ipv4":"","static_ip":"","static_subnet":"","static_gateway":"","static_dns1":"","static_dns2":""}')
health=json.loads('{"evt":"HEALTH","gateway_id":"67010B0004","start_time":1670500657,"present_time":1670500658,"powered_by":"battery","battery":95,"packet_number":18064,"utc_time":1670500658,"access_token":"asdfghjklasdfghjk","cellular_enabled":1,"mode":"wifi","imei":"860987053948334","sim_ccid":"89910273304011072766","wifi_enabled":1,"ble0_enabled":1,"ble0_count":3,"ble1_enabled":0,"ble1_count":0,"restart_count":0,"firmware_version":"1.0","hardware_version":"1.01","gps_enabled":0,"mod_bus_enabled":0,"communication_mode":"Plain_MQTT","mac":"","wifi_status":"Connected","wifi_mode":"AP+Station","connected_ap":"","dhcp":"","local_ipv4":"","ap_ipv4":"","static_ip":"","static_subnet":"","static_gateway":"","static_dns1":"","static_dns2":""}')
set_ble_sensors=json.loads('{"evt":"SET_BLE_SENSORS","ack_id":"12","id_type":"DEV_ID","ble_port":0,"count":4,"data":"0,00300015,60,1,00300016,60,2,00300017,60,3,00300018,60"}')
samples=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000700,1A:00:01:00:0F:00,1,1000,167240700,0,100,2000,0,0,0,0,0,0#1000700,1A:00:01:00:0F:00,1,2000,1672408380,0,100,2000,0,0,0,0,0,0#1000700,1A:00:01:00:0F:00,1,3000,1672410600,0,100,1000,0,0,0,0,0,0#1000800,1A:00:01:00:0F:00,1,3000,1672410600,0,100,2000,0,0,0,0,0,0#1000800,1A:00:01:00:0F:00,1,1000,167240700,0,100,2000,0,0,0,0,0,0#1000900,1A:00:01:00:0F:00,1,4000,167240700,0,100,2000,0,0,0,0,0,0#"}')#
#1672421700
s1000100=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1000,9000,0,0,0,0,0,0#1000100,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1000,10000,0,0,0,0,0,0#"}')
s1000200=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000200,1A:00:01:00:0F:00,2,4000,1672421700,0,60,6000,9000,0,0,0,0,0,0#1000200,1A:00:01:00:0F:00,2,5000,1672422000,0,60,6000,9000,0,0,0,0,0,0#"}')
s1000300=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000300,1A:00:01:00:0F:00,2,4000,1672421700,0,60,3000,9000,0,0,0,0,0,0#1000300,1A:00:01:00:0F:00,2,5000,1672422000,0,60,6000,6000,0,0,0,0,0,0#"}')#double verification
s1000400=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000400,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1000,4000,0,0,0,0,0,0#1000400,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1000,4000,0,0,0,0,0,0#"}')
s1000500=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000500,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1000,8000,0,0,0,0,0,0#1000500,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1000,8000,0,0,0,0,0,0#"}')
s1000600=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000600,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1000,2900,0,0,0,0,0,0#1000600,1A:00:01:00:0F:00,2,5000,1672422000,0,60,4500,7000,0,0,0,0,0,0#"}')#double verification
s1000700=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000700,1A:00:01:00:0F:00,2,4000,1672421700,0,29,1000,8000,0,0,0,0,0,0#1000700,1A:00:01:00:0F:00,2,5000,1672422000,0,29,1000,8000,0,0,0,0,0,0#"}')
s1000800=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000800,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1000,1000,0,0,0,0,0,0#1000800,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1000,8000,0,0,0,0,0,0#"}')#double verfication
s1000900=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"1000900,1A:00:01:00:0F:00,2,4000,1672421700,0,60,2000,1000,0,0,0,0,0,0#1000900,1A:00:01:00:0F:00,2,5000,1672422000,0,60,4000,5500,0,0,0,0,0,0#"}')#double verfication
s2000100=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,3000,1000,0,0,0,0,0,0#2000100,1A:00:01:00:0F:00,2,5000,1672422000,0,60,3000,1000,0,0,0,0,0,0#"}')#trible verification verfication
s2000200=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000200,1A:00:01:00:0F:00,2,4000,1672421700,0,60,4500,1000,0,0,0,0,0,0#2000200,1A:00:01:00:0F:00,2,5000,1672422000,0,60,4500,1000,0,0,0,0,0,0#"}')#double verification verfication
s2000300=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000300,1A:00:01:00:0F:00,2,4000,1672421700,0,60,7200,1000,0,0,0,0,0,0#2000300,1A:00:01:00:0F:00,2,5000,1672422000,0,60,7200,1000,0,0,0,0,0,0#"}')#double verification verfication
s2000400=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000400,1A:00:01:00:0F:00,2,4000,1672421700,0,60,7300,7300,0,0,0,0,0,0#2000400,1A:00:01:00:0F:00,2,5000,1672422000,0,60,6000,9500,0,0,0,0,0,0#"}')#trible verfication
s2000500=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000500,1A:00:01:00:0F:00,2,4000,1672421700,0,60,400,7300,0,0,0,0,0,0#2000500,1A:00:01:00:0F:00,2,5000,1672422000,0,60,400,7300,0,0,0,0,0,0#"}')#trible verfication
s2000600=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000600,1A:00:01:00:0F:00,2,4000,1672421700,0,60,600,7300,0,0,0,0,0,0#2000600,1A:00:01:00:0F:00,2,5000,1672422000,0,60,600,7300,0,0,0,0,0,0#"}')#trible verfication
s2000700=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000700,1A:00:01:00:0F:00,2,4000,1672421700,0,60,900,7300,0,0,0,0,0,0#2000700,1A:00:01:00:0F:00,2,5000,1672422000,0,60,900,7300,0,0,0,0,0,0#"}')#4 times verfication
s2000800=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000800,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1900,7300,0,0,0,0,0,0#2000800,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1900,7300,0,0,0,0,0,0#"}')#double verfication
s2000900=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"2000900,1A:00:01:00:0F:00,2,4000,1672421700,0,60,8400,7300,0,0,0,0,0,0#2000900,1A:00:01:00:0F:00,2,5000,1672422000,0,60,8400,7300,0,0,0,0,0,0#"}')#double verfication
s3000100=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1900,7300,0,0,0,0,0,0#3000100,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1900,7300,0,0,0,0,0,0#"}')#trible verfication
s3000200=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000200,1A:00:01:00:0F:00,2,4000,1672421700,0,60,900,7300,0,0,0,0,0,0#3000200,1A:00:01:00:0F:00,2,5000,1672422000,0,60,7300,900,0,0,0,0,0,0#"}')#double verfication
s3000300=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000300,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1900,7100,0,0,0,0,0,0#3000300,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1900,7100,0,0,0,0,0,0#"}')#double verfication
s3000400=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000400,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1900,1900,0,0,0,0,0,0#3000400,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1900,1900,0,0,0,0,0,0#"}')#trible verfication
s3000500=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000500,1A:00:01:00:0F:00,2,4000,1672421700,0,60,900,1900,0,0,0,0,0,0#3000500,1A:00:01:00:0F:00,2,5000,1672422000,0,60,900,1900,0,0,0,0,0,0#"}')#trible verfication
s3000600=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000600,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1300,1900,0,0,0,0,0,0#3000600,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1300,1900,0,0,0,0,0,0#"}')#4 times verfication
s3000700=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000700,1A:00:01:00:0F:00,2,4000,1672421700,0,60,8200,1900,0,0,0,0,0,0#3000700,1A:00:01:00:0F:00,2,5000,1672422000,0,60,8200,1900,0,0,0,0,0,0#"}')#trible verfication
s3000800=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000800,1A:00:01:00:0F:00,2,4000,1672421700,0,60,9100,1900,0,0,0,0,0,0#3000800,1A:00:01:00:0F:00,2,5000,1672422000,0,60,9100,1900,0,0,0,0,0,0#"}')#4 times verfication
s3000900=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"3000900,1A:00:01:00:0F:00,2,4000,1672421700,0,60,1900,1900,0,0,0,0,0,0#3000900,1A:00:01:00:0F:00,2,5000,1672422000,0,60,1900,1900,0,0,0,0,0,0#"}')#trible verfication
s4000100=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"4000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,800,1900,0,0,0,0,0,0#4000100,1A:00:01:00:0F:00,2,5000,1672422000,0,4,1500,1500,0,0,0,0,0,0#"}')#5 times verfication

s6000100=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"6000100,1A:00:01:00:0F:00,1,4000,1672421700,0,60,1400,0,0,0,0,0,0#6000100,1A:00:01:00:0F:00,1,5000,1672422000,0,60,1300,0,0,0,0,0,0#"}')
s6000200=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"6000200,1A:00:01:00:0F:00,1,4000,1672421700,0,60,7100,0,0,0,0,0,0#6000200,1A:00:01:00:0F:00,1,5000,1672422000,0,60,7100,0,0,0,0,0,0#"}')
s6000300=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"6000300,1A:00:01:00:0F:00,1,4000,1672421700,0,60,2900,0,0,0,0,0,0#6000300,1A:00:01:00:0F:00,1,5000,1672422000,0,60,2900,0,0,0,0,0,0#"}')
s6000400=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"6000400,1A:00:01:00:0F:00,1,4000,1672421700,0,60,2900,0,0,0,0,0,0#6000400,1A:00:01:00:0F:00,1,5000,1672422000,0,100,4000,0,0,0,0,0,0#"}')

#print(json.loads(s1000600))
'''def gateway_start():
    return ggbw100.input_data(startup)
gateway_start()
def gateway_health():
    return ggbw100.input_data(startup)
gateway_health()
def gateway_config():
    return ggbw100.input_data(set_ble_sensors)
gateway_config()'''
dat=[s1000100,
s1000200,
s1000300,
s1000400,
s1000500,
s1000600,
s1000700,
s1000800,
s1000900,
s2000100,
s2000200,
s2000300,
s2000400,
s2000500,
s2000600,
s2000700,
s2000800,
s2000900,
s3000100,
s3000200,
s3000300,
s3000400,
s3000500,
s3000600,
s3000700,
s3000800,
s3000900,
s4000100]
h=[s6000100,s6000200,s6000300,s6000400]
import time
samples=json.loads('{"evt":"SAMPLES","gateway_id":"67010B0007","packet_number":5949,"utc_time":1671165370,"access_token":"asdfghjklasdfghjk","signal_strength":-16,"comm_mode":"cellular","powered_by":"mains","battery":96,"Scanner":1,"sensor_data":"9000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,5000,10000,0,0,0,0,0,0#9000100,1A:00:01:00:0F:00,2,4000,1672421700,0,60,5000,10000,0,0,0,0,0,0#"}')# 
from pymongo import MongoClient

def o(data):
    db=MongoClient()
    dmn=db['Sensors_Data']
    col=dmn['device_shadows']
    find_database_data=col.find()
    get_database_data=[]
    for t in find_database_data:
        get_database_data.append(t)

    Ble_TH_Sensor_Data_Processing(json.loads(data),get_database_data)
    One_Wire_Temperature_Sensor_Data_Processing(json.loads(data),get_database_data)
    Door_Sensor_Data_Processing(json.loads(data),get_database_data)
    #Get_Ble_TH_Sensor_Duplicate_Data(json.loads(data))
    #Get_Door_Sensor_Duplicate_Data(json.loads(data))
    #Get_One_Wire_Temperature_Sensor_Duplicate_Data(json.loads(data))
   

#duplicate samples

#th_is_duplicate()
#th_data()
# {"00100":[{},{},{},{},{},{},{},{}],"00101":[{},{},{}]}
''' 
duplicate_sensosrs ={
    "0100301":10
}'''
    

