def get_status(available_units, is_out_of_service):
    """Determine the availability status of a bathroom."""
    if is_out_of_service:
        return "out_of_service"
    if available_units > 0:
        return "available"
    elif available_units == 0:
        return "occupied"
    else:
        raise ValueError("available_units cannot be negative")


def add_status(bathroom):
    """Return a bathroom record with a calculated status field."""
    return {
        **bathroom,
        "status": get_status(
            bathroom["available_units"],
            bathroom["is_out_of_service"]
        )
    }