import datetime
from datetime import datetime
from bin.get_data import Ble_TH_Data,Ble_TH_Duplicate_Data,get_sensor_notification_data,device_logs_data
import pytz
import calendar      

class  Notification_Alert_Processing:
    
    def __init__(self,sensor_data,database_data):
        self.data=sensor_data
        
        self.get_database_data=database_data 
        #print(self.data)
        #print(self.get_database_data)
        self.get_notification_sensor_ids=[]
        
        for j in self.get_database_data:
            if 'notification' in j.keys():
                if j['notification']!=None and j['product_code'].lower()=="BLE_TH".lower():
                    self.get_notification_sensor_ids.append(j['_id']) 
        
        for u in self.data:
            if str(u['sensor_id']) in self.get_notification_sensor_ids:
                
                for h in database_data:
                    if str(u['sensor_id'])==h['_id']:
                        my_time = datetime.now(pytz.timezone(h['notification']['timezone_id']))
                        
                        end_time=(h['notification']['time']['start']).split(':')
                        
                        start_time=h['notification']['time']['start'][0:5].split(':')
                        
                        s_time_to_int=[int(x) for x in start_time]
                        
                        hour=int(my_time.strftime("%H"))
                        minute=int(my_time.strftime("%M"))
                        
                        start_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),s_time_to_int[0],s_time_to_int[1])
                        start_time_to_utc=calendar.timegm(start_time.timetuple())
                        
                        end_time=h['notification']['time']['end'].split(':')
                        e_time_to_int=[int(x) for x in end_time]
                        e_hour=int(end_time[0])
                        e_minute=int(end_time[1])
                        e_second=int(end_time[2])
                        
                        ending_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),e_hour,e_minute,e_second)
                        ending_time_to_utc=calendar.timegm(ending_time.timetuple())
                        
                        present_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),hour,minute)
                        present_time_to_utc=calendar.timegm(present_time.timetuple())
                        actions=[['TEMPERATURE_LOW'],['TEMPERATURE_HIGH'],sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH']),['HUMIDITY_LOW'],['HUMIDITY_HIGH'],sorted(['HUMIDITY_LOW','HUMIDITY_HIGH']),['BATTERY_LOW'],sorted(['TEMPERATURE_LOW','HUMIDITY_LOW']),sorted(['TEMPERATURE_LOW','HUMIDITY_HIGH']),sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH']),sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW']),sorted(['TEMPERATURE_HIGH','HUMIDITY_HIGH']),sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_HIGH']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH']),sorted(['TEMPERATURE_LOW','BATTERY_LOW']),sorted(['TEMPERATURE_HIGH','BATTERY_LOW']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','BATTERY_LOW']),sorted(['HUMIDITY_LOW','BATTERY_LOW']),sorted(['HUMIDITY_HIGH','BATTERY_LOW']),sorted(['HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']),sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','BATTERY_LOW']),sorted(['TEMPERATURE_LOW','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']),sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW']),sorted(['TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','BATTERY_LOW']),sorted(['TEMPERATURE_LOW','TEMPERATURE_HIGH','HUMIDITY_LOW','HUMIDITY_HIGH','BATTERY_LOW'])]
                        t_k={"TEMPERATURE_LOW":['temperature','min'],"TEMPERATURE_HIGH":['temperature','max'],"HUMIDITY_LOW":['humidity','min'],"HUMIDITY_HIGH":['humidity','max'],"BATTERY_LOW":['battery','min']}
                        my_date = datetime.now(pytz.timezone(h['notification']['timezone_id']))
                        
                        
                        for q in h['notification']['days']:
                            if q==str(my_date.strftime("%A"))[0:3]:
                                
                                if present_time_to_utc>=start_time_to_utc and present_time_to_utc<=ending_time_to_utc and h['last_alert_at']==None:
                                    if sorted(h['notification']['action']) in actions:
                                        for k in h['notification']['action']:
                                            if k.endswith("LOW"):
                                                if float(u['payload'][str(t_k[k][0])])<float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])]):
                                                    
                                                    def forward_notification_data():
                                                        shadow_data={'_id':str(u['sensor_id']),'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}
                                                        device_alerts={'device_id':u['sensor_id'],'gateway_id':u['gateway_id'],'group_id':h['group_id'],'solution_id':h['solution_id'],'display_name':'BLE-T','action_type':h['notification']['action'],'payload':{k:{'current_value':u['payload'][str(t_k[k][0])],'compare_value':float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])])}},'timestamp':h['timestamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':u['sensor_type'],"notify_to":h['notification']['emails'],'description':"","__v":0}
                                                        return get_sensor_notification_data(shadow_data,device_alerts)
                                                    forward_notification_data()
                                                    print('firing the 1st time alert ',u['sensor_id'])
                                                    break
                                            elif k.endswith("HIGH"):
                                                if float(u['payload'][str(t_k[k][0])])>float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])]):       
                                                    @staticmethod
                                                    def forward_notification_data():
                                                        shadow_data={'_id':str(u['sensor_id']),'last_alert_at':my_time.strftime("%H:%M"),'is_alert':False}
                                                        device_alerts={'device_id':u['sensor_id'],'gateway_id':u['gateway_id'],'group_id':h['group_id'],'solution_id':h['solution_id'],'display_name':'BLE-T','action_type':h['notification']['action'],'payload':{k:{'current_value':u['payload'][str(t_k[k][0])],'compare_value':float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])])}},'timestamp':h['timestamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':u['sensor_type'],"notify_to":h['notification']['emails'],'description':"","__v":0}
                                                        return get_sensor_notification_data(shadow_data,device_alerts)
                                                    forward_notification_data()
                                                    print('firing the 1st time alert ',u['sensor_id'])
                                                    break
                                    else:
                                        print('invalid action')
                                elif present_time_to_utc>=start_time_to_utc and present_time_to_utc<=ending_time_to_utc and h['last_alert_at']!=None:
                                    intervel_time=int(h['notification']['intervel_value'])
                                    last_alert_at=h['last_alert_at'].split(':')
                                    last_time_to_int=[int(x) for x in last_alert_at]
                                    last_time_hour=int(last_time_to_int[0])
                                    last_time_minue_minute=int(last_time_to_int[1])
                                    last_time=datetime(int(my_time.strftime("%Y")),int(my_time.strftime('%m')),int(my_time.strftime('%d')),last_time_hour,last_time_minue_minute)
                                    last_time_to_utc=calendar.timegm(last_time.timetuple())
                                    if (abs(present_time_to_utc-last_time_to_utc)//60)>=intervel_time:
                                        
                                        if sorted(h['notification']['action']) in actions:
                                            
                                            for k in h['notification']['action']:
                                                if k.endswith("LOW"):
                                                    if float(u['payload'][str(t_k[k][0])])<float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])]):
                                                        @staticmethod
                                                        def forward_notification_data():
                                                            shadow_data={'_id':str(u['sensor_id']),'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}
                                                            device_alerts={'device_id':u['sensor_id'],'gateway_id':u['gateway_id'],'group_id':h['group_id'],'solution_id':h['solution_id'],'display_name':'BLE-T','action_type':h['notification']['action'],'payload':{k:{'current_value':u['payload'][str(t_k[k][0])],'compare_value':float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])])}},'timestamp':h['timestamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':u['sensor_type'],"notify_to":h['notification']['emails'],'description':"","__v":0}
                                                            return get_sensor_notification_data(shadow_data,device_alerts)
                                                        forward_notification_data()
                                                     
                                                        print('firing the 2nd time alert',u['sensor_id'],last_time_to_int)
                                                        break
                                                elif k.endswith("HIGH"):
                                                    if float(u['payload'][str(t_k[k][0])])>float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])]):       
                                                        
                                                        @staticmethod
                                                        def forward_notification_data():
                                                            shadow_data={'_id':str(u['sensor_id']),'last_alert_at':my_time.strftime("%H:%M"),'is_alert':True}
                                                            device_alerts={'device_id':u['sensor_id'],'gateway_id':u['gateway_id'],'group_id':h['group_id'],'solution_id':h['solution_id'],'display_name':'BLE-T','action_type':h['notification']['action'],'payload':{k:{'current_value':u['payload'][str(t_k[k][0])],'compare_value':float(h['configuration_params'][str(t_k[k][0])][str(t_k[k][1])])}},'timestamp':h['timestamp'],'created_at':my_time.strftime('%d-%m-%Y %H:%M'),'sensor_type':u['sensor_type'],"notify_to":h['notification']['emails'],'description':"","__v":0}
                                                            return get_sensor_notification_data(shadow_data,device_alerts)
                                                        forward_notification_data()
                                                        print('firing the 2nd time alert',u['sensor_id'],last_time_to_int)
                                                        break
                                        else:
                                            print('fail')                
                                        #2nd alert
                                    else:
                                        
                                        print('wait for alert time',u['sensor_id'])
                                else:
                                    print('wait for start time or alert time overed')
                                    def forward_notification_data():
                                        shadow_data={'_id':str(u['sensor_id']),'last_alert_at':None,'is_alert':False}
                                        return get_sensor_notification_data(shadow_data,None)
                                    forward_notification_data()
            else:
                #print("new sensor",u)                
                pass           
                            
