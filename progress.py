import time
class Progress:
	def __init__(self, range = 100, cols = 30):
		self.range = range
		self.cols = cols
		self.count = 0
		self.message = ''
	def update(self, m):
		self.message = m
	@staticmethod
	def getmaxlength(n):
		n = str(n)
		return len(n)
	def bar(self):
		self.count += 1
		p = int(self.count / self.range * 100)
		p_cols = int(p / 100 * self.cols)
		blank = self.cols - p_cols
		max_l = Progress.getmaxlength(self.range)
		if self.message:
			print('\r%-*s'%(self.cols * 2, self.message))
		print('\r|' + ('█' * p_cols) + (' ' * blank) + '| [%*d/%d] %3d %%'%(max_l, self.count, self.range, p), end = '')
	def __iter__(self):
		return self
	def __next__(self):
		if self.count == self.range:
			print()
			raise StopIteration
		self.bar()
p = Progress(50)
for n in p:
	p.update('Hello')
	time.sleep(0.1) 
