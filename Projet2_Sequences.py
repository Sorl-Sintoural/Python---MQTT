#+-#######################################
#@    author : Sorl_Sintoural
#todo###### DO NOT RUN THIS CODE #########
#+-                                    -+#
import time

pub_delais = 0.1  #! Delais entre les Publications

sequence_is = 7

sequence = ['Stop',
            'Pied Gauche vers la Gauche',
            'Pied Gauche vers la Droite',
            'Equilibre sur Jambe Droite',
            'Debout',
            'Marche']

#? Reception Message Optionnel
def on_message(client, userdata, message):
   msg_is    = (message.payload.decode("utf-8"))
   topic_is  = message.topic
   qos_is    = message.qos
   flag_is   = message.retain
   print(f"Message Received : {msg_is}    ±"
         f"±   Topic : {topic_is}   ±"
         f"±   Qos : {qos_is}   ±"
         f"±   Retain flag : {flag_is} \n")

# Mets les moteurs a 90 degree
def start_debout(user):
   user.publish("/cm/biped/1" , Biped_Debout[7][1]-90)
   user.publish("/cm/biped/2" , Biped_Debout[7][2]-90)
   user.publish("/cm/biped/3" , Biped_Debout[7][3]-90)
   user.publish("/cm/biped/4" , Biped_Debout[7][4]-90)
   user.publish("/cm/biped/5" , Biped_Debout[7][5]-90)
   user.publish("/cm/biped/6" , Biped_Debout[7][6]-90)
   time.sleep(pub_delais)


# Selection de Sequence
def input_sequence(): 
   return int(input(f"\n - Choose a Sequence (number): \n"
                    f"0. {sequence[0]} ;\n"
                    f"1. {sequence[1]} ;\n"
                    f"2. {sequence[2]} ;\n" 
                    f"3. {sequence[3]} ;\n"
                    f"4. {sequence[4]} ;\n"
                    f"5. {sequence[5]} ;\n"
                    "\nInput : "))

# Publication
def publish_for(n , user):
   for sequence_at in range(n):
      print("\nPublishing Messages -  -  - Sequence left :" , n-sequence_at)
      print("  -  Calculating   .  .  .   ", end='')
      user.publish("/cm/sequence" , sequence[sequence_is])
      
      try:
         if (sequence_is == 1):
            print("   Action Time Left : {} seconds".format((len(Pied_Gauche_Gauche)*pub_delais)*(n-sequence_at)))
            for x in range(len(Pied_Gauche_Gauche)):
               for repeat in range(5):
                  user.publish("/cm/biped/1" , Pied_Gauche_Gauche[x][1]-90)
                  time.sleep(pub_delais)

         elif (sequence_is == 2):
            print("   Action Time Left : {} seconds".format((len(Pied_Gauche_Droite)*pub_delais)*(n-sequence_at)))
            for x in range(len(Pied_Gauche_Droite)):
               for repeat in range(5):
                  user.publish("/cm/biped/1" , Pied_Gauche_Droite[x][1]-90)
                  time.sleep(pub_delais)

         elif (sequence_is == 3):
            print("   Action Time Left : {} seconds".format((len(Equilibre_sur_Droite)*pub_delais)*(n-sequence_at)))
            for x in range(len(Equilibre_sur_Droite)):
               for repeat in range(5):
                  user.publish("/cm/biped/2" , Equilibre_sur_Droite[x][2]-90)
                  time.sleep(pub_delais)

         elif (sequence_is == 4):
            print("   Action Time Left : {} seconds".format((len(Biped_Debout)*pub_delais)*(n-sequence_at)))
            for x in range(len(Biped_Debout)):
               for repeat in range(5):
                  user.publish("/cm/biped/1" , Biped_Debout[x][1]-90)
                  user.publish("/cm/biped/2" , Biped_Debout[x][2]-90)
                  user.publish("/cm/biped/3" , Biped_Debout[x][3]-90)
                  user.publish("/cm/biped/4" , Biped_Debout[x][4]-90)
                  user.publish("/cm/biped/5" , Biped_Debout[x][5]-90)
                  user.publish("/cm/biped/6" , Biped_Debout[x][6]-90)
                  time.sleep(pub_delais)

         elif (sequence_is == 5):
            print("   Action Time Left : {} seconds".format((len(Marche)*pub_delais)*(n-sequence_at)))
            for x in range(len(Marche)):
               for repeat in range(5):
                  user.publish("/cm/biped/1" , Marche[x][1]-90)
                  user.publish("/cm/biped/2" , Marche[x][2]-90)
                  user.publish("/cm/biped/3" , Marche[x][3]-90)
                  user.publish("/cm/biped/4" , Marche[x][4]-90)
                  user.publish("/cm/biped/5" , Marche[x][5]-90)
                  user.publish("/cm/biped/6" , Marche[x][6]-90)
                  time.sleep(pub_delais)
      except KeyboardInterrupt:
         print("  -  -  -  Interrupting  -  -  -")
         start_debout(user)
         break
   time.sleep(1)

