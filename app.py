#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)


# In[2]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        bedroom = request.form.get("bedroom")
        bathroom = request.form.get("bathroom")
        garage = request.form.get("garage")
        floor_area = request.form.get("floor_area")
        distance = request.form.get("Distance (km)")
        school = request.form.get("school")
        if school == "Yes":
            near_school = 1
        else:
            near_school = 0           
        print(bedroom, bathroom, garage*1000, floor_area, distance, school)
        model = joblib.load("Housing Estimates Model")
        pred = model.predict([[float(bedroom), float(bathroom), float(garage)*1000, float(floor_area), float(distance), float(near_school)]])
        s = f""" You have entered the following details:
    Number of bedrooms: {bedroom}
    Number of bathrooms: {bathroom}
    Number of garage: {garage}
    Estimated floor area: {floor_area}
    Distance from CBD: {distance} km
    Any school-going children? {school}
The predicted house price will be {str(pred[0])} """
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Model loading..."))


# In[3]:


if __name__== "__main__":
    app.run()

