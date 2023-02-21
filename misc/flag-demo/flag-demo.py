import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import PySimpleGUI as sg

layout = [
    [sg.T("Plebeian Algorithm: Flag Phase Demonstration", font=('Any 18'))],
    [sg.T("Please enter text to determine if it would get flagged:")],
    [sg.Multiline("", size=(80,10), k="IN")],
    [sg.Button("Submit", k="OK")]
]

window = sg.Window("Plebeian Algorithm: Flag Phase Demonstration", layout)
while True:
    event, values = window.read()
    if event == "OK":
        text = values['IN']
        break
    elif event == sg.WIN_CLOSED:
        quit()

print(text)

window.close()

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

print(f'Analyzing \"{text}\".')

pol_score = sia.polarity_scores(text)

if pol_score['compound'] < -0.2:
    flag_text = "TRUE"
    flag_color = 'yellow'
    flag_desc = "This result indicates that your post may contain\nmisinformation due to a high negative sentiment. \nIt would proceed to the Jury Phase."
elif pol_score['neu'] == 1:
    flag_text = "UNKNOWN"
    flag_color = 'magenta'
    flag_desc = "This result indicates a lack of certainly in the\nsentiment analyzer. Instances like this will\ndecrease over time, as the model becomes trained."
else:
    flag_text = "FALSE"
    flag_color = 'green'
    flag_desc = "This result indicates that your post probably\ndoes not contain misinformation. It's comments would\nbe analyzed further."


layout = [
    [sg.T("Your Results", font=('Any 24'))],
    [sg.T("Based on your input, the flag would be set to...")],
    [sg.T(flag_text, font=('Any 28'), text_color=flag_color)],
    [sg.T(flag_desc)],
    [sg.T("")],
    [sg.T("Here is your score:")],
    [sg.T(f"Positivity: {pol_score['pos']}")],
    [sg.T(f"Neutrality: {pol_score['neu']}")],
    [sg.T(f"Negativity: {pol_score['neg']}")],
    [sg.T(f"Compound: {pol_score['compound']}")],
    [sg.T("")],
    [sg.T("Please note that entries with a neutrality of 1.0\nrepresent a lack of lexical data in the sentiment\nanalyzer. The frequecy of these instances decrease\nover time. However, in the initial implementation\nof the Plebeian Algorithm, accuracy will be decreased.")],
    [sg.Button("OK", k="OK")]
]

window = sg.Window("Plebeian Algorithm: Flag Phase Demonstration", layout)
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

print(pol_score)