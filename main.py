from flask import Flask, jsonify, request
from storage import all_articles,liked_articles, not_liked_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(all_articles[12])

@app.route("/")
def get_articles():
    articles_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13] or "N/A",
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15],
    }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    articles = all_articles[0]
    liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_articles():
    articles = all_articles[0]
    not_liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    articles_data = []
    for articles in output:
        _d = {
            "url": articles[0],
            "title": articles[1],
            "text": articles[2] or "N/A",
            "lang": articles[3],
            "total_events": articles[4],
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_articles in liked_articles:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    articles_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2] or "N/A",
            "lang": recommended[3],
            "total_events": recommended[4],
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()




if __name__ == "__main__":
      app.run()

