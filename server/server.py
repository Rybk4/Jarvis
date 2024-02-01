from flask import Flask, render_template, request, jsonify
import controls1.volume as v

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_ajax.html')

@app.route('/switch', methods=['POST'])
def switch():
    switch_id = request.form['switch_id']
    action = request.form['action']

    if action == 'on':
        switch_on(switch_id)
    elif action == 'off':
        switch_off(switch_id)

    return jsonify({'result': 'success'})

def switch_on(switch_id):
    if switch_id == 'switch1':
        v.volumeMax()
        
        
def switch_off(switch_id):
    if switch_id == 'switch1':
        v.volumeMute()

if __name__ == '__main__':
    app.run(debug=True)