#* Matrix de Sequences
Pied_Gauche_Gauche = [[1   ,9   ,0 ,0 ,0 ,0 ,0],
                      [2   ,18  ,0 ,0 ,0 ,0 ,0],
                      [3   ,27  ,0 ,0 ,0 ,0 ,0],
                      [4   ,36  ,0 ,0 ,0 ,0 ,0],
                      [5   ,45  ,0 ,0 ,0 ,0 ,0],
                      [6   ,54  ,0 ,0 ,0 ,0 ,0],
                      [7   ,63  ,0 ,0 ,0 ,0 ,0],
                      [8   ,72  ,0 ,0 ,0 ,0 ,0],
                      [9   ,81  ,0 ,0 ,0 ,0 ,0],
                      [10  ,90  ,0 ,0 ,0 ,0 ,0],
                      [11  ,81  ,0 ,0 ,0 ,0 ,0],
                      [12  ,72  ,0 ,0 ,0 ,0 ,0],
                      [13  ,63  ,0 ,0 ,0 ,0 ,0],
                      [14  ,54  ,0 ,0 ,0 ,0 ,0],
                      [15  ,45  ,0 ,0 ,0 ,0 ,0],
                      [16  ,36  ,0 ,0 ,0 ,0 ,0],
                      [17  ,27  ,0 ,0 ,0 ,0 ,0],
                      [18  ,18  ,0 ,0 ,0 ,0 ,0],
                      [19  ,9   ,0 ,0 ,0 ,0 ,0],
                      [20  ,0   ,0 ,0 ,0 ,0 ,0]]

Pied_Gauche_Droite = [[1   ,-9  ,0  ,0  ,0  ,0  ,0],
                      [2   ,-18 ,0  ,0  ,0  ,0  ,0],
                      [3   ,-27 ,0  ,0  ,0  ,0  ,0],
                      [4   ,-36 ,0  ,0  ,0  ,0  ,0],
                      [5   ,-45 ,0  ,0  ,0  ,0  ,0],
                      [6   ,-54 ,0  ,0  ,0  ,0  ,0],
                      [7   ,-63 ,0  ,0  ,0  ,0  ,0],
                      [8   ,-72 ,0  ,0  ,0  ,0  ,0],
                      [9   ,-81 ,0  ,0  ,0  ,0  ,0],
                      [10  ,-90 ,0  ,0  ,0  ,0  ,0],
                      [11  ,-81 ,0  ,0  ,0  ,0  ,0],
                      [12  ,-72 ,0  ,0  ,0  ,0  ,0],
                      [13  ,-63 ,0  ,0  ,0  ,0  ,0],
                      [14  ,-54 ,0  ,0  ,0  ,0  ,0],
                      [15  ,-45 ,0  ,0  ,0  ,0  ,0],
                      [16  ,-36 ,0  ,0  ,0  ,0  ,0],
                      [17  ,-27 ,0  ,0  ,0  ,0  ,0],
                      [18  ,-18 ,0  ,0  ,0  ,0  ,0],
                      [19  ,-9  ,0  ,0  ,0  ,0  ,0],
                      [20  ,0   ,0  ,0  ,0  ,0  ,0]]

Equilibre_sur_Droite = [[1    ,0  ,99  ,0  ,0  ,0  ,0],
                        [2    ,0  ,108 ,0  ,0  ,0  ,0],
                        [3    ,0  ,117 ,0  ,0  ,0  ,0],
                        [4    ,0  ,126 ,0  ,0  ,0  ,0],
                        [5    ,0  ,135 ,0  ,0  ,0  ,0],
                        [6    ,0  ,144 ,0  ,0  ,0  ,0],
                        [7    ,0  ,153 ,0  ,0  ,0  ,0],
                        [8    ,0  ,162 ,0  ,0  ,0  ,0],
                        [9    ,0  ,171 ,0  ,0  ,0  ,0],
                        [10   ,0  ,180 ,0  ,0  ,0  ,0]]

