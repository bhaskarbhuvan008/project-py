import pandas as pd
import logging
import cleaners_common as cleaners  

logging.basicConfig(
    level=logging.INFO,
    format= " %(asctime)s %(levelname)s %(message)s"
)






def clean_roaster(raw):
    df = raw.copy()
    df["gender"] = cleaners.clean_gender(df["gender"])
    df["state"] = cleaners.clean_state(df["state"])
    mask = df["member_id"].str.strip() != ""
    mask2 = df["member_id"].str.strip() == ""
    mask3 = df.duplicated(subset=["member_id"],keep ="last")
    rejected = df[mask2|mask3]
   
    df = df[mask]
    df = df.drop_duplicates(subset=["member_id"],keep ="last")

    # print(f"""Raw Data:-{len(raw)} Cleaned Data:- {len(df)} Rejected Data:- {len(rejected)}

    #       """)

    logging.info(
    """
        Raw Data:- %d 
        Cleaned Data:- %d 
        Rejected Data:- %d
            """,
    len(raw),len(df),len(rejected)
    )
    
    assert len(raw) == len(df) + len(rejected)
    return df,rejected



raw = pd.DataFrame({
    "member_id": ["M1", " ", "M2", "M1", ""],
    "gender":    [" f", "Male", "FEMALE ", "F", "m"],
    "state":     ["tx", "fl", " ca", "tx", "ny"],
})



cleaned , Rejected = clean_roaster(raw)
print(cleaned)
print(Rejected)

# print(clean_gender(pd.Series([" M ","m","F","Male","Female","other"])))

# print(clean_state(pd.Series(["fl","ca",""])))
