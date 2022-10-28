from pymavlink import mavutil 

address = 'udpin:localhost:14551' #simulasyon
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

def getPosition():
    message = vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking= True)
    alt = message.relative_alt / 1000
    
