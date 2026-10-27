import pandas as pd

def clean_gender(series):
    clean = series.str.strip().str.upper()
    clean = clean.replace({
            "MALE":"M",
            "FEMALE":"F"
            })
    clean = clean.where(clean.isin(["M","F",""]),"U")

    return clean

def clean_state(Series):
    clean = Series.str.strip().str.upper()

    return clean