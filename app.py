import time
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
    t_start = time.perf_counter()
    data = request.form.to_dict()
    hash_code = data['hashCode']
    
    for i in hash_code:
      if i != '0' and i != '1':
        alert_msg = '只允許輸入0或1，請重新輸入'
        return render_template('index.html', alert_msg=alert_msg)
    
    print(hash_code)
    
    length = len(hash_code)
    
    results = {}
    id = 1
    while True:
      temp = mine(length)
      results[id] = temp
      if temp == hash_code:
        execution_time = f'{time.perf_counter() - t_start: .8f}'
        print(f'execution_time: {time.perf_counter() - t_start: .8f}s')
        return render_template('index.html', hash_code=hash_code, total=id, results=results, execution_time=execution_time)
      id += 1
    
  return render_template('index.html')


if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    port=8000,
    debug=True
  )