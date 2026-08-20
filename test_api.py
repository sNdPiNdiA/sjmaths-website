import os
import json
import urllib.request

api_key = os.environ.get('GEMINI_API_KEY')
if not api_key and os.path.exists('.env'):
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('GEMINI_API_KEY='):
                api_key = line.split('=', 1)[1].strip()

# Testing gemini-2.5-flash / gemini-2.0-flash / gemini-1.5-flash
for model in ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash']:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
    data = {
        'contents': [{'parts': [{'text': 'Return JSON: {"status": "success", "model": "' + model + '"}'}]}],
        'generationConfig': {'responseMimeType': 'application/json'}
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f'✅ Model {model} succeeded:', res['candidates'][0]['content']['parts'][0]['text'].strip())
            break
    except Exception as e:
        print(f'❌ Model {model} failed:', str(e))
