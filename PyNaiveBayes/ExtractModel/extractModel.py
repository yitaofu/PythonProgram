#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

###  伯努利模型抽取  ###########################
def Bernoulli_countCidTerm(filename, termDict):
	cidDict = {}
	cid_termDict = {}
	total_cidNum = 0
	file = open(filename)

	for line in file.readlines():
		line = line.strip('\n')
		list = line.split('\t')  # 对每行以'\t'分隔

	 	# 处理cid
		cid = list[2]
		if cid in cidDict:
			cidDict[cid] += 1
		else:
			cidDict[cid] = 1
		total_cidNum += 1 # 统计cid的总数

		# 处理term
		termlist = list[3].split(' ') # 对每个标题以' '分隔
		termrecord = {}
		# 每个标题中的term去重
		for term in termlist:
			if term not in termDict:  # 判断是否在term字典中
				continue

			if term in termrecord:
				termrecord[term] += 1
			else:
				termrecord[term] = 1
		# 统计cid和term的数量
		for term in termrecord:
			cid_term = cid + ' ' + term
			if cid_term in cid_termDict:
				cid_termDict[cid_term] += 1
			else:
				cid_termDict[cid_term] = 1
	
	file.close()

	return cidDict, total_cidNum, cid_termDict

def Bernoulli_extractProb(filename, termDict):
	cidProb = {}
	cid_termProb = {}
	# 获得各个参数
	cidDict, total_cidNum, cid_termDict = Bernoulli_countCidTerm(filename, termDict)
	
	for cid in cidDict:
		cidprob = float(cidDict[cid]) / total_cidNum  # 计算cid的先验概率
		cidProb[cid] = math.log(cidprob)
		
		cid_term = cid + ' NULL'
		cid_termprob = 1.0 / (cidDict[cid] + 2)  # 计算cid和NULL特征的后验概率
		cid_termProb[cid_term] = math.log(cid_termprob)

	# 计算cid和term的后验概率
	for cid_term in cid_termDict:
		list = cid_term.split(' ')
		cid = list[0]
		cid_termprob = float(cid_termDict[cid_term] + 1) / (cidDict[cid] + 2)  # 计算cid和term的后验概率
		cid_termProb[cid_term] = math.log(cid_termprob)

	return cidProb, cid_termProb

################################################


###  多项式模型抽取  ###########################
def Polynomial_countCidTerm(filename, termDict):
	pass
	# return cidDict, total_cidNum, cid_termDict, total_cid_termNum

def Polynomial_extractProb(filename, termDict):
	pass

################################################

###  获取特征集
def Get_TermDict(termname):
	file = open(termname)
	termDict = set([])
	
	for line in file.readlines():
		line = line.strip('\n')
		list = line.split(' ')
		termDict.add(list[0])

	file.close()
	print '共有', len(termDict), '个特征'

	return termDict

def main():
	filename = '../File/trainFile'
	termname = '../GetTermDict/TermSet'
	file_cidProb = open('CidProb', 'w')
	file_cidtermProb = open('TermCidProb', 'w')

	termDict = Get_TermDict(termname)  # 获得特征集
	cidProb, cid_termProb = Bernoulli_extractProb(filename, termDict)  # 伯努利模型

	# 写cid的先验概率
	for cid in cidProb:
		cidprob = cid + '\t' + str(cidProb[cid]) + '\n'
		file_cidProb_write.write(cidprob)
	# 写cid和term的后验概率
	for cid_term in cid_termProb:
		cidtermprob = cid_term + '\t' + str(cid_termProb[cid_term]) + '\n'
		file_cidtermProb_write.write(cidtermprob)

	file_cidProb.close()
	file_cidtermProb.close()


if __name__ == '__main__':
	main()
