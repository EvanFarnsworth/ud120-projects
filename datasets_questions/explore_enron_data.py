
"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle as pick

enron_data = pick.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0

for key in enron_data:
    if enron_data[key]["email_address"] != 'NaN':
        count += 1

print(count)

