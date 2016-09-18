#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

###  计算决策函数 #########################
def sigmoid(z):
	h = 1 / (1 + np.exp(-z))

	return h

###  计算损失函数和相应梯度  ##############
def costfunction(theta, X, Y):
	m = len(Y)
	z = np.dot(X, theta)
	h = sigmoid(z)
	
	# 计算损失函数
	costSum = 0
	print '当前h: ', h
	for i in range(m):
		print '第', i, '个h: ', h[i]
		costSum += (-Y[i])*math.log(h[i]) - (1-Y[i])*math.log(1-h[i])
	costSum = costSum / m

	# 计算theta梯度
	grad = np.zeros(len(theta))
	n = len(theta)

	for j in range (n):
		minH = h - Y
		tempX = X[0:m, j]
		grad[j] =  np.dot(minH, tempX) / m
	
	print 'costSum :', costSum

	return costSum, grad

###  模型训练  ##############################
def trainModel(X, Y):
	# X加一个截距
	tempX = np.ones(len(X), int)
	X = np.c_[tempX, X]
	print 'X :', X

	theta = np.zeros(len(X[0]))
	print 'theta :', theta
	lamda = 1

	for i in range(1000):
		print '第', i, '次迭代！'
		[costSum, grad] = costfunction(theta, X, Y)
		theta = theta - lamda * grad

	z = np.dot(X, theta)
	h = sigmoid(z)
	print '预测结果 :', h

def main():
	X = np.array([[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 1, 1 ,0]])
	Y = np.array([1, 1, 0, 0, 1])
	
	trainModel(X, Y)

if __name__ == '__main__':
	main()