class Temperature_Humidity_Sensor:
  
    def get_sensor_data(sensor_data,db_data):
        ord_data=[]
        for g in sensor_data:
            if g not in ord_data:
                ord_data.append(g)
        if len(ord_data)>0:
            for x in range(len(ord_data)):
                ord_data[x].update({'payload':{'temperature':ord_data[x]['temperature'],'humidity':ord_data[x]['humidity'],'battery':ord_data[x]['battery_percentage']}})
                ord_data[x].update({'gateway_id':ord_data[x]['gateway_info']['gateway_id']})
                ord_data[x].pop('gateway_info')
                ord_data[x].pop('temperature')
                ord_data[x].pop('humidity')
                ord_data[x].pop('battery_percentage')

            return Ble_TH_Data(ord_data),Notification_Alert_Processing(ord_data,db_data)
        else:
            print('No Data Found')
class Ble_TH_Sensor_Data_Processing():
    def __init__(self,data,db_data):
        
        self.data=data
        #gateway parameters
        class Gateway_Data(Ble_TH_Sensor_Data_Processing):
            def __init__(self):
                for validate in data:
                    if data[validate]=='':
                        raise ValueError('value not found for showing key : '.title(),validate)
                else:
                    self.gateway_id=data['gateway_id']
                    self.gateway_packet_number=int(data["packet_number"])
                    self.gateway_timestamp=str(datetime.utcfromtimestamp(int(data["utc_time"])))
                    self.gateway_access_token=data["access_token"]
                    self.gateway_signal_strength=int(data["signal_strength"])
                    self.gateway_comm_mode=data["comm_mode"]
                    self.gateway_powered_by=data["powered_by"]
                    self.gateway_battery=int(data["battery"])
                
        #sensor parameters
        
        self.sensor_data=self.data["sensor_data"].split("#")
        self.sensor_data.pop()
        
        self.final_sensor_data=[]
        
        count=0
        self.sensor_type=[]
        for xx in self.sensor_data:
            self.sensor_type.append(xx.split(","))
        for lll in self.sensor_type:
            #try:
                if lll[2]=='2':
                    if int(len(lll))==15:
                        self.ble_th_sensor_data_titles=['sensor_id','mac_id','sensor_type','packet_number','timestamp','reserved_packet','battery_percentage','temperature','humidity']
                        a='sensor '
                        count+=1
                        t={a+str(count):{key:value for key,value in zip(self.ble_th_sensor_data_titles,lll)}}
                        self.final_sensor_data.append(t)
                    else:
                        raise Exception('in temperature and humidity sensor some data is missing from incoming data data or not a valid data'.title())
                elif lll[2]=='1':
                    pass
                elif lll[2]=='8':
                    pass
                else:
                    raise Exception('entered sensor type not matching with availble pre-defined sensors type or some data is missing from incoming data'.title(),'entered sensor type is : '.title(),lll[2])
            #except:
                #raise Exception('enter the valid data,input data is not valid',self.data)
        #print(self.final_sensor_data)
        #data converstion
        for q in self.final_sensor_data:
            for j in q:
                for l in q[j]:
                    if q[j][l].isdigit():
                        if l=='temperature':
                            q[j].update({l:int(q[j][l])/100})
                        elif l=='humidity':
                            q[j].update({l:int(q[j][l])/100})
                        elif l=='timestamp':
                            q[j].update({l:str(datetime.utcfromtimestamp(int(q[j][l])))})
                        else:
                            q[j].update({l:int(q[j][l])})
                    else:
                        if l=="temperature":
                            q[j].update({l:int(q[j][l])/100})
                        elif l=="humidity":
                            q[j].update({l:int(q[j][l])/100})
        #print(self.final_sensor_data)
        @staticmethod
        def proccess_data_for_forward_to_the_individual_sensors():
            temperature_humidity_sensor_data=[]
            x=Gateway_Data().__dict__
            for qq in self.final_sensor_data:
                for z in qq:
                    if qq[z]['sensor_type']==2:#ble temperature and humidity sensor
                        temperature_humidity_sensor_data.append(qq[z])
            if len(temperature_humidity_sensor_data)>=0:
                for w in range(len(temperature_humidity_sensor_data)):
                    gg=temperature_humidity_sensor_data[w].update({'gateway_info':{hh:x[hh] for hh in x}})
                
                #get latest sensor information
                data=[]
                for x in temperature_humidity_sensor_data:
                    q=[z for z in temperature_humidity_sensor_data if x['sensor_id']==z['sensor_id']]
                    data.append(q)
                ord_data=[]
                for j in data:
                    if j not in ord_data:
                        ord_data.append(j)
                for h in range(len(ord_data)):
                    
                    for e in range(len(ord_data[h])):
                        a=datetime( int(ord_data[h][e]['timestamp'][:4]),int(ord_data[h][e]['timestamp'][5:7]),int(ord_data[h][e]['timestamp'][8:10]),int(ord_data[h][e]['timestamp'][11:13]),int(ord_data[h][e]['timestamp'][14:16]))
                        aa=calendar.timegm(a.timetuple())
                        ord_data[h][e].update({'timestamp':aa})
                k=[]
                for j in range(len(ord_data)):
                    d=[ord_data[j][y]['timestamp']for y in range(len(ord_data[j]))]
                    
                    k.append(ord_data[j][d.index(max(d))])
                for t in range(len(k)):
                    
                    k[t].update({'timestamp':str(datetime.utcfromtimestamp(k[t]['timestamp']))})
                device_logs_data(temperature_humidity_sensor_data)
                Temperature_Humidity_Sensor.get_sensor_data(k,db_data)

        proccess_data_for_forward_to_the_individual_sensors()
     

