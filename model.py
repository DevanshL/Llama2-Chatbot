import os
import wget

def download_bar(curr, total, width=100):
    print("Downloading %d%% [%d / %d] bytes" % (curr / total * 100, curr, total))

def download_model():
    model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q8_0.gguf"
    hf_token = os.getenv('HF_TOKEN') 
    if hf_token is None:
        raise ValueError("Hugging Face API key not found in environment variables")
    headers = {'Authorization': f'Bearer {hf_token}'}
    model_path = wget.download(model_url, bar=download_bar)
    return model_path

if __name__ == "__main__":
    download_model()
