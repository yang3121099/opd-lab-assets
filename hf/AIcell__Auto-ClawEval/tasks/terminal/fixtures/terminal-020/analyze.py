import sqlite3
import sys

def analyze(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Average salary by department
    cur.execute("""
        SELECT department, ROUND(AVG(salary), 2) as avg_salary, COUNT(*) as headcount
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
    """)
    dept_stats = cur.fetchall()

    print("=== Department Statistics ===")
    for row in dept_stats:
        print(f"  {row[0]}: avg_salary={row[1]}, headcount={row[2]}")

    # Top earner per department
    cur.execute("""
        SELECT department, name, salary
        FROM employees e1
        WHERE salary = (
            SELECT MAX(salary) FROM employees e2
            WHERE e2.department = e1.department
        )
        ORDER BY department
    """)
    top_earners = cur.fetchall()

    print("\n=== Top Earner Per Department ===")
    for row in top_earners:
        print(f"  {row[0]}: {row[1]} (${row[2]:,.2f})")

    # Active projects with lead names and budgets
    cur.execute("""
        SELECT p.name, e.name, p.budget
        FROM projects p
        JOIN employees e ON p.lead_id = e.id
        WHERE p.status = 'active'
        ORDER BY p.budget DESC
    """)
    active_projects = cur.fetchall()

    print("\n=== Active Projects ===")
    for row in active_projects:
        print(f"  {row[0]} | Lead: {row[1]} | Budget: ${row[2]:,.2f}")

    # Total budget of active projects
    cur.execute("""
        SELECT ROUND(SUM(budget), 2)
        FROM projects
        WHERE status = 'active'
    """)
    total_budget = cur.fetchone()[0]
    print(f"\nTotal active project budget: ${total_budget:,.2f}")

    # Employees with no project lead role
    cur.execute("""
        SELECT name, department
        FROM employees
        WHERE id NOT IN (SELECT lead_id FROM projects)
        ORDER BY name
    """)
    non_leads = cur.fetchall()

    print("\n=== Employees Not Leading Any Project ===")
    for row in non_leads:
        print(f"  {row[0]} ({row[1]})")

    conn.close()

if __name__ == '__main__':
    db = sys.argv[1] if len(sys.argv) > 1 else 'data.db'
    analyze(db)
