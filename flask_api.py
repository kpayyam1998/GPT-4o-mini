import os
from flask import Flask,jsonify,request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

@app.route("/api/gpt4omini" , methods=['POST','GET'])
def getResponse():

    # We are going to use make request gpt4omini
    try:
        key=os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key=key)
        data=request.get_json()
        prompt=data.get('prompt')
        if prompt:

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system","content": "you are a helpfull assistent"},
                    {"role": "user", "content": prompt}
                ]
            )
        else:
            raise ValueError("Please enter your promot")

        response=completion.choices[0].message.content

        return jsonify(message=response),200
    except ValueError as e:
        return jsonify(error=str(e)),400
    
if __name__=="__main__":
    app.run(debug=True)