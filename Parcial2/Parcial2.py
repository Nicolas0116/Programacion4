from  flask import Flask, jsonify
import pandas as pd
import json

df = pd.read_csv('API_SH.IMM.MEAS_DS2_en_csv_v2_4673017.csv',header=4,lineterminator='\n')
df_p = df[df['Country Name'] == 'Panama']
data = df_p.to_json(orient='records')
x = json.loads(data)
print(x)

app = Flask(__name__)
@app.route('/data',methods=['GET'])
def api_data():
    return jsonify(x)

if __name__ == '__main__':
    app.run(debug=True)