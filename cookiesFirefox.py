import sqlite3

def get_firefox_cookies(cookies_sqlite):
    try:
        conn = sqlite3.connect(cookies_sqlite)
        cursor = conn.cursor()
        cursor.execute("SELECT name, value, host from moz_cookies")
        for row in cursor:
            name = str(row[0])
            value = str(row[1])
            host = str(row[2])
            print("[+] " + name + " " + value + " " + " " + host)
    except Exception as e:
        print("[-] Erreur : " + str(e))
        exit(1)

get_firefox_cookies("resources/cookies.sqlite")