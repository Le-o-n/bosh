import segmentation_models_pytorch as smp
import torch

model = smp.Unet(
    encoder_name="resnet18",
    encoder_weights=None,
    in_channels=1,
    classes=1
)

state_dict = torch.load(
    "bosh.resnet18.axial.smri.t2_se.seg.brain.fp32.v1.0.0.pt",
    map_location="cpu",
    weights_only=True  # PyTorch >= 2.0
)

model.load_state_dict(state_dict)
model.eval()