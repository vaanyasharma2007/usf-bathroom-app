# USF Bathroom Availability App

## Overview

The USF Bathroom Availability App is a full-stack web application that allows students to view and update the availability of bathrooms in residence halls in real time.

## Problem

Students often walk to bathrooms only to find every stall or shower occupied. This application reduces wasted time by providing live occupancy updates.

## Current Features
FastAPI backend
Bathroom availability API
Occupancy status calculation
Bathroom data model
Castor hall MVP

## Planned Features
PostgreSQL database
React frontend
Live occupancy updates
Multi-building support
Gender-neutral bathroom support
Campus map integration
Maintance reporting
Favorites

## Tech Stack

- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- Version Control: Git & GitHub

## Development status
This project is actively being developed as a portfolio project while learning backend engineering.

The current focus is building a scalable backend architecture before implementing the frontend and database.

## Author

Vaanya Sharma

## Example API Response

```json
[
  {
    "id": 1,
    "building": "Castor Hall",
    "floor": 1,
    "gender": "women",
    "area_type": "toilet",
    "available_units": 3,
    "status": "available"
  }
]