import time
class progress:
	def __init__(self, _range=100, cols=30):
		self._range = _range
		self.cols = cols
	def __iter__(self):
		self.num = 0
		return self
	def __next__(self):
		if self.num >= self._range:
			raise StopIteration
		self.num += 1
		p = int((self.num / self._range) * 100)
		p_ = int((p / 100) * self.cols)
		print('\r {0:3}% |{1}| {2}/{3}'.format(p, '█' * p_ + ' ' * (self.cols - p_), self.num, self._range), end="")
		time.sleep(0.1)
		return self.num
for n in progress(_range=200):
	pass