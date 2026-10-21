import sqlite3

def get_top_scores(db_path, limit=3):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.player, s.score, l.name, ROUND(s.score * l.multiplier, 0) as final_score
        FROM scores s
        JOIN levels l ON s.level = l.id
        ORDER BY final_score DESC
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def print_leaderboard(rows):
    print('Rank | Player | Score | Level | Final Score')
    print('-' * 45)
    for i, (player, score, level, final) in enumerate(rows, 1):
        print(f'{i:4} | {player:<6} | {score:5} | {level:<6} | {int(final)}')

if __name__ == '__main__':
    rows = get_top_scores('scores.db', limit=3)
    print_leaderboard(rows)
