# Download model
import wget
import json

def download_bar(curr,total,width=100):
  print("Downloading %d%% {%d / %d} bytes" % (curr / total * 100, curr, total))

def download_model():
    model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q8_0.gguf"
    config = json.load(open('config.json'))
    hf_token = config['HF_TOKEN']
    model_path = wget.download(model_url, bar=download_bar)
    return model_path
