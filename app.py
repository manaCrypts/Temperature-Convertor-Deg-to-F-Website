from flask import Flask, render_template, request

app = Flask(__name__)


def convert_temperature(value: float, unit: str) -> tuple[float, str]:
    if unit == "celsius":
        fahrenheit = (value * 9 / 5) + 32
        return fahrenheit, "Fahrenheit"
    if unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
        return celsius, "Celsius"
    raise ValueError("Unsupported unit")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_unit = "celsius"
    output_unit = "fahrenheit"
    input_value = ""

    if request.method == "POST":
        input_value = request.form.get("temperature", "")
        input_unit = request.form.get("unit", "celsius")
        input_label = "Celsius" if input_unit == "celsius" else "Fahrenheit"
        output_label = "Fahrenheit" if input_unit == "celsius" else "Celsius"

        try:
            value = float(input_value)
            converted_value, _ = convert_temperature(value, input_unit)
            result = {
                "input_value": value,
                "input_unit": input_label,
                "output_value": round(converted_value, 2),
                "output_unit": output_label,
            }
        except ValueError:
            result = {"error": "Please enter a valid number."}

    return render_template("index.html", result=result, input_unit=input_unit, input_value=input_value)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
