import this

from cortex import Cortex
import csv
import time
import serial
import random



class Subcribe():
    """
    A class to subscribe data stream.

    Attributes
    ----------
    c : Cortex
        Cortex communicate with Emotiv Cortex Service

    Methods
    -------
    start():
        start data subscribing process.
    sub(streams):
        To subscribe to one or more data streams.
    on_new_data_labels(*args, **kwargs):
        To handle data labels of subscribed data 
    on_new_eeg_data(*args, **kwargs):
        To handle eeg data emitted from Cortex
    on_new_mot_data(*args, **kwargs):
        To handle motion data emitted from Cortex
    on_new_dev_data(*args, **kwargs):
        To handle device information data emitted from Cortex
    on_new_met_data(*args, **kwargs):
        To handle performance metrics data emitted from Cortex
    on_new_pow_data(*args, **kwargs):
        To handle band power data emitted from Cortex
    """


    def __init__(self, app_client_id, app_client_secret, **kwargs):
        """
        Constructs cortex client and bind a function to handle subscribed data streams
        If you do not want to log request and response message , set debug_mode = False. The default is True
        """
        print("Subscribe __init__")
        self.c = Cortex(app_client_id, app_client_secret, debug_mode=True, **kwargs)
        self.c.bind(create_session_done=self.on_create_session_done)
        self.c.bind(new_data_labels=self.on_new_data_labels)
        self.c.bind(new_eeg_data=self.on_new_eeg_data)
        self.c.bind(new_mot_data=self.on_new_mot_data)
        self.c.bind(new_dev_data=self.on_new_dev_data)
        self.c.bind(new_met_data=self.on_new_met_data)
        self.c.bind(new_pow_data=self.on_new_pow_data)
        self.c.bind(inform_error=self.on_inform_error)






    def start(self, streams, headsetId=''):
        """
        To start data subscribing process as below workflow
        (1)check access right -> authorize -> connect headset->create session
        (2) subscribe streams data
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power
        'eq' : EEQ Quality

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']
        headsetId: string , optional
             id of wanted headet which you want to work with it.
             If the headsetId is empty, the first headset in list will be set as wanted headset
        Returns
        -------
        None
        """
        self.streams = streams

        if headsetId != '':
            self.c.set_wanted_headset(headsetId)

        self.c.open()

    def sub(self, streams):
        """
        To subscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']

        Returns
        -------
        None
        """
        self.c.sub_request(streams)

    def unsub(self, streams):
        """
        To unsubscribe to one or more data streams
        'eeg': EEG
        'mot' : Motion
        'dev' : Device information
        'met' : Performance metric
        'pow' : Band power

        Parameters
        ----------
        streams : list, required
            list of streams. For example, ['eeg', 'mot']

        Returns
        -------
        None
        """
        self.c.unsub_request(streams)

    def on_new_data_labels(self, *args, **kwargs):
        """
        To handle data labels of subscribed data 
        Returns
        -------
        data: list  
              array of data labels
        name: stream name
        For example:
            eeg: ["COUNTER","INTERPOLATED", "AF3", "T7", "Pz", "T8", "AF4", "RAW_CQ", "MARKER_HARDWARE"]
            motion: ['COUNTER_MEMS', 'INTERPOLATED_MEMS', 'Q0', 'Q1', 'Q2', 'Q3', 'ACCX', 'ACCY', 'ACCZ', 'MAGX', 'MAGY', 'MAGZ']
            dev: ['AF3', 'T7', 'Pz', 'T8', 'AF4', 'OVERALL']
            met : ['eng.isActive', 'eng', 'exc.isActive', 'exc', 'lex', 'str.isActive', 'str', 'rel.isActive', 'rel', 'int.isActive', 'int', 'foc.isActive', 'foc']
            pow: ['AF3/theta', 'AF3/alpha', 'AF3/betaL', 'AF3/betaH', 'AF3/gamma', 'T7/theta', 'T7/alpha', 'T7/betaL', 'T7/betaH', 'T7/gamma', 'Pz/theta', 'Pz/alpha', 'Pz/betaL', 'Pz/betaH', 'Pz/gamma', 'T8/theta', 'T8/alpha', 'T8/betaL', 'T8/betaH', 'T8/gamma', 'AF4/theta', 'AF4/alpha', 'AF4/betaL', 'AF4/betaH', 'AF4/gamma']
        """
        data = kwargs.get('data')
        stream_name = data['streamName']
        stream_labels = data['labels']
        #print('{} labels are : {}'.format(stream_name, stream_labels))

    def on_new_eeg_data(self, *args, **kwargs):
        """
        To handle eeg data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array eeg match the labels in the array labels return at on_new_data_labels
        For example:
           {'eeg': [99, 0, 4291.795, 4371.795, 4078.461, 4036.41, 4231.795, 0.0, 0], 'time': 1627457774.5166}
        """
        data = kwargs.get('data')
        #print('eeg data: {}'.format(data))

    def on_new_mot_data(self, *args, **kwargs):
        """
        To handle motion data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array motion match the labels in the array labels return at on_new_data_labels
        For example: {'mot': [33, 0, 0.493859, 0.40625, 0.46875, -0.609375, 0.968765, 0.187503, -0.250004, -76.563667, -19.584995, 38.281834], 'time': 1627457508.2588}
        """
        data = kwargs.get('data')
        #print('motion data: {}'.format(data))

    def on_new_dev_data(self, *args, **kwargs):
        """
        To handle dev data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array dev match the labels in the array labels return at on_new_data_labels
        For example:  {'signal': 1.0, 'dev': [4, 4, 4, 4, 4, 100], 'batteryPercent': 80, 'time': 1627459265.4463}
        """
        data = kwargs.get('data')
        #print('dev data: {}'.format(data))

    def on_new_met_data(self, *args, **kwargs):
        """
        To handle performance metrics data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array met match the labels in the array labels return at on_new_data_labels
        For example: {'met': [True, 0.5, True, 0.5, 0.0, True, 0.5, True, 0.5, True, 0.5, True, 0.5], 'time': 1627459390.4229}
        """
        data = kwargs.get('data')
        #print('pm data: {}'.format(data))
        
        

    
    def on_new_pow_data(self, *args, **kwargs):
        """
        To handle band power data emitted from Cortex

        Returns
        -------
        data: dictionary
             The values in the array pow match the labels in the array labels return at on_new_data_labels
        For example: {'pow': [5.251, 4.691, 3.195, 1.193, 0.282, 0.636, 0.929, 0.833, 0.347, 0.337, 7.863, 3.122, 2.243, 0.787, 0.496, 5.723, 2.87, 3.099, 0.91, 0.516, 5.783, 4.818, 2.393, 1.278, 0.213], 'time': 1627459390.1729}
        """
        data = kwargs.get('data')
        print('pow data: {}'.format(data))

        #================================== L E D ' s =============================
        txt = format(data)
        x = txt.split("[", 2)
        y = x[1].split("]", 2)
        z = y[0].split(", ")
        print(z)

        i = 0
        promedio_eeg = []

        while i <= 4:
            promedio_eeg.append((float(z[i]) + float(z[i+5]) + float(z[i+10]) + float(z[i+15]) + float(z[i+20]))/5)
            i += 1

        etiquetas_eeg = ['Theta', 'Alpha', 'BetaL', 'BetaH', 'Gamma']

        #for numero in promedio_eeg:
         #   print(numero)

        for indice in range(0, len(etiquetas_eeg)):
            print(etiquetas_eeg[indice],' : ', promedio_eeg[indice])
        
        # Buscando a la onda mayor         
        max_value = None
        max_idx = None

        for idx, num in enumerate(promedio_eeg):
            if (max_value is None or num > max_value):
                max_value = num
                max_idx = idx

        
