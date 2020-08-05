'''
from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x1504,
                          idProduct=0x0006,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01) #Create the printer object with the connection params
'''



from escpos.connections import getNetworkPrinter


printer = getNetworkPrinter()(host='192.168.1.87', port=9100)
#printer.text("Hello World")
printer.image('C:/Users/Maybe_shah/Documents/flask_app/FaceMask/table.png') #"C:\Users\Maybe_shah\Documents\flask_app\FaceMask\table.png"
printer.lf()



'''from escpos.connections import getNetworkPrinter


printer = getNetworkPrinter()(host='192.168.0.20', port=9100)

printer.text("Hello World")
printer.lf()'''