import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")

print("Path to dataset files:", path)
#I moved the csv file to the free_coding folder

def read_file(csv):
    "reads the csv file dataset and splits it into lists by '\n'."
    with open(csv, "r") as file:
        csv_file = file.readlines()
        new_csv = []
        id_list = []
        for i in csv_file:
            new_i = i.split(',')
            if new_i[0] in id_list:
                continue
            new_csv.append(new_i)
            id_list.append(new_i[0])
    return new_csv

def make_dictionary(csv_file):
    dict_list = []
    for i in range(1,len(csv_file)):
        if len(csv_file[i]) == 23:
            dict = {
                'track_id': csv_file[i][0],
                'track_name': csv_file[i][1],
                'track_artist': csv_file[i][2],
                'track_popularity': csv_file[i][3],
                'genre': csv_file[i][9],
                'danceability': csv_file[i][11],
                'energy': csv_file[i][12],
                'key': csv_file[i][13],
                'loudness': csv_file[i][14],
                'speechiness': csv_file[i][16],
                'acousticness': csv_file[i][17],
                'instrumentness': csv_file[i][18],
                'liveness': csv_file[i][19],
                'valence': csv_file[i][20],
                'tempo': csv_file[i][21],
            }
            dict_list.append(dict)

def input_preference():
    energy = int(input("Do you like energetic songs? Rate from 1(low) to 3(high)\n"))
    genre = input("What kind of genre do you prefer? Choose from: edm, r&b, latin, rock, rap, pop\n")
    tempo = int(input("Do you like fast tempo or slow tempo? Type 1 for fast and 2 for slow\n"))
    popularity = input("Looking for top track songs or want to discover new songs? Type T or N\n")
    if energy not in [1, 2, 3]:
        raise ValueError("Energy must be between 1 and 3.")
    if genre.lower() not in ['edm', 'r&b', 'latin', 'rock', 'rap', 'pop']:
        raise ValueError("Genre must be one of the specified options.")
    if tempo not in [1, 2]:
        raise ValueError("Tempo must be either 1 or 2.")
    if popularity.lower() not in ['t', 'n']:
        raise ValueError("Popularity must be either T or N.")
    return energy, genre.lower(), tempo, popularity.lower()

def filter_energy(energy,dict_list):
def filter_energy(energy, dict_list):
    energy_list = []
    if energy == 1:
        energy_list = [d for d in dict_list if float(d['energy']) <= 0.3]
    elif energy == 2:
        energy_list = [d for d in dict_list if 0.3 < float(d['energy']) <= 0.6]
    elif energy == 3:
        energy_list = [d for d in dict_list if float(d['energy']) > 0.6]
    return energy_list

def filter_genre(genre, energy_list):
    genre_and_energy = [d for d in energy_list if d['genre'].lower() == genre]
    return genre_and_energy

def filter_tempo(tempo, genre_and_energy):
    temp_genre_energy = []
    if tempo == 1:
        temp_genre_energy = [d for d in genre_and_energy if float(d['tempo']) <= 80]
    elif tempo == 2:
        temp_genre_energy = [d for d in genre_and_energy if 80 < float(d['tempo']) <= 120]
    return temp_genre_energy


def recommend_song_popular_or_no(popularity, tempo_genre_energy):
    if popularity == 't':
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'], reverse=True)
    else:
        return sorted(tempo_genre_energy, key=lambda x: x['track_popularity'])




def main():
dataset = 'spotify_songs copy.csv'
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
