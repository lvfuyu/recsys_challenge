############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/14 14:56:14
File:    score.py
"""

def score(S,T):

    score = 0.0
    uid,recommendedItems = S.rstrip().split('\t')
    uid,relevantItems = T.rstrip().split('\t')
    r = recommendedItems.split(',')
    t = relevantItems.split(',')
    t = set(t)
    # keep r list structure
    score += 20 * (precisionAtK(r,t,2) + precisionAtK(r,t,4) + recall(r,t) + userSuccess(r,t) ) + 10 * (precisionAtK(r,t,6) + precisionAtK(r,t,20))

    if score > 100:
        score = 100

    return score

def precisionAtK(recommendedItems, relevantItem, k):

    topK = recommendedItems[0:k]
    topK = set(topK)

    return len(topK & relevantItem)*1.0/k

def recall(recommendedItems, relevantItem):

    recommendedItems = set(recommendedItems)
    if len(relevantItem) > 0:
        return len(recommendedItems & relevantItem)*1.0/len(relevantItem)
    else:
        return 0.0

def userSuccess(recommendedItems, relevantItem):

    recommendedItems = set(recommendedItems)
    if len(recommendedItems & relevantItem) > 0:
        return 1.0
    else:
        return 0.0

pred_result = open('pred.csv', 'r')
ground_truth = open('ground_truth.csv', 'r')

line_pred = pred_result.readline()
line_truth = ground_truth.readline()
point = 0.0
while line_pred and line_truth:
    point += score(line_pred, line_truth)
    line_pred = pred_result.readline()
    line_truth = ground_truth.readline()

print point
pred_result.close()
ground_truth.close()

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
