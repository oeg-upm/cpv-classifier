# CPV Classifier

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6554604.svg)](https://doi.org/10.5281/zenodo.6554604) [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

In this work we compare different approaches to Common Procurement Vocabulary (CPV) codes classification, using data extracted from the [Spanish Treasury](https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx). 

## Resources
All training, testing datasets and code are [available in Zenodo](https://doi.org/10.5281/zenodo.6554604). Check them out!

## Pre-processing
In order to preprocess the data, follow the steps below:

1. Download the atom datasets into a folder (in our case `licitacionesPerfilesContratanteCompleto3_2019`)
2. Run `atom2csvBS.py`, which will save the results in `docs.csv` 
3. Run `data2tt.py` using `docs.csv`. As a result, you will obtain `train.csv` and `test.csv`, which are the datasets used in the notebooks

## Notebooks
The notebooks below contain the different approaches compared:

Test for classic approaches: https://www.kaggle.com/marianavasloro/cpvtwodigitsml

Test for the MKaan approach:
https://www.kaggle.com/code/marianavasloro/mkaan

Training and evaluation of fine-tuned RoBERTa:
https://www.kaggle.com/code/marianavasloro/fine-tuned-roberta-for-spanish-cpv-codes


## Datasets

Full: https://www.kaggle.com/datasets/marianavasloro/dataset

10%: https://www.kaggle.com/datasets/marianavasloro/dataset10


## How to cite
If you use these datasets or our notebooks, please cite this repository and our 2022 SEPLN paper (to appear):

```
@software{maria_navas_loro_2022_6554604,
  author       = {María Navas Loro and
                  Daniel Garijo and
                  Oscar Corcho},
  title        = {Multi-label Text Classification for Public Procurement in Spanish},
  month        = may,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.6554604},
  url          = {https://doi.org/10.5281/zenodo.6554604}
}
```

## Acknowledgements
This work has been supported by NextProcurement European Action and the Madrid Government (Comunidad de Madrid-Spain) under the Multiannual Agreement with Universidad Politécnica de Madrid in the line Support for R&D projects for Beatriz Galindo researchers, in the context of the V PRICIT (Regional Programme of Research and Technological Innovation). 

We would like to thank **Jennifer Tabita** for her contributions to the initial set of notebooks, and the AI4Gov master students for their validation of the approach. 

Source of the data: [Ministerio de Hacienda](https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx).