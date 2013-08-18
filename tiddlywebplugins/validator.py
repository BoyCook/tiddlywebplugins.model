

class Validator():

	def validate(self, tiddler):
		print 'Validate tiddler'

	def validate_create(self, tiddler):
		print 'Validate tiddler'
		self.validate_attributes(tiddler)
		self.validate_associations(tiddler)
		# - check mandatory attributes
		# - check mandatory associations (is owner needed?)

	def validate_update(self, tiddler):
		print 'Validate tiddler'
		self.validate_attributes(tiddler)
		self.validate_associations(tiddler)		
		# - check mandatory attributes
		# - check mandatory associations (is owner needed?)
		# - check immutable

	def validate_delete(self, tiddler):
		print 'Validate tiddler'
		self.validate_associations(tiddler)		
		# - check mandatory associations (do children exist?)

	def validate_attributes(self, tiddler):		
		self.validate_mandatory_attributes(tiddler)
		self.validate_immutable_attributes(tiddler)
		print 'Validate tiddler'

	def validate_mandatory_attributes(self, tiddler):		
		print 'Validate tiddler'

	def validate_immutable_attributes(self, tiddler):		
		print 'Validate tiddler'

	def validate_associations(self, tiddler):		
		print 'Validate tiddler'

	def validate_mandatory_associations(self, tiddler):		
		print 'Validate tiddler'


