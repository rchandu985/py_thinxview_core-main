"""def data_pushing(**kwargs):
    print('from data pushing',kwargs['x'])
def time_processing(a):
    return data_pushing(x=a)
class k:
    def __init__(self):
        for j in range(1,10):    
            @staticmethod
            def test():
                return time_processing(j)
            test()    
o=k()

from datetime import timezone
from datetime import datetime

import pytz

#from thteading import Thread

p_time=datetime(2022,12,29,9,50,48)#1672309126
to_utc=int(p_time.timestamp())
print(to_utc)
a=datetime.utcfromtimestamp(1672309447)
#2022-12-29 09:50:48
print(a)"""
import datetime
import calendar      

a=[{'sensor_id': 1000700, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 888, 'time_stamp': '2022-12-29 05:00:10', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
   {'sensor_id': 1000300, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 13900, 'time_stamp': '2022-12-29 04:32:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
   {'sensor_id': 1000900, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 138250, 'time_stamp': '2022-12-29 04:35:48', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 30.0},
   {'sensor_id': 1000900, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 138280, 'time_stamp': '2022-12-29 04:50:48', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 30.0},
   {'sensor_id': 1000700, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 48940, 'time_stamp': '2022-12-29 02:27:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
    {'sensor_id': 1000200, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 48940, 'time_stamp': '2022-12-29 02:27:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
    {'sensor_id': 1000200, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 48945, 'time_stamp': '2022-12-29 03:45:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
    {'sensor_id': 1000700, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 13889, 'time_stamp': '2022-12-29 04:31:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0},
    {'sensor_id': 1000300, 'mac_id': '1A:00:01:00:0F:00', 'sensor_type': 1, 'packet_number': 13889, 'time_stamp': '2022-12-29 04:31:00', 'reserved_packet': 0, 'battery_percentage': 100, 'temperature': 20.0}]
data=[]
for x in a:
    q=[z for z in a if x['sensor_id']==z['sensor_id']]
    data.append(q)
ord_data=[]
for j in data:
    if j not in ord_data:
        ord_data.append(j)
for h in range(len(ord_data)):
    
    for e in range(len(ord_data[h])):
        a=datetime.datetime( int(ord_data[h][e]['time_stamp'][:4]),int(ord_data[h][e]['time_stamp'][5:7]),int(ord_data[h][e]['time_stamp'][8:10]),int(ord_data[h][e]['time_stamp'][11:13]),int(ord_data[h][e]['time_stamp'][14:16]))
        aa=calendar.timegm(a.timetuple())
        ord_data[h][e].update({'time_stamp':aa})
k=[]
for j in range(len(ord_data)):
    d=[ord_data[j][y]['time_stamp']for y in range(len(ord_data[j]))]
    
    k.append(ord_data[j][d.index(max(d))])
for t in range(len(k)):
    #1671161220
    k[t].update({'time_stamp':str(datetime.datetime.utcfromtimestamp(k[t]['time_stamp']))})
    
print(datetime.datetime.utcfromtimestamp(1672703999))

'''def firing_the_alert(**kwrgs):
    #print(kwrgs)
    db=MongoClient()
    dmn=db['Sensors_Data']
    alert=dmn['coldchain_device_alerts']
    my_time = datetime.now(pytz.timezone(kwrgs['time_zone']))
    database_sensor_ids=[]
    x=alert.find()
    for i in x:
        database_sensor_ids.append(i['device_id'])
    print("firing the alert ")
    if kwrgs['action'] == ['TEMPERATURE_LOW']:
        if kwrgs['sensor_id'] in database_sensor_ids:
            cursor = alert.update_one({'device_id':kwrgs['sensor_id']},{'$set':{'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_LOW':{'current_value':kwrgs['payload'],'compare_value':kwrgs['min_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']}})
            for i in x:
                database_sensor_ids.append(i['device_id'])
        else:
            alert.insert_one({'device_id':kwrgs['sensor_id'],'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_LOW':{'current_value':kwrgs['payload'],'compare_value':kwrgs['min_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']})
            for i in x:
                database_sensor_ids.append(i['device_id'])
    elif kwrgs['action'] == ['TEMPERATURE_HIGH']:
        if kwrgs['sensor_id'] in database_sensor_ids:
            cursor = alert.update_one({'device_id':kwrgs['sensor_id']},{'$set':{'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_HIGH':{'current_value':kwrgs['payload'],'compare_value':kwrgs['max_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']}})
            for i in x:
                database_sensor_ids.append(i['device_id'])
        else:
            alert.insert_one({'device_id':kwrgs['sensor_id'],'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_HIGH':{'current_value':kwrgs['payload'],'compare_value':kwrgs['max_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']})
            for i in x:
                database_sensor_ids.append(i['device_id'])
    elif sorted(kwrgs['action'])==sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH']):
        if kwrgs['sensor_id'] in database_sensor_ids:
            cursor = alert.update_one({'device_id':kwrgs['sensor_id']},{'$set':{'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_LOW':{'current_value':kwrgs['payload'],'compare_value':kwrgs['min_temperature']},'TEMPERATURE_HIGH':{'current_value':kwrgs['payload'],'compare_value':kwrgs['max_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']}})
            for i in x:
                database_sensor_ids.append(i['device_id'])
        else:
            alert.insert_one({'device_id':kwrgs['sensor_id'],'gateway_id':kwrgs['gateway_id'],'group_id':kwrgs['group_id'],'solution_id':kwrgs['solution_id'],'display_name':'BLE-T','action_type':kwrgs['action'],'payload':{'TEMPERATURE_LOW':{'current_value':kwrgs['payload'],'compare_value':kwrgs['min_temperature']},'TEMPERATURE_HIGH':{'current_value':kwrgs['payload'],'compare_value':kwrgs['max_temperature']}},'timestamp':kwrgs['time_stamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':kwrgs['sensor_type'],"notify_to":kwrgs['notify_to']})
            for i in x:
                database_sensor_ids.append(i['device_id'])
    else:
        print('invalid action'.title())
class Notification_Processing():
    def __init__(self,data):

        self.data=data
        self.db=MongoClient()
        self.dmn=self.db['Sensors_Data']
        self.col=self.dmn['device_shadows']
        self.find_database_data=self.col.find()
        self.get_database_data=[]
        self.get_notification_sensor_ids=[]
        for t in self.find_database_data:
            self.get_database_data.append(t)
        for j in range(len(self.get_database_data)):
            if self.get_database_data[j]['notification']!=None:
                self.h=self.col.find_one({'_id':self.get_database_data[j]['_id']})
                if self.h['product_code']=='BLE_T':
                    self.get_notification_sensor_ids.append(int(self.get_database_data[j]['_id']))
        #print(self.get_notification_sensor_ids)
        for u in self.data:
            if u['sensor_id'] in self.get_notification_sensor_ids:
                
                h=self.col.find_one({'_id':str(u['sensor_id'])})
                my_time = datetime.now(pytz.timezone(h['notification']['timezone_id']))
                end_time=(h['notification']['time']['start']).split(':')
                start_time=h['notification']['time']['start'][0:5].split(':')
                s_time_to_int=[int(x) for x in start_time]
                hour=int(my_time.strftime("%H"))
                minute=int(my_time.strftime("%M"))
                end_time=h['notification']['time']['end'].split(':')
                e_time_to_int=[int(x) for x in end_time]
                e_hour=int(my_time.strftime("%H"))
                e_minute=int(my_time.strftime("%M"))
                e_second=int(my_time.strftime("%S"))

                last_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),int(h['last_alert_at'][:2]),int(h['last_alert_at'][3:]))
                last_time_to_utc=calendar.timegm(last_time.timetuple())
                present_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),hour,minute)
                present_time_to_utc=calendar.timegm(present_time.timetuple())
                my_date = datetime.now(pytz.timezone(h['notification']['timezone_id']))
                for q in h['notification']['days']:
                    if q==str(my_date.strftime("%A"))[0:3]:
                        if h['notification']['action']==["TEMPERATURE_HIGH"]:
                            
                            if float(u['payload']['temperature'])>float(h['configuration_params']['temperature']['max']):
                                print('temperature matching')
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],max_temperature=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],max_temperature=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                            else:
                                print('temperature not matching')
                        elif h['notification']['action']==["TEMPERATURE_LOW"]:
                            if float(u['payload']['temperature'])<float(h['configuration_params']['temperature']['min']):
                                print('temperature matching',h['configuration_params']['temperature']['min'],u['payload']['temperature'])
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],min_temperature=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],min_temperature=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('temperature not matching')
                        elif sorted(h['notification']['action'])==sorted(["TEMPERATURE_LOW","TEMPERATURE_HIGH"]):
                            
                            if float(u['payload']['temperature'])<float(h['configuration_params']['temperature']['min']) or float(u['payload']['temperature'])>float(h['configuration_params']['temperature']['max']):
                                print('temperature matching',h['configuration_params']['temperature']['min'],u['payload']['temperature'])
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],min_temperature=h['configuration_params']['temperature']['min'],max_temperature=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['temperature'],min_temperature=h['configuration_params']['temperature']['min'],max_temperature=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                            else:
                                print('temperature not matching')
                        elif h['notification']['action']==["HUMIDITY_LOW"]:
                            if float(u['payload']['humidity'])<float(h['configuration_params']['humidity']['min']):
                                
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('humidity not matching')
                        elif h['notification']['action']==["HUMIDITY_HIGH"]:
                            if float(u['payload']['humidity'])>float(h['configuration_params']['humidity']['max']):
                                
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('humidity not matching')
                                
                        elif h['notification']['action']==["HUMIDITY_HIGH"]:
                            if float(u['payload']['humidity'])>float(h['configuration_params']['humidity']['max']):
                                
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('humidity not matching')
                    elif sorted(h['notification']['action'])==sorted(["HUMIDITY_LOW","HUMIDITY_HIGH"]):
            
                        if float(u['payload']['humidity'])<float(h['configuration_params']['humidity']['min']) or float(u['payload']['humidity'])>float(h['configuration_params']['humidity']['max']):
                                #print('temperature matching',h['configuration_params']['temperature']['min'],u['payload']['temperature'])
                            if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],max_temperature=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                                        
                                else:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                    print('alert time overed')
                            elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                    if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_temperature=h['configuration_params']['humidity']['min'],max_temperature=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                            else:
                                print('humidity not matching')
                    elif h['notification']['action']==["BATTERY_LOW"]:
                            if float(u['payload']['battery'])<float(h['configuration_params']['battery']['min']):
                                
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['battery'],min_battery=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],min_battery=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('batatery value  not matching')
                    elif h['notification']['action']==["BATTERY_HIGH"]:
                            if float(u['payload']['battery'])<float(h['configuration_params']['battery']['max']):
                                
                                if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['battery'],max_battery=h['configuration_params']['battery']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                                        
                                    else:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                        print('alert time overed')
                                elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                    if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                        if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                            self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                            @staticmethod
                                            def send_data():
                                                return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['humidity'],max_battery=h['configuration_params']['battery']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                            send_data()
                                        
                                    else:
                                        print(hour,s_time_to_int[0],int(h['last_alert_at'][3:])+h['notification']['intervel_value'])
                                else:
                                    print('wait for start time')
                            else:
                                print('battery value not matching')
                    elif sorted(h['notification']['action'])==sorted(["BATTERTY_LOW","BATTERY_HIGH"]):
            
                        if float(u['payload']['battery'])<float(h['configuration_params']['battery']['min']) or float(u['payload']['battery'])>float(h['configuration_params']['battery']['max']):
                                #print('temperature matching',h['configuration_params']['temperature']['min'],u['payload']['temperature'])
                            if hour>=s_time_to_int[0] and minute>=s_time_to_int[1] and h['last_alert_at']==None:
                                if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['battery'],min_battery=h['configuration_params']['battery']['min'],max_battery=h['configuration_params']['battery']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                                        
                                else:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':None}})
                                    print('alert time overed')
                            elif hour>=s_time_to_int[0] and h['last_alert_at']!=None:
                                    #after first alert it will be updated
                                if e_hour<=e_time_to_int[0] and e_minute<=e_time_to_int[1] and e_second<=e_time_to_int[2]:
                                        #d = now.strftime("%d/%m/%Y, %H:%M:%S")
                                        
                                    if abs((last_time_to_utc-present_time_to_utc))/60>=h['notification']['intervel_value']:
                                        self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}})
                                        @staticmethod
                                        def send_data():
                                            return firing_the_alert(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload=u['payload']['battery'],min_battery=h['configuration_params']['battery']['min'],max_battery=h['configuration_params']['battery']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                        send_data()
                            else:
                                print('battery values not matching')
'''
from pymongo import MongoClient
db=MongoClient()
dmn=db['Sensors_Data']
alert=dmn['test']
for x in range(1,5):
    alert.insert_one({str(x):x})
'''   
Temperature_Low=[['TEMPERATURE_LOW']]
Temperature_High=[['TEMPERATURE_HIGH']]
Temperatur_High_Low=[['TEMPERATURE_LOW','TEMPERATURE_HIGH']]

Humidity_Low=[['HUMIDITY_LOW']]
Humidity_High=[['HUMIDITY_HIGH']]
Humidity_High_Low=[['HUMIDITY_LOW','HUMIDITY_HIGH']]

Battery_Low=[['BATTERY_LOW']]
Battery_High=[['BATTERY_HIGH']]
Battery_High_Low=[['BATTERY_LOW','BATTERY_HIGH']]


t_h_min=[['TEMPERATURE_LOW','HUMIDITY_LOW'],['TEMPERATURE_LOW','HUMIDITY_HIGH'],['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH']]
t_h_max=[['TEMPERATURE_HIGH','HUMIDITY_LOW'],['TEMPERATURE_HIGH','HUMIDITY_HIGH'],['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']]
t_h_min_max=[['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']]

t_b_min=[['TEMPERATURE_LOW','BATTERY_LOW'],['TEMPERATURE_LOW''BATTERY_HIGH'],['TEMPERATURE_LOW','BATTERY_HIGH','BATTERY_LOW']]
t_b_max=[['TEMPERATURE_HIGH','BATTERY_LOW'],['TEMPERATURE_HIGH','BATTERY_HIGH'],['TEMPERATURE_HIGH','BATTERY_LOW','BATTERY_HIGH']]
t_b_min_max=[['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW','BATTERY_HIGH']]

th_b_min=[['HUMIDITY_LOW','BATTERY_LOW'],['HUMIDITY_LOW','BATTERY_HIGH'],['HUMIDITY_LOW','BATTERY_LOW','BATTERY_HIGH']]
th_b_max=[['HUMIDITY_HIGH','BATTERY_LOW'],['HUMIDITY_HIGH','BATTERY_HIGH'],['HUMIDITY_HIGH','BATTERY_LOW','BATTERY_HIGH']]
th_b_min_max=[['HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW'],['HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_HIGH'],['HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW','BATTERY_HIGH']]

t_h_b_min=[['TEMPERATURE_LOW','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATURE_LOW','HUMIDITY_HIGH','BATTERY_HIGH'],['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW','BATTERY_HIGH']]
t_h_b_max=[['TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATURE_HIGH','HUMIDITY_HIGH','BATTERY_HIGH'],['TEMPERATUR_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW','BATTERY_HIGH']]
t_h_b_min_max=[['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH','BATTERY_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW','BATTERY_HIGH']]
'''
a='''if h['notification']['action']==['TEMPERATURE_LOW']:
                                if u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_LOW':u['payload']['temperature']},temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==['TEMPERATURE_HIGH']:
                                if u['payload']['temperature']>h['configuration_params']['temperature']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature']},temperature_low=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH']):
                                if u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['temperature']<=h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature']},temperature_low=h['configuration_params']['temperature']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==['HUMIDITY_LOW']:
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_LOW':u['payload']['humidity']},temperature_low=h['configuration_params']['humidity']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==['HUMIDITY_HIGH']:
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity']},temperature_low=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==sorted(['HUMIDITY_LOW','HUMIDITY_HIGH']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['humidity']<h['configuration_params']['humidity']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity']},humidity_low=h['configuration_params']['humidity']['min'],humidity_high=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif h['notification']['action']==['BATTERY_LOW']:
                                if u['battery_percentage']>h['configuration_params']['battery']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'BATTERY_LOW':u['battery_percentage']},temperature_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            elif h['notification']['action']==sorted(['TEMPERATURE_LOW','HUMIDITY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity']},humidity_low=h['configuration_params']['humidity']['min'],humidity_high=h['configuration_params']['humidity']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['HUMIDITY_HIGH','BATTERY_LOW']
                            elif h['notification']['action']==sorted(['HUMIDITY_HIGH','BATTERY_LOW']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['battery_percantage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'BATTERY_LOW':u['battery_percantage']},humidity_high=h['configuration_params']['humidity']['max'],battery_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif h['notification']['action']==sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_LOW':u['payload']['humidity'],'TEMPERATURE_HIGH':u['payload']['humidity']},humidity_low=h['configuration_params']['humidity']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif h['notification']['action']==sorted(['TEMPERATURE_LOW','HUMIDITY_HIGH']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database(sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity']},humidity_ax=h['configuration_params']['humidity']['max'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif sorted(h['notification']['action']) == sorted(['HUMIDITY_LOW','BATTERY_LOW']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['min'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_LOW':u['payload']['humidity'],'BATTERY_LOW':u['battery_percentage']},humidity_low=h['configuration_params']['humidity']['min'],battery_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_HIGH','HUMIDITY_HIGH']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] and u['temperature']>h['configuration_params']['temperature']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'TEMPERATURE_HIGH':u['temperature']},humidity_high=h['configuration_params']['humidity']['max'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','BATTERY_LOW']):
                                if u['payload']['temperature']<h['configuration_params']['temperature']['min'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_LOW':u['payload']['temperature'],'BATTERY_LOW':u['battery_percentage']},temperature_low=h['configuration_params']['temperature']['min'],battery_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_HIGH','BATTERY_LOW']):
                                if u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature'],'BATTERY_LOW':u['battery_percentage']},temperature_high=h['configuration_params']['temperature']['max'],battery_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            elif sorted(h['notification']['action']) == sorted(['HUMIDITY_HIGH', 'BATTERY_LOW']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'BATTERY_LOW':u['battery_percentage']},humidity_high=h['configuration_params']['humidity']['max'],battery_low=h['configuration_params']['battery']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'HUMIDITY_LOW':u['humidity'],'TEMPERATURE_LOW':u['temperature']},humidity_high=h['configuration_params']['temperature']['max'],humidity_low=h['configuration_params']['temperature']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'HUMIDITY_HIGH']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']):
                                if u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'HUMIDITY_LOW':u['humidity'],'TEMPERATURE_HIGH':u['temperature']},humidity_high=h['configuration_params']['temperature']['max'],humidity_low=h['configuration_params']['temperature']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW', 'TEMPERATURE_HIGH', 'HUMIDITY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW']):
                                if u['payload']['temperature']<h['configuration_params']['temperature']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['humidity']<h['configuration_params']['humidity']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_LOW':u['payload']['humidity'],'TEMPERATURE_LOW':u['temperature'],'TEMPERATURE_HIGH':u['temperature']},temperature_high=h['configuration_params']['temperature']['max'],humidity_low=h['configuration_params']['humidity']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH']):
                                if u['payload']['temperature']<h['configuration_params']['temperature']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['humidity']<h['configuration_params']['humidity']['max']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'HUMIDITY_HIGH':u['payload']['humidity'],'TEMPERATURE_LOW':u['temperature'],'TEMPERATURE_HIGH':u['temperature']},temperature_high=h['configuration_params']['temperature']['max'],humidity_high=h['configuration_params']['humidity']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            
                            #['TEMPERATURE_LOW', 'TEMPERATURE_HIGH', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW']):
                                if u['payload']['temperature']<h['configuration_params']['temperature']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'BATTERY_LOW':u['payload']['battery_percantage'],'TEMPERATURE_LOW':u['temperature'],'TEMPERATURE_HIGH':u['temperature']},temperature_high=h['configuration_params']['temperature']['max'],battery_low=h['configuration_params']['battery']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['HUMIDITY_LOW', 'HUMIDITY_HIGH', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'BATTERY_LOW':u['payload']['battery_percantage'],'TEMPERATURE_LOW':u['temperature'],'TEMPERATURE_HIGH':u['temperature']},temperature_high=h['configuration_params']['temperature']['max'],battery_low=h['configuration_params']['battery']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW', 'HUMIDITY_LOW', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']<h['configuration_params']['temperature']['min'] or u['payload']['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'BATTERY_LOW':u['payload']['battery_percantage'],'TEMPERATURE_LOW':u['temperature'],'HUMIDITY_LOW':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],battery_low=h['configuration_params']['battery']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'BATTERY_LOW':u['payload']['battery_percantage'],'TEMPERATURE_HIGH':u['temperature'],'HUMIDITY_LOW':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],battery_low=h['configuration_params']['battery']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                        #['TEMPERATURE_LOW', 'TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'HUMIDITY_HIGH']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_LOW':u['payload']['temperature'],'TEMPERATURE_HIGH':u['temperature'],'HUMIDITY_LOW':u['humidity'],'HUMIDITY_HIGH':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],humidityh_high=h['configuration_params']['humidity']['max'],temperature_high=h['configuration_params']['temperature']['max'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW', 'HUMIDITY_LOW', 'HUMIDITY_HIGH', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['battery_percantage']>h['configuration_params']['battery']['max'] or u['payload']['temperature']<h['configuration_params']['temperature']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_LOW':u['payload']['temperature'],'BATTEREY_LOW':u['battery_percentage'],'HUMIDITY_LOW':u['humidity'],'HUMIDITY_HIGH':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],humidityh_high=h['configuration_params']['humidity']['max'],battery_low=h['configuration_params']['battery']['min'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'HUMIDITY_HIGH', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['battery_percantage']>h['configuration_params']['battery']['max'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature'],'BATTEREY_LOW':u['battery_percentage'],'HUMIDITY_LOW':u['humidity'],'HUMIDITY_HIGH':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],humidityh_high=h['configuration_params']['humidity']['max'],battery_low=h['configuration_params']['battery']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW', 'TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['temperature']<h['configuration_params']['temperature']['max'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature'],'BATTEREY_LOW':u['battery_percentage'],'HUMIDITY_LOW':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],battery_low=h['configuration_params']['battery']['min'],temperature_high=h['configuration_params']['temperature']['max'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()
                            #['TEMPERATURE_LOW', 'TEMPERATURE_HIGH', 'HUMIDITY_LOW', 'HUMIDITY_HIGH', 'BATTERY_LOW']
                            elif sorted(h['notification']['action']) == sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']):
                                if u['payload']['humidity']<h['configuration_params']['humidity']['min'] or u['payload']['humidity']>h['configuration_params']['humidity']['max'] or u['payload']['temperature']>h['configuration_params']['temperature']['max'] or u['payload']['temperature']<h['configuration_params']['temperature']['max'] or u['battery_percentage']<h['configuration_params']['battery']['min']:
                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}})
                                    @staticmethod
                                    def send_data():
                                        return push_alert_to_the_database( sensor_id=u['sensor_id'],gateway_id=u['gateway_id'],group_id=h['group_id'],solution_id=h['solution_id'],action=h['notification']['action'],payload={'TEMPERATURE_HIGH':u['payload']['temperature'],'TEMPERATURE_LOW':u['payload']['temperature'],'BATTEREY_LOW':u['battery_percentage'],'HUMIDITY_LOW':u['humidity']},humidity_low=h['configuration_params']['humidity']['min'],battery_low=h['configuration_params']['battery']['min'],temperature_high=h['configuration_params']['temperature']['max'],temperature_low=h['configuration_params']['temperature']['min'],time_stamp=h['timestamp'],sensor_type=u['sensor_type'],time_zone=h['notification']['timezone_id'],notify_to=h['notification']['emails'])
                                    send_data()'''
actions=[['TEMPERATURE_LOW'],['TEMPERATURE_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH'],['HUMIDITY_LOW'],['HUMIDITY_HIGH'],['HUMIDITY_LOW','HUMIDITY_HIGH'],['BATTERY_LOW'],['TEMPERATURE_LOW','HUMIDITY_LOW'], ['TEMPERATURE_LOW','HUMIDITY_HIGH'],['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH'],['TEMPERATURE_HIGH','HUMIDITY_LOW'],['TEMPERATURE_HIGH','HUMIDITY_HIGH'],['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH'],['TEMPERATURE_LOW','BATTERY_LOW'],['TEMPERATURE_HIGH','BATTERY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW'],['HUMIDITY_LOW','BATTERY_LOW'],['HUMIDITY_HIGH','BATTERY_LOW'],['HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW'],['TEMPERATURE_LOW','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW'],['TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATUR_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW'],['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']]
y=[]
n=[]
for k in actions:
    if a in k:
        y.append(k)
    else:
        n.append(k)
print(n,len(n))