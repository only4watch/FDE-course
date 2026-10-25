inspection_score = 85
total_inspection = 0

class InspectionLimitOff(Exception):
    pass

try :
    if total_inspection < 2:
        raise InspectionLimitOff("Daily 2 mandatory inspection is required.")
    #logic
    # logic
except Exception as error:
    print(error)