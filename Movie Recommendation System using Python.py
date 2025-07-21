# Simple Content-Based Recommendation System

movies = {
    "Inception": "dream technology action thriller",
    "Interstellar": "space time science fiction",
    "The Matrix": "virtual reality hacker science fiction",
    "Titanic": "romance ship drama",
    "The Notebook": "love romance drama",
    "The Avengers": "superheroes action team",
}

def recommend(movie_name):
    movie_desc = movies.get(movie_name)
    if not movie_desc:
        return "Movie not found."

    recommendations = []
    for title, desc in movies.items():
        if title == movie_name:
            continue
        # Count common words
        common_words = set(movie_desc.split()) & set(desc.split())
        score = len(common_words)
        recommendations.append((title, score))

    # Sort by score and return top matches
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [title for title, score in recommendations if score > 0]

# Try it
movie = "Inception"
recommended = recommend(movie)

print(f"Because you liked '{movie}', you might also like:")
for r in recommended:
    print("- " + r)
