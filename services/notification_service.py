from datetime import datetime
from sqlalchemy import func

from extensions import db

from models.notification import Notification
from models.expense import Expense
from models.income import Income
from models.budget import Budget
from models.goal import Goal
from models.investment import Investment


# =====================================================
# CREATE NOTIFICATION
# =====================================================

def create_notification(user_id, title, message, notification_type, category):

    today = datetime.utcnow().date()

    existing = Notification.query.filter(
        Notification.user_id == user_id,
        Notification.title == title,
        Notification.category == category,
        func.date(Notification.created_at) == today
    ).first()

    if existing:

        if existing.message != message:
            existing.message = message
            existing.type = notification_type
            db.session.commit()

        return

    notification = Notification(
        user_id=user_id,
        title=title,
        message=message,
        type=notification_type,
        category=category,
        is_read=False
    )

    db.session.add(notification)
    db.session.commit()


# =====================================================
# BUDGET
# =====================================================

def generate_budget_notifications(user_id):

    budgets = Budget.query.filter_by(user_id=user_id).all()
    expenses = Expense.query.filter_by(user_id=user_id).all()

    total_budget = sum(b.budget_amount for b in budgets)
    total_expense = sum(e.amount for e in expenses)

    if total_budget <= 0:

        create_notification(
            user_id,
            "No Budget",
            "Create a monthly budget to track your expenses.",
            "information",
            "budget"
        )
        return

    utilization = (total_expense / total_budget) * 100
    remaining = total_budget - total_expense

    if utilization >= 100:

        create_notification(
            user_id,
            "Budget Exceeded",
            f"You exceeded your budget by ₹{abs(remaining):,.2f}.",
            "critical",
            "budget"
        )

    elif utilization >= 80:

        create_notification(
            user_id,
            "Budget Warning",
            f"You have used {utilization:.0f}% of your budget.",
            "warning",
            "budget"
        )


# =====================================================
# GOALS
# =====================================================

def generate_goal_notifications(user_id):

    goals = Goal.query.filter_by(user_id=user_id).all()

    if not goals:

        create_notification(
            user_id,
            "Create a Goal",
            "Start a savings goal to achieve your financial targets.",
            "information",
            "goal"
        )

        return

    for goal in goals:

        if goal.saved_amount >= goal.target_amount:

            create_notification(
                user_id,
                "Goal Achieved",
                f"Congratulations! '{goal.goal_name}' has been achieved.",
                "information",
                "goal"
            )

        else:

            progress = (goal.saved_amount / goal.target_amount) * 100

            if progress >= 80:

                create_notification(
                    user_id,
                    "Goal Near Completion",
                    f"'{goal.goal_name}' is {progress:.0f}% completed.",
                    "warning",
                    "goal"
                )


# =====================================================
# INCOME
# =====================================================

def generate_income_notifications(user_id):

    incomes = Income.query.filter_by(user_id=user_id).all()

    if not incomes:

        create_notification(
            user_id,
            "No Income",
            "Add your income to improve financial tracking.",
            "warning",
            "income"
        )

        return

    latest = max(incomes, key=lambda x: x.income_date)

    create_notification(
        user_id,
        "Income Recorded",
        f"Latest income of ₹{latest.amount:,.2f} added from {latest.source}.",
        "information",
        "income"
    )


# =====================================================
# EXPENSE
# =====================================================

def generate_expense_notifications(user_id):

    expenses = Expense.query.filter_by(user_id=user_id).all()

    if not expenses:
        return

    latest = max(expenses, key=lambda x: x.expense_date)

    create_notification(
        user_id,
        "Expense Recorded",
        f"₹{latest.amount:,.2f} spent on {latest.category}.",
        "information",
        "expense"
    )


# =====================================================
# INVESTMENTS
# =====================================================

