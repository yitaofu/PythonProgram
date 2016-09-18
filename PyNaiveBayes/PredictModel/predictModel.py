#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt

###  加载模型  #########################################
def LoadDictModel(cidFileName, termcidFileName):
	cidProb = {}
	cid_termProb = {}
	file_cid = open(cidFileName)
	file_termcid = open(termcidFileName)

	# 加载cid先验概率
	for line in file_cid.readlines():
		line = line.strip('\n')
		list = line.split('\t')
		cid = list[0]
		prob = list[1]
		cidProb[cid] = prob

	# 加载cid和term后验概率
	for line in file_termcid.readlines():
		line = line.strip('\n')
		list = line.split('\t')
		cid_term = list[0]
		prob = list[1]
		cid_termProb[cid_term] = prob	

	file_cid.close()
	file_termcid.close()
	
	print '模型加载完毕'

	return cidProb, cid_termProb

########################################################

###  预测模型  #########################################
def PredictModel(testFileName, cidProb, cid_termProb):
	testResult = []
	file = open(testFileName)
	correctNum = 0
	totalNum = 0
	count = 0

	for line in file.readlines():
		count += 1
		if count % 500 == 0:
			print count
		line = line.strip('\n')
		list = line.split('\t')
		cidReal = list[2]
		termline = list[3]
		termlist = termline.split(' ')

		# 开始预测
		maxProb = -100000
		cidPredict = ''
		for cid in cidProb:
			cidprob = float(cidProb[cid])
			predictprob = 0
			cid_null = cid + ' NULL'
			
			# cid和term的后验概率加和
			for term in termlist:
				cid_term = cid + ' ' + term
				if cid_term in cid_termProb:
					predictprob += float(cid_termProb[cid_term])
				else:
					predictprob += float(cid_termProb[cid_null])

			predictprob += cidprob  # cid的先验概率加和
			if predictprob > maxProb:
				maxProb = predictprob
				cidPredict = cid

		testResult.append(cidPredict)  # 将预测结果放入list中
		
		# 预测检验
		totalNum += 1
		if cidReal == cidPredict:
			correctNum += 1
	
	accuracyRate = float(correctNum) / totalNum
	print '预测完毕，正确率为', accuracyRate

	file.close()

	return testResult

########################################################

def main():
	cidFileName = '../ExtractModel/CidProb'
	termcidFileName = '../ExtractModel/TermCidProb'
	#
	opts, args = getopt.getopt(sys.argv[1:], 'hi:o:')
	testFileName = ''
	resultFileName = ''
	
	for op, value in opts:
		if op == '-i':
			testFileName = value
		elif op == '-o':
			resultFileName = value
		elif op == '-h':
			usage()
			sys.exit()
	#
	file_result = open(resultFileName, 'w')

	cidProb, cid_termProb = LoadDictModel(cidFileName, termcidFileName)  # 加载模型
	testResult = PredictModel(testFileName, cidProb, cid_termProb)  # 预测模型

	for result in testResult:
		result += '\n'
		file_result.write(result)

if __name__ == '__main__':
	main()
