#!/bin/env python3

import re

features = {
	# sandra
	#'presse': '{True,False}',
	# abdenour
	# agathe
	# andrea
	'vous': 'numeric',
	'suspen': 'numeric',
	# arthur
	'vs': 'numeric',
	'selon': 'numeric',
	# audrey
	# chloe
	# damien
	'ameri': 'numeric',
	'impers': 'numeric',
	'ponctuation' : 'numeric',
	# giovanna
	# guanhua
	'Corée': 'numeric',
	# jielei
	'bande':'numeric',
	# mingqiang
	'Chine': 'numeric',
	# morgane
	# nico
	'référendum': 'numeric',
	# sotiria
	'onu': 'numeric',
	# xi
	# yousef
	# yunbei
	'russe':'numeric',
	# yuran
}

def getfeature(text, name):
	# sandra
	if name == 'presse':
		nbpresse = 0
		nbpresse += text.count('presse')
		nbpresse += text.count('presses')
		return nbpresse
	# abdenour
	# agathe
	# andrea
	if name == 'vous':
		nbvous = 0
		nbvous += text.count(' vous ')
		nbvous += text.count('Vous ')
		return nbvous
	if name == 'suspen':
		nbsuspen = 0
		nbsuspen += text.count('...')
		nbsuspen += text.count('…')
		return nbsuspen
	# arthur
	if name == 'vs':
		vs = 0
		vs += text.count('vous')
		vs += text.count('Vous')
		return vs
	if name == 'selon':
		nbselon = 0
		nbselon += text.count('Selon')
		nbselon += text.count('selon')
		return nbselon
	# audrey
	# chloe
	# damien
	if name == 'ameri':
		if 'Améri' in text:
			return 1
		return 0
	if name == 'impers':
		nbimpers = 0
		nbimpers += text.count('on')
		nbimpers += text.count('nous')
		return nbimpers
	if name == 'ponctuation':
		nbponct = 0
		nbponct += text.count('.')
		nbponct += text.count('!')
		nbponct += text.count('?')
		return nbponct
	# giovanna
	# guanhua
	if name == 'Corée':
		nbcoree = 0
		nbcoree += text.count('Corée')
		nbcoree += text.count('coréen')
		return nbcoree
	# jielei
	if name == 'bande':
		if 'bande' in text:
			return 1
		return 0
	# mingqiang
	if name == 'Chine':
		if 'Chine' in text:
			return 1
		return 0
	# morgane
	# nico
	if name == 'référendum':
		if 'ONU' in text:
			return 1
		return 0
	# sotiria
	if name == 'onu':
		if 'ONU' in text:
			return 1
		return 0
	if name == 'ponctuation':
		nbponct = 0
		nbponct += text.count('.')
		nbponct += text.count(',')
		nbponct += text.count('!')
		return nbponct
	# xi
	# yousef
	# yunbei
	if name =='russe':
		nbrusse = 0
		path = re.compile(r'(R|r)usse(s)?')
		match = path.findall(text)
		return(len(match))
	# yuran
	return None