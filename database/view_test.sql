CREATE VIEW v_pole_position
  AS
    SELECT DISTINCT
      qualifying.raceId,
      qualifying.q1,
      qualifying.q2,
      qualifying.q3,
      races.name,
      races.year,
      races.raceId,
      drivers.forename,
      drivers.surname
    FROM
      qualifying, races, drivers, circuits
    WHERE
      qualifying.position = 1
      AND qualifying.raceId = races.raceId
      AND circuits.circuitId = races.circuitId
      AND drivers.driverId = qualifying.driverId

