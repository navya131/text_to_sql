from flask import Flask, render_template, request
from sql_generator import generate_sql

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    generated_query = ""
    prompt = ""

    if request.method == "POST":

        prompt = request.form.get("prompt")

        if prompt:

            generated_query = generate_sql(prompt)

            history.append({
                "prompt": prompt,
                "query": generated_query
            })

    return render_template(
        "index.html",
        generated_query=generated_query,
        history=history,
        prompt=prompt
    )

if __name__ == "__main__":
    app.run(debug=True)