
# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        carat = float(request.form['carat'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        
        
        # cut
        if(cut == "Good"):
            cut = 1
        elif(cut == "Ideal"):
            cut = 2 
        elif(cut == "Premium"):
            cut = 3
        elif(cut == "Very Good"):
            cut = 4           
        else:
            cut = 0


        # clarity
        if(clarity == "lF"):
            clarity = 1
        elif(clarity == "Sl1"):
            clarity = 2 
        elif(clarity == "Sl2"):
            clarity = 3
        elif(clarity == "VS1"):
            clarity = 4    
        elif(clarity == "VS2"):
            clarity = 5
        elif(clarity == "VVS1"):
            clarity = 6
        elif(clarity == "VVS2"):
            clarity = 7                        
        else:
            clarity = 0


        # color
        if(color == "E"):
            color = 1
        elif(color == "F"):
            color = 2 
        elif(color == "G"):
            color = 3
        elif(color == "H"):
            color = 4    
        elif(color == "I"):
            color = 5
        elif(color == "J"):
            color = 6                       
        else:
            color = 0    
            
        prediction = model.predict([[cut, color, clarity, carat, depth, table, x, y, z]])

        
        return render_template('prediction.html', prediction_text='Diamond Price is $ {}'.format(prediction))

    else:
        return render_template('prediction.html')


if __name__ == "__main__":
    app.run(debug=True)
