from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from flask import current_app
import threading

class Generator:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.model_name = current_app.config.get("MODEL_NAME")
        self._load()

    def _load(self):
        # Load tokenizer and model once. Uses transformers + torch.
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.pipe = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer, device=-1)

    @classmethod
    def get(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance

    def generate(self, prompt: str, max_length: int = 200, temperature: float = 0.9, top_k: int = 40, num_return_sequences: int = 1):
        out = self.pipe(prompt, max_length=max_length, do_sample=True, temperature=temperature, top_k=top_k, num_return_sequences=num_return_sequences)
        # each element has 'generated_text'
        return [r["generated_text"] for r in out]
