def get_status(available_units,is_out_of_service):
    if is_out_of_service:
        return "out_of_service"
    if available_units>0:
        return "available"
    elif available_units==0:
        return "occupied"
    elif available_units<0:
        return None
    