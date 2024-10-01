import snap7
from snap7.util import *

# PLC bağlantısı
plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)  # IP adresi, rack ve slot numarası

# Veri yazma
data = bytearray([1, 2, 3, 4])  # Koordinat bilgisi burada byte olarak iletilmeli
plc.db_write(1, 0, data)  # 1 numaralı DB'ye veriyi yaz

plc.disconnect()
