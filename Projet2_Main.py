#+-#######################################
#@    author : Sorl_Sintoural
#! Main Python File Program
#todo######## MAIN CODE TO RUN ###########
#+-                                    -+#
print("\n  -  -  -  Starting Code  -  -  -")

# Imports
print("Importing Libraries -  -  -")
import Projet2_Sequences as p2_s
import time
import paho.mqtt.client as mqtt
time.sleep(0.3)

# MQTT Client Creation
print("Connecting to MQTT   -  -  -")
Ordi_Biped = mqtt.Client("Ordi_Biped")
Ordi_Biped.connect("broker.hivemq.com")
# MQTT Callback 
Ordi_Biped.on_message = p2_s.on_message   #? Optionnel
time.sleep(0.3)

# Initialize les moteurs a 90 degre
p2_s.start_debout(Ordi_Biped)

# Module de Communication
while (p2_s.sequence_is > 0):
   Ordi_Biped.loop_start() #start the loop
   Ordi_Biped.subscribe("/cm/sequence")   #? Optionnel
   
   # Prise de la sequence voulu
   p2_s.sequence_is = p2_s.input_sequence()
   print("Sequence chosen :" , p2_s.sequence[p2_s.sequence_is])
   if p2_s.sequence_is == 0 :   #! Sequence 0 = Arret du Programme
      break
   elif p2_s.sequence_is == 1 or p2_s.sequence_is == 2:
      motor_is = input("  -  Choix d'un Moteur :")
      p2_s.test_uniMotor(motor_is, Ordi_Biped)
   else :
      # Selection de repetition
      num_times = int(input("\n - Number of sequence : "))
      p2_s.publish_for(num_times , Ordi_Biped)
   
   print("  -  -  -  Loading  -  -  -")
   time.sleep(0.3)
   Ordi_Biped.loop_stop() #stop the loop

print("  -  -  -  Quitting Code  -  -  -  \n")
