""" Main python script to clean you the csv files from kaggel """
import csv
import json

from discription_csv_to_django import create_description
from image_csv_to_django import create_image_json

description = create_description()
header_image = create_image_json("steam_media_data.csv",)
data = []
categories = []
categories_id = []
genres = []
tags = []
ids = []
cat_values = {
    "Co-op": "1",
    "Full controller support": "2",
    "Mods": "3",
    "Shared/Split Screen": "4",
    "Local Co-op": "5",
    "Single-player": "6",
    "VR Support": "7",
    "Online Co-op": "8",
    "MMO": "9",
    "Partial Controller Support": "10",
    "Local Multi-Player": "11",
    "Cross-Platform Multiplayer": "12",
    "Includes level editor": "13",
    "Multi-player": "14",
    "Online Multi-Player": "15",
    "In-App Purchases": "16",
}

gen_values = {
    "Casual": "1",
    "RPG": "2",
    "Free to Play": "3",
    "Indie": "4",
    "Racing": "5",
    "Gore": "6",
    "Massively Multiplayer": "7",
    "Action": "8",
    "Sports": "9",
    "Adventure": "10",
    "Strategy": "11",
    "Education": "12",
    "Simulation": "13",
}

tag_values = {
    "Twin Stick Shooter": "1",
    "Hand-drawn": "2",
    "Souls-like": "3",
    "Mod": "4",
    "Masterpiece": "5",
    "Realistic": "6",
    "Open World": "7",
    "Dog": "8",
    "VR": "9",
    "Dark": "10",
    "Magic": "11",
    "Time Attack": "12",
    "Alternate History": "13",
    "Experimental": "14",
    "Split Screen": "15",
    "Gore": "16",
    "Trains": "17",
    "Match 3": "18",
    "Football": "19",
    "Retro": "20",
    "Runner": "21",
    "Procedural Generation": "22",
    "Perma Death": "23",
    "Naval": "24",
    "Illuminati": "25",
    "Rogue-lite": "26",
    "Action RPG": "27",
    "Gun Customization": "28",
    "Dystopian ": "29",
    "Tower Defense": "30",
    "Underwater": "31",
    "Rogue-like": "32",
    "Education": "33",
    "Team-Based": "34",
    "Beautiful": "35",
    "3D Vision": "36",
    "Moddable": "37",
    "Local Co-Op": "38",
    "Kickstarter": "39",
    "Hunting": "40",
    "Motorbike": "41",
    "Cold War": "42",
    "Ninja": "43",
    "Co-op": "44",
    "Crime": "45",
    "Arena Shooter": "46",
    "Bikes": "47",
    "Battle Royale": "48",
    "God Game": "49",
    "Dinosaurs": "50",
    "Wrestling": "51",
    "First-Person": "52",
    "Third-Person Shooter": "53",
    "Resource Management": "54",
    "Turn-Based Tactics": "55",
    "Typing": "56",
    "Comedy": "57",
    "Board Game": "58",
    "Cult Classic": "59",
    "Medieval": "60",
    "Swordplay": "61",
    "Puzzle": "62",
    "Space": "63",
    "Short": "64",
    "Batman": "65",
    "Skating": "66",
    "Space Sim": "67",
    "Colorful": "68",
    "Historical": "69",
    "BMX": "70",
    "Hex Grid": "71",
    "Inventory Management": "72",
    "On-Rails Shooter": "73",
    "Post-apocalyptic": "74",
    "Faith": "75",
    "Level Editor": "76",
    "Blood": "77",
    "Sokoban": "78",
    "Indie": "79",
    "Gambling": "80",
    "Anime": "81",
    "Sailing": "82",
    "Flight": "83",
    "Online Co-Op": "84",
    "City Builder": "85",
    "Pixel Graphics": "86",
    "Turn-Based Strategy": "87",
    "Motocross": "88",
    "Sexual Content": "89",
    "Cute": "90",
    "Survival Horror": "91",
    "Agriculture": "92",
    "Tennis": "93",
    "Heist": "94",
    "Zombies": "95",
    "Robots": "96",
    "Classic": "97",
    "Multiplayer": "98",
    "4 Player Local": "99",
    "Software": "100",
    "3D Platformer": "101",
    "Parody ": "102",
    "Fishing": "103",
    "Cycling": "104",
    "Dating Sim": "105",
    "Time Management": "106",
    "CRPG": "107",
    "Golf": "108",
    "Grid-Based Movement": "109",
    "Gothic": "110",
    "Metroidvania": "111",
    "Romance": "112",
    "Dark Humor": "113",
    "Touch-Friendly": "114",
    "Fantasy": "115",
    "Casual": "116",
    "Sandbox": "117",
    "Steampunk": "118",
    "Snowboarding": "119",
    "Action-Adventure": "120",
    "Abstract": "121",
    "FMV": "122",
    "Party-Based RPG": "123",
    "Benchmark": "124",
    "Hacking": "125",
    "Warhammer 40K": "126",
    "4X": "127",
    "Sci-fi": "128",
    "RPG": "129",
    "MMORPG": "130",
    "JRPG": "131",
    "Cats": "132",
    "Choose Your Own Adventure": "133",
    "Family Friendly": "134",
    "Top-Down Shooter": "135",
    "Investigation": "136",
    "Cinematic": "137",
    "Sports": "138",
    "Noir": "139",
    "Racing": "140",
    "Voxel": "141",
    "Video Production": "142",
    "Lovecraftian": "143",
    "Visual Novel": "144",
    "Action": "145",
    "Choices Matter": "146",
    "Economy": "147",
    "Futuristic": "148",
    "Crafting": "149",
    "NSFW": "150",
    "Rome": "151",
    "Grand Strategy": "152",
    "Photo Editing": "153",
    "Strategy RPG": "154",
    "Movie": "155",
    "Arcade": "156",
    "Diplomacy": "157",
    "Point & Click": "158",
    "Intentionally Awkward Controls": "159",
    "Multiple Endings": "160",
    "Cyberpunk": "161",
    "Old School": "162",
    "Baseball": "163",
    "Dungeon Crawler": "164",
    "Lara Croft": "165",
    "Soccer": "166",
    "Great Soundtrack": "167",
    "1990's": "168",
    "Hockey": "169",
    "Management": "170",
    "Snow": "171",
    "Mechs": "172",
    "Base-Building": "173",
    "Relaxing": "174",
    "Exploration": "175",
    "Nonlinear": "176",
    "Real Time Tactics": "177",
    "Strategy": "178",
    "Vampire": "179",
    "Score Attack": "180",
    "Physics": "181",
    "Early Access": "182",
    "Detective": "183",
    "Basketball": "184",
    "Web Publishing": "185",
    "Supernatural": "186",
    "Mature": "187",
    "e-sports": "188",
    "Psychological": "189",
    "Psychological Horror": "190",
    "2.5D": "191",
    "Assassin": "192",
    "Competitive": "193",
    "Parkour": "194",
    "Pool": "195",
    "Drama": "196",
    "Turn-Based": "197",
    "Hidden Object": "198",
    "Singleplayer": "199",
    "Western": "200",
    "Controller": "201",
    "RTS": "202",
    "Isometric": "203",
    "Adventure": "204",
    "Stylized": "205",
    "World War II": "206",
    "Female Protagonist": "207",
    "Third Person": "208",
    "Character Action Game": "209",
    "Shoot 'Em Up": "210",
    "Chess": "211",
    "Military": "212",
    "War": "213",
    "Rhythm": "214",
    "Driving": "215",
    "Story Rich": "216",
    "Local Multiplayer": "217",
    "Logic": "218",
    "Programming": "219",
    "Violent": "220",
    "Bowling": "221",
    "Turn-Based Combat": "222",
    "Atmospheric": "223",
    "Word Game": "224",
    "Class-Based": "225",
    "Massively Multiplayer": "226",
    "Mining": "227",
    "RPGMaker": "228",
    "Text-Based": "229",
    "Tactical RPG": "230",
    "Documentary": "231",
    "Werewolves": "232",
    "Star Wars": "233",
    "Spectacle fighter": "234",
    "Difficult": "235",
    "Spelling": "236",
    "Offroad": "237",
    "Lemmings": "238",
    "Cartoon": "239",
    "Interactive Fiction": "240",
    "PvP": "241",
    "Design & Illustration": "242",
    "Mystery": "243",
    "Mini Golf": "244",
    "Trading Card Game": "245",
    "Villain Protagonist": "246",
    "Thriller": "247",
    "Simulation": "248",
    "Linear": "249",
    "Shooter": "250",
    "Real-Time with Pause": "251",
    "Skateboarding": "252",
    "Tanks": "253",
    "Politics": "254",
    "Otome": "255",
    "LEGO": "256",
    "Pinball": "257",
    "Real-Time": "258",
    "Funny": "259",
    "Horror": "260",
    "Mythology": "261",
    "6DOF": "262",
    "Walking Simulator": "263",
    "2D": "264",
    "Bullet Hell": "265",
    "Mars": "266",
    "Satire": "267",
    "Bullet Time": "268",
    "Side Scroller": "269",
    "Submarine": "270",
    "Replay Value": "271",
    "Character Customization": "272",
    "Mouse only": "273",
    "Trading": "274",
    "Music-Based Procedural Generation": "275",
    "FPS": "276",
    "Time Travel": "277",
    "Science": "278",
    "Remake": "279",
    "Aliens": "280",
    "Loot": "281",
    "World War I": "282",
    "Tactical": "283",
    "2D Fighter": "284",
    "Superhero": "285",
    "MOBA": "286",
    "VR Only": "287",
    "Card Game": "288",
    "Martial Arts": "289",
    "Survival": "290",
    "Pirates": "291",
    "Hack and Slash": "292",
    "Conversation": "293",
    "Clicker": "294",
    "Narration": "295",
    "Fighting": "296",
    "Psychedelic": "297",
    "Puzzle-Platformer": "298",
    "Dark Fantasy": "299",
    "Time Manipulation": "300",
    "Top-Down": "301",
    "Comic Book": "302",
    "Mystery Dungeon": "303",
    "1980s": "304",
    "Surreal": "305",
    "Cartoony": "306",
    "America": "307",
    "Fast-Paced": "308",
    "Dragons": "309",
    "Free to Play": "310",
    "Stealth": "311",
    "Horses": "312",
    "Philisophical": "313",
    "Epic": "314",
    "Destruction": "315",
    "Demons": "316",
    "Building": "317",
    "Sniper": "318",
    "3D": "319",
    "Beat 'em up": "320",
    "Music": "321",
    "Political": "322",
    "Minimalist": "323",
    "Platformer": "324",
    "Wargame": "325",
    "Capitalism": "326",
    "Dungeons & Dragons": "327",
}


