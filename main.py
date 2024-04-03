from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Калькулятор площади</title>
</head>
<body>
    <h1>Калькулятор площади прямоугольника</h1>
    <form method="post">
        <label for="width">Ширина:</label>
        <input type="number" id="width" name="width" required>
        <label for="height">Высота:</label>
        <input type="number" id="height" name="height" required>
        <input type="submit" value="Рассчитать">
    </form>
    {% if area %}
    <p>Площадь прямоугольника: {{ area }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculate_area():
    area = None
    if request.method == 'POST':
        width = float(request.form.get('width'))
        height = float(request.form.get('height'))
        area = width * height
    return render_template_string(HTML_FORM, area=area)

if __name__ == '__main__':
    app.run(debug=True)