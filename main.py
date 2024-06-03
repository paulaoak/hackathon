from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_sum', methods=['POST'])
def check_sum():
    try:
        # Assuming these inputs should be integers
        num1 = int(request.form['input1'])
        num2 = int(request.form['input2'])
        sum_result = """For a detailed experimental setup on the reaction between carbon dioxide (CO₂) and water (H₂O), I found a relevant study that outlines the necessary procedures. The study titled "The catalysis of the reaction between carbon dioxide and water" published in the Journal of the Chemical Society A details various methods used to examine this reaction.
Experimental Setup Overview:
1. Materials and Reagents:
-Pure CO₂ gas.
-Distilled water.
-Various buffers to maintain different pH levels.
2. Apparatus:
-A manometric setup to measure gas pressure changes.
-A reaction vessel equipped with a pH meter.
-Temperature control system to maintain the desired reaction temperature.
-Gas flow controllers to regulate the CO₂ introduction into the reaction vessel.
3. Procedure:
-Preparation: Fill the reaction vessel with a known volume of distilled water. Add buffer solutions to achieve the desired pH levels.
-CO₂ Introduction: Introduce CO₂ gas into the water under controlled conditions. Use gas flow controllers to ensure a steady and precise flow rate.
-Monitoring: Continuously monitor the pressure changes using the manometric system. Simultaneously, measure the pH changes with the pH meter.
-Data Collection: Record the pressure and pH at regular intervals to track the reaction progress. Ensure that temperature remains constant throughout the experiment.
-Catalyst Testing: If catalysts are to be tested, add them to the reaction vessel before introducing CO₂. Observe any changes in reaction rate or equilibrium states.
4. Analysis:
-Analyze the pressure and pH data to determine the rate of CO₂ absorption and conversion into carbonic acid (H₂CO₃).
-Evaluate the effect of different pH levels and buffer compositions on the reaction kinetics.
5. Safety Considerations:
-Ensure proper ventilation to avoid CO₂ accumulation.
-Use personal protective equipment (PPE) such as gloves and safety goggles.
For more detailed information and specific data, you can access the full study through the Royal Society of Chemistry's website: https://pubs.rsc.org/en/content/articlelanding/1966/j1/j19660000812
This setup allows for a controlled examination of the interaction between CO₂ and H₂O, providing insights into the reaction kinetics and mechanisms."""
        return render_template('index2.html', sum_result=sum_result)
    except ValueError:
        return render_template('index2.html', error_message='Please enter valid numbers!')

if __name__ == '__main__':
    app.run(debug=True)
