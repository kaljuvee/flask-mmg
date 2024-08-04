from flask import Blueprint, render_template, url_for

bp = Blueprint("treatments", __name__)

@bp.route('/orthopaedics')
def orthopaedics():
    return render_template('treatments/orthopaedics/orthopaedics.html')

@bp.route('/orthopaedics/get-quote')
@bp.route('/orthopaedics/get_quote')
def orthopaedics_get_quote():
    # Implement the logic for getting a quote
    return render_template('treatments/orthopaedics/get_quote.html')