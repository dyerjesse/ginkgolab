
"""heart_rate = list(100, 120, 140, 160, 180, 194)
user = input("What's your heart rate?")

def switch_demo (hrZone) {
	1 : if user > 100 and user < 120 :
			print("easy")
	2 : if user > 120 and user < 140 :
			print("moderate")
	3 : if user > 140 and user < 160 :
			print("moderate")
	4 : if user > 160 and user < 180 :
			print("Aerobic")
	5 : if user > 180 and user < 194 :
			print("Anaerobic")
	6 : if user >= 194 :
			print("Max")		
}"""

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print user.get(argument, "Invalid month")
