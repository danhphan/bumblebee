import transformers
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

print(classifier("Let's make a poem"))


generator = pipepline("text-generation")

