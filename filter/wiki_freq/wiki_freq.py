import wikipedia
import wiki2plain
import sys
sys.path.append('../')
import word_freq_dictionary as w

class WikiFreq:
#	d = {}
	total = 0.0
	alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	eng_frequency = w.EnglishFrequency()
	threshold = 1000000

	def __init__(self, title):
		self.filt = []
		self.d = {}
		lang = 'en'
		wiki = wikipedia.Wikipedia(lang)
		r = ''
		try:
			r = wiki.article(title)
		except:
			print "Could not find article"
		if r:
			w = wiki2plain.Wiki2Plain(r)
			content = w.text
			self.calc_freq(content)
			self.filt = self.generate_list()

	def calc_freq(self, text):
		lst = text.split()
		for i in lst:
			boo = False
			for j in i:
				if j not in self.alphabet:
					boo = True
					break

			if not boo:
				if i in self.d.keys():
					temp = self.d[i]
					self.d[i] = temp+1
				else:
					self.d[i] = 1
				self.total += 1
		print self.total

	def generate_list(self):
		lst = self.d.keys()
		ret = []
		for i in lst:
			temp = 0
			try:
				temp = self.eng_frequency.get_freq(i.lower())
			except:
				temp = 0 #Word not in the english language
			if self.d[i] / self.total >= self.threshold * temp:
				ret = ret + [i]
#		ret.remove('Wikia')
#		ret.remove('website')
#		ret.remove('websites')
		return ret

