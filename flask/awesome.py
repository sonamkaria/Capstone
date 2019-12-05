# imports
import pandas as pd
import pickle
import numpy as np
import os

from flask import Flask, request, Response, render_template, jsonify

# initialize the flask app
app = Flask('myApp')

### route 4: show a form to the user
# define the route
@app.route('/form')
# create the controller
def form():
    # return the view
    return render_template('form.html', combined_scores1= "", combined_scores2= "", combined_scores3= "")


# define the route
@app.route('/submit')
# create the controller
def submit():
    user_input = request.args
    book_name = user_input['book-title']
    data = str(book_name)

    recommender_df = pd.read_csv(os.getcwd() + '/assets/recommender_1.csv', index_col = 'book_name')
    recommender_df_2 = pd.read_csv(os.getcwd() + '/assets/recommender_2.csv', index_col = 'book_name')


# recommender function
    def average_similar_books(book_name):
        list_1 = list(recommender_df[book_name].sort_values()[1:6].index)
        list_2 = list(recommender_df_2[book_name].sort_values()[1:6].index)

        intersection = list(set(list_1).intersection(set(list_2)))
        intersection_recommender_1 = recommender_df.loc[list_1,:][book_name][intersection]
        intersection_recommender_2 = recommender_df_2.loc[list_2,:][book_name][intersection]

        average_scores = (intersection_recommender_1 + intersection_recommender_2) /2
        first_recommender_scores = recommender_df.loc[list_1,:][book_name].drop(labels = intersection)
        second_recommender_scores = recommender_df_2.loc[list_2,:][book_name].drop(labels = intersection)

        book_results = pd.concat([average_scores,first_recommender_scores,second_recommender_scores], axis = 0).sort_values(ascending = True)
        combined_scores = list(book_results.index)[:3]
        return combined_scores



    combined_scores1 = average_similar_books(data)[0]
    combined_scores2 = average_similar_books(data)[1]
    combined_scores3 = average_similar_books(data)[2]
    # print (combined_scores)
    # return the view
    return render_template('form.html', combined_scores1= combined_scores1, combined_scores2= combined_scores2, combined_scores3= combined_scores3)


# run the app
if __name__ == '__main__':
	app.run(debug=True)
