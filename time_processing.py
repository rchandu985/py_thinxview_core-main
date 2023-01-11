"""l=h['last_alert_at']
                                            i=h['notification']['intervel_value']
                                            data=[l]
                                            end_time_hour="24:00"
                                            #while data[-1]!=end_time_hour :
                                            while data[-1][:2]!=end_time_hour[:2]:
                                                    #print(int(data[-1][3:]))
                                                if int(data[-1][3:])+i>=60:
                                                        
                                                        hour=(int(data[-1][:2]))+1
                                                        minute=(int(data[-1][3:])+i)-60
                                                        if len(str((int(data[-1][3:])+i)-60))==1:
                                                                k=str(minute).zfill(2)
                                                                time=str(hour)+':'+k
                                                                data.append(time)
                                                        else:
                                                                time=str(hour)+':'+str(minute)
                                                                data.append(time)
                                                else:
                                                        hour=data[-1][:2]
                                                        minute=(int(data[-1][3:]))+i
                                                        if len(str(minute))==1:
                                                                k=str(minute).zfill(2)
                                                                time=str(hour)+':'+k
                                                                data.append(time)
                                                        else:
                                                                time=str(hour)+':'+str(minute)
                                                                data.append(time)
                                            hour=my_time.strftime("%H")
                                            minute=int(my_time.strftime("%M"))
                                            k=[]
                                            for h in data:
                                                if h[:2]==hour:
                                                    k.append(h)
                                            
                                            print('k',k)
                                            final_data=[]
                                            for j in k:
                                                if int(j[3:])>minute:
                                                    q=data.index(j)
                                                    final_data.append(data[q-1])
                                                    break
                                            if len(final_data)==0:
                                                    print('latest time updated')
                                                    self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':k[-1],'is_alert':True}})
                                            else:
                                                print('latest time updated')
                                                self.col.update_one({'_id':str(u['sensor_id'])},{'$set':{'last_alert_at':final_data[-1],'is_alert':True}})
                                            get_t=self.col.find_one({'_id':str(u['sensor_id'])})
                                            if get_t['last_alert_at']==my_time.strftime("%H:%M"):
                                                print(' im backup time')
                                                alert=self.dmn['coldchain_device_alerts']
                                                database_sensor_ids=[]
                                                x=alert.find()
                                                o=self.col.find_one({'_id':str(u['sensor_id'])})
                                                for i in x:
                                                    database_sensor_ids.append(i['device_id'])
                                                    
                                                if u['sensor_id'] in database_sensor_ids:
                                                    cursor = alert.update_one({'device_id':u['sensor_id']},{'$set':{'gateway_id':u['gateway_id'],'group_id':o['group_id'],'solution_id':o['solution_id'],'display_name':'BLE-T','action_type':o['notification']['action'],'payload':{'TEMPERATURE_LOW':{'current_value':u['payload']['temperature'],'compare_value':o['configuration_params']['temperature']['min']}},'timestamp':o['timestamp'],'created_at':my_time,'sensor_type':u['sensor_type']}})
                                                    
                                                    for i in x:
                                                        database_sensor_ids.append(i['device_id'])
                                                        
                                                else:
                                                        
                                                    alert.insert_one({'device_id':u['sensor_id'],'gateway_id':u['gateway_id'],'group_id':o['group_id'],'solution_id':o['solution_id'],'display_name':'BLE-T','action_type':o['notification']['action'],'payload':{'TEMPERATURE_LOW':{'current_value':u['payload']['temperature'],'compare_value':o['configuration_params']['temperature']['min']}},'timestamp':o['timestamp'],'created_at':my_time,'sensor_type':u['sensor_type']})
                                                    for i in x:
                                                        database_sensor_ids.append(i['device_id'])
"""