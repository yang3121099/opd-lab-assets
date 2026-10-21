import sqlite3
import sys

def analyze(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Average salary by department
    cursor.execute("""
        SELECT department, ROUND(AVG(salary), 2) as avg_salary, COUNT(*) as headcount
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
    """)
    dept_stats = cursor.fetchall()

    print("=== Department Statistics ===")
    for row in dept_stats:
        print(f"  {row[0]}: avg_salary={row[1]}, headcount={row[2]}")

    # Top earner per department
    cursor.execute("""
        SELECT department, name, salary
        FROM employees e1
        WHERE salary = (
            SELECT MAX(salary) FROM employees e2
            WHERE e2.department = e1.department
        )
        ORDER BY department
    """)
    top_earners = cursor.fetchall()

    print("\n=== Top Earner Per Department ===")
    for row in top_earners:
        print(f"  {row[0]}: {row[1]} (${row[2]:,.2f})")

    # Active projects with lead names and budgets
    cursor.execute("""
        SELECT p.name, e.name, p.budget
        FROM projects p
        JOIN employees e ON p.lead_id = e.id
        WHERE p.status = 'active'
        ORDER BY p.budget DESC
    """)
    active_projects = cursor.fetchall()

    print("\n=== Active Projects ===")
    for row in active_projects:
        print(f"  {row[0]} | Lead: {row[1]} | Budget: ${row[2]:,.2f}")

    # Total budget of active projects
    cursor.execute("""
        SELECT ROUND(SUM(budget), 2)
        FROM projects
        WHERE status = 'active'
    """)
    total_budget = cursor.fetchone()[0]
    print(f"\nTotal active project budget: ${total_budget:,.2f}")

    # Employees hired before 2020
    cursor.execute("""
        SELECT name, hire_date
        FROM employees
        WHERE hire_date < '2020-01-01'
        ORDER BY hire_date
    """)
    veterans = cursor.fetchall()

    print("\n=== Employees Hired Before 2020 ===")
    for row in veterans:
        print(f"  {row[0]} (hired: {row[1]})")

    conn.close()

if __name__ == '__main__':
    db = sys.argv[1] if len(sys.argv) > 1 else 'data.db'
    analyze(db)
