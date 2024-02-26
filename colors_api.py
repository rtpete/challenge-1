from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/colors', methods=['GET'])
def get_colors():
    colors = ['Red to Green', 'Green to Red', 'Blue to Orange', 
              'Orange to Blue', 'Purple to Yellow', 'Yellow to Purple']
    return jsonify(colors)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1:5000')
