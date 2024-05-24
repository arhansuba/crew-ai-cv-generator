#!/bin/zsh

# variables
model_name="llama3:8b"

custom_model_name="crewai-llama3:8b"

#get the base model
ollama pull $model_name

#create the model file
ollama create $custom_model_name -f ./Llama2ModelFile