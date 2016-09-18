#!/usr/bin/env python
# -*- coding: utf-8 -*-

###  统计均衡的类目  ##########################################
def StaticCid(fileName):
	file = open(fileName)
	cidDict = {}
	num = 4000
	cidNum = 2
	cidName = {}

	for line in file.readlines():
		list = line.strip('\n').split('\t')
		cid = list[2]
		if (cid in cidDict):
			cidDict[cid] += 1
		else:
			cidDict[cid] = 1
	print 'cidDict len :', len(cidDict)
	count = 0
	for cid in cidDict:
		if count == 2:
			break
		
		if (cidDict[cid] == 8126 or cidDict[cid] == 8274):
			print cid
			cidName[cid] = cidDict[cid]
			count += 1

	file.close()

	return cidName

###  抽取语料  ####################################################
def ExactFile(cidName, fileName):
	# 获得两个类中训练和测试语料的数量
	cid1 = cidName.keys()[0]
	cid2 = cidName.keys()[1]
	cid1Num = cidName[cid1]
	cid2Num = cidName[cid2]
	print 'cid1 :', cid1, 'cid2 :', cid2
	print 'cid1Num :', cid1Num, 'cid2Num :', cid2Num
		
	cid1TrainNum = int(cid1Num * 0.8)
	cid2TrainNum = int(cid2Num * 0.8)
	cid1TestNum = cid1Num - cid1TrainNum
	cid2TestNum = cid2Num - cid2TrainNum
	print 'train1 :', cid1TrainNum, 'train2 :', cid2TrainNum
	print 'test1 :', cid1TestNum, 'test2 :', cid2TestNum

	# 获得语料
	file = open(fileName)
	file_trainName = open('trainFile', 'w')
	file_testName = open('testFile', 'w')
	cid1Count = 0
	cid2Count = 0

	for line in file.readlines():
		list = line.strip('\n').split('\t')
		cid = list[2]
		termline = list[3]

		if cid == cid1 or cid == cid2:
			if cid == cid1:
				strline = termline + '\t' + '0' + '\n'
				if cid1Count < cid1TrainNum:
					file_trainName.write(strline)
				else:
					file_testName.write(strline)
				cid1Count += 1
			elif cid == cid2:
				strline = termline + '\t' + '1' + '\n'
				if cid2Count < cid2TrainNum:
					file_trainName.write(strline)
				else:
					file_testName.write(strline)
				cid2Count += 1

	file.close()
	file_trainName.close()
	file_testName.close()

def main():
	fileName = '../File/part-00000'

	cidName = StaticCid(fileName)
	ExactFile(cidName, fileName)

if __name__ == '__main__':
	main()
