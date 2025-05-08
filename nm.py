import openai
from flask import Flask, request, jsonify

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        chatbot_reply = response.choices[0].message['content'].strip()
        return jsonify({'response': chatbot_reply})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
