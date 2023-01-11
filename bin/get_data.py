from pymongo import MongoClient
#                cursor = device_logs.update_one({'sensor_id' : k['sensor_id'],'sensor_type' : k['sensor_type'],'mac_id':k['mac_id']},{'$set':{'battery_percentage':k['battery_percentage'],'gateway_id':k['gateway_id'],'packet_number':k['packet_number'],'battery_percentage':k['battery_percentage'],'timestamp':k['timestamp'],'reserved_packet':k['reserved_packet'],'payload':{'door_status':k['payload']['door_status']}}})
#                cursor = device_logs.update_one({'sensor_id' : k['sensor_id'],'sensor_type' : k['sensor_type'],'mac_id':k['mac_id']},{'$set':{'battery_percentage':k['battery_percentage'],'gateway_id':k['gateway_id'],'packet_number':k['packet_number'],'battery_percentage':k['battery_percentage'],'timestamp':k['timestamp'],'reserved_packet':k['reserved_packet'],'payload':{'temperature':k['payload']['temperature'],'humidity':k['payload']['humidity']}}})
# cursor = device_logs.update_one({'sensor_id' : k['sensor_id'],'sensor_type' : k['sensor_type'],'mac_id':k['mac_id']},{'$set':{'battery_percentage':k['battery_percentage'],'gateway_id':k['gateway_id'],'packet_number':k['packet_number'],'battery_percentage':k['battery_percentage'],'timestamp':k['timestamp'],'reserved_packet':k['reserved_packet'],'payload':{'temperature':k['payload']['temperature']}}})
db=MongoClient()
table_name=db['Sensors_Data']
device_logs=table_name['device_logs']
device_alerts=table_name['coldchain_device_alerts']
device_shadows=table_name['device_shadows']


x=device_logs.find()

def Ble_Door_Data(ord_data):
    z=device_shadows.find()
    
    
    database_sensor_ids=[]
    for x in z:
        g=list(x.keys())
        if 'product_code' in g:
            if x['product_code']=='BLE_DR':
                database_sensor_ids.append(str(x['_id']))
    
    for j in ord_data:
        if str(j['sensor_id']) in database_sensor_ids:
            device_shadows.update_one({'_id':str(j['sensor_id'])},{'$set':{'timestamp':j['timestamp'],'payload':j['payload']}})
        else:
            #print('from ble t',str(j['sensor_id']))
            device_shadows.insert_one({'_id':str(j['sensor_id']),'display_name':str(j['sensor_id']),'product_code':'BLE_DR','shared_key':None,'timestamp':j['timestamp'],'payload':j['payload'],'alert_stage':0,'buzzer_state':0})
            
            for w in z:
                if w['product_code']=="BLE_DR":
                    database_sensor_ids.append(str(w['_id']))
def Ble_TH_Data(ord_data):
    z=device_shadows.find()
    
    #device_logs.insert_one(k)
    database_sensor_ids=[]
    for x in z:
        g=list(x.keys())
        if 'product_code' in g:
            if x['product_code']=='BLE_TH':
                database_sensor_ids.append(str(x['_id']))
   
    for j in ord_data:
        if str(j['sensor_id']) in database_sensor_ids:
            device_shadows.update_one({'_id':str(j['sensor_id'])},{'$set':{'timestamp':j['timestamp'],'payload':j['payload']}})
        else:
            #print('from ble t',str(j['sensor_id']))
            device_shadows.insert_one({'_id':str(j['sensor_id']),'display_name':str(j['sensor_id']),'product_code':'BLE_T','shared_key':None,'timestamp':j['timestamp'],'payload':j['payload'],'alert_stage':0,'buzzer_state':0})
            for w in z:
                if w['product_code']=="BLE_TH":
                    database_sensor_ids.append(str(w['_id']))
    
def Ble_Temperature_Data(ord_data):
    z=device_shadows.find()
    
    #device_logs.insert_one(k)
    database_sensor_ids=[]
    for x in z:
        g=list(x.keys())
        if 'product_code' in g:
            if x['product_code']=='BLE_T':
                database_sensor_ids.append(str(x['_id']))

    for j in ord_data:
        if str(j['sensor_id']) in database_sensor_ids:
            device_shadows.update_one({'_id':str(j['sensor_id'])},{'$set':{'timestamp':j['timestamp'],'payload':j['payload']}})
        else:
            #print('from ble t',str(j['sensor_id']))
            device_shadows.insert_one({'_id':str(j['sensor_id']),'display_name':str(j['sensor_id']),'product_code':'BLE_T','shared_key':None,'timestamp':j['timestamp'],'payload':j['payload'],'alert_stage':0,'buzzer_state':0})
            for w in z:
                if w['product_code']=="BLE_T":
                    database_sensor_ids.append(str(w['_id']))
       
        
