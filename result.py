from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect_random_numbers():
    data = request.get_json()
    number = data.get('number')
    
    with open('result.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number])

    return 'Number saved to CSV'

if __name__ == '__main__':
    app.run()
