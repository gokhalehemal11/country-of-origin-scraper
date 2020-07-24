# server.py
# where your python app starts

# init project
from flask import Flask, jsonify, render_template, request
import wikipedia
application = Flask(__name__)


# I've started you off with Flask, 
# but feel free to use whatever libs or frameworks you'd like through `.requirements.txt`.

# unlike express, static files are automatic: http://flask.pocoo.org/docs/0.12/quickstart/#static-files

# http://flask.pocoo.org/docs/0.12/quickstart/#routing
# http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates
@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/search', methods=['GET'])
def get_searches():
	search_results = wikipedia.search(request.args['query'])
	#print(products)
	output = '<ul class="list-unstyled">'
	for res in search_results:
		output+= '<li>'+res+'</li>'
	output+='</ul>'
	return output


# # could also use the POST body instead of query string: http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
@application.route('/searches', methods=['GET'])
def search_brand():
	URL= "https://en.wikipedia.org/wiki/"+request.args['query']
	page= requests.get(URL, headers=headers)
	soup= BeautifulSoup(page.content, 'html.parser')
	output= None

	table_rows= soup.find_all('tr')
	flag= 0
	for row in table_rows:
		header= row.find('th')
		description= row.find('td')
		try:
			#print(header.get_text())
			if('headquarter' in header.get_text().lower() or 'country' in header.get_text().lower()):
				#print(header.get_text(), description.get_text())
				flag= 1
				all_countries= list(pc.countries)
				for country in all_countries:
					#print(country.name)
					if (country.name.lower() in description.get_text().lower() or description.get_text().lower() in country.name.lower() or country.alpha_2 in description.get_text().replace('.','') or country.alpha_3 in description.get_text().replace('.','')):
						#print(header.get_text())
						output= [header.get_text(), description.get_text()]
					else:
						output= [header.get_text(), description.get_text()]

		except Exception as e:
			continue
		
	if(flag == 0):		
		for row in table_rows:
			header= row.find('th')
			description= row.find('td')
			try:
				if('parent' == header.get_text().lower() or 'manufacturer' == header.get_text().lower()):
					#print(description.get_text())
					output= search_wiki(description.get_text())

			except Exception as e:
				continue
	if(output is None):
		output= wikipedia.summary(searched_product, sentences= 5)
	return jsonify(output)
  
# listen for requests :)
if __name__ == "__main__":
	headers={"User-Agent":'Chrome/83.0.4103.106'}
	import requests
	from bs4 import BeautifulSoup
	import pycountry as pc
	import wikipedia
	application.run(debug= True)