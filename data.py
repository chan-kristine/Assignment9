import json

data= {
  "Basic Details": {
    "Name": "KRISTINE AGCAY CHAN",
    "Age": "18 years old",
    "Weight": "51 kg",
    "Height": "173 cm",
    "Address": "Paju, Gyeonggi Province, South Korea"
  },
  "Contact Details": {
    "Cellphone No.": "+63 939-269-5513",
    "E-mail": "kimdami123@gmail.com"
  },
  "Objectives": [
    {
      "Job Objectives": "Entertain, convey characters and express emotions in front of a live audience."
    }
  ],
  "Educational Attainment": {
    "Tertiary Level": {
      "School Name": "Seoul National University",
      "School Address": "Bldg.504, Department of Life Sciences, Seoul National University, 1 Gwanak-ro, South Korea, Seoul, Gwanak-gu"
    },
    "secondary": {
      "School Name": "Korea International School Pangyo Campus",
      "School Address": "#27 385, Daewangpangyo-ro, Bundang-gu, Seongnam-si, Gyeonggi-do, South Korea"
    },
    "Primary": {
      "School Name": "Asia Pacific International School Seoul",
      "School Address": "57 Wolgye-ro 45ga-gil, Nowon-gu, Seoul, South Korea"
    }
  },
  "Educational Achievements": {
    "Primary Level Achievements": {
      "1": "Valedictorian",
      "2": "Journalsit of the Year ",
      "3": "Athlete of the Year",
      "4": "1st Place in News Writing in Division School Press Conference",
      "5": "Leadership Awardee"
    },
    "Secondary Level Achievements": {
      "1": "With High Honors",
      "2": "Athlete of the Year",
      "3": "Leadership Awardee",
      "4": "Academic Exellence Awardee"
    },
    "Work experience": {
      "Position": "Actress",
      "Company": "TVN",
      "Cddress": "CJ E&M Center, 66 Sangamsan-ro, Sangam-dong, Mapo-gu, Seoul, South Korea"
    },
    "Skills": {
      "1": "Ability to work as a team and also individually.",
      "2": "Experience in improvisation/ad-libbing.",
      "3": "Ability to take direction."
    }
  }
}


json_file = json.dumps(data, indent = 2)
with open("resume.json", "w") as collect:
  collect.write(json_file)