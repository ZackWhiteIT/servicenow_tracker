# -*- coding: utf-8 -*-
"""User views."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required
from servicenow_tracker.user.forms import TicketForm
from servicenow_tracker.utils import flash_errors

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")


@blueprint.route("/my_tickets/", methods=["GET", "POST"])
@login_required
def my_tickets():
    """Tickets page."""
    form = TicketForm(request.form)
    # Create ticket
    if request.method == "POST":
        if form.validate_on_submit():
            create_ticket(form.user)
            flash("Ticket created", "success")
            redirect_url = request.args.get("next") or url_for("user.my_tickets")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("users/my_tickets.html", form=form)

