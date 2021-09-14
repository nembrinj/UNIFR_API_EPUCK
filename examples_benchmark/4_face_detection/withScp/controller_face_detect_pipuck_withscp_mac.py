from unifr_api_epuck_test import wrapper
import os, time, json
import cv2
import numpy as np
#ip address of the Rasberrypy


data = {
        'start_time':[],
        'exchange_data':[],
        'take_image':[],
        'process_image':[]
        }

timer = time.time()
r = wrapper.get_robot('192.168.224.89',is_pipuck=True)
data['start_time'] += [time.time()-timer]

cam_width = 640
cam_height = 480
size = (cam_width,cam_height)
    
r.init_camera('.', size=size)
r.init_client_communication('192.168.224.24')
r.go_on()
has_process_started = False
process_timer = 0

time_start = time.time()
while time_start + 60 > time.time():
    exch_timer = time.time()
    r.go_on()
    data['exchange_data'] += [time.time()-exch_timer]

    if not has_process_started:
        image_timer = time.time()
        _,img = r.get_camera_read()
        cv2.imwrite('pipuck_image_video.jpg', img)
        os.system('scp "%s" "%s:%s"' % ('pipuck_image_video.jpg', 'THEMACBOOK@192.168.224.24', '/Users/THEMACBOOK/Desktop/GoogleDrive/UNIFR/semestres/Travail_Bachelor/benchmark/4_face_detection/withScp/'))
        data['take_image'] += [time.time()-image_timer]
        r.send_msg_all('process')
        print('finish_sending')

  
        process_timer = time.time()
        has_process_started = True

    if has_process_started:
        if r.has_receive_msg():
            msg = r.receive_msg()
            print(msg)

            if msg in ['left','right', 'center', 'nothing']: 
                has_process_started = False
                print('process finish')
                data['process_image'] += [time.time() - process_timer]

                if msg == 'right':
                    r.set_speed(0.5,-0.5)
                
                if msg == 'left':
                    r.set_speed(-0.5, 0.5)

                if msg == 'center':
                    r.set_speed(0)

                #give time to move according the feedback
                r.sleep(1)
                r.set_speed(0)

    


    
r.send_msg_all('finish')


with open(str(cam_width)+str(cam_height)+'_results_pi_withScpMac_face_detection.txt', 'w') as json_file:
    json.dump(data, json_file)
    print('results saved sucessfully')
    r.send_msg_all('finish')





