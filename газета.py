import numpy as np
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import datetime



def write():
	time = ["6:00 a.m.", "6:15 a.m"]
	date = ["Sun, 18th Feb", "Sun, 18th Feb"]
	start_day = [1, 0]
	went_bed = [0, 0]
	rest_half_an_hour = [0, 0]
	brushed_teeth = [0, 0]
	clean_nails = [0, 0]
	washed_face = [0, 0]
	disinfect_body = [0, 0]
	full_body_wash_soap = [0, 1]
	washed_clothes = [0, 0]
	collected_clothes = [0, 0]
	set_clothes_dry = [0, 0]
	collected_dry_clothes = [0, 0]
	had_meal = [0, 1, 0]
	what_meal = [0, "Coffee with no sugar"]
	did_woolies = [0, 0]

	df = pd.DataFrame({"Time": time, "Date": date, "Started day": start_day, "Went to bed": went_bed, "Rest for half an hour": rest_half_an_hour, "Brushed Teeth": brushed_teeth, "Cleaned nails and washed hands": clean_nails, "Washed face": washed_face, "Washed clothes": washed_clothes, "Collected clothes from wash": collected_clothes, "Disinfected body": disinfect_body, "Washed entire body with soap": full_body_wash_soap, "Set Clothes to Dry": set_clothes_dry, "Collected dry clothes": collected_dry_clothes, "Had meal": had_meal, "What meal": what_meal, "Did shopping": did_woolies})
	print(df)
	df.to_csv('журнал_ч_траскотт.csv')
	
def DailyPractice():
	pass
	
DailyPractice()
write()