def get_sensor_notification_data(shadow_data,alert_data):
    y=device_alerts.find()
    database_sensor_ids=[]
    for i in y:
        database_sensor_ids.append(i['device_id'])
    
    device_shadows.update_one({'_id':str(shadow_data['_id'])},{'$set':{'last_alert_at':shadow_data['last_alert_at'],'is_alert':shadow_data['is_alert']}})
    
    if alert_data['device_id'] in database_sensor_ids:
        cursor = device_alerts.update_one({'device_id':alert_data['device_id']},{'$set':{'gateway_id':alert_data['gateway_id'],'group_id':alert_data['group_id'],'solution_id':alert_data['solution_id'],'display_name':alert_data['display_name'],'action_type':alert_data['action_type'],'payload':alert_data['payload'],'timestamp':alert_data['timestamp'],'created_at':alert_data['created_at'],'sensor_type':alert_data['sensor_type'],"notify_to":alert_data['notify_to'],'description':alert_data['description'],"__v":alert_data["__v"]}})
            
    else:
        cursor = device_alerts.insert_one({'device_id':alert_data['device_id'],'gateway_id':alert_data['gateway_id'],'group_id':alert_data['group_id'],'solution_id':alert_data['solution_id'],'display_name':alert_data['display_name'],'action_type':alert_data['action_type'],'payload':alert_data['payload'],'timestamp':alert_data['timestamp'],'created_at':alert_data['created_at'],'sensor_type':alert_data['sensor_type'],"notify_to":alert_data['notify_to'],'description':alert_data['description'],"__v":alert_data["__v"]})
        for i in y:
            database_sensor_ids.append(i['device_id'])
    
        
    
#get duplicate data
dev_dup_logs=table_name['device_duplicate_logs']
def Ble_Door_Duplicate_Data(**kwargs):
    for h in kwargs:
        print(h,kwargs[h])
def Ble_TH_Duplicate_Data(**kwargs):
    for h in kwargs:
        print(h,kwargs[h])
def Ble_Temperature_Duplicate_Data(**kwargs):
    for h in kwargs:
        print(h,kwargs[h])   

def gateway_health(data):
    z=device_shadows.find()
    db_data=[]
    print(data)
    for k in z:
        o=list(k.keys())
        if "evt" in o and k['evt'].lower()=='health':
            db_data.append(k['gateway_id'])
    for ff in data:
        if ff=='gateway_id':
            if data['gateway_id'] in db_data:
                device_shadows.update_one({'gateway_id':data['gateway_id'],'evt':'HEALTH'},{'$set':data})
            else:
                device_shadows.insert_one(data)
                for k in z:
                    o=list(k.keys())
                    if "evt" in o and k['evt'].lower()=='health':
                        db_data.append(k['gateway_id'])
    
def gateway_set_ble(data):
    z=device_shadows.find()
    db_data=[]
    
    device_shadows.insert_one(data)
                
def gateway_start_up(data):
    z=device_shadows.find()
    db_data=[]
    
    for k in z:
        o=list(k.keys())
        if "evt" in o and k['evt'].lower()=='start_up':
            db_data.append(k['gateway_id'])
    for ff in data:
        if ff=='gateway_id':
            if data['gateway_id'] in db_data:
                device_shadows.update_one({'gateway_id':data['gateway_id'],'evt':'START_UP'},{'$set':data})
            else:
                device_shadows.insert_one(data)
                for k in z:
                    o=list(k.keys())
                    if "evt" in o and k['evt'].lower()=='start_up':
                        db_data.append(k['gateway_id'])

def device_logs_data(osd):
    
    s_data=[]
    
    for k in osd:
        if k['sensor_type']==1:
            device_logs.insert_one({"sensor_id":k['sensor_id'],"mac_id":k['mac_id'],"sensor_type":k['sensor_type'],"timestamp":k['timestamp'],'packet_number':k['packet_number'],'temperature':k['temperature'],'gateway_id':k['gateway_info']['gateway_id']})
        elif k['sensor_type'] == 2:
            device_logs.insert_one({"sensor_id":k['sensor_id'],"mac_id":k['mac_id'],"sensor_type":k['sensor_type'],"timestamp":k['timestamp'],'packet_number':k['packet_number'],'temperature':k['temperature'],'humidity':k['humidity'],'gateway_id':k['gateway_info']['gateway_id']})
        elif k['sensor_type'] == 8:
            device_logs.insert_one({"sensor_id":k['sensor_id'],"mac_id":k['mac_id'],"sensor_type":k['sensor_type'],"timestamp":k['timestamp'],'packet_number':k['packet_number'],"door_status":k['door_status'],'gateway_id':k['gateway_info']['gateway_id']})
        else:
            print('happend',type(k['sensor_type']),k['sensor_type'])              
    d=dev_dup_logs.find()
    for w in osd:
        if w not in s_data:
            s_data.append(w)
    db_exist_data=[]
    for kk in dev_dup_logs.find():
        qq={'device_id':kk['device_id'],'packet_number':kk['packet_number']}
        if qq not in db_exist_data:
            db_exist_data.append(qq)
            
    
    for u in s_data:    
        h=device_logs.find({'sensor_id':u['sensor_id'],"packet_number":u['packet_number'],'sensor_type':u['sensor_type']})
        p=[]
        for q in h:
            
            p.append(q['_id'])
        if len(p)>1:
            if {'device_id':u['sensor_id'],"packet_number":u['packet_number']} in db_exist_data:
                #print(p,len(p))
                
                dev_dup_logs.update_one({'device_id':u['sensor_id'],"packet_number":u['packet_number']},{'$set':{'count':len(p),'log_ids':p}})   
            else:
                
                dev_dup_logs.insert_one({'device_id':u['sensor_id'],"packet_number":u['packet_number'],'count':len(p),'log_ids':p})
                for kk in dev_dup_logs.find():
                    qq={'device_id':kk['device_id'],'packet_number':kk['packet_number']}
            
                    db_exist_data.append(qq)
    #make duplicate database
    
    
     
    