def create_games_json(input_file, output_file, games_model):
    """
    Create the games json file used for turn games models using the kaggle dataset
    """

    pk = 0
    # open the csv file sent into the function
    with open(input_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        # Clean the CSV files data
        for record, row in enumerate(rows):

            # class arrays
            cat_num = []
            gen_num = []
            tag_num = []
            # loop through each field in the record and pick out only the categories wanted
            for key, val in row.items():
                if type(val) == str:
                    if ";" in val:
                        # split the data into manageable arrays
                        row[key] = val.split(";")
                        # Filter categories
                        if key == "categories":
                            excluded_categories = [
                                "Steam Trading Cards",
                                "Steam Turn Notifications",
                                "Valve Anti-Cheat enabled",
                                "Commentary available",
                                "Steam Cloud",
                                "Mods (require HL2)",
                                "Steam Achievements",
                                "Steam Leaderboards",
                                "Stats",
                                "Steam Workshop",
                                "Captions available",
                                "Includes Source SDK",
                                "SteamVR Collectibles",
                            ]
                            for category in row[key]:
                                # remove any unwanted categories
                                if not category in excluded_categories:
                                    categories.append(category)
                                    cat_num.append(int(cat_values[category]))

                        # Filter genres
                        if key == "genres":
                            excluded_genres = [
                                "Software Training",
                                "Sexual Content",
                                "Accounting",
                                "Animation & Modeling",
                                "Game Development",
                                "Tutorial",
                                "Early Access",
                                "Photo Editing",
                                "Utilities",
                                "Web Publishing",
                                "Video Production",
                                "Violent",
                                "Nudity",
                                "Audio Production",
                                "Design & Illustration",
                                "Documentary",
                            ]
                            for genre in row[key]:
                                # remove any unwanted genres
                                if not genre in excluded_genres:
                                    genres.append(genre)
                                    gen_num.append(int(gen_values[genre]))

                        # Filter tags
                        if key == "steamspy_tags":
                            excluded_tags = [
                                "Nudity",
                                "Voice Control",
                                "Games Workshop",
                                "360 Video",
                                "Game Development",
                                "GameMaker",
                                "Quick-Time Events",
                                "Animation & Modeling",
                                "Utilities",
                                "Audio Production",
                                "Software Training",
                                "Memes",
                            ]
                            for tag in row[key]:
                                # remove any unwanted tags
                                if not tag in excluded_tags:
                                    tags.append(tag)
                                    tag_num.append(int(tag_values[tag]))
            # remove unwanted data
            del row["owners"]
            del row["median_playtime"]
            del row["average_playtime"]
            del row["achievements"]

            # reduce size if dataset to post 2019-03-01 games
            if row["release_date"] > "2019-03-01" and row["english"] == "1":
                # tidy up platform field
                platform_list = row["platforms"]
                platforms = (
                    ", ".join(platform_list)
                    if type(platform_list) == list
                    else platform_list
                )
                # tidy up developer list
                developer_list = row["developer"]
                developers = (
                    ", ".join(developer_list)
                    if type(developer_list) == list
                    else developer_list
                )
                # make publisher the same as developer (for simplicity)
                publisher_list = row["developer"]
                publishers = (
                    ", ".join(publisher_list)
                    if type(publisher_list) == list
                    else publisher_list
                )
                # create the fixture record formatted for django
                pk += 1
                ids.append(row["appid"])
                entry = {
                    "model": games_model,
                    "pk": int(pk),
                    "fields": {
                        "name": row["name"],
                        "description": description[row["appid"]],
                        "header_image_url": header_image[row["appid"]],
                        "header_image": "",
                        "release_date": row["release_date"],
                        "developer": developers,
                        "publisher": publishers,
                        "platforms": platforms,
                        "required_age": row["required_age"],
                        "positive_ratings": row["positive_ratings"],
                        "negative_ratings": row["negative_ratings"],
                        "price": row["price"],
                        "categories": cat_num,
                        "genres": gen_num,
                        "tags": tag_num,
                    },
                }

                data.append(entry)

    # Save as json file
    with open(output_file, "w") as f:
        json.dump(data, f)
        print("Total Games Records: " + str(pk))


def create_category_json(output_filename, category_model):
    """ create the category json file """
    pk = 0
    categories_data = []
    filtered_categories = list(set(categories))
    # create the fixture record formatted for django
    for category in filtered_categories:
        pk += 1
        entry = {
            "model": category_model,
            "pk": int(pk),
            "fields": {
                "name": category.lower().replace(" ", "_").replace("-", "_"),
                "friendly_name": category,
            },
        }
        categories_data.append(entry)

    # Save as json file
    with open(output_filename, "w") as f:
        json.dump(categories_data, f)
        print("Total Category Records: " + str(pk))


def create_genre_json(output_filename, genre_model):
    """ create the genre json file """
    pk = 0
    genre_data = []
    filtered_genres = list(set(genres))
    # create the fixture record formatted for django
    for genre in filtered_genres:
        pk += 1
        entry = {
            "model": genre_model,
            "pk": int(pk),
            "fields": {
                "name": genre.lower().replace(" ", "_").replace("-", "_"),
                "friendly_name": genre,
            },
        }
        genre_data.append(entry)

    # Save as json file
    with open(output_filename, "w") as f:
        json.dump(genre_data, f)
        print("Total Genre Records: " + str(pk))


def create_tags_json(output_filename, tag_model):
    """ create the tags json file"""
    pk = 0
    tags_data = []
    filtered_tags = list(set(tags))
    # create the fixture record formatted for django
    for tag in filtered_tags:
        pk += 1
        entry = {
            "model": tag_model,
            "pk": int(pk),
            "fields": {
                "name": tag.lower().replace(" ", "_").replace("-", "_"),
                "friendly_name": tag,
            },
        }
        tags_data.append(entry)

    # Save as json file
    with open(output_filename, "w") as f:
        json.dump(tags_data, f)
        print("Total Tags Records: " + str(pk))


if __name__ == "__main__":
    create_games_json("steam.csv", "games.json", "games.game")
    create_category_json("categories.json", "games.category")
    create_genre_json("genres.json", "games.genre")
    create_tags_json("tags.json", "games.tag")