class Temperature_Humidity_Sensor_Duplicate_Data:
  
    def get_sensor_data(sensor_data):
        ord_data=[]
        for g in sensor_data:
            if g not in ord_data:
                ord_data.append(g)
        p=[]
        duplicate_data_by_sensor_id=[]
        total_duplicate_count=0
        for x in ord_data:
            if sensor_data.count(x)>1:
                total_duplicate_count+=sensor_data.count(x)-1
                m={str(x['sensor_id']):[x]*(sensor_data.count(x)-1)}
                for z in m.keys():
                    m[z][0].pop('sensor_id')
                    m[z][0].update({'gateway_id':m[z][0]['gateway_info']['gateway_id']})
                    m[z][0].pop('gateway_info')
                p.append(m)
        if len(p)>0:

            for q in p:
                for z in q:
                    #print(z,len(q[z]))
                    w={str(z):len(q[z])}
                    duplicate_data_by_sensor_id.append(w)

            return Ble_TH_Duplicate_Data(total_duplicate_count=total_duplicate_count,duplicate_data_by_sensor_id=duplicate_data_by_sensor_id,duplicate_data=p) 
        else:
            return Ble_TH_Duplicate_Data(NoDuplicateDataFound="")
 

class Get_Ble_TH_Sensor_Duplicate_Data():
    def __init__(self,data):
        
        self.data=data
        #gateway parameters
        class Gateway_Data(Get_Ble_TH_Sensor_Duplicate_Data):
            def __init__(self):
                for validate in data:
                    if data[validate]=='':
                        raise ValueError('value not found for showing key : '.title(),validate)
                else:
                    self.gateway_id=data['gateway_id']
                    self.gateway_packet_number=int(data["packet_number"])
                    self.gateway_timestamp=str(datetime.utcfromtimestamp(int(data["utc_time"])))
                    self.gateway_access_token=data["access_token"]
                    self.gateway_signal_strength=int(data["signal_strength"])
                    self.gateway_comm_mode=data["comm_mode"]
                    self.gateway_powered_by=data["powered_by"]
                    self.gateway_battery=int(data["battery"])
                
        #sensor parameters
        
        self.sensor_data=self.data["sensor_data"].split("#")
        self.sensor_data.pop()
        
        self.final_sensor_data=[]
        
        count=0
        self.sensor_type=[]
        for xx in self.sensor_data:
            self.sensor_type.append(xx.split(","))
        for lll in self.sensor_type:
            try:
                if lll[2]=='2':
                    if int(len(lll))==15:
                        self.door_sensor_data_titles=['sensor_id','mac_id','sensor_type','packet_number','timestamp','reserved_packet','battery_percentage','temperature','humidity']
                        a='sensor '
                        count+=1
                        t={a+str(count):{key:value for key,value in zip(self.door_sensor_data_titles,lll)}}
                        self.final_sensor_data.append(t)
                    else:
                        raise Exception('in temperature and humidity sensor some data is missing from incoming data data or not a valid data'.title())
                elif lll[2]=='1':
                    pass
                elif lll[2]=='8':
                    pass
                else:
                    raise Exception('entered sensor type not matching with availble pre-defined sensors type or some data is missing from incoming data'.title(),'entered value is : '.title(),lll[2])
            except:
                raise Exception('enter the valid data,input data is not valid',self.data)
        #print(self.final_sensor_data)
        #data converstion
        for q in self.final_sensor_data:
            for j in q:
                for l in q[j]:
                    if q[j][l].isdigit():
                        if l=='temperature':
                            q[j].update({l:int(q[j][l])/100})
                        elif l=='humidity':
                            q[j].update({l:int(q[j][l])/100})
                        elif l=='timestamp':
                            q[j].update({l:str(datetime.utcfromtimestamp(int(q[j][l])))})
                        else:
                            q[j].update({l:int(q[j][l])})
                    else:
                        if l=="temperature":
                            q[j].update({l:int(q[j][l])/100})
                        elif l=="humidity":
                            q[j].update({l:int(q[j][l])/100})
        #print(self.final_sensor_data)
        @staticmethod
        def proccess_data_for_forward_to_the_individual_sensors():
            temperature_humidity_sensor_data=[]
            x=Gateway_Data().__dict__
            for qq in self.final_sensor_data:
                for z in qq:
                    if qq[z]['sensor_type']==2:#ble temperature and humidity sensor
                        temperature_humidity_sensor_data.append(qq[z])
            if len(temperature_humidity_sensor_data)>=0:
                for w in range(len(temperature_humidity_sensor_data)):
                    gg=temperature_humidity_sensor_data[w].update({'gateway_info':{hh:x[hh] for hh in x}})
                
                Temperature_Humidity_Sensor_Duplicate_Data.get_sensor_data(temperature_humidity_sensor_data)

        proccess_data_for_forward_to_the_individual_sensors()
     