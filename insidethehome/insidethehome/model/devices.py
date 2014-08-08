import insidethehome.controller

class DeviceManager(object):
	def __init__(self, app):
		self.hi = 0
		
	def get_devices(self):
		return controller.get_all_devices()

	def get_device_by_mac(self, mac):
		return controller.get_device_by_mac()

	
