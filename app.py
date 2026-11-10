   from flask import Flask, jsonify
   import json, datetime, os

   app = Flask(__name__)
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))

   @app.route('/')
   def index():
       return 'Welcome ENSIA Students from Flask!'

   @app.route('/news.all.get')
   def get_news_all_articles():
       with open(os.path.join(BASE_DIR, 'news_data.json'), 'r') as f:
           data = json.load(f)
       return jsonify(data)

   @app.route('/news.categories.get')
   def get_news_categories():
       now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       return jsonify({
           'title': 'List of Categories',
           'time': now,
           'categories': [
               {'id': 1, 'name': 'Sports'},
               {'id': 2, 'name': 'Politics'},
               {'id': 3, 'name': 'Education'}
           ]
       })

   if __name__ == "__main__":
       app.run(port=8080)
