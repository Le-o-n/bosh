<p align="center">
  <img src=".readme/images/bosh_title.png" alt="BOSH Title Banner">
</p>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.18776178">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.18776178.svg" alt="DOI">
  </a>
  <a href="https://github.com/Le-o-n/bosh/releases">
    <img src="https://img.shields.io/github/v/release/Le-o-n/bosh" alt="Release">
  </a>
  <a href="https://github.com/Le-o-n/bosh/stargazers">
    <img src="https://img.shields.io/github/stars/Le-o-n/bosh" alt="Stars">
  </a>
  <a href="https://github.com/Le-o-n/bosh/network/members">
    <img src="https://img.shields.io/github/forks/Le-o-n/bosh" alt="Forks">
  </a>
</p>

Brain Optical Segmentation Helper (BOSH) is a collection of Open Neural Network Exchange (ONNX) segmentation models trained for MRI-based segmentation tasks.

---

## 🧠 Model Catalogue

| Status | Example | Model Name                         | Params (10⁶) | Size (MB) | Axis  | Weighting | Function |
|------------------------------------|--------------:|-----------:|-------|-----------|--------------------|--------|----------|
| 🟢  | ![T2 Example](models/bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0.gif) | `bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0.onnx`     | 14.3          | 54.6      | Axial | T2-SE       | Brain segmentation |


> 🟢 Implemented 🔵 In Development ⚪ Planned

## 📚 Citation

If you use BOSH in your research or tool, please cite it using the following:

```bibtex
@software{bass2026bosh,
  author    = {Bass, Leon},
  title     = {BOSH: Brain Optical Segmentation Helper},
  month     = feb,
  year      = {2026},
  publisher = {Zenodo},
  version   = {v1.0.0},
  doi       = {10.5281/zenodo.18776178},
  url       = {https://doi.org/10.5281/zenodo.18776178},
  note      = {ORCID: 0009-0009-2158-9612}
}
```