Biped_Debout = [[1   ,90 ,90 ,90 ,90 ,90 ,90],
                [2   ,90 ,90 ,90 ,90 ,90 ,90],
                [3   ,90 ,90 ,90 ,90 ,90 ,90],
                [4   ,90 ,90 ,90 ,90 ,90 ,90],
                [5   ,90 ,90 ,90 ,90 ,90 ,90],
                [6   ,90 ,90 ,90 ,90 ,90 ,90],
                [7   ,90 ,90 ,90 ,90 ,90 ,90],
                [8   ,90 ,90 ,90 ,90 ,90 ,90],
                [9   ,90 ,90 ,90 ,90 ,90 ,90],
                [10  ,90 ,90 ,90 ,90 ,90 ,90],
                [11  ,90 ,90 ,90 ,90 ,90 ,90],
                [12  ,90 ,90 ,90 ,90 ,90 ,90],
                [13  ,90 ,90 ,90 ,90 ,90 ,90],
                [14  ,90 ,90 ,90 ,90 ,90 ,90],
                [15  ,90 ,90 ,90 ,90 ,90 ,90],
                [16  ,90 ,90 ,90 ,90 ,90 ,90],
                [17  ,90 ,90 ,90 ,90 ,90 ,90],
                [18  ,90 ,90 ,90 ,90 ,90 ,90],
                [19  ,90 ,90 ,90 ,90 ,90 ,90],
                [20  ,90 ,90 ,90 ,90 ,90 ,90]]

Marche = [[1   ,90 ,90 ,90 ,90 ,90 ,90],
          [2   ,90 ,90 ,90 ,90 ,90 ,90],
          [3   ,90 ,90 ,90 ,90 ,90 ,90],
          [4   ,90 ,90 ,90 ,90 ,90 ,90],
          [5   ,90 ,90 ,90 ,90 ,90 ,90],
          [6   ,90 ,90 ,90 ,90 ,90 ,90],
          [7   ,90 ,90 ,90 ,90 ,90 ,90],
          [8   ,90 ,90 ,90 ,90 ,90 ,90],
          [9   ,90 ,90 ,90 ,90 ,90 ,90],
          [10  ,90 ,90 ,90 ,90 ,90 ,90],
          [11  ,84 ,90 ,90 ,84 ,90 ,90],
          [12  ,78 ,90 ,90 ,78 ,90 ,90],
          [13  ,72 ,90 ,90 ,72 ,90 ,90],
          [14  ,66 ,90 ,90 ,66 ,90 ,90],
          [15  ,60 ,90 ,90 ,60 ,90 ,90],
          [16  ,54 ,90 ,90 ,54 ,90 ,90],
          [17  ,48 ,90 ,90 ,48 ,90 ,90],
          [18  ,42 ,90 ,90 ,42 ,90 ,90],
          [19  ,36 ,90 ,90 ,36 ,90 ,90],
          [20  ,30 ,90 ,90 ,30 ,90 ,90],
          [21  ,30 ,84 ,84 ,30 ,84 ,84],
          [22  ,30 ,78 ,78 ,30 ,78 ,78],
          [23  ,30 ,72 ,72 ,30 ,72 ,72],
          [24  ,30 ,66 ,66 ,30 ,66 ,66],
          [25  ,30 ,60 ,60 ,30 ,60 ,60],
          [26  ,30 ,54 ,54 ,30 ,54 ,54],
          [27  ,30 ,48 ,48 ,30 ,48 ,48],
          [28  ,30 ,42 ,42 ,30 ,42 ,42],
          [29  ,30 ,36 ,36 ,30 ,36 ,36],
          [30  ,30 ,30 ,30 ,30 ,30 ,30],
          [31  ,36 ,30 ,30 ,36 ,30 ,30],
          [32  ,42 ,30 ,30 ,42 ,30 ,30],
          [33  ,48 ,30 ,30 ,48 ,30 ,30],
          [34  ,54 ,30 ,30 ,54 ,30 ,30],
          [35  ,60 ,30 ,30 ,60 ,30 ,30],
          [36  ,66 ,30 ,30 ,66 ,30 ,30],
          [37  ,72 ,30 ,30 ,72 ,30 ,30],
          [38  ,78 ,30 ,30 ,78 ,30 ,30],
          [39  ,84 ,30 ,30 ,84 ,30 ,30],
          [40  ,90 ,30 ,30 ,90 ,30 ,30],
          [41  ,90 ,36 ,36 ,90 ,36 ,36],
          [42  ,90 ,42 ,42 ,90 ,42 ,42],
          [43  ,90 ,48 ,48 ,90 ,48 ,48],
          [44  ,90 ,54 ,54 ,90 ,54 ,54],
          [45  ,90 ,60 ,60 ,90 ,60 ,60],
          [46  ,90 ,66 ,66 ,90 ,66 ,66],
          [47  ,90 ,72 ,72 ,90 ,72 ,72],
          [48  ,90 ,78 ,78 ,90 ,78 ,78],
          [49  ,90 ,84 ,84 ,90 ,84 ,84],
          [50  ,90 ,90 ,90 ,90 ,90 ,90]]