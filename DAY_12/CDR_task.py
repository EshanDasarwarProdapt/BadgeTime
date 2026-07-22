'''
Fields, in order: msisdn | call_duration_sec | data_used_gb | is_roaming | plan_type

Split raw_cdr on "|" into 5 separate string variables.
Cast each into its correct Python type (str, int, float, bool, str). — Note: casting the string "True" directly with bool() will NOT give you what you expect. Figure out why, and write a correct conversion.
Print each variable together with its type().
'''

raw_cdr = "9876543210|247|3.8|True|prepaid"


list_cdr = raw_cdr.split("|")

cdr_dict = {
    "msisdn": list_cdr[0],
    "duration": list_cdr[1],
    "charge": list_cdr[2],
    "is_valid": list_cdr[3],
    "plan_type": list_cdr[4]
}

msisdn = cdr_dict["msisdn"]
duration = int(cdr_dict["duration"])
data_used_gb = float(cdr_dict["charge"])
is_roaming = bool(cdr_dict["is_valid"])
plan_type = cdr_dict["plan_type"]



print(type(msisdn), msisdn  )
print(type(duration), duration  )
print(type(data_used_gb), data_used_gb  )
print(type(is_roaming), is_roaming  )
print(type(plan_type), plan_type )