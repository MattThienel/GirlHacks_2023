import redis

class Database:
	def __init__(self, host, port, password):	
		if password != None:
			self.db = redis.Redis(host=host, port=port, password=password)
		else:
			self.db = redis.Redis(host=host, port=port)

	def addTrashEntry(self, timestamp, trash_type, confidence, photo):
		self.db.hmset(timestamp, {"type": "trash_entry", "trash_type": trash_type, "confidence": confidence, "photo": photo})

	def getTrashEntries(self, key):
		return self.db.hgetall(key)

	def getKeys(self):
		return self.db.keys('*')

	def addPersonEntry(self, timestamp, person, status):
		self.db.hmset(timestamp, {"type": "person_entry", "person": person, "status": status})

	def addResupplyEntry(self, timestamp):
		self.db.hmset(timestamp, {"type": "resupply_entry"})
