# Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles

[![arXiv](http://img.shields.io/badge/arXiv-1612.01474-B31B1B.svg)](https://arxiv.org/abs/1612.01474)

The purpose of this repository is to provide an easy-to-run demo using PyTorch for the ideas proposed in the paper *Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles* by Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell.

The paper can be accessed over at: [https://arxiv.org/abs/1612.01474](https://arxiv.org/abs/1612.01474)

Part of: [31st Conference on Neural Information Processing Systems (NIPS 2017)](https://papers.nips.cc/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Paper.pdf)

## 📝 Table of Contents
- [About](#about)
- [Paper Abstract](#abstract)
- [Authors](#authors)
- [Demonstration](#demonstration)
- [Usage](#usage)
- [License](./LICENSE)
- [Requirements](./requirements.txt)

## 📚 Paper Abstract <a name = "abstract"></a>

Deep neural networks (NNs) are powerful black box predictors that have recently achieved impressive performance on a wide spectrum of tasks. Quantifying predictive uncertainty in NNs is a challenging and yet unsolved problem. Bayesian NNs, which learn a distribution over weights, are currently the state-of-the-art for estimating predictive uncertainty; however these require significant modifications to the training procedure and are computationally expensive compared to standard (non-Bayesian) NNs. We propose an alternative to Bayesian NNs that is simple to implement, readily parallelizable, requires very little hyperparameter tuning, and yields high quality predictive uncertainty estimates. Through a series of experiments on classification and regression benchmarks, we demonstrate that our method produces well-calibrated uncertainty estimates which are as good or better than approximate Bayesian NNs. To assess robustness to dataset shift, we evaluate the predictive uncertainty on test examples from known and unknown distributions, and show that our method is able to express higher uncertainty on out-of-distribution examples. We demonstrate the scalability of our method by evaluating predictive uncertainty estimates on ImageNet.