#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask
app = Flask(__name__)


# In[7]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        bedroom = request.form.get("bedroom")
        bathroom = request.form.get("bathroom")
        floor_area = request.form.get("floor_area")
        distance = request.form.get("Distance (km)")
        age = request.form.get("Age")
        school = request.form.get("school")
        if school == "Yes":
            near_school = 1
        else:
            near_school = 0           
        print(bedroom, bathroom, floor_area, distance, age, school)
        model = joblib.load("Housing Estimates XG")
        pred = model.predict([[float(bedroom), float(bathroom), float(floor_area), float(distance), float(age), float(near_school)]])
        s = f""" You have entered the following details:
    Number of bedrooms: {bedroom}
    Number of bathrooms: {bathroom}
    Estimated floor area: {floor_area}
    Distance from CBD: {distance} km
    Preferred age of house: {age} years
    Any school-going children? {school}
The predicted house price will be {str(pred[0])} """
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Model loading..."))


# In[5]:


if __name__== "__main__":
    app.run()


# In[ ]:




