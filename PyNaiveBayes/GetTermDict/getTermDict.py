#!/usr/bin/env python
# -*- coding: utf-8 -*-

###  词频获得特征  #################################
def Tf_GetTerm(filename, stopSet):
	file = open(filename)
	termDict = {}

	for line in file.readlines():
		line = line.strip('\n')
		list = line.split('\t')
		termlist = list[3].split(' ')
		for term in termlist:
			if term in stopSet or term == '':  # 判断是不是停用词
				continue

			if term in termDict:
				termDict[term] += 1
			else:
				termDict[term] = 1
	
	file.close()
	
	# 输出term
	file_term_write = open('TermSet', 'w')
	for term in termDict:
		termStr = term + ' ' + str(termDict[term]) + '\n'
		file_term_write.write(termStr)
	file_term_write.close()

	print '特征抽取完毕，共抽取', len(termDict), '个特征'
	
####################################################

###  tf-idf获得特征  ###############################
def TfIdf_GetTerm():
	pass

####################################################

###  IG获得特征  ###################################
def IG_GetTerm():
	pass

####################################################

###  MI获得特征  ###################################
def MI_GetTerm():
	pass

####################################################

###  获得停用词表  #################################
def Get_StopSet(stopname):
	stopSet = set([])
	file = open(stopname)

	for line in file.readlines():
		line = line.strip('\n')
		stopSet.add(line)

	file.close()
	return stopSet

#####################################################

def main():
	filename = '../File/trainFile'
	stopname = '../File/stopwords.txt'

	stopSet = Get_StopSet(stopname)
	Tf_GetTerm(filename, stopSet)

if __name__ == '__main__':
	main()
