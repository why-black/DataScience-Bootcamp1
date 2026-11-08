from config import *
from analytics import Research, Analytics, Calculations

def dict(count, word):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    if count < len(numbers):
        return numbers[count]
    else:
        return str(count)
    
if __name__ == '__main__':
    research = Research(path)
    data = research.file_reader()

    analytics = Analytics(data)
    h, t = analytics.counts()
    frac_h, frac_t = analytics.fractions()

    prediction = analytics.predict_random(count_steps)
    h_pr_count = 0
    t_pr_count = 0
    for pred in prediction:
        if pred[0] == 1:
            h_pr_count += 1
        else:
            t_pr_count += 1

    predictions_text = f"{dict(t_pr_count, 'tail')} tail{'s' if t_pr_count != 1 else ''} and {dict(h_pr_count, 'head')} head{'s' if h_pr_count != 1 else ''}"

    report = text.format(
        S = len(data),
        tails = dict(t, 'tail'),
        heads = dict(h, 'head'),
        tails_p = frac_t * 100,
        heads_p = frac_h * 100,
        num_steps = count_steps,
        predictions=predictions_text
    )
    analytics.save_file(report, filename, extension)