import pandas as pd
# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")

# Assuming the CSV file is in the same directory as the script
path = 'spotify_songs copy.csv'

def read_file(csv):
def read_file(csv):
    """Reads the CSV file dataset and splits it into lists by '\n'."""
    df = pd.read_csv(csv)
    return df.drop_duplicates(subset='track_id').values.tolist()

def make_dictionary(df):
    dict_list = [{'track_id': row[0], 'track_name': row[1], 'track_artist': row[2],
                 'track_popularity': row[3], 'genre': row[9], 'danceability': row[11],
                 'energy': row[12], 'key': row[13], 'loudness': row[14],
                 'speechiness': row[16], 'acousticness': row[17], 'instrumentness': row[18],
                 'liveness': row[19], 'valence': row[20], 'tempo': row[21]}
                for index, row in df.iterrows()]
    return dict_list
    return dict_list
def input_preference():
    energy = int(input("Do you like energetic songs? Rate from 1(low) to 3(high)
"))
    genre = input("What kind of genre do you prefer? Choose from: edm ,r&b, latin, rock, rap, pop
")
    tempo = int(input("Do you like fast tempo or slow tempo? Type 1 for fast and 2 for slow
"))
    popularity = input("Looking for top track songs or want to discover new songs? Type T or N
")
    return energy, genre, tempo, popularity

def filter_energy(energy, dict_list):
    return [d for d in dict_list if float(d['energy']) <= (0.3 + 0.6 * energy / 2)]


def filter_genre(genre, energy_list):
    return [d for d in energy_list if d['genre'] == genre]


def filter_tempo(tempo, genre_and_energy):
    return [d for d in genre_and_energy if float(d['tempo']) <= (80 + 40 * tempo)]
    return  temp_genre_energy
def recommend_song_popular_or_no(popularity, tempo_genre_energy):
    if popularity == 'Y':
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'])
    else:
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'], reverse=True)



def main():
    dataset = 'spotify_songs copy.csv'
    df = pd.read_csv(dataset)
    dict_data = make_dictionary(df)
    energy, genre, tempo, popularity = input_preference()
    filtered_data = filter_energy(energy, dict_data)
    filtered_data = filter_genre(genre, filtered_data)
    filtered_data = filter_tempo(tempo, filtered_data)
    recommended_songs = recommend_song_popular_or_no(popularity, filtered_data)
    print("Try these 5 songs!")
    for song in recommended_songs[:5]:
        print(f"{song['track_name']} by {song['track_artist']} id: {song['track_id']}")
    main()
