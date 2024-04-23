FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords
CMD ["python", "word_freq_analysis.py"]