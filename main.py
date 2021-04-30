from flask import Flask, request, make_response, jsonify, render_template, session, redirect, url_for
import requests
import custom_payload

app = Flask(__name__)

@app.route("/")
def home_view():
    return "<h1>Welcome to Geeks for Geeks</h1>"
    
@app.route('/webhook', methods=['GET','POST'])
def whook():
    req = request.get_json(silent=True, force=True)
    
    query_result = req.get('queryResult')
    
    # if query_result.get('action') == 'subchapter':
    #     text = "Please select subchapter"
    #     return custom_payload.general_horizontal_cards(text)
    if query_result.get('action') == 'select.chapter':
        app.logger.info(query_result)
        text = "Please select the following chapter."
        return custom_payload.chapter_list(text)
    
    if query_result.get('action') == 'select.subchapter':
        app.logger.info(query_result)
        # text = "Please select subchapter"
        return custom_payload.file_selector()
    

if __name__ == "__main__":
    
    app.run(debug = True, port = 5000)
