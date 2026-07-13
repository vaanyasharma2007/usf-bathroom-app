# API Design

## Overview

The USF Bathroom Availability System provides a REST API for retrieving bathroom availability information.

The current MVP focuses on Castor Hall before expanding to additional buildings across the USF campus.

---

## Current Endpoints

### GET /

**Description**

Returns a welcome message to verify that the backend is running.

**Response**

```json
{
  "message": "Welcome to the bathroom availability app!"
}
```

---

### GET /bathrooms

**Description**

Returns all bathroom availability records.

Each record contains:

- id
- building
- floor
- gender
- area_type
- total_units
- available_units
- status

---

## Planned Endpoints

### GET /bathrooms/{id}

Return information for a single bathroom area.

### POST /reports

Allow users to report maintenance issues.

### PUT /bathrooms/{id}

Update bathroom availability.

### DELETE /bathrooms/{id}

Remove a bathroom record (admin only).

---

## Future Improvements

- PostgreSQL database
- React frontend
- Multi-building support
- Live occupancy updates
- Interactive campus map
- Favorites
- Maintenance notifications