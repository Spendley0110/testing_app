import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")

print("Path to dataset files:", path)
#I moved the csv file to the free_coding folder

def read_file(csv):
    with open(csv, 'r') as file:
        csv_file = file.readlines()
    header = csv_file[0].strip().split(',')
    data = [dict(zip(header, line.strip().split(','))) for line in csv_file[1:]]
    return data

def make_dictionary(csv_file):
    return [{'track_id': d['id'], 'track_name': d['name'], 'track_artist': d['artist'], 'track_popularity': d['popularity'],
              'genre': d['genre'], 'danceability': d['danceability'], 'energy': d['energy'], 'key': d['key'],
              'loudness': d['loudness'], 'speechiness': d['speechiness'], 'acousticness': d['acousticness'],
              'instrumentness': d['instrumentness'], 'liveness': d['liveness'], 'valence': d['valence'], 'tempo': d['tempo']}
             for d in csv_file if len(d) == 23]

def input_preference():
def input_preference():
    energy = int(input('Do you like energetic songs? Rate from 1(low) to 3(high): '))
    genre = input('What kind of genre do you prefer? Choose from: edm, r&b, latin, rock, rap, pop: ').lower()
    tempo = int(input('Do you like fast tempo or slow tempo? Type 1 for fast and 2 for slow: '))
    popularity = input('Looking for top track songs or want to discover new songs? Type T for top or N for new: ').upper()
    return energy, genre, tempo, popularity

def filter_energy(energy,dict_list):
def filter_energy(energy, dict_list):
    energy_thresholds = {1: 0.3, 2: 0.6, 3: float('inf')}
    return [d for d in dict_list if float(d['energy']) <= energy_thresholds[energy]]

def filter_genre(genre, energy_list):
    return [d for d in energy_list if d['genre'] == genre]

def filter_tempo(tempo, genre_and_energy):
    tempo_thresholds = {1: 80, 2: 120, 3: float('inf')}
    return [d for d in genre_and_energy if float(d['tempo']) <= tempo_thresholds[tempo]]


def recommend_song(popularity, tempo_genre_energy):
    if popularity == 'Y':
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'])
    else:
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'], reverse=True)



def main():
dataset = input('Enter the path to the dataset file: ')
    dataset_list = read_file(dataset)
    dict_data = make_dictionary(dataset_list)
    #print(dict_data)
    energy, genre, tempo, popularity = input_preference()
    energy_list = filter_energy(energy,dict_data)
    genre_and_energy = filter_genre(genre, energy_list)
    tempo_and_genre_and_energy = filter_tempo(tempo, genre_and_energy)
    popularity_sorted = recommend_song_popular_or_no(popularity, tempo_and_genre_and_energy)
    print("Try these 5 songs!")
    for dict in popularity_sorted[:5]:
        print(f"{dict["track_name"]} by {dict["track_artist"]} id: {dict["track_id"]}")






if __name__ == '__main__':
    main()
