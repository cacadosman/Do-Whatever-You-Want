from PIL import Image, ImageDraw, ImageFont
from collections import OrderedDict
from string import punctuation

import numpy as np
import random
import os
import sys


class Scrapbook(object):
	__scrapbook = []
	__margin = 25

	def partition(self, images):
		for _ in range(0,len(images),50):
			nimgs = images[_:_+32]
			count = 0
			parts = []
			tmp_w = 0
			tmp_l = []

			while count < len(nimgs):
				if tmp_w + nimgs[count].size[0] < 1000:
					tmp_l.append(nimgs[count])
					tmp_w += nimgs[count].size[0]
					count += 1
				else:
					parts.append(tmp_l)
					tmp_l = []
					tmp_w = 0
				# print count,
			parts.append(tmp_l)
			# print
			self.create(parts)

	def create(self, parts):
		max_w = max(map(lambda x : sum([y.size[0] for y in x]), parts)) + 115
		max_h = sum([parts[i][0].size[1] for i in range(len(parts))]) + len(parts)*10 + 50
		base  = Image.new('RGB',(max_w, max_h), 'white')
		x,y   = [self.__margin] * 2

		for p in parts:
			tmp = []
			for _,q in enumerate(p):
				base.paste(q,(x,y))
				tmp.append(q.size[1])
				x += q.size[0] + 10
			y += max(tmp) + 10
			x  = self.__margin
		self.__scrapbook.append(base)

	def apply(self):
		try:
			os.mkdir('scrapbook')
		except OSError:
			pass

		for enum,instance in enumerate(self.__scrapbook):
			path = os.path.join('scrapbook', '%s.png' %(str(enum).zfill(2)))
			instance.save(path)


class Painter(Scrapbook):
	def __init__(self, message):
		self.message = message
		self.content = []
		self.images  = [] 

	def __scolor(self):
		vals = 'abc0123456789'
		cols = [random.choice(vals) for i in range(6)]
		return '#' + ''.join(cols)

	def __draw_canvas(self, word):
		wdlen = len(word)
		w,h   = (35*wdlen,100)
		W,H   = (w/20*4.5, 30) 
		if wdlen == 1:
			w,h = (100,100)
			W,H = (40,30)
		font  = ImageFont.truetype('fonts/UbuntuMono-R.ttf',35)
		bgrd  = Image.new('RGB',(w,h),self.__scolor())
		base  = ImageDraw.Draw(bgrd)
		base.text((W, H), word, font=font)
		return bgrd

	def draw(self):
		for enum, instance in enumerate(self.message):
			image = self.__draw_canvas(instance)
			self.images.append(image)
			self.save(image, '{}.png'.format(enum))
		self.partition(self.images)

	def save(self, image, pathname):
		try:
			os.mkdir('imgs')
		except OSError:
			pass
		finally:
			path = os.path.join('imgs', pathname)
			image.save(path)

if __name__ == "__main__":
	pathname = sys.argv[1]
	message = open(pathname).read()
	message = message.replace('.', '')
	message = message.replace(',', '')

	painter = Painter(message.split())
	painter.draw()
	painter.apply()

	target = pathname.split('/')[-1].split('.')[0]
	os.system('convert scrapbook/*.png ../{}.pdf'.format(target))