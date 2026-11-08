count_steps = 3
path = 'data.csv'
filename = 'report'
extension = 'txt'

text = """We made {S} observations by tossing a coin: {tails} were tails and {heads} were heads. The probabilities are {tails_p:.2f}% and {heads_p:.2f}%, respectively. Our forecast is that the next {num_steps} observations will be: {predictions}."""