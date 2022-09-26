import sqlite3

def get_firefox_history(places_sqlite):
    try:
        conn = sqlite3.connect(places_sqlite)
        cursor = conn.cursor()
        cursor.execute("select url, datetime(last_visit_date/1000000, \
        \"unixepoch\") from moz_places, moz_historyvisits \
        where visit_count > 0 and moz_places.id == moz_historyvisits.place_id")
        for row in cursor:
            url = str(row[0])
            date = str(row[1])
            print("[+] " + url + " " + date)
    except Exception as e:
        print("[-] Erreur : " + str(e))
        exit(1)
        
get_firefox_history("resources/places.sqlite")