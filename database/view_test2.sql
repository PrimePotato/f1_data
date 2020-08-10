-- SELECT driver.forename, driver.surname, race.name, race.year, qualifying.q1, circuit.name, qualifying.q2, qualifying.q3
SELECT
  races.name,
  races.year,
  races.raceId,
  drivers.forename,
  drivers.surname,
  results.position
FROM
  races, drivers, results
WHERE
  drivers.driverId = results.driverId
  AND races.raceId = results.raceId
  AND drivers.surname = "Hamilton"
  AND results.raceId = races.raceId
ORDER BY races.year
  DESC

