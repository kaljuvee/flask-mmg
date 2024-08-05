from flask import Blueprint, render_template, url_for, request, redirect

bp = Blueprint("treatments", __name__)

@bp.route('/orthopaedics')
def orthopaedics():
    return render_template('treatments/orthopaedics/orthopaedics.html')

@bp.route('/orthopaedics/get-quote', methods=['GET', 'POST'])
@bp.route('/orthopaedics/get_quote', methods=['GET', 'POST'])
def orthopaedics_get_quote():
    if request.method == 'POST':
        treatment_type = request.form.get('treatmentType')
        if treatment_type:
            # Here you can implement the logic to get the quote based on the treatment type
            # For now, we'll just redirect to the results page with the treatment type as a query parameter
            return redirect(url_for('treatments.orthopaedics_quote_results', treatment_type=treatment_type))
    return render_template('treatments/orthopaedics/get_quote.html')

@bp.route('/orthopaedics/quote-results')
@bp.route('/orthopaedics/quote_results')
def orthopaedics_quote_results():
    treatment_type = request.args.get('treatment_type')
    # Implement the logic to display the quote results based on the treatment type
    return render_template('treatments/orthopaedics/quote_results.html', treatment_type=treatment_type)