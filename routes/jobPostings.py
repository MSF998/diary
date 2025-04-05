from flask import Blueprint, render_template, request, jsonify
import json
import os

job_postings_bp = Blueprint('job_postings', __name__)

@job_postings_bp.route('/job-postings')
def job_postings():
    #Aggregate job postings from various sites
    """
    Product Based or Service Based
    Company Name
    Position Name
    Date posted
    YOE Required
    Location
    """
    return "Scrape Job Postings Here"