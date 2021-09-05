[![License](https://img.shields.io/badge/License-BSD%203--Clause-red.svg)](https://github.com/imperial-qore/GON/blob/master/LICENSE)
![Python 3.7, 3.8](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fimperial-qore%2FSAN&count_bg=%23FFC401&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# GON
Generative Optimization Network for Memory-Constrained Anomaly Detection. 

Hypothesis: "A discriminator is all you need". A sufficiently trained discriminator could not only indicate whether an input belongs to a data distribution but also how to tweak the input to make it resemble more closely to the target distribution. Thus, we can use only a discriminator for data generation and use those as fake samples in a self-adversarial training fashion. This allows us to reduce the parameter size significantly compared to traditional GANs.

In this repo, we use a GON to train a reconstruction based time-series anomaly detector and show that it outperforms baselines by reducing memory footprint and improving detection accuracy.

## Result Reproduction

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

Run model `<M>` on dataset `<D>`:
```bash
python3 main.py --model <M> --dataset <D> --retrain
```
This will train the model and give results. `<M>` can be one of GON, USAD, MAD_GAN, SlimGAN, DILOF, IF, TranAD, ONLAD, SVM. `<D>` can be one of SMD, MSDS, FTSAD-1, FTSAD-25, FTSAD-55. All preprocessed datasets are in the `processed` folder.

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