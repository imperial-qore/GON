<h1 align="center">Generative Optimization Networks</h1>

<div align="center">
  <a href="https://github.com/imperial-qore/GON/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203--Clause-red.svg" alt="License">
  </a>
   <a>
    <img src="https://img.shields.io/badge/python-3.8%20%7C%203.9-blue.svg" alt="Python 3.8, 3.9">
  </a>
   <a>
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fimperial-qore%2FGON&count_bg=%23FFC401&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="Hits">
  </a>
 <br>
   <a href="https://gitpod.io/#https://github.com/imperial-qore/GON/">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in gitpod">
  </a>
</div>

## GON for Memory-Efficient Data Generation

Hypothesis: "A discriminator is all you need". A sufficiently trained discriminator could not only indicate whether an input belongs to a data distribution but also how to tweak the input to make it resemble more closely to the target distribution. Thus, we can use only a discriminator for data generation and use those as fake samples in a self-adversarial training fashion. This allows us to reduce the parameter size significantly compared to traditional GANs. GON stands for Generative Optimization Network and is an ML framework that is similar to GANs but does not use a generator. GONs use a single discriminator network that also generated new data samples by maximizing discriminator output by modigying the input (i.e. neural network inversion). Without the generator, GONs enable significant gains in terms of memory footprints and allow us to deploy generative models in resource constrined Edge devices.

In this repo, we use a GON to train a reconstruction based time-series anomaly detector. Experiments on a Raspberry-Pi testbed with two existing and a new suite of datasets show that our framework gives up to 32% higher detection F1 scores and 58% lower memory consumption, with only 5% higher training overheads compared to the state-of-the-art.

## Result Reproduction

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
python3 -m pip install -r torch==1.9.1+cpu torchvision==0.10.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
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

## Gitpod
You can directly run tests and generate results using a Gitpod Workspace without needing to install anything on your local machine. Click "Open in Gitpod" on top of the page and test the code by running `python3 main.py --model GON --dataset FTSAD-1 --retrain`.

## Supplementary video

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/NN79i7hB3-s/0.jpg)](https://www.youtube.com/watch?v=NN79i7hB3-s)

## External Links
| Items | Contents | 
| --- | --- |
| **Pre-print** | https://arxiv.org/pdf/2110.02912.pdf |
| **Supplementary** | https://github.com/imperial-qore/GON_MNIST |
| **Video** | https://youtu.be/NN79i7hB3-s |
| **Contact**| Shreshth Tuli ([@shreshthtuli](https://github.com/shreshthtuli))  |
| **Funding**| Imperial President's scholarship |

## Cite this work
Our work is published in NeurIPS 2021, Workshop on ML for Systems. Cite our work using the bibtex entry below.
```bibtex
@article{tuli2021generative,
  title={Generative Optimization Networks for Memory Efficient Data Generation},
  author={Tuli, Shreshth and Tuli, Shikhar and Casale, Giuliano and Jennings, Nicholas R},
  journal={Advances in Neural Information Processing Systems, Workshop on ML for Systems},
  year={2021}
}

```

## License

BSD-3-Clause. 
Copyright (c) 2021, Shreshth Tuli.
All rights reserved.

See License file for more details.