#         print('El mayor es ', etiquetas_eeg[max_idx])
        
        
        #LEDs + EEG
        arduino = serial.Serial('COM6',9600)
                


        #BPM del Sensor de Pulso
        arduino2 = serial.Serial('COM5', 9600)
        line = arduino2.readline()
        string = line.decode()
        stripped_string = string.strip()
        bpm_aux = stripped_string + "."
        bpm = int(stripped_string)
        print("*****BPM: ", bpm)
        #arduino2.close()




        # LEDs + Pulso
        arduino3 = serial.Serial('COM4', 9600)
        #arduino3.close()
        
        #Mandando señal de EEG a Leds
        promedio_betas = (promedio_eeg[2] + promedio_eeg[3])/2   
        

        ciclos = 1
        aux = ""

        while ciclos < 10:
            

            #leds del sensor de pulso
            arduino3.write(bpm_aux.encode())
            print("*****BPM: ", bpm)
            
            
            print("Promedio Beta:", promedio_betas)
            
            if (ciclos <= 3):    
                                    
                if (promedio_betas >= 3.5 and promedio_betas <= 20):
                    aux = "beta" + " " + str(promedio_betas) + " " + str(bpm) +  "."
                    print(arduino.write(aux.encode()))
                    print("Beta: ", promedio_betas)
                
                
                else:
                    aux = "alpha" + " " + str(promedio_eeg[1]) + " " + str(bpm) + "."
                    print(arduino.write(aux.encode()))
                    print("Alpha: ", promedio_eeg[1])
                     

                
            print("Ciclo: ", ciclos)    
            time.sleep(60/bpm)
            ciclos+=1
            
        #arduino.close()  #leds + EEG
        #arduino3.close() #leds + pulso
        
       
        

        
        #Guardando en CSV
        #with open('pow_EEG.csv', 'w', newline='') as csvfile:    #solo escribimos una vez, en el archivo
             #fieldnames = ['EEG']
         #    fieldnames = promedio_eeg
          #   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
           #  writer.writeheader()

             #writer.writerow({'EEG': z})
             #writer.writerow({'EEG': promedio_eeg[0]})


        # ==================================================================

    # callbacks functions
    def on_create_session_done(self, *args, **kwargs):
        print('on_create_session_done')

        # subribe data 
        self.sub(self.streams)

    def on_inform_error(self, *args, **kwargs):
        error_data = kwargs.get('error_data')
        print(error_data)

# -----------------------------------------------------------
# 
# GETTING STARTED
#   - Please reference to https://emotiv.gitbook.io/cortex-api/ first.
#   - Connect your headset with dongle or bluetooth. You can see the headset via Emotiv Launcher
#   - Please make sure the your_app_client_id and your_app_client_secret are set before starting running.
#   - In the case you borrow license from others, you need to add license = "xxx-yyy-zzz" as init parameter
# RESULT
#   - the data labels will be retrieved at on_new_data_labels
#   - the data will be retreived at on_new_[dataStream]_data
# 
# -----------------------------------------------------------

def main():

    # Please fill your application clientId and clientSecret before running script
    your_app_client_id = 'X45K5UrKMCYpVVkE2FFUhRrt6oXurOAF1w3SI10q'
    your_app_client_secret = 'GJbLXplvcouIlw584OzjNCHpV2t7OC0hRkHOtcNaFEabuTn67M9bSb3QMlunZbfZXLDqhO2iTN8p0aras9QQGKSRGE2MUc9YA7FRLNhi3CKGFvsoe1LHwc24qYAPT4vp'

    s = Subcribe(your_app_client_id, your_app_client_secret)

    # list data streams
    streams = ['eeg','mot','met','pow']
    s.start(streams)



if __name__ =='__main__':
    main()

# -----------------------------------------------------------
