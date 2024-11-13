import csv

# Extraccion de Metodos 
def process_votes(file_path):
    results = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 

        # Renombrar las variables de las filas para saber que fila esta iterando
        for city, candidate, vote_count in reader:
            # Simplificacion de condicionales
            votes = int(vote_count) if vote_count.isdigit() else 0
            # Simplificacion de codigo al utilizar el get
            results[candidate] = results.get(candidate, 0) + votes
    return results

def display_results(results):
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

def find_winner(results):
    # utilizar max en lugar de sorted para simplificar
    max_votes = max(results.values())
    winners = [candidate for candidate, votes in results.items() if votes == max_votes]
    return winners


def count_votes(file_path):
    results = process_votes(file_path)
    display_results(results)
    winners = find_winner(results)
    if len(winners) == 1:
        print(f"winner is {winners[0]}")
    else:
        print("it's a tie between: " + winners[0] + ", " + winners[1])

# Example usage
count_votes('votes.csv')
