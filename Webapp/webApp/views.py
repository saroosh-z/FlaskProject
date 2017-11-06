from flask import render_template
from . import app

camping_checklist_food = ['Small Pot', '1 Granola Bar per day','1 Oatmeal pack per day',
'1 Mixed Nuts pack per day','Tuna','Jerky','Crackers','Instant Potatoes',
'Limon Packs','Spices','Dried Sausage','Hot Chocolate + Milk Powder']

camping_checklist_safety = [
'Bear Spray','Bug Spray','First Aid','Asprin','Bronkaid','Personal alarm']

camping_personal_list = ['Personal Toiletries','Toilet Paper','Paper Towel',
'Wipes','snack bars', 'ramen','Instant coffee','Pot with cover', 'Lotion',
'Extra shirt','pants','socks','Fork/Spoon/Knife','Cups','Bowl', 'Pot',
'3 Liters of water','Multitool','Fire Starter','String',
'Gum','Toothbrush/Toothpaste/Mouthwash','Towel','Facewash'
'Pillow','Gloves','scarf','Tape', 'Lens Cleaner'
]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/drinks')
def drinks():
	return render_template('drinks.html')

@app.route('/camping')
def camping():
	return render_template('camping.html', food_list = camping_checklist_food,
								safety_list = camping_checklist_safety,
								personal_list = camping_personal_list)
@app.route('/art-sy')
def artsy():
	return render_template('art-sy.html')