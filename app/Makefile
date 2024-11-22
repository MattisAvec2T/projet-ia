venv:
	@if [ ! -d ".venv" ]; then \
		echo "/// Creating venv... ///"; \
		python3 -m venv .venv; \
		echo "/// .venv created ///"; \
	fi
	@echo "/// To activate venv, run: [ source .venv/bin/activate ] ///"

requirements:
	pip install -r requirements.txt
	pip install --no-cache-dir \
		--index-url https://download.pytorch.org/whl/nightly/cpu \
		torch \
		torchvision \
		torchaudio

ollama :
	ollama pull llama3
	ollama pull mxbai-embed-large