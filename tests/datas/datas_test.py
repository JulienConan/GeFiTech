
base_technician = ["Sylvie","Solo"]

base_patch = [
                {"source": "Kick in", "reference": "SM91", "stand": "GP", "pad": 0, "48V": 0},
                {"source": "Kick Out", "reference": "BETA52", "stand": "PP", "pad": 0, "48V": 0},
                {"source": "Snare Top", "reference": "SM57", "stand": "PP", "pad": 0, "48V": 0}
                ]

base_patch2 = [
                {"source": "Kick in", "reference": "SM91", "stand": "GP", "pad": 0, "48V": 0},
                {"source": "Kick Out", "reference": "D6", "stand": "PP", "pad": 0, "48V": 0},
                {"source": "Snare Top", "reference": "M441", "stand": "CLAMP", "pad": 0, "48V": 0}
                ]               

base_band = {
        "name": "Groupe1",
        "rider_date": {"year" : 2000, "month" : 1, "day" : 1},
        "foh_technician": ["Julien", "CONAN"],
        "monitor_technician": ["Piotr", "Skotnicki"],
        "patch": base_patch
        }

base_band2 = {
        "name": "Groupe2",
        "rider_date": {"year" : 2000, "month" : 1, "day" : 2},
        "foh_technician": ["Gael", "Rabbiosi"],
        "monitor_technician": ["Manu", "Cadiou"],
        "patch": base_patch2
        }

base_day = {"date" : {"year" : 2000, "month" : 1, "day" : 1},
        "band_list" : [base_band, base_band2]}