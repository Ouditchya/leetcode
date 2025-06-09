import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    
    def check_valid(s):
        octets = s.split(".")
        if len(octets) != 4: return False
        for octet in octets:
            if (octet[0] == "0" and len(octet) > 1) or (int(octet) > 255): return False
        return True
    
    logs["invalid"] = logs["ip"].apply(check_valid)
    ans = (
        logs[logs["invalid"] == False]
            .groupby(["ip"])
            .agg({"log_id": "count"})
            .rename(columns = {"log_id": "invalid_count"})
            .sort_values(by = ["invalid_count", "ip"], ascending = False)
            .reset_index()
    )
    # print(ans)

    return pd.DataFrame(ans)