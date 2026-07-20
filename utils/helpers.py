from datetime import datetime

def time_ago(dt):
    if dt is None:
        return ""

    now = datetime.utcnow()
    diff = now - dt

    if diff.days == 0:
        if diff.seconds < 60:
            return "Just now"
        elif diff.seconds < 3600:
            mins = diff.seconds // 60
            return f"{mins} min ago"
        else:
            hrs = diff.seconds // 3600
            return f"{hrs} hr ago"

    elif diff.days == 1:
        return "1 day ago"

    elif diff.days < 7:
        return f"{diff.days} days ago"

    elif diff.days < 30:
        weeks = diff.days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"

    else:
        months = diff.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"