Variational Quantum Simulation of the Fokker-Planck Equation of Quantum Radiation Reaction
=============================================================================================================================

<a href="https://arxiv.org/abs/2406.02491" style='vertical-align:middle; display:inline;'><img
							src="https://img.shields.io/badge/plasm--ph-arXiv%3A2406.02491-B31B1B.svg" class="plain" style="height:25px;" /></a>

This repository contains the code developed in the paper by Ó. Amaro _et al._ ["Variational Quantum Simulation of the Fokker-Planck Equation of Quantum Radiation Reaction"](https://arxiv.org/abs/2406.02491) (2024).

Authors of paper and repository: [Óscar Amaro](https://github.com/OsAmaro), [L. Gamiz](https://github.com/linigoga), M. Vranic

Abstract: _Near-future experiments in Petawatt class laser scattering are expected to produce a high flux of gamma-ray photons and electron-positron pairs through Strong Field Quantum Electrodynamical processes. We study the stochastic cooling of an electron beam in a strong constant uniform magnetic field, both their particle distribution functions and their energy momenta. We apply the quantum-hybrid Variational Quantum Imaginary Time Evolution to the Fokker-Planck equation describing this process. We also obtain approximate closed-form analytical solutions, filling a gap in the literature. This work will be useful as a first step towards quantum simulation of strong-field plasma physics where diffusion processes are important_

---


## Introduction

In this work we focus on


## Directory Structure

- ```models``` - directory where trained models are stored
- ```scripts``` - example scripts on how to create datasets

### OSIRIS

The open-source version (currently without the ML modules) of the OSIRIS PIC code can be found [here](https://osiris-code.github.io/). To access the developer maintaned version with ML modules, see [here](https://epp.tecnico.ulisboa.pt/osiris/).



### Reproducing Paper Results

All figures in the manuscript should be reproducible following the instructions in the notebooks.



### Citation

If you use the code, consider citing our [paper](https://arxiv.org/abs/2406.02491):

```
@misc{amaroNeuralNetworkSampling2024,
  title = {Neural Network Sampling of {{Bethe-Heitler}} Process in Particle-in-Cell Codes},
  author = {Amaro, {\'O}scar and Badiali, Chiara and Martinez, Bertrand},
  year = {2024},
  month = jun,
  number = {arXiv:2406.02491},
  eprint = {2406.02491},
  primaryclass = {physics},
  publisher = {arXiv},
  urldate = {2024-06-05},
  archiveprefix = {arXiv},
  copyright = {All rights reserved},
  keywords = {Physics - Computational Physics,Physics - Plasma Physics}
}
```

## RePlasma see also these papers:
#### Radiation Reaction
- [Shen 1971 PRL](https://github.com/RePlasma/PhysRevLett.28.455)
- [Neitz 2013 PRL](https://github.com/RePlasma/PhysRevLett.111.054802)
- [Neitz 2014 PRA](https://github.com/RePlasma/PhysRevA.90.022102)
- [Yoffe 2015 NJP](https://github.com/RePlasma/Yoffe_2015_New_J._Phys._17_053025)
- [Vranic 2016 NJP](https://github.com/RePlasma/Vranic_2016_New_J._Phys._18_073035)
- [Ridgers 2017 JPP](https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/signatures-of-quantum-effects-on-radiation-reaction-in-laserelectronbeam-collisions/29DE2EE1FA9375440C85ED700DC1E98B)
- [Niel 2018 PRE](https://github.com/RePlasma/PhysRevE.97.043209)
- [Zhang 2023 MRE](https://github.com/RePlasma/5.0157663)
- [Bilbao 2023 PRL](https://github.com/RePlasma/PhysRevLett.130.165101)
- [Blackburn 2024 PRA](https://github.com/RePlasma/PhysRevA.109.022234)
- [Bulanov 2024 FPP](https://github.com/RePlasma/j.fpp.2024.100036)

#### Quantum Algorithms
- [Endo 2020 PRL](https://github.com/RePlasma/PhysRevLett.125.010501)
- [Kubo 2021 PRA](https://github.com/RePlasma/PhysRevA.103.052425)
- [Alghassi 2022 Quantum](https://github.com/RePlasma/q-2022-06-07-730)
- [Dasgupta 2023](https://github.com/RePlasma/2208.13372)
- [Sato 2024 PhysRevRe](https://github.com/RePlasma/PhysRevResearch.6.033246)
