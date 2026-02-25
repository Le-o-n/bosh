## Model Card for bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0

### Short summary
Lightweight brain tissue segmentation model for 2D T2‑weighted axial TSE head MRI scans. Inputs: 2D axial T2 slices. Outputs: per‑pixel segmentation map of brain tissue regions.

## Model Details

- **Model name / version:** bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0 
- **Developed by:** Leon Bass (https://orcid.org/0009-0009-2158-9612), Warwick Manufacturing Group (WMG), University of Warwick  
- **Repository:** https://github.com/Le-o-n/bosh  
- **Hugging Face:** https://huggingface.co/LeonBass/bosh-resnet18-axial-smri-t2_se-seg-brain-fp32 
- **Backup / archival:** Zenodo (DOI to be added after GitHub release)  
- **Demo:** models/bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0.ipynb in the GitHub repo  
- **License:** see  
- **Weights hosted:** GitHub release and Hugging Face model repo

## One-line purpose
Per‑slice pixelwise segmentation of brain tissue from 2D T2‑weighted axial MRI (TSE) scans.

## Model Description
Residual convolutional U‑Net style architecture with residual encoder → decoder blocks. Parameter count: 14.3x10^6 parameters, 54.6 MB weight size on disk. Designed to be lightweight and run on consumer GPUs.

## Model Sources
- **Repository:** https://github.com/Le-o-n/bosh  
- **Paper / citable publication:** Working citation (related): Bass L., Goswami A., Mohammad, K. F., Olaizola, I. G., Harrington K., Chalmers A., "The potential of Flavour Perception Ability testing to detect early the presence of Alzheimer’s Disease" 

## Uses

- Direct use: slice‑level brain tissue segmentation for research, visualisation, preprocessing pipelines, or human-in-the-loop annotation assistance.
- Downstream use: can be used as an initialisation for further fine‑tuning on task‑specific segmentation datasets.

## Bias, Risks, and Limitations
- Trained on data from 20 patients only — limited diversity and poor generalization expected to other scanners, protocols, populations, age groups.
- Failure modes: preprocessing distribution shifts (e.g., applying z‑scoring → min‑max → z‑scoring or inconsistent intensity scaling) can produce inaccurate outputs.
- Not evaluated on held‑out external test cohorts; accuracy and robustness are uncertain.
- Labels were produced by the developer (single annotator), potential annotation bias.

### Recommendations
- Validate on your own local test data before any downstream use.
- Use human review for all outputs, especially on out‑of-distribution scans.
- Standardise preprocessing to the pipeline used during training (see “Preprocessing” below).

## How to get started
- Clone the repo: https://github.com/Le-o-n/bosh  
- See demo notebook: `models/bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0.ipynb` for example inference code and usage.
- Model weights and model card available in the GitHub release and Hugging Face repo; Zenodo DOI will be added to this card after archiving.

## Training Details

### Training data
- Source: Private dataset collected by the author.
- Subjects: 20 patients.
- Slices: ~30 axial T2 slices per scan (per‑slice labels).
- Labels: Per‑pixel segmentation produced by the author.
- Split: 80% train, 20% validation (no formal external test split).

### Preprocessing
- Typical preprocessing used during training: intensity normalization (z‑score) and augmentation pipeline including cropping, rotation, additive noise, and translation. NOTE: inconsistent or compound normalization steps (e.g., z‑score → min‑max → z‑score) cause distribution shift and model failure.

### Training procedure
- Hardware: NVIDIA GeForce RTX 3060 Ti (8 GB VRAM).
- Training time: ~1 day.
- Mixed precision: not specified.
- Hyperparameters: optimizer, learning rate schedule, batch size, number of epochs — [PLACEHOLDER — insert exact values].

## Evaluation

### Architecture & objective
- Residual convolutional encoder–decoder (U‑Net style) with residual blocks. Objective: per‑pixel segmentation (cross‑entropy / Dice loss).

### Compute infrastructure
- Single consumer GPU (RTX 3060 Ti), local workstation.


## Citation

**Suggested citation:**

```
BibTeX:

@software{bass2026bosh_model,
  author  = {Bass, Leon},
  title   = {Brain Optical Segmentation Helper (BOSH): ResNet18 Axial T2-SE Brain Model},
  year    = {2026},
  version = {v1.0.0},
  doi     = {10.5281/zenodo.XXXXXXXX},
  url     = {https://doi.org/10.5281/zenodo.XXXXXXXX}
}

```

## Model card authors / contact
- Author: Leon Bass (https://orcid.org/0009-0009-2158-9612), WMG, University of Warwick  
- Contact: open GitHub issues on the repository

## Additional files to include
- CITATION.cff (recommended)
- requirements.txt / environment.yml
- License file with exact non‑commercial research terms