def generate_investment_notifications(user_id):

    investments = Investment.query.filter_by(user_id=user_id).all()

    if not investments:

        create_notification(
            user_id,
            "Start Investing",
            "Investments help build long-term wealth.",
            "information",
            "investment"
        )

        return

    total_cost = 0
    total_value = 0

    for inv in investments:

        total_cost += inv.quantity * inv.buy_price
        total_value += inv.quantity * inv.current_price

    profit = total_value - total_cost

    if profit >= 0:

        create_notification(
            user_id,
            "Investment Profit",
            f"Your portfolio is up by ₹{profit:,.2f}.",
            "information",
            "investment"
        )

    else:

        create_notification(
            user_id,
            "Investment Loss",
            f"Your portfolio is down by ₹{abs(profit):,.2f}.",
            "warning",
            "investment"
        )


# =====================================================
# SAVINGS
# =====================================================

def generate_savings_notifications(user_id):

    income = db.session.query(
        func.coalesce(func.sum(Income.amount), 0)
    ).filter_by(user_id=user_id).scalar()

    expense = db.session.query(
        func.coalesce(func.sum(Expense.amount), 0)
    ).filter_by(user_id=user_id).scalar()

    savings = income - expense

    if savings < 0:

        create_notification(
            user_id,
            "Negative Savings",
            "Your expenses are higher than your income.",
            "critical",
            "savings"
        )

    elif savings == 0:

        create_notification(
            user_id,
            "No Savings",
            "Try to save some money every month.",
            "warning",
            "savings"
        )

    else:

        create_notification(
            user_id,
            "Savings Updated",
            f"Current savings: ₹{savings:,.2f}.",
            "information",
            "savings"
        )


# =====================================================
# FINANCIAL HEALTH
# =====================================================

def generate_financial_health_notifications(user_id):

    income = db.session.query(
        func.coalesce(func.sum(Income.amount), 0)
    ).filter_by(user_id=user_id).scalar()

    expense = db.session.query(
        func.coalesce(func.sum(Expense.amount), 0)
    ).filter_by(user_id=user_id).scalar()

    if income == 0:
        return

    savings_rate = ((income - expense) / income) * 100

    score = 0

    if savings_rate >= 30:
        score += 40
    elif savings_rate >= 20:
        score += 30
    elif savings_rate >= 10:
        score += 20
    else:
        score += 10

    budget = Budget.query.filter_by(user_id=user_id).count()

    if budget:
        score += 20

    goals = Goal.query.filter_by(user_id=user_id).count()

    if goals:
        score += 20

    investments = Investment.query.filter_by(user_id=user_id).count()

    if investments:
        score += 20

    if score >= 80:
        status = "Excellent"
    elif score >= 60:
        status = "Good"
    elif score >= 40:
        status = "Average"
    else:
        status = "Poor"

    create_notification(
        user_id,
        "Financial Health",
        f"Financial Health Score: {score}/100 ({status})",
        "insight",
        "financial_health"
    )


# =====================================================
# SPENDING INSIGHTS
# =====================================================

def generate_spending_insights(user_id):

    expenses = Expense.query.filter_by(user_id=user_id).all()

    if not expenses:
        return

    category_totals = {}

    for expense in expenses:

        category_totals.setdefault(expense.category, 0)
        category_totals[expense.category] += expense.amount

    highest_category = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_category]

    total = sum(category_totals.values())

    percentage = (highest_amount / total) * 100

    if percentage >= 50:

        create_notification(
            user_id,
            "High Spending Alert",
            f"{highest_category} accounts for {percentage:.0f}% of your spending.",
            "warning",
            "spending"
        )

    else:

        create_notification(
            user_id,
            "Spending Insight",
            f"Highest spending category is {highest_category}.",
            "insight",
            "spending"
        )


# =====================================================
# MASTER FUNCTION
# =====================================================

def generate_notifications(user_id):

    generate_budget_notifications(user_id)
    generate_goal_notifications(user_id)
    generate_income_notifications(user_id)
    generate_expense_notifications(user_id)
    generate_investment_notifications(user_id)
    generate_savings_notifications(user_id)
    generate_financial_health_notifications(user_id)
    generate_spending_insights(user_id)