def format_date(date):
    return date.strftime("%Y-%m-%d")

def generate_random_color():
    import random
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def calculate_percentage(part, whole):
    if whole == 0:
        return 0
    return round((part / whole) * 100, 2)

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def filter_dataframe(df, column, value):
    return df[df[column] == value]