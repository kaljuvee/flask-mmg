from flask import Blueprint, render_template, url_for, request, redirect, session

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

@bp.route('/patient')
def patient_information():
    session_state_defaults = {
        'first_name': '',
        'last_name': '',
        'email': '',
        'phone': '',
        'problem': '',
        'urgency': 'As soon as possible - within 6 weeks',
        'call_you': 'No',
        'financing': 'Self financed',
        'preferred_countries': ['Lithuania', 'Poland', 'Romania',  'Portugal', 'Spain'],
        'validated': 'No'
    }

    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['phone'] = request.form['phone']
        session['problem'] = request.form['problem']
        session['validated'] = request.form['validated']
        session['urgency'] = request.form['urgency']
        session['call_you'] = request.form['call_you']
        session['financing'] = request.form['financing']
        session['preferred_countries'] = request.form.getlist('preferred_countries')

        if request.form['action'] == 'submit':
            return redirect(url_for('treatments.view_quote'))
        elif request.form['action'] == 'more_info':
            return redirect(url_for('user.account'))

    all_countries = [
        'Bulgaria', 'Croatia', 'Czech Republic', 'Estonia', 'Hungary', 'Latvia', 
        'Lithuania', 'Poland', 'Romania', 'Slovakia', 'Slovenia', 'Albania', 
        'Bosnia and Herzegovina', 'Greece', 'Italy', 'North Macedonia', 'Portugal', 'Spain', 'Serbia'
    ]

    return render_template('treatments/patient_information.html', session_state=session_state_defaults, all_countries=all_countries)
