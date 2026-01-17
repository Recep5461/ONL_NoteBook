from db import get_connection_users, get_connection_notes

# ==================== USER İŞLEMLERİ ========================

def get_user_id(user, passw):
    conn = get_connection_users()
    cursor = conn.cursor() 
    
    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (user, passw)
    )
    row = cursor.fetchone()
    print(row)
    conn.commit()
    conn.close()
    if row:
        print(row[0])
        return row[0]
    return None


def user_ekle(user, passw):
    conn = get_connection_users()
    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user, passw)
        )
    conn.commit()
    conn.close()
    return True

def user_sil(uid):
    conn = get_connection_users()
    cursor = conn.cursor()
    cursor.execute(
            "DELETE FROM users WHERE id=?",
            (uid,)
        )
    conn.commit()
    conn.close()
    tum_notlari_sil(uid)
    return True

# ====================== NOT İŞLEMLERİ =======================
def tum_notlari_sil(uid):
    conn = get_connection_notes()
    cursor = conn.cursor()
    cursor.execute(
            "DELETE FROM notes WHERE user_id=?",
            (uid,)
        )
    conn.commit()
    conn.close()

def not_sil(not_id):
    conn = get_connection_notes()
    cursor = conn.cursor()
    cursor.execute(
            "DELETE FROM notes WHERE id=?",
            (not_id,)
        )
    conn.commit()
    conn.close()

def not_ekle(uid, not_baslik, not_icerik):
    conn = get_connection_notes()
    cursor = conn.cursor()
    
    not_al = [
            (uid, not_baslik, not_icerik),   
        ]
    cursor.executemany(
            "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
            not_al
        )
    conn.commit()
    conn.close()

def notes_getir(id):
    conn = get_connection_notes()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE user_id = ?",
        (id,)
        )
    rows = cursor.fetchall()

    notes = []
    for r in rows:
        notes.append({
            "id": r[0],
            "user_id": r[1],
            "title": r[2],
            "notlar": r[3]
        })

    return notes 


def not_guncelle(not_id, yeni_baslik, yeni_icerik):
    conn = get_connection_notes()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE notes SET title = ?, content = ? WHERE id = ?",
        (yeni_baslik, yeni_icerik, not_id)
    )

    conn.commit()
    conn.close()
    return True







