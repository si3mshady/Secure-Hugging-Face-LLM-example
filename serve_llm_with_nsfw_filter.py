from flask import Flask, request, jsonify
import json
from transformers import pipeline
from transformers import pipeline, TFAutoModelForSequenceClassification, AutoTokenizer



app = Flask(__name__)


model_name = "michellejieli/NSFW_text_classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSequenceClassification.from_pretrained(model_name, from_pt=True)



# Create the pipeline using the loaded model
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
question_answerer = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')

# Now you can use the classifier as before

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the request body from the Flask request
        request_body = request.get_json()

        print(request_body['body'])

        request_body['body']
        req_dict=json.loads(request_body['body'])

        

        # Perform sentiment analysis
        sentiment_result = classifier(req_dict['inputs']['question'])
        print(sentiment_result)

        question = req_dict['inputs']['question']
        context =  req_dict['inputs']['context']

        print(question)
        print(context)

        # Check for NSFW content
        if sentiment_result[0]['label'] == "NSFW":
            return jsonify({'error': 'NSFW content detected'}), 400
        

        if sentiment_result[0]['label'] == "SFW":
    
             # Prepare data for SageMaker in the required format
            result = question_answerer(question=question,     context=context)
            print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

            return jsonify(result['answer']), 200
            

    except Exception as e:
        # Handle any exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run(debug=True)
   

# https://huggingface.co/docs/transformers/installation
# https://huggingface.co/docs/sagemaker/inference !!!
# https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-real-time.html

