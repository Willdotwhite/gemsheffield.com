import calendar
import datetime
from bs4 import BeautifulSoup


def get_meetup_day_for_month(year, month):
    c = calendar.Calendar(firstweekday=calendar.MONDAY)

    month_cal = c.monthdatescalendar(year, month)
    saturdays_for_month = [day for week in month_cal for day in week if
                           day.weekday() == calendar.SATURDAY and day.month == month]
    return saturdays_for_month[1]  # Second Saturday of the month


def get_meetup_date():
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    # Overrides allow us to shift dates for whatever reason,
    # without having to record this mess every time
    overrides = {
        "2023_5":  datetime.date(2023, 5, 20),
        "2023_8":  datetime.date(2023, 7, 20)
    }

    override_key = f'{current_year}_{current_month}'
    if override_key in overrides:
        return overrides.get(override_key)


    meetup_this_month = get_meetup_day_for_month(current_year, current_month)

    # If the meetup hasn't happened yet this month
    if current_day < meetup_this_month.day:
        return meetup_this_month
    # If the meetup is next month (non-December)
    elif current_month < 12:
        return get_meetup_day_for_month(current_year, current_month + 1)
    # If it's December, and so the meetup is next January
    else:
        return get_meetup_day_for_month(current_year + 1, 1)


def get_day_of_week_ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return suffix


def change_meetup_date_on_homepage(meetup_date):
    with open('./index.html', 'r') as html_file:
        # BeautifulSoup doesn't preserve whitespace by default
        whitespace_preserved_html = '<pre>' + html_file.read() + '</pre>'
        soup = BeautifulSoup(whitespace_preserved_html, features='html.parser')

        # Find the #meetup-date field and replace the contents
        for tag in soup.find(id='meetup-date'):
            tag.string.replace_with(meetup_date)

    # Save updated HTML
    with open('./index.html', 'w') as html_file:
        # Remove <pre></pre> tags to save updated HTML contents
        html = str(soup).replace('<pre>', '').replace('</pre>', '')
        html_file.write(html)


def main():
    meetup_date = get_meetup_date()
    meetup_date_str = meetup_date.strftime("%B %-d") + get_day_of_week_ordinal(meetup_date.day)
    change_meetup_date_on_homepage(meetup_date_str)


if __name__ == "__main__":
    main()
