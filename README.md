[![License](https://img.shields.io/badge/License-BSD%203--Clause-red.svg)](https://github.com/imperial-qore/SAN/blob/master/LICENSE)
![Python 3.7, 3.8](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fimperial-qore%2FSAN&count_bg=%23FFC401&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# GON
Generative Optimization Network for Memory-Constrained Anomaly Detection. 

Important references: 'self-supervised adversarial training', 'DGSAN'.
Baselines: memory constrained GANs/VAEs, memory constrained fault detection models. 

## Figures

For a fixed memory limit per application take the model that has the minimum memory footprint considering the set of models with the best score. Or use weighted combination. For such models, give best scores, memory consumption, training and testing times.

1. Performance scores: 
	- P, R, F1, ROC AUC, F1/KB.
2. Memory Comparison:
	- Stacked bar graphs (input size, backprop size, param size).
3. Training and testing time:
	- Double column graph with training time on left and test time on right.
4. Performance Sensitivity:
	- Comparison of performance with increasing memory footprint (line-plots).

## Result Reproduction

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

Run model `<M>` on dataset `<D>`:
```bash
python3 main.py --model <M> --dataset <D> --retrain
```
This will train the model and give results. `<M>` can be one of SAN, USAD, MAD_GAN, SlimGAN, DILOF, IF, TranAD, ONLAD, SVM. `<D>` can be one of SMD, MSDS, FTSAD-1, FTSAD-25, FTSAD-55. All preprocessed datasets are in the `processed` folder.

To train all models at once:
```bash
./train.sh
```

To generate accuracy scores for model `<M>` on dataset `<D>`:
```bash
python3 main.py --model <M> --dataset <D> --test
```

To generate the memory consumpion profile of a model:
```bash
python3 main.py --model <M> --dataset <D> --memory
```

## License

BSD-3-Clause. 
Copyright (c) 2021, Shreshth Tuli.
All rights reserved.

See License file for more details.
