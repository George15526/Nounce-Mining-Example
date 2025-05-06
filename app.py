from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
import random

app = Flask(__name__)

def mine(length):
  temp = ''
  for i in range(length):
    temp += str(random.randint(0, 1))
    
  print(temp)
  return temp

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    data = request.form.to_dict()
    hash_code = data['hashCode']
    print(hash_code)
    
    length = len(hash_code)
    
    results = {}
    id = 1
    while True:
      temp = mine(length)
      results[id] = temp
      if temp == hash_code:
        return render_template('index.html', total=id, results=results)
      id += 1
    
  return render_template('index.html')


if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=8000,
    debug=True
  )