import calendar
import datetime
from bs4 import BeautifulSoup


def get_meetup_day_for_month(year, month):
    c = calendar.Calendar(firstweekday=calendar.MONDAY)

    month_cal = c.monthdatescalendar(year, month)
    saturdays_for_month = [day for week in month_cal for day in week if
                           day.weekday() == calendar.SATURDAY and day.month == month]
    third_saturday = saturdays_for_month[2]
    return third_saturday


def get_meetup_date():
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    if current_day < 21:
        return get_meetup_day_for_month(current_year, current_month)
    elif current_month < 12:
        return get_meetup_day_for_month(current_year, current_month + 1)
    else:
        return get_meetup_day_for_month(current_year + 1, 1)


def get_day_of_week_ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return suffix


def change_meetup_date_on_homepage(meetup_date):
    with open('./../index.html', 'r') as html_file:
        # BeautifulSoup doesn't preserve whitespace by default
        whitespace_preserved_html = '<pre>' + html_file.read() + '</pre>'
        soup = BeautifulSoup(whitespace_preserved_html, features='html.parser')

        # Find the #meetup-date field and replace the contents
        for tag in soup.find(id='meetup-date'):
            tag.string.replace_with(meetup_date)

    # Save updated HTML
    with open('./../index.html', 'w') as html_file:
        # Remove <pre></pre> tags to save updated HTML contents
        html = str(soup).replace('<pre>', '').replace('</pre>', '')
        html_file.write(html)


def main():
    meetup_date = get_meetup_date()
    meetup_date_str = meetup_date.strftime("%B %-d") + get_day_of_week_ordinal(meetup_date.day)
    change_meetup_date_on_homepage(meetup_date_str)


if __name__ == "__main__":
    main()
