#-*- coding: utf-8 -*-

def stopwords(stop_list):
	with open(stop_list) as f:
		stopwords = [line.strip() for line in f]
	return stopwords

if __name__ == '__main__':
	stop_list = 'data/stopwords.txt'
	print stopwords(stop_list)	

