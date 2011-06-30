"""

More:
- Knapsack problem
- Cutting stock problem

"""

import Image, tools

class CouturierException(Exception):
	pass

class Couturier(object):
	"""Couturier (abstract)
	
	Sews the images on the canvas.
	
	Parameters:
		* ``canvas``: Image canvas
		* ``image_list``: iterable of images
		* ``options``: dictionary of options to be used by the couturier.
	
	"""
	
	def __init__(self, image_list, options={}):
		self.image_list = [Image.open(i) for i in image_list]
		self.options = {}
	
	def sew(self):
		"""Sews the images together
		
		returns: Image
		"""
		
		raise NotImplementedError()


class LeColumnCouturier(Couturier):
	"""This one is adapted to 500px wide images from tumblr
	
	options:
		* ``width``: width of the columns
		* ``order``: fill rows or columns first
		* ``resize_mode``: resize mode ('NEAREST', 'BILINEAR', 'BICUBIC', 'ANTIALIAS')
	"""
	ORDER_FILL_COLUMNS = 0
	ORDER_FILL_ROWS = 1
	
	default_order =  ORDER_FILL_ROWS
	default_width = 500
	
	def sew(self, canvas):
		
		# Fill order
		order = self.options.get('order', LeColumnCouturier.default_order)
		
		# Get dimensions
		w = canvas.size[0]
		h = canvas.size[1] 
		
		# Find number of columns
		col_w = self.options.get('width', LeColumnCouturier.default_width)
		col_n = w/col_w
		
		# [0, 0, ..]
		column_last_height = [0]*(col_n+1)
		column_index = 0
		
		for image in self.image_list:
			
			# If image too wide: resize
			if image.size[0] > col_w: 
				image = tools.resize(image, col_w, resize_mode=self.options.get('resize_mode', tools.DEFAULT_RESIZE_MODE))
			
			canvas.paste(image, (column_index*col_w, column_last_height[column_index]))
			column_last_height[column_index] = column_last_height[column_index] + image.size[1]
			
			if order == LeColumnCouturier.ORDER_FILL_COLUMNS:
				# Go to next column
				if column_last_height[column_index] > h:
					column_last_height[column_index] = 0
					column_index += 1
				# If last column full, patchwork done!
				if column_index > col_n: 
					print column_index
					return
				
			elif order == LeColumnCouturier.ORDER_FILL_ROWS:
				
				column_index = (column_index+1) % (col_n+1)
				tmp = -1
				
				# Find next empty column if this one is full
				while column_last_height[column_index] > h and column_index != tmp:
					if tmp == -1: tmp = column_index
					column_index = (column_index+1) % (col_n+1)
				
				# Nothing found
				if column_last_height[column_index] > h:
					return
			
	

		