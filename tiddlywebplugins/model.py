
class Model():
	
	attribute_types = []
	association_types = []

	def __init__(self, tiddler):
		self.tiddler = tiddler
		
	def validate_model_tidder(self):
		print 'Valiate model in tiddler is accutate'
		
	def parse_tiddler(self):
		print 'Parse tiddler JSON and create object'
		tiddler.text['attributeTypes']
		tiddler.text['associationTypes']
