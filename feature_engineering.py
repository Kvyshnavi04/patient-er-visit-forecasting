
def create_features(df):
    df['prev_visits_ratio'] = df['previous_visits'] / (df['age'] + 1)
    df['chronic_flag'] = df['chronic_conditions'].apply(lambda x: 1 if x > 0 else 0)
    df['visit_trend'] = df['visits_last_6m'] - df['visits_last_12m'] / 2
    return df
