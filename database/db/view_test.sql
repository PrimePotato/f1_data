-- SELECT driver.forename, driver.surname, race.name, race.year, qualifying.q1, circuit.name, qualifying.q2, qualifying.q3
SELECT
  qualifying.raceId,
  qualifying.q1,
  qualifying.q2,
  qualifying.q3,
  race.name,
  race.year,
  race.raceId
--   driver.forename,
--   driver.surname
FROM qualifying, race
-- JOIN circuit ON
-- circuit.circuitId = race.circuitId
-- JOIN driver ON
-- driver.driverId = qualifying.driverId
-- LEFT JOIN qualifying ON
-- qualifying.raceId = result.raceId AND qualifying.driverId = driver.driverId
WHERE qualifying.position = 1
-- AND
      AND race.year = 2019
--       AND
      -- AND qualifying.raceId = race.raceId
--       AND circuit.circuitId = race.circuitId
--       AND driver.driverId = qualifying.driverId
      AND race.raceId = qualifying.raceId


-- ORDER BY race.year
--   DESC

