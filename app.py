from flask import Flask, render_template, request

app = Flask(__name__)

def bionic_reading(text):
    words = text.split()
    bionic_text = []
    for word in words:
        bold_part = word[:len(word)//2]
        normal_part = word[len(word)//2:]
        bionic_text.append(f"<strong>{bold_part}</strong>{normal_part}")
    return ' '.join(bionic_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    bionic_text = ""
    if request.method == 'POST':
        text = request.form['text']
        if text:
            bionic_text = bionic_reading(text)
            print(f"Text input: {text[:200]}...")  # Debugging print
    return render_template('index.html', bionic_text=bionic_text)

if __name__ == '__main__':
    app.run(debug=True)
