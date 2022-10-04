#%%
import BLIP.models.blip as blip

#%%
blip_model = blip.blip_decoder(
    pretrained="https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base.pth")
blip_model.eval()
blip_model = blip_model.to(device